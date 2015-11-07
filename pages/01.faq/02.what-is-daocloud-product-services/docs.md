---
title: 'DaoCloud 提供什么产品和服务？'
taxonomy:
    category:
        - docs
---

开发运维一体化

DaoCloud 对接 GitHub、Coding、GitCafe 等国内外代码托管库，采用云端 SaaS 化服务，帮助开发者实现自动化持续集成测试和 Docker 容器镜像构建。DaoCloud 镜像构建服务基于全球分布式网路，构建速度极快，提供私有镜像存储空间，为容器化交付和跨团队合作奠定了基础。

容器云平台

DaoCloud 实现了支持一键部署的容器云平台，以非常直观的方式实现应用的负载均衡、私有域名绑定、性能监控等应用生命周期服务，是实现微服务架构、轻量级应用部署和运维的理想平台。该平台目前部署在公有云环境，目前为开发者提供一定数量的免费容器资源。

混合云解决方案

国内首个支持包括公有云、私有云、虚拟化平台和物理服务器，并且可跨云跨网进行混合式管理的容器服务平台，该项服务能够与 DaoCloud 云端持续集成、镜像构建、应用发布流程无缝对接，实现容器化应用在公有云、私有云的灵活交付。

DaoCloud平台的创新

DaoCloud 平台与之前的云平台技术相比，创新性体现在以下几点：

首先，DaoCloud 采用 Docker 轻量级虚拟化技术，针对分布式应用的痛点，推出支持多种语言和后台服务的 DaoCloud 持续集成服务。持续集成是分布式系统开发必不可少的关键测试方式，传统的继续集成平台建设复杂，费时费力。SaaS 化的持续集成服务，是 DaoCloud 在国内的首创，用户在提交代码后，能够触发自动化测试，检测代码质量并及早发现问题，为分布式服务发布前的质量控制提供了完整而且便捷的解决方案。

第二，容器化应用发布，离不开 Docker 镜像的构建。Docker 镜像的构建需要访问大量互联网资源，在国内不同的网络环境内受限较大。DaoCloud 提供的创新镜像构建过程，包含了大量的网络层优化，为用户提供了基于集群环境的高速构建能力，极大的提升了发布效率。同时，依托 DaoCloud 遍布全球的云服务节点，能够帮助用户实现秒级的全球业务启停。

最后，应用到云端的部署和发布管理，在快速迭代和持续交付的时代，是很多开发项目的痛点。DaoCloud 采取了一键部署上云端的 Docker 化 PaaS 技术，允许用户在多种基础云平台之间灵活选择，以非常直观的方式实现应用的负载均衡、私有域名绑定、性能监控等应用生命周期服务。

为什么要使用 DaoCloud？

DaoCloud 采用了对网络、镜像缓存等方面进行了大量优化的 Docker 镜像构建过程，在 DaoCloud 平台构建 Docker 镜像，比在本机环境快 5 ~ 10 倍。 在快速迭代的开发场景下，加速「Code to Cloud」的过程，避免繁琐的手工构建，无需关心云主机的配置细节。 以 Docker 容器作为软件的交付件在 DaoCloud 应用市场发布应用可以快速的为客户提供演示环境、获取产品反馈、抓住市场机会。 更高效率的利用云资源：相比使用虚拟机成本更低、应用启停更快、弹性能力更好。

代码构建

与用户在 Github 上的 Repository 一一对应。在创建项目时，用户需要通过 OAuth 授权 DaoCloud 应用访问 GitHub，获得代码的读取权限，并根据需要设置 WebHook。「代码构建」的主要目的是完成 Docker 镜像的构建，「代码构建」的输入是 GitHub 代码仓库，与项目目录中预先编写好的 Dockerfile；「代码构建」的输出是构建完成的 Docker 镜像。在构建的过程中，可以根据设定执行 CI 以检测代码是否通过集成测试。

镜像仓库

是 Docker 镜像存储的场所，也是 Docker 化方式交付软件的「目的地」。在技术上，「镜像仓库」是一个 Docker Registry，目前 DaoCloud 支持 DaoCloud 自带的镜像仓库，也计划支持 Docker Hub 和企业私有 Registry。「镜像仓库」中的陈列的项目分为两类，一类是用户的私有项目，是在「代码构建」中配置并完成 Docker 镜像的构建后所产生的各个版本镜像的存储库；另一类是公有示例项目，这些是我们预制的一些比较成熟的 Docker 化打包软件，可以直接在云上以 Docker 化的方式部署和运行。

服务集成

