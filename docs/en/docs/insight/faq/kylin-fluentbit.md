---
hide:
  - toc
---

# Fluent Bit Fails to Start on NeoKylin Linux V10

The Fluent Bit Pod log contains the following output:

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

## Root Cause

The `memory page size` of the Kylin system is `64K`, while that of `CentOS/Ubuntu` systems is `4K`. However, the Fluent Bit container requires a `memory page size` of `4K`.

## Solution

> Supported Fluent Bit versions: Fluent Bit 4.0.1+

Refer to the community [answer][1] and replace the image with the one [built by DaoCloud][2]: `ghcr.m.daocloud.io/openinsight-proj/fluent-bit:4.0.1`. Note: the image is under the **openinsight-proj** repository.

Difference from the official image: only the `jemalloc` feature is disabled at compile time; everything else is identical to the official image.

## Notes

Fluent Bit uses the `jemalloc` memory allocator by default, but it can be disabled via a compile-time option. Disabling `jemalloc` mainly affects memory management efficiency, performance, and compatibility. The details are as follows:

1. Reduced memory management efficiency

    jemalloc is a memory allocator designed for high-performance scenarios, excelling at reducing memory fragmentation and lock contention. If jemalloc is disabled, Fluent Bit falls back to the system's default memory allocator (such as glibc's malloc), which may increase memory fragmentation and thus memory usage. This change may be more noticeable when processing massive amounts of data.

2. Potentially degraded performance

    One of jemalloc's design goals is to improve the performance of multithreaded applications. For a high-concurrency data processing tool like Fluent Bit, using jemalloc effectively reduces lock contention between threads. Once jemalloc is disabled, Fluent Bit's throughput under high load may decrease and latency may increase.

3. Resolved compatibility issues in specific scenarios

    Although jemalloc generally enhances performance, it may conflict with other libraries or system configurations in certain special environments. For example, in container environments or certain embedded systems, disabling jemalloc may resolve some compatibility issues.

4. Smaller binary size

    The jemalloc library increases the size of the Fluent Bit binary. Disabling it reduces the size of the resulting binary accordingly, which is beneficial for environments that need to shrink container image sizes or have strict storage limits.

## Recommendations by Scenario

### When to Enable jemalloc

- Your application runs in a high-concurrency, high-load production environment.
- You expect better memory usage efficiency and performance.
- There are no known compatibility issues.

### When to Consider Disabling jemalloc

- You encounter jemalloc-related compatibility issues, such as crashes or memory leaks.
- You need to reduce the binary size.
- Your application has a low workload and does not require sophisticated memory management.

[1]: https://github.com/fluent/fluent-bit/blob/master/dockerfiles/Dockerfile#L79
[2]: https://github.com/openinsight-proj/fluent-bit-distributions
