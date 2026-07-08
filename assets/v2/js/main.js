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

  document.addEventListener("click", function (e) {
    var toggle = e.target.closest("[data-theme-toggle]");
    if (toggle) {
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
})();
