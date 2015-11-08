---
title: 集群的概念
taxonomy:
    category:
        - docs
process:
    twig: true
---

### 管理主机

#### 主机

在添加了自有主机以后，您就可以开始管理您的自有主机了。

这时在「我的主机」中的主机列表就可以看到已经与当前账号绑定的自有主机和它们的主机名、IP 地址、容器数量和 CPU、内存以及硬盘的使用比率。

![我的主机：主机列表](/img/screenshots/features/runtimes/management/hosts-list.png)

在主机列表中点击主机名，您就可以看到这台自有主机的详细信息了，也可以进入主机的「容器」、「监控」和「设置」选项卡。

---

容器选项卡可以查看运行于该主机容器的容器名、镜像名、映射的端口、和当前的容器状态。

![主机列表：容器](/img/screenshots/features/runtimes/management/host-containers.png)

> 提示：这里的容器是主机 Docker 上正在运行的所有容器，某些容器也许不是 DaoCloud 管理的应用。

---

监控选项卡可以显示当前主机实时（一小时内）和二十四小时内的 CPU、内存以及硬盘使用比率的统计信息。

![主机列表：监控](/img/screenshots/features/runtimes/management/host-monitor.png)

---

设置界面中，可以重新配置主机名、修改部署标签、查看 Daomonit 版本并更新，也可以删除该主机。

![主机列表：设置](/img/screenshots/features/runtimes/management/host-settings.png)

> 提示：删除主机不会影响 Docker 的容器。如有必要删除，请手动用 `docker rm 容器名/ID` 进行删除。

#### 容器

同时在「我的主机」中的容器列表也可以看到运行在自有主机上的容器和它们的容器名、镜像名、主机名、映射的端口和当前的容器状态。

![我的主机：容器列表](/img/screenshots/features/runtimes/management/containers-list.png)

在容器列表中点击容器名，您就可以看到这个容器的详细信息了，也可以进入容器的「概览」、「日志」和「监控」选项卡。

在这里您还可以启动/停止容器、重启容器、暂停容器（暂不支持）和强制终止容器。

<!-- TODO: 是暂停么？ -->

---

概览选项卡可以检视当前容器执行的命令、映射的端口映射的容器卷和配置的环境变量。

![容器列表：概览](/img/screenshots/features/runtimes/management/container-overview.png)

---

日志选项卡可以查看当前容器的运行日志。

![容器列表：日志](/img/screenshots/features/runtimes/management/container-logs.png)

---

监控选项卡可以显示当前容器实时（一小时内）和二十四小时内的 CPU、内存以及网络使用比率的统计信息。

![容器列表：监控](/img/screenshots/features/runtimes/management/container-monitor.png)

### 添加主机

如果想要使用自有主机功能，首先您需要添加至少一台自有主机。

接下来我们将会为您介绍添加自有主机的三种方式：分别是免费体验、手动安装和使用第三方应用市场。

#### 免费体验

如果您还没有一台装有 Linux 的主机，我们邀请您体验「免费胶囊主机」。

要启动一台胶囊主机请参考下面的步骤：

第一步：在控制台点击「我的主机」。

![控制台：点击我的主机](/img/screenshots/features/runtimes/new/dashboard.png)

---

第二步：在「我的主机」的界面中点击「添加新主机」。

![我的主机：准备添加新主机](/img/screenshots/features/runtimes/new/runtimes-index.png)

---

第三步：在「添加新主机」的界面中点击「免费胶囊主机」。

![添加新主机：免费胶囊主机](/img/screenshots/features/runtimes/new/try.png)

---

这时点下「免费体验」即可启动一台「胶囊主机」。

> 提示：胶囊主机已经预先配置了 Docker，用来学习 [Docker 新手入门 30 min](../../tutorials/README.md) 会很方便哦。

> 警告：每个「胶囊」的生命目前是 120 分钟。尽管胶囊主机里使用 DaoCloud 管理的应用信息会被保留下来，但是胶囊主机内的其他文件和数据将被删除，故不要存放重要文件。

