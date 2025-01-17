# Use official Ruby image as the base image
FROM ruby:3.1-slim

# Set working directory inside the container
WORKDIR /app

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
  build-essential \
  git \
  && rm -rf /var/lib/apt/lists/*

# Install Jekyll and Bundler gems
RUN gem install jekyll bundler

# Copy the Jekyll project files into the container
COPY . /app

# Install project dependencies
RUN bundle install

# Expose the port that Jekyll will serve on
EXPOSE 4000

# Command to run Jekyll server
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]