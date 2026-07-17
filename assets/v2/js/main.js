// v2 — theme toggle + mobile nav. No dependencies.
(function () {
  var root = document.documentElement;

  // Theme: explicit choice wins, otherwise follow the system.
  var stored = null;
  try { stored = localStorage.getItem("theme"); } catch (e) {}
  if (stored === "light" || stored === "dark") {
    root.setAttribute("data-theme", stored);
  }

  function currentTheme() {
    var explicit = root.getAttribute("data-theme");
    if (explicit) return explicit;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  // iOS Safari only applies :active (pressed) states when a touch listener exists.
  document.addEventListener("touchstart", function () {}, { passive: true });

  var themeFadeTimer;
  document.addEventListener("click", function (e) {
    var toggle = e.target.closest("[data-theme-toggle]");
    if (toggle) {
      // .theme-fade makes the palette swap a 200ms cross-fade (see main.css).
      root.classList.add("theme-fade");
      clearTimeout(themeFadeTimer);
      themeFadeTimer = setTimeout(function () { root.classList.remove("theme-fade"); }, 280);
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (err) {}
      return;
    }

    var navToggle = e.target.closest("[data-nav-toggle]");
    var menu = document.querySelector("[data-nav-menu]");
    if (navToggle && menu) {
      var open = menu.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
      return;
    }

    // Close the mobile menu after choosing a link.
    if (menu && menu.classList.contains("open") && e.target.closest("[data-nav-menu] a")) {
      menu.classList.remove("open");
    }
  });

  // Lightbox for project galleries.
  var items = Array.prototype.slice.call(
    document.querySelectorAll("[data-lightbox] .gallery-item img")
  );
  var box = document.querySelector(".lightbox");
  if (items.length && box && typeof box.showModal === "function") {
    var lbImg = box.querySelector(".lb-img");
    var lbCounter = box.querySelector(".lb-counter");
    var prevBtn = box.querySelector("[data-lb-prev]");
    var nextBtn = box.querySelector("[data-lb-next]");
    var current = 0;

    if (items.length === 1) {
      prevBtn.hidden = true;
      nextBtn.hidden = true;
    }

    function show(i) {
      current = (i + items.length) % items.length;
      lbImg.src = items[current].src;
      lbImg.alt = items[current].alt;
      lbCounter.textContent = (current + 1) + " / " + items.length;
    }

    items.forEach(function (img, i) {
      img.closest(".gallery-item").addEventListener("click", function () {
        show(i);
        box.showModal();
      });
    });

    box.addEventListener("click", function (e) {
      if (e.target.closest("[data-lb-prev]")) show(current - 1);
      else if (e.target.closest("[data-lb-next]")) show(current + 1);
      else if (e.target.closest("[data-lb-close]")) box.close();
      // Click on the dark backdrop (the dialog itself, not its children) closes.
      else if (e.target === box) box.close();
    });

    document.addEventListener("keydown", function (e) {
      if (!box.open) return;
      if (e.key === "ArrowLeft") show(current - 1);
      if (e.key === "ArrowRight") show(current + 1);
    });
  }

  // Video poster: click swaps the poster for the real iframe (never autoplay
  // before the click; the src carries autoplay=1 so playback starts on tap).
  document.addEventListener("click", function (e) {
    var poster = e.target.closest(".video-poster[data-video-src]");
    if (!poster || !poster.dataset.videoSrc) return;
    var wrap = document.createElement("div");
    wrap.className = "video";
    var frame = document.createElement("iframe");
    frame.src = poster.dataset.videoSrc;
    frame.title = "Video";
    frame.setAttribute("allowfullscreen", "");
    frame.setAttribute("allow", "autoplay");
    wrap.appendChild(frame);
    poster.replaceWith(wrap);
  });

  // Post mini-TOC: left rail, wide screens only, built from h2 headings.
  // Only long posts get one (3+ sections); short posts stay chrome-free.
  var postContainer = document.querySelector(".post .container");
  var postBody = document.querySelector(".post .post-body");
  if (postContainer && postBody) {
    var heads = Array.prototype.slice.call(postBody.querySelectorAll("h2[id]"));
    if (heads.length >= 3) {
      var toc = document.createElement("aside");
      toc.className = "post-toc";
      toc.setAttribute("aria-label", "On this page");
      var inner = document.createElement("div");
      var label = document.createElement("p");
      label.className = "toc-label";
      label.textContent = "On this page";
      inner.appendChild(label);
      var list = document.createElement("ol");
      var links = heads.map(function (h) {
        var li = document.createElement("li");
        var a = document.createElement("a");
        a.href = "#" + h.id;
        a.textContent = h.textContent;
        li.appendChild(a);
        list.appendChild(li);
        return a;
      });
      inner.appendChild(list);
      toc.appendChild(inner);
      postContainer.insertBefore(toc, postBody);

      var currentIdx = -1;
      function spy() {
        var cur = 0;
        heads.forEach(function (h, k) {
          if (h.getBoundingClientRect().top < 120) cur = k;
        });
        if (cur !== currentIdx) {
          currentIdx = cur;
          links.forEach(function (a, k) {
            a.classList.toggle("is-current", k === cur);
          });
        }
      }
      window.addEventListener("scroll", spy, { passive: true });
      spy();
    }
  }

  // Mermaid diagrams: ```mermaid fences in a post render client-side into SVG.
  // The library is only fetched (CDN) on pages that actually contain one.
  var mermaidNodes = Array.prototype.slice.call(
    document.querySelectorAll(".post-body .language-mermaid")
  ).map(function (el) {
    var code = el.querySelector("code") || el;
    var pre = document.createElement("pre");
    pre.className = "mermaid";
    pre.dataset.mermaidSrc = code.textContent;
    pre.textContent = code.textContent;
    var container = el.closest(".highlighter-rouge") || el;
    container.replaceWith(pre);
    return pre;
  });

  if (mermaidNodes.length) {
    var mermaidScript = document.createElement("script");
    mermaidScript.src = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js";
    mermaidScript.onload = function () {
      function renderMermaid() {
        mermaidNodes.forEach(function (n) {
          n.removeAttribute("data-processed");
          n.textContent = n.dataset.mermaidSrc;
        });
        window.mermaid.initialize({
          startOnLoad: false,
          securityLevel: "strict",
          theme: currentTheme() === "dark" ? "dark" : "neutral",
          fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
        });
        window.mermaid.run({ nodes: mermaidNodes });
      }
      renderMermaid();
      // Diagrams re-render when the theme toggle flips data-theme.
      new MutationObserver(renderMermaid).observe(root, { attributes: true, attributeFilter: ["data-theme"] });
    };
    document.head.appendChild(mermaidScript);
  }
})();
