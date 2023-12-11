# 集成 Harbor 实现镜像安全扫描

本文将介绍如何在流水线中集成 Harbor 并实现镜像安全扫描。

## 在 Harbor 中开启自动扫描镜像

1. 登录 Harbor，点击一个具体的项目。

    ![harbor](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/harbor01.png)

2. 选择 **配置管理** 页签，勾选 **自动扫描镜像** 。

    ![harbor](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/harbor02.png)

## 在应用工作台配置流水线

1. 在应用工作台，创建一条流水线，参考[快速创建流水线](deploy-pipeline.md)，配置完毕后点击 **立即执行** 。

    ![harbor](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/harbor03.png)

1. 在弹出的对话框中输入上述 Harbor 配置的项目中的镜像仓库地址。

    ![harbor](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/harbor04.png)

1. 等待流水线执行成功。

## 在 Harbor 中查看镜像安全扫描信息

在 Harbor 中依次访问  **项目**  ->  **镜像仓库** ，查看镜像的漏洞信息。

![harbor](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/harbor05.png)
