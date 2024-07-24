---
hide:
  - toc
---

# 构建 vGPU 显存超配镜像

[Hami 项目](https://github.com/Project-HAMi/HAMi)中 vGPU 显存超配的功能已经不存在，目前使用有显存超配的 `libvgpu.so` 文件重新构建。

```bash title="Dockerfile"
FROM docker.m.daocloud.io/projecthami/hami:v2.3.11
COPY libvgpu.so /k8s-vgpu/lib/nvidia/
```

执行以下命令构建镜像：

```bash
docker build -t release.daocloud.io/projecthami/hami:v2.3.11 -f Dockerfile .
```

然后把镜像 push 到 `release.daocloud.io` 中。
