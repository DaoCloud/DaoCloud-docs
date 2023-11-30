# 使用流水线实现代码扫描

代码仓库中的源代码作为软件的最初原始形态，其安全缺陷是导致软件漏洞的直接根源。
因此，通过代码扫描分析发现源代码中的安全缺陷是降低软件潜在漏洞的一种重要方法。

例如，SonarQube 是一款代码自动审查工具，用于检测项目代码中的 bug 错误，提高测试覆盖率等。
它可以与项目中现有的工作流程集成，以便在项目分支和拉取请求之间进行连续的代码检查。

本文将介绍如何在流水线中集成 SonarQube 来实现代码扫描能力。

## 工作空间集成 SonarQube

请确保已有 SonarQube 环境，并且与当前环境网络联通无问题。

1. 进入`工具链集成` 页面，点击`工具链集成`按钮。

    ![tool01](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/tool01.png)

2. 参考以下说明，配置相关参数：

    - 工具：选择一个工具链类型进行集成。
    - 集成名称：集成工具的名称，不可重复。
    - SonarQube 地址：可访问工具链的地址，以 http://, https:// 开头的域名或 IP 地址。
    - Token：在 SonarQube 生成管理员令牌（Token），操作路径为：My Account -> Profile -> Security -> Generate -> Copy

    ![scan](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/sonarqube11.png)

3. 点击`确定`，集成成功返回到工具链列表页面。

## 创建流水线

1. 在流水线页面，点击`创建流水线`。

    ![scan](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/scanp01.png)

2. 选择`自定义创建`。

    ![scan](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/scanp02.png)

3. 输入名称，其他可使用默认值，点击`确定`。

    ![scan](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/sonarqube12.png)

## 编辑流水线步骤

1. 点击一个流水线进入其详情页面，在右上角点击`编辑流水线`。

    ![scan](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/sonarqube13.png)

2. 配置全局设置：

    ![scan](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/sonarqube14.png)

3. 图形化界面定义阶段一 `git clone` 如下配置：

    ![scan](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/sonarqube15.png)

4. 图形化界面定义阶段二 `SonarQube analysis` 如下配置：

   - SonarQube 实例：选择上述步骤中集成的 SonaQube 实例。
   - 代码语言：由于不同代码语言对应的 SonaQube 的扫描命令不同，如果 java 语言，请选择 maven，其他语言则选择其他，本示例选择其他。
   - 项目：定义在 SonarQube 中扫描的项目
   - 扫描文件：需要扫描代码仓库中文件目录地址

    ![scan](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/sonarqube16.png)
    
    ![scan](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/sonarqube17.png)

5. 保存后立即运行该流水线，并等待流水线运行成功。

## 查看代码扫描结果

1. 等待流水线运行成功后，在流水线详情页面点击`代码质量检查`。

    ![scan](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/sonarqube18.png)

2. 查看代码扫描结果，点击`查看更多`可前往 SonarQube 后台查看更多扫描信息。

    ![scan](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/sonarqube19.png)
