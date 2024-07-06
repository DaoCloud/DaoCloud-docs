#!/bin/bash

# run pull request preview site with netlify

# install required packages
pip install mkdocs-material \
    mkdocs-git-revision-date-plugin \
    mkdocs-mermaid2-plugin \
    mkdocs-rss-plugin \
    mkdocs-minify-plugin \
    mkdocs-macros-plugin \
    mkdocs-git-revision-date-localized-plugin \
    mkdocs-awesome-pages-plugin \
    mkdocs-redirects \
    mkdocs-print-site-plugin \
    mkdocs-swagger-ui-tag \
    pyyaml

# Ensure the git repository is up to date.
git fetch origin main

# Get the current build commit SHA
CURRENT_COMMIT_SHA=$(git rev-parse HEAD)
echo "Current commit SHA: $CURRENT_COMMIT_SHA"

# Get the latest commit SHA of the main branch
MAIN_COMMIT_SHA=$(git rev-parse origin/main)
echo "Main commit SHA: $MAIN_COMMIT_SHA"

# Get the list of changed files and convert it to a space-separated string.
CHANGED_FILES=$(git diff --name-only $MAIN_COMMIT_SHA $CURRENT_COMMIT_SHA | tr '\n' ' ')

# Add the list of modified files to the environment variable.
export CHANGED_FILES

# Print environment variables to confirm
echo "CHANGED_FILES environment variable:"
echo "$CHANGED_FILES"

# Generate the navigation for the docs
python scripts/generate_nav.py

# Perform different operations based on the modified files.
if echo "$CHANGED_FILES" | grep -q 'docs/zh/docs/'; then
  echo "Chinese docs were modified, running mkdocs build for Chinese docs..."
  mkdocs build -f docs/zh/mkdocs.yml -d ../../public/
fi

if echo "$CHANGED_FILES" | grep -q 'docs/en/docs/'; then
  echo "English docs were modified, running mkdocs build for English docs..."
  mkdocs build -f docs/en/mkdocs.yml -d ../../public/en/
fi

# Check if the public/ directory exists, and create it if it does not.
if [ ! -d "public" ]; then
  echo "Public directory not found. Creating public/ directory."
  mkdir -p public/en/
  echo "<html><body><h1>Welcome to the public directory</h1></body></html>" > public/index.html
  echo "<html><body><h1>Welcome to the public directory</h1></body></html>" > public/en/index.html
fi