应用的运行离不开后台的服务，随着互联网应用复杂度的提升，应用对服务的需求，从单一的关系型数据库，逐渐过渡到多种类型、自建和 SaaS 化服务相结合的模式。在 DaoCloud 系统中，「服务集成」提供了用户配置和初始化各类后台服务的功能，服务市场汇集了一系列来自于 DaoCloud 以及其他第三方 SaaS 提供商的热门应用服务，用户可以按需配置。配置初始化完成后的服务，会列出在「我的服务」的选项卡中，供后续与应用绑定。「服务集成」包括了如下三个类别：

Dao 服务：由 DaoCloud 运维的数据服务，目前支持 MongoDB、MySQL、Redis 和 InfluxDB。

第三方「SaaS 服务」，集成了 New Relic 等服务，可以很容易与应用绑定。

我的服务：由用户创建的服务实例。

加速器

即 DaoCloud Mirror 服务，基于 Docker Registry 的 Mirror 机制，只需要在 Docker 守护进程的配置文件中加入 Mirror 参数，即可在全局范围内透明的访问官方的 Docker Hub，避免了对D ockerfile 镜像引用来源的修改。「加速器」章节会对此进行详细说明。

DaoCloud 官方于 2015 年 3 月 19 日宣布 Docker Hub Mirror 服务永久免费。

用户中心

用户可进行用户属性的更改、设置以及关联第三方服务。

Grav has intentionally been designed with few requirements.  You can easily run Grav on your local computer, as well as 99% of all Web hosting providers. If you have a pen handy, jot down the following Grav system requirements:

1. Webserver (Apache, Nginx, LiteSpeed, IIS, etc.)
2. PHP 5.4 or higher
3. hmm... that's it, (but please look at php requirements for a smooth experience)!

Grav is built with plain text files for your content. There is no database needed.

>>> A PHP user cache such as APC, APCU, XCache, Memcache, Redis is highly recommended for optimal performance.  Not to worry though, these are usually already part of your hosting package!

## Web Servers

Even though technically you do not need a standalone Web server, it is better to run one, even for local development. Luckily there are many options depending on your platform:

### Mac