#### 手动安装

如果您有一台 Linux 主机（不论是裸机还是虚机），我们推荐您手动安装 `daomonit` 以配置自有主机。

`daomonit` 为 DaoCloud 的主机监控程序，帮助与用户账户或组织账户进行绑定以及对 Docker 服务进行监控和管理。

##### 安装前准备

安装前请确保：

* 已连接至互联网（但不需要公网 IP）。
* 建议使用官方支持的操作系统。

目前由 DaoCloud 官方支持的操作系统：

* Ubuntu
  - 兼容版本：12.04、14.04、15.04\*
* CentOS
  - 兼容版本：6、7
* Debian
  - 兼容版本：7\*
* Fedora
  - 兼容版本：18\*、20\*

> 提示：带有 `*` 的版本仅提供安装支持。

##### 安装 `daomonit`

要安装 `daomonit` 到自有主机请参考下面的步骤：

第一步：在控制台点击「我的主机」。

![控制台：点击我的主机](/img/screenshots/features/runtimes/new/dashboard.png)

---

第二步：在「我的主机」的界面中点击「添加新主机」。

![我的主机：准备添加新主机](/img/screenshots/features/runtimes/new/runtimes-index.png)

---

第三步：按照最新的安装步骤进行操作。

![我的主机：手动添加](/img/screenshots/features/runtimes/new/manual.png)

---

完成后，您将会看到「检测到主机」。

##### 开启或关闭自动启动

* 对于非 systemd 管理的系统请使用 `chkconfig daomonit on|off`。
* 对于 systemd 管理的系统请使用 `systemctl enable|disable daomonit`。

##### 要启动、停止或重启

* 对于非 systemd 管理的系统请使用 `service daomonit start|stop|restart`。
* 对于 systemd 管理的系统请使用 `systemctl start|stop|restart daomonit`。

##### 卸载 `daomonit`

* 对于 CentOS 和 Fedora 请使用 `rpm -e daomonit`。
* 对于 Ubuntu 和 Debian 请使用 `dpkg -r daomonit`。

#### 应用市场

为了方便用户部署，我们在国内的多家云主机厂商的应用市场中发布了镜像。

要使用应用市场中的镜像模板，请参考下面的流程。

##### 腾讯云

要在腾讯云使用应用市场模板请参考下面的步骤：

