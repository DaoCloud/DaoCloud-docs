---
title: '「Allen 谈 Docker 系列」Docker 容器的 root 安全吗？'
---

<!-- reviewed by fiona -->

>**「Allen 谈 Docker 系列」**

>DaoCloud 正在启动 Docker 技术系列文章，每周都会为大家推送一期真材实料的精选 Docker 文章。主讲人为 DaoCloud 核心开发团队成员 Allen（孙宏亮），他是 InfoQ 「Docker 源码分析」专栏作者，已出版《Docker 源码分析》一书。Allen 接触 Docker 近两年，爱钻研系统实现原理，及 Linux 操作系统。

---

Docker 是 Linux 平台上容器的管理引擎，其提供的容器服务一方面可以很好地分配物理资源，不论是资源还是权限都能够达到隔离的效果；另一方面，Docker 的设计把更多的目光投向了「应用」本身，简化了应用从开发、测试、发布等迭代发展的生命周期。

Docker 带着「重新定义应用」的豪言，冲击着大家对软件的理解，在云计算领域更是如此。然而，新技术的诞生往往需要接受行业千锤百炼似的考验，安全无疑是业界最关心的因素之一。传统的硬件虚拟化等技术发展了数十年，逐渐步入成熟期，成为如今云计算技术的中坚技术，其高隔离性自然是保障安全的首要功臣；对于应用而言，安全问题尤为严峻，系统业务核心几乎全部通过应用来实现，应用的安全一旦失守，后果不堪设想。

正视安全，Docker 无法回避。在众多安全性考量中，有一点经常被 Docker 实践者提起，那就是 Docker 容器的 root 安全性。由于截止到目前的 docker 1.8.3 版本，Docker 依然没有完成对 Linux User Namespace 的支持，因此对于 Docker 容器而言，容器内部的 root 和宿主机上的 root 属于同一个用户，两者的 UID 均为 0。容器中的超级用户，是否会影响其他容器，乃至宿主机，自然成了大家最关心的安全问题。


## Docker 容器 root 和宿主机 root

意识到 Docker 容器内的 root 用户属于超级用户之外，更多的忧虑逐渐表露，比如「使用 root 用户运行 Docker 容器内部的应用，是否安全？」，比如「容器内的 root 是否可以操纵宿主机资源？」……

如果 Docker 容器内的 root 用户和宿主机的 root 用户完全一致，那么 Docker 容器可以认为在权限方面拥有宿主机上 root 相应的权限，此时的 Docker 容器拥有超级管理员权限，原则上 Docker 容器本身完全有能力操纵宿主机的一切。然而，结果真是如此吗？

答案自然是否定的，否则的话，Docker 的安全简直不堪一击。虽然 Docker 容器内的 root 用户直接是宿主机的 root 用户，但是 Docker 可以保证两者在权限方面，拥有巨大的差异。此时，这种差异的存在完全是借助于**Linux 内核的 Capabilities 机制**。换言之，正是 Capabilities 在保障 Docker 容器的安全性。

Capabilities 在 Docker 容器的管理过程中使用非常方便。如果不需要授予 Docker 容器足够的系统权限，也就是足够的 Capabilities，只需在运行 Docker 容器时不使用 `--privileged` 参数，如：

```
docker run -it --priviledged=false ubuntu:14.04 /bin/bash 
或者
docker run -it ubuntu:14.04 /bin/bash
```

如果需要授予 Docker 容器足够的管理权限，则直接将 `--privileged` 参数设为 true，如：

```
docker run -it --privileged=true ubuntu:14.04 /bin/bash
```

另外，在 `docker run` 命令中，添加 `--cap-add` 以及 `--cap-drop` 参数也完全可以更灵活的添加以及移除 Linux Capabilities。

## Linux Capabilities

既然 Docker 采用了 Linux Capabilities 机制，那么何为 Linux Capabilities，我们来一探究竟。

大家一定知道，在传统的 Unix 系统中，为了实现权限的检查，操作系统上运行的进程可以分为两种：`特权进程（priviledged processes）`和`非特权进程（unpriviledged processes）`。其中，前者的有效用户 ID 为 0，也就是大家常说的超级用户或者 root 用户，而后者的有效用户 ID 为非 0，也常被称为普通用户。特权进程在运行时们可以绕过所有的内核权限检查，而非特权进程则必须完全接受这些检查。

