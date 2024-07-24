# vGPU 显存超配镜像构建

社区 `Hami` 项目中 `vgpu` 显存超配的功能已经不存在，目前通过使用有显存超配的 `libvgpu.so` 文件重新构建。

- Dockerfile

```
FROM docker.m.daocloud.io/projecthami/hami:v2.3.11
COPY libvgpu.so /k8s-vgpu/lib/nvidia/
```

`docker build -t release.daocloud.io/projecthami/hami:v2.3.11 -f Dockerfile .` 执行这个命令进行镜像构建，然后把镜像 `push` 到 `release.daocloud.io` 中。
