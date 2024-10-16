#!/bin/bash
# Cleanup script for interrupted DaoCloud Enterprise installation

echo "Starting cleanup process..."

# Stop running containers
containers=$(podman ps -q --filter "name=dce-cluster-installer")
if [ -n "$containers" ]; then
  echo "Stopping running containers..."
  podman stop $containers
  podman rm $containers
else
  echo "No running containers found."
fi

# Remove temporary files
echo "Removing temporary files..."
rm -rf /path/to/temp/files/*

echo "Cleanup completed successfully."