虽然如此，然而实际情况要比以上的描述复杂一些。实际情况下，Linux 会将传统超级用户的特权划分为多个单位，也就是我们关心的 Capabilties。Capabilities 会有很多种，而且对于 root 用户而言，完全可以单独启用或者关闭，因此同为 root 用户，权限却因 Capabilities 的不同而存在差异。

Linux Capabilities 机制将超级用户的权限划分非常之细，所有的 Capabilities 列表有接近 40 项之多。我们可以通过几个具体的 Capability 来看看他们各自管理的权限范围。

- **CAP_SYS_ADMIN**：`CAP_SYS_ADMIN` 实现一系列的系统管理权限，比如实现磁盘配额的 quotactl，实现文件系统挂载的 mount 权限；比如在 fork 子进程时，通过 clone 和 unshare 系统调用，使用 `CLONE_* 的 flag` 参数来为子进程创建新的 namespaces；比如实现各种特权块设备以及文件系统的 ioctl 操作等。

- **CAP_NET_ADMIN**：`CAP_NET_ADMIN` 实现一系列的网络管理权限，比如网络设备的配置，IP 防火墙，IP 伪装以及统计等功能；比如路由表的修改，TOS 的配置，混杂模式的配置等。

- **CAP_SETUID**：`CAP_SETUID` 有能力对进程 UID 做出任何管控。

- **CAP_SYS_MODULE**：`CAP_SYS_MODULE` 帮助 root 用户加载或者卸载相应的 Linux 内核模块。

- **CAP_SYS_NICE**：`CAP_SYS_NICE` 有能力对任意进程修改其 NICE 值，同时支持对任何进程设置调度策略与优先级，还有在进程的 CPU 亲和性以及 I/O 调度方面有相应的配置权限。

……

Linux 总共有接近 40 项的 Capabilities，然而初步接触以上 5 项 Capabilties，我们可以发现：**` Linux 对于超级用户的特权也进行了种类繁多的划分，有划分就意味着有区别，有区别就意味着并不是所有的 root 用户都拥有相同的权限.`**

那么 Linux Capabilties 与 Docker 容器的关系究竟如何？

## Docker 容器与 Linux Capabilities

大家已经清楚 Docker 容器中的 root 用户与宿主机的 root 用户同属一个 uid，均为 0；并且大家也可以发现不同的 Capabilities 可以区分 root 用户的权限，那么 Docker 容器中的 root 用户的 Capabilities 情况到底是什么样，这种现状会存在安全隐患吗？

上文已经涉及了 docker run 命令创建容器时 privileged 参数的用法，实际上 Docker 容器的Capabilties 情况也会因用户设置而异。

#### Docker 容器的非特权模式

默认情况下，docker run 命令的 privileged 参数值为 false。因此，毫无疑问，Docker 容器内部的 root 用户将受到严格的权限限制，很多有系统相关的操作权限都将被剥夺，只具备超级用户的一些基本权限。

研究 Docker 的源码，我们可以发现：**`在 Linux 接近40项的 Capabilities 中，Docker为了确保容器的安全，仅仅支持了其中的14项基本的 Capabilities`**，现在，我们不妨来看看这些 Capabilities 到底有哪些，它们分别是： `CAP_CHOWN`、 `CAP_DAC_OVERRIDE`、 `CAP_FSETID`、 `CAP_MKNOD`、 `FOWNER`、 `NET_RAW`、 `SETGID`、 `SETUID`、 `SETFCAP`、 `SETPCAP`、 `NET_BIND_SERVICE`、 `SYS_CHROOT`、 `KILL` 和 `AUDIT_WRITE`。

我们可以发现：在这 14 项中几乎没有一项涉及到系统管理权限，比如 Docker 容器的 root 用户不具备 CAP_SYS_ADMIN，磁盘限额操作、mount 操作、创建进程新命名空间等均无法实现；比如由于没有 CAP_NET_ADMIN，网络方面的配置管理也将受到管制。因此，默认情况下，Docker 容器中的 root 用户并没有以往我们想象得那么能力超群，Docker 依然对其存在限制，这样设计的出发点之一自然是安全。