* OS X 10.9 Mavericks already ships with the Apache Web server and PHP 5.4, so job done!
* [MAMP/MAMP Pro](http://mamp.info) comes with Apache, MySQL and of course PHP.  It is a great way to get more control over which version of PHP you are running, setting up virtual hosts, plus other useful features such as automatically handling dynamic DNS.

### Windows

* [XAMPP](https://www.apachefriends.org/index.html) provides Apache, PHP, and MySQL in one simple package
* [EasyPHP](http://www.easyphp.org/) provides a personal Web hosting package as well as a more powerful developer version
* [MAMP for Windows](http://mamp.info) is a long-time Mac favorite, but now available for Windows.
* [IIS with PHP](http://php.iis.net/) is a fast way to run PHP on Windows.

### Linux

* Many distributions of Linux already come with Apache and PHP built-in, if it's not built-in, then usually the distribution provides a package manager where you can install Apache and PHP without much hassle.  More advanced configurations should be investigated with the help of a good search engine.

>>> Running Grav with the built-in Web server provided with PHP 5.4 is explained in more detail in the next chapter.

### Apache Requirements

Even though most distributions of Apache come with everything needed, for the sake of completeness, here is a list required Apache modules:

* `mod_cache`
* `mod_expires`
* `mod_headers`
* `mod_rewrite`
* `mod_ssl`

You should also ensure you have `AllowOveride All` set in the `<Directory>` and/or `<VirtualHost>` blocks so that the `.htaccess` file processes correctly and rewrite rules take effect.

### IIS Requirements

Although IIS is considered a webserver ready to 'run-out-of-box' there are some changes that need to be made.
To get **Grav** to run on an IIS server you need to install **URL Rewrite.** This can be accomplished using **Microsoft Web Platform Installer** from within IIS. You can also install URL Rewrite by going to [iis.net](http://www.iis.net/downloads/microsoft/url-rewrite).

### PHP Requirements

Most hosting providers and even local LAMP setups have PHP pre-configured with everything you need for Grav to run out of the box.  However, some windows setups, and even Linux distributions local or on VPS (I'm looking at you Debian!) ship with a very minimal PHP compile. Therefore, you may need to install or enable these PHP modules:

* `gd` (a graphics library used to manipulate images)
* `curl` (client for URL handling used by GPM)
* `openssl` (secure sockets library used by GPM)
* zip support (used by GPM)
* `mbstring` (multibyte string support)

For enabling `openssl` and (un)zip support you will need to find in the `php.ini` file of your Linux distribution for lines like:

  - `;extension=openssl.so`.
  - `;extension=zip.so`.

and remove the leading semicolon.

##### Optional Modules

* `apc` (PHP 5.4) or `apcu` (PHP 5.5+) for increased cache performance
* `opcache` (PHP 5.5+) for increased PHP performance
* `xcache` alternative to *apc*, not as fast, but still pretty good
* `yaml` PECL Yaml provides native yaml processing and can dramatically increase performance
* `xdebug` useful for debugging in development environment



### Permissions

For Grav to function properly your webserver needs to have the appropriate **file permissions** in order to write logs, caches, etc.  When using either the [CLI](/advanced/grav-cli) or [GPM](/advanced/grav-gpm), the user running PHP from the command line, also needs to have the appropriate permissions to modify files.

By default, Grav will install with `644` and `755` permissions for files and folders respectively. Most hosting providers have configurations that ensure the webserver running PHP will allow you to create and modify files within your user account.  This means that Grav runs **out-of-the-box** on the vast majority of hosting providers.

However, if you are running on a dedicated server, or even your local environment, you may need to adjust permissions to ensure you **user** and your **webserver** can modify files as needed.  There are a couple of approaches you can take.

1. In a **local development environment**, you can usually configure your webserver to run under you user profile.  This way the web server will always allow you to create and modify files.

2. Change the **group permissions** on all files and folders so that the webserver's group has write access to files and folders while keeping the standard permissions.  This requires a few commands to make this work (note: adjust `www-data` to be the group your apache runs under [`www-data`, `apache`, `nobody`, etc.]):

```
chgrp -R www-data .
find . -type f | xargs chmod 664
find . -type d | xargs chmod 775
find . -type d | xargs chmod +s
umask 0002
```



## Recommended Tools

### Text Editors

Although you can get away with Notepad, Textedit, Vi, or whatever default text editor comes with your platform, we recommend using a good text editor with syntax highlighting to make things easier.  Here are some recommended options:

1. [SublimeText](http://www.sublimetext.com/) - OS X/Windows/Linux - A commercial developer's editor, but well worth the price. Very powerful especially combined with plugins such as [Markdown Extended](https://sublime.wbond.net/packages/Markdown%20Extended), [Pretty YAML](https://sublime.wbond.net/packages/Pretty%20YAML), and [PHP-Twig](https://sublime.wbond.net/packages/PHP-Twig).
2. [Atom](http://atom.io) - OS X/Windows - A new editor developed by Github. It's free and open source.  It is similar to Sublime, but does not have the sheer depth of plugins available yet.
3. [Notepad++](http://notepad-plus-plus.org/) - Windows - A free and very popular developer's editor for Windows.
4. [Bluefish](http://bluefish.openoffice.nl/index.html) - OS X/Windows/Linux - A free, open source text editor geared towards programmers and web developers.

### Markdown Editors

Another option if you primarily work with just creating content, is to use a **Markdown Editor**. These often are very content-centric and usually provide a **live-preview** of your content rendered as HTML.  There are literally hundreds of these, but some good options include:

1. [LightPaper](http://www.ashokgelal.com/lightpaper-for-mac) - OS X - Free, clean, powerful.  Our markdown editor of choice on the Mac.
2. [MarkDrop](http://culturezoo.com/markdrop/) - OS X - $5, but super clean and and Droplr support built-in.
3. [MarkdownPad](http://markdownpad.com/) - Windows - Free and Pro versions. Even has YAML front-matter support.  A very solid solution for Windows users .

### FTP Clients

Although there are many ways to deploy **Grav**, the simplest is to simply copy your local site to your hosting provider.  The easiest way to accomplish this is with an [FTP Client](http://en.wikipedia.org/wiki/File_Transfer_Protocol).  There are many available, but some recommended ones include:

1. [Transmit](http://panic.com/transmit/) - OS X - The de facto FTP/SFTP client on OS X.  Easy to use, fast, folder-syncing and pretty much anything else you could ask for.
2. [FileZilla](https://filezilla-project.org/) - OS X/Windows/Linux - Probably the best option for Windows and Linux users. Free and very powerful (but very ugly on the Mac!).
3. [Cyberduck](http://cyberduck.io/) - OS X/Windows - A decent free option for both OS X and Windows users.  Not as full featured as the others.
4. [ForkLift](http://www.binarynights.com/forklift/) - OS X - A solid alternative to Transmit, and slightly cheaper to boot.


