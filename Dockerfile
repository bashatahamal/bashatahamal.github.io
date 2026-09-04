FROM ruby:3.1-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  git \
  && rm -rf /var/lib/apt/lists/*

# Gems first, so this layer stays cached until the Gemfile changes
COPY Gemfile ./
RUN bundle install

COPY . /app

EXPOSE 4000

# --force_polling: file-change events do not cross the Windows bind mount,
# so poll for changes instead (otherwise edits require a container restart)
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--force_polling"]
