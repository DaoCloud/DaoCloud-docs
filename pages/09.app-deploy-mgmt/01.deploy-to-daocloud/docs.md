---
title: '向 DaoCloud 云平台发布应用'
taxonomy:
    category:
        - docs
process:
    twig: true
---

## 应用部署的步骤

1. 发布应用，首先需要从应用商店选择一个版本的 Docker 镜像。
2. 点击「镜像仓库」。
3. 点击项目名称，从属性列表中选择一个要发布的版本，点击「部署」，也可以直接点击屏幕右上角的「部署最新版本」。
4. 在部署的页面中，需要指定容器实例的名称。
5. 目前 DaoCloud 为用户提供格式为 `*.daoapp.io` 的二级域名，域名的默认构成方式为项目名称和容器名称的组合，中间用中划线连接。
6. 选择容器资源，选择部署目标，高级选项中可以做一些更细致的微调。
7. 点击部署。

部署开始后，页面上部的状态会显示「启动中」。部署采用 Docker 镜像的方式，部署和启动速度是超乎您的想象的。

> 注意：部署完成后的应用实例，并不会在镜像仓库中列出。因为我们认为，镜像仓库是 docker 化软件交付件的静态存储展示区域。您的应用实例，会在首页以图标的方式显示。请您牢记这一点，避免迷路。

## 绑定服务

1. 应用启动后，可以点击 URL 访问。走到这一步，我们只是创建了应用 Docker 容器的运行实例，绝大多数情况下，还需要与服务绑定。
2. 点击应用实例，在属性栏中点击「服务&设置」选项卡，我们会看到服务实例的清单和环境变量的清单。
3. 绑定服务需要知道应用预设的`环境变量别名`，并根据服务实例的实际参数，填写这些环境变量，如果您的代码时 Fork 来的，请仔细阅读代码的 README。
4. 在绑定服务时，请检查您在程序代码中定义的环境变量名，确保使用正确的环境变量名，与服务的对应参数进行关联。

![](http://blog.daocloud.io/wp-content/uploads/2015/03/55.jpg)

应用运行后，您还可以查看性能曲线、日志等等信息。


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
