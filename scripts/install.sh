set -e
trap 'echo "Error occurred during decompression"' ERR
@@ -25,0 +28,2 @@
if ! tar -xzf package.tar.gz; then
  echo "Decompression failed. Please check the integrity of the package." >&2
@@ -26,0 +31,2 @@
  exit 1
fi
@@ -30,0 +37,1 @@
echo "Decompression completed successfully."