#### Docker 容器的特权模式

了解完 Docker 容器的非特权模式，大家也许会觉得 Docker 容器的 root 权限被削减得有点难以置信，`确保安全，却剥夺了过多系统权限`。其实，Docker 作为一个管理容器的工具，并未在容器 root 方面「一刀切」，Docker 容器的非特权模式就可以满足 root 用户的权限最大化。

一旦将 docker run 命令的 privileged 参数设为 true，那么 Docker 容器的 root 权限将得到大幅度的提升。此时，Docker容器的 root 用户将获得 37 项 Capabilities 能力。`由于 Docker 容器与宿主机处于共享同一个内核操作系统的状态，因此，Docker 容器将完全拥有内核的管理权限`。安全隐患，瞬间浮出水面。

#### 两种模式的比较

Docker 容器的实践，不能缺少场景。谈到以上两种模式的比较，场景更是如此。**`安全`**与**`权限`**，孰轻孰重，鱼与熊掌，是否可以兼得？

云计算领域，公有云一向被认为是一项技术甚至一种产品的试金石。Docker 这项技术更是需要在公有云领域展现自己的价值。安全这个话题，在公有云中尤为敏感，这一点相信已经毋庸赘言。那么，在安全至上的情况下，开启 Docker 容器的特权模式将完全不现实，如此一来，Docker 容器的权限将不得不做出妥协。Docker 技术在公有云领域，不论服务于 PaaS，还是目前兴起的 CaaS，权限的削减是否会影响这两种云计算模式？

Docker 容器 root 用户权限的缺失，主要还是集中于系统管理方面。那我们就从`系统管理权限`，来分析 PaaS 和 CaaS 对 Docker 需求的区别。

**PaaS**：Docker 作为 PaaS 技术的底层技术，完全有能力支撑起用户应用的运行。对于提供运行时环境而言，应用将无需过多的与系统管理相关联；同时，从应用本身出发，高移植性应该是重要的设计目标之一，过多的与系统耦合同样将会带来运维成本。

**CaaS**：CaaS 与 PaaS 最大的区别，在于 CaaS 带来的服务模式要更广。CaaS 中容器的范畴很广，完全可以不限于用户应用的运行。CaaS 中 Docker 的自足点将不再是专注于应用本身，而是将计算资源的管理也圈入其内，比如提供类似于传统虚拟机的计算单元。由于为了安全，无法提供与虚拟机 root 用户相同的权限，因此 Docker 容器的`权限`问题将无情暴露，CaaS 的服务质量必将受到影响。

## Docker与Linux User Namespace

Docker 容器的 root 安全吗？相信大家已经有了一定的认识。这个问题，其实并不是仅仅涉及安全这一个话题，而是一种**`安全与权限的博弈`**。既然如此，难道就只能取舍，鱼和熊掌，不可兼得吗？

答案是否定的。Linux User Namespace 的支持将大大缓解这种情况。（目前，docker 1.8.3 仍未支持 User Namespace。）一旦完成对 Linux User Namespace 的支持，Docker 容器内部的 root 用户在宿主机看来 UID 将不再是 0，换言之，在宿主机上仅仅是一个普通用户，而在 Docker 容器内部，原则上可以应用更多的 Capabilities，实现权限的提升。Docker 与 Linux User Namespace 的渊源，后续我们再深入。

## 总结

Docker 容器中 root 用户的安全性一直备受关注。安全性问题，并未想象中的那么坏，当然也绝对不是无懈可击，更多的是一种**`安全与权限的博弈`**。

Docker 大潮一波高过一波，我们没有理由怀疑 Docker 的未来。Docker 对 Linux User Namespace 的支持也是万众瞩目。User Namespace 不仅能够从 Capabilities 的角度提升 Docker 容器 root 的容器内系统权限，而且也有能力对 ulimit 的支持更加完善。理论上，User Namespace 对于安全与隔离是存在巨大的共享，但是这也仅仅是一种**`极大的缓解`**。缘何如此，根在共享内核。

