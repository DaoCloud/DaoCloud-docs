#!/bin/bash

# This script builds the documentation using the versioned configuration.

# Navigate to the docs directory
cd docs

# Build the documentation with versioning support
sphinx-build -b html -c versioned_conf.py . _build/html