第一步：访问腾讯云[服务市场](http://market.qcloud.com/detail.php?productId=143)并点击「立即使用」。

![腾讯云：服务市场](/img/screenshots/features/runtimes/new/qcloud-market.png)

---

第二步：登录腾讯云[云主机管理](http://console.qcloud.com/cvm/index)找到新创建的腾讯云主机并点击「登陆到 Web 客户端」。

![腾讯云：管理云主机](/img/screenshots/features/runtimes/new/qcloud-manage.png)

> 提示：如果找不到新创建的主机，请确认选择正确的区域，实例中为「华东区-上海」。

---

第三步：在 Web 客户端中找到绑定用的网址，并输入到浏览器中。

![腾讯云：开启 Web 客户端](/img/screenshots/features/runtimes/new/qcloud-console.png)

---

第四步：在打开的网页中选择要绑定到的账户，并点击「确认绑定」。

![我的主机：主机绑定](/img/screenshots/features/runtimes/new/binding.png)

---

就这么简单，这时您已经成功创建了一台腾讯云主机并和 DaoCloud 账户成功绑定了。您可以在主机列表中找到这台主机。

![腾讯云：绑定成功](/img/screenshots/features/runtimes/new/qcloud-success.png)

> **Aliyun 和 UCloud 即将上线。**

<!-- ##### Aliyun -->

<!-- ##### UCloud -->

#### 下一步

至此，您已经掌握了如何在 DaoCloud 上添加一台自有主机。

下面您可以：

* 了解如何对自有主机进行管理：参考[管理主机](management.md)。
* 了解如何将应用部署到我的主机：参考[应用部署](../deployment.md)。

<!-- TODO: 部署部分完成后更新链接 -->

## 自有主机

混合式容器主机（自有主机）管理服务是国内首个支持包括公有云、私有云、虚拟化平台和物理服务器，并且可跨云跨网进行混合式管理的容器服务平台，该项服务能够与 DaoCloud 云端持续集成、镜像构建、应用发布流程无缝对接，实现容器化应用在公有云、私有云的灵活交付。

### 功能描述

混合式容器主机管理服务是 DaoCloud 的一项独创技术，使用这项功能，DaoCloud 用户可以通过一致的界面和流程，管理在公有云、私有云甚至是企业防火墙之后的各类物理和虚拟主机资源，把这些资源汇聚成跨云跨网的分布式容器主机资源池，实现容器化应用的高速部署和灵活调度。DaoCloud 已经支持包括微软 Azure、亚马逊 AWS、阿里云、UCloud、青云等国内外一线公有云厂商，并且正在帮助企业客户实施内网私有云容器集群的混合式管理，为企业客户打造能够支持微服务和轻应用的新一代混合式容器云平台。

### 添加主机

请参考：[添加主机](new.md)。

### 管理主机

请参考：[管理主机](management.md)。

### 常见问题

问：容器服务启动后，如何访问容器内的应用？

答：不同于 DaoCloud 提供的云端容器管理集群，您需要在您的自有主机上映射容器端口和主机的端口，必要时开需要开启防火墙端口。

---

问：部署在自有主机上的容器应用，如何使用数据库服务？

答：您可以在自有主机上以容器的方式部署 MySQL 等数据库服务，或使用您的 IT 环境中已有的数据库服务，通过环境变量的方式，让容器内的应用访问您的数据服务。

---

问：自有主机环境，跟 DaoCloud 提供的云端容器运行环境，有何区别？

答：DaoCloud 提供的云端容器运行环境，是一套完备的容器化应用管理平台，提供了包括应用起停、服务集成、弹性扩展、性能监控、日志管理、域名绑定等应用生命周期服务，具备了 PaaS 平台的全部功能。

自有主机是由用户进行管理维护的主机，DaoCloud 通过先进的跨云跨网技术，将 DaoCloud 云端持续集成、镜像构建功能与用户自有资源无缝对接，实现混合式应用交付。应用部署到自有主机后，用户需要自行完成网络端口映射、负载均衡等操作。

---

问：如果把自有主机关机，DaoCloud 会如何处理？

答：自有主机关机后，DaoCloud 会显示主机处在失联状态，您开机后，会自动重新建立连接。

---

问：在自有主机上安装的主机监控程序起什么作用？

答：主机监控程序负责自有主机与 DaoCloud 云端管理平台的通信工作，并且通过调用自有主机上的 Docker API 来完成容器的管理工作。

---

问：在自有主机部署应用，或者进行容器管理时，响应速度较慢，是什么原因？

答：响应速度取决于自有主机的网络带宽，如果网络速度较慢，可能会引起镜像下载超时，与 DaoCloud 云端服务链接中断等问题。请确保您的自有主机接入高速稳定的网络，或在 DaoCloud 操作界面选择重试、重新部署或刷新页面。


The **Grav Administration Panel** plugin for [Grav](http://github.com/getgrav/grav) is a web GUI (graphical user interface) that provides a convenient way to configure Grav and easily create and modify pages.  This will remain a totally optional plugin, and is not in any way required or needed to use Grav effectively.  In fact, the admin provides an intentionally limited view to ensure it remains easy to use and not overwhelming.  Power users will still prefer to work with the configuration files directly.

>>>> This plugin is currently in development as is to be considered a **beta release**.  As such, use this in a production environment **at your own risk!**.

![](admin-dashboard.png)

### Features

* User login with automatic password encryption
* Forgot password functionality
* Logged-in-user management
* One click Grav core updates
* Dashboard with maintenance status, site activity and latest page updates
* Ajax-powered backup capability
* Ajax-powered clear-cache capability
* System configuration management
* Site configuration management
* Normal and Expert modes which allow editing via forms or YAML
* Page listing with filtering and search
* Page creation, editing, moving, copying, and deleting
* Powerful syntax highlighting code editor with instant Grav-powered preview
* Editor features, hot keys, toolbar, and distraction-free fullscreen mode
* Drag-n-drop upload of page media files including drag-n-drop placement in the editor
* One click theme and plugin updates
* Plugin manager that allows listing and configuration of installed plugins
* Theme manager that allows listing and configuration of installed themes
* GPM-powered installation of new plugins and themes
* ACL for admin users access to features

### Support

We have tested internally, but we hope to use this public beta phase to identify, isolate, and fix issues related to the plugin to ensure it is as solid and reliable as possible.

For **live chatting**, please use the dedicated [Gitter Chat Room for the admin plugin](https://gitter.im/getgrav/grav-plugin-admin) for discussions directly related to the admin plugin.

For **bugs, features, improvements**, please ensure you [create issues in the admin plugin GitHub repository](https://github.com/getgrav/grav-plugin-admin).

### Installation

First ensure you are running the latest **Grav {{ grav_version }} or later**.  This is required for the admin plugin to run properly (`-f` forces a refresh of the GPM index).

```
$ bin/gpm selfupgrade -f
```

The admin plugin actually requires the help of 3 other plugins, so to get the admin plugin to work you first need to install **admin**, **login**, **forms**, and **email** plugins.  These are available via GPM, and because the plugin has dependencies you just need to proceed and install the admin plugin, and agree when prompted to install the others:

```
$ bin/gpm install admin
```

### Creating a User

With Grav {{ grav_version }}, you can now create a user account with the CLI:

```
$ bin/grav newuser
```

Simply follow along with the prompts to create the user account.

Alternatively, you can create a `user/accounts/admin.yaml` file manually. This filename is actually the **username** that you will use to login. The contents will contain the other information for the user.

```
password: 'password'
email: 'youremail@mail.com'
fullname: 'Johnny Appleseed'
title: 'Site Administrator'
access:
  admin:
    login: true
    super: true
```

Of course you should edit your `email`, `password`, `fullname`, and `title` to suit your needs.

### Manual Installation

Manual installation is not the recommended method of installation, however, it is still possible to install the admin plugin manually. Basically, you need to download each of the following plugins individually:

* [admin](https://github.com/getgrav/grav-plugin-admin/archive/develop.zip)
* [login](https://github.com/getgrav/grav-plugin-login/archive/develop.zip)
* [form](https://github.com/getgrav/grav-plugin-form/archive/develop.zip)
* [email](https://github.com/getgrav/grav-plugin-email/archive/develop.zip)

Extract each archive file into your `user/plugins` folder, then ensure the folders are renamed to just `admin/`, `login/`, `form/`, and `email/`.  Then proceed with the **Usage instructions below**.

### Usage

By default, you can access the admin by pointing your browser to `http://yoursite.com/admin`. You can simply log in with the `username` and `password` set in the YAML file you configured earlier.

> After logging in, your **plaintext password** will be removed and replaced by an **encrypted** one.

### Standard Free & Paid Pro Versions

If you have been following the [blog](http://getgrav.org/blog), [Twitter](https://twitter.com/getgrav), [gitter.im chat](https://gitter.im/getgrav/grav), etc., you probably already know now that our intention is to provide two versions of this plugin.

The **standard free version**, is very powerful, and has more functionality than most commercial flat-file CMS systems.

We also intend to release in the near future a more feature-rich **pro version** that will include enhanced functionality, as well as some additional nice-to-have capabilities. This pro version will be a **paid** plugin the price of which is not yet 100% finalized.
