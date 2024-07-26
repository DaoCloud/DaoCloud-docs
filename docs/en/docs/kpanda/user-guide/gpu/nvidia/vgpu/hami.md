---
hide:
  - toc
---

# Build a vGPU Memory Oversubscription Image

The vGPU memory oversubscription feature in the [Hami Project](https://github.com/Project-HAMi/HAMi)
no longer exists. To use this feature, you need to rebuild with the `libvgpu.so` file
that supports memory oversubscription.

```bash title="Dockerfile"
FROM docker.m.daocloud.io/projecthami/hami:v2.3.11
COPY libvgpu.so /k8s-vgpu/lib/nvidia/
```

Run the following command to build the image:

```bash
docker build -t release.daocloud.io/projecthami/hami:v2.3.11 -f Dockerfile .
```

Then, push the image to `release.daocloud.io`.
