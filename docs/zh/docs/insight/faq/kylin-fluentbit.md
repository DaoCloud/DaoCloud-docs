---
hide:
  - toc
---

# NeoKylin Linux V10 系统中启动 Fluent Bit 失败

观察 Fluent Bit Pod 日志有如下字段：

```text
<jemalloc>: Unsupported system page size
<jemalloc>: Unsupported system page size
<jemalloc>: Unsupported system page size
<jemalloc>: Unsupported system page size
<jemalloc>: Unsupported system page size
<jemalloc>: Unsupported system page size
<jemalloc>: Unsupported system page size
<jemalloc>: Unsupported system page size
<jemalloc>: Unsupported system page size
<jemalloc>: Unsupported system page size
<jemalloc>: Unsupported system page size
Error in GnuTLS initialization: ASN1 parser: Element was not found.
```

## 问题根因

kylin 系统的 `memory page size` 大小是 `64K`，`Centos/Ubuntu` 系统的 `memory page size` 大小是 `4K`。 而 FB 容器所需的 `memory page size` 大小是 `4K`。

## 解决办法

> Fluent Bit 支持范围：Fluent Bit 4.0.1+

参考社区的[解答][1] 将镜像替换成道客[自行构建][2]的镜像：`ghcr.m.daocloud.io/openinsight-proj/fluent-bit:4.0.1`; 注意：镜像地址是 **openinsight-proj** 。

与官方的差别：仅在编译时关闭 `jemalloc` 特性，其余与官方一致。

## 注意

Fluent Bit 在默认情况下会使用 `jemalloc` 内存分配器，不过也能够通过编译选项将其关闭。关闭 `jemalloc` 所产生的影响，主要体现在内存管理效率、性能以及兼容性等方面，下面为你详细介绍：

1. 内存管理效率降低

    jemalloc 是专门为高性能场景打造的内存分配器，它在减少内存碎片、降低锁竞争方面表现出色。要是关闭了 jemalloc，Fluent Bit 就会转而使用系统默认的内存分配器（像 glibc 的 malloc），这可能会使内存碎片增多，进而造成内存使用量上升。在处理海量数据的场景中，这种变化可能会更为明显。

2. 性能表现可能变差

    jemalloc 的设计目标之一就是提升多线程应用程序的性能。对于 Fluent Bit 这种高并发的数据处理工具而言，使用 jemalloc 能够有效减少线程间的锁竞争。一旦关闭 jemalloc，Fluent Bit 在高负载情况下的吞吐量可能会有所下降，延迟也可能会增加。

3. 特定场景兼容性问题得到解决

    尽管 jemalloc 通常能增强性能，但在某些特殊环境中，它可能会和其他库或者系统配置产生冲突。比如，在容器环境或者某些嵌入式系统中，关闭 jemalloc 也许可以解决一些兼容性方面的问题。

4. 二进制文件体积变小

    jemalloc 库会增加 Fluent Bit 二进制文件的大小，关闭它之后，生成的二进制文件体积会相应减小。这对于需要减小容器镜像体积或者对存储有严格限制的环境来说，是非常有利的。

## 适用场景建议

### 推荐启用 jemalloc 的情况

- 你的应用处于高并发、高负载的生产环境。
- 你期望获得更优的内存使用效率和性能表现。
- 不存在已知的兼容性问题。

### 可以考虑关闭 jemalloc 的情况

- 你遇到了与 jemalloc 相关的兼容性问题，例如出现崩溃或者内存泄漏的情况。
- 你需要减小二进制文件的体积。
- 你的应用工作负载较低，对内存管理的要求不高。

[1]: https://github.com/fluent/fluent-bit/blob/master/dockerfiles/Dockerfile#L79
[2]: https://github.com/openinsight-proj/fluent-bit-distributions
