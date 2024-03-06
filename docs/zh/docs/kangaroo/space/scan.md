# 镜像扫描

镜像被下载后可以直接使用，为用户提供了很多方便，但是不一定安全，可能被恶意植入后门。用户需要扫描下载的镜像，获知镜像安全信息。

在 (DevOps) CI/CD 过程中，镜像被直接推送到镜像仓库，无法保证镜像的安全性，存在持续安全集成自动扫描的需求。

安全扫描是一种主动的防范措施，能有效避免黑客攻击行为，做到防患于未然，建议定时/手动扫描镜像。

（投产）容器到生产环境之后，生产环境对容器的安全性要求较高，需要容器的安全性得到保证，因此使用镜像运行容器前，一定要对镜像进行扫描，从而提高安全性。

最后扫描结果应提供更多有关纠正措施的指导。当用户收到容器镜像受到漏洞困扰的坏消息时，需要为自己找出修复方法，漏洞来自哪里？可以做些什么来解决问题？

## 镜像扫描特性

目前 DCE 5.0 的镜像仓库模块支持以下几种扫描镜像：

- 托管的 Harbor 仓库支持 Trivy 扫描。
- 原生的 Harbor 仓库支持 Clair 和 Trivy 扫描，具体取决于用户安装了什么插件。

用户在扫描镜像索引时，会同步扫描被索引的所有镜像，扫描结果为被索引镜像的扫描结果之和。

## 手动扫描镜像

对于关联和集成的仓库，将出现在镜像列表中。您可以按需手动扫描某些镜像。

1. 进入镜像仓库的 __镜像列表__ 中，选择一个实例和镜像空间，点击某一个镜像。

    ![镜像列表](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/scan01.jpg)

2. 在镜像详情列表中，点击列表右侧的 __⋮__ ，在弹出菜单中选择 __扫描__ 。

    ![扫描](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/scan02.jpg)

3. 系统开始扫描镜像，通常状态依次为 __排队中__ 、 __扫描中__ 、 __扫描完成__ 。

    ![排队中](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/scan03.jpg)

    ![扫描中](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/scan04.jpg)

    ![扫描完成](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/scan05.jpg)

    扫描状态包括：

    - 未扫描：镜像从未被扫描过。
    - 不支持：此镜像不支持扫描。
    - 排队中：扫描任务已安排但尚未运行。
    - 扫描中：扫描任务正在进行中，并显示进度条。
    - 查看日志：扫描任务未能完成。点击 __查看日志__ 以查看相关日志。
    - 扫描完成：扫描任务成功完成。

4. 扫描完成后，将光标悬浮在扫描完成的比例条上，可以查看扫描详情。

    ![扫描完成](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/scan06.jpg)

## 扫描原生 Harbor 镜像

集成的原生 Harbor 仓库，支持按 Clair 或 Trivy 进行扫描。

具体操作步骤为：

1. 以平台管理员登录镜像仓库，点击左侧底部的 __仓库集成__ 。

    ![仓库集成](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/harbor01.jpg)

2. 在集成的仓库列表中，光标悬浮于某个仓库上，点击 __原生 Harbor__ 图标。

    ![仓库集成](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/harbor02.jpg)

3. 跳转到原生 Harbor，参阅[扫描 Harbor 镜像](https://goharbor.io/docs/2.1.0/administration/vulnerability-scanning/scan-individual-artifact/)。
