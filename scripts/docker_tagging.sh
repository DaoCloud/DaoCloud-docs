#!/bin/bash
# This script tags Docker images with a dynamic tag based on the current Git commit ID.

# Extract the short commit ID
COMMIT_ID=$(git rev-parse --short HEAD)

# Define the image name and tag
IMAGE_NAME="myimage"
TAG="${COMMIT_ID}"

# Build and tag the Docker image
docker build -t ${IMAGE_NAME}:${TAG} .
