# 使用流水线发布多云资源到Kairship

## 环境准备

### 代码仓库准备

1. 需要一个文件夹存放需要部署的资源的 yaml，并且包含Kairship的`PropagationPolicy`(在resourceSelectors中把期望的资源添加进去)
2. 一个 Dockerfile 用于构建镜像
3. 一个 token 用于在流水线中访问这个代码仓库(或者设置为公开)

### Kairship准备

1. 创建一个Kairship的实例，获取到对应实例的 Kubeconfig 证书，并且把证书添加到 Amamba 的流水线凭证当中
2. 在 Kairship 实例中创建一个多云命名空间

下图是获取证书的页面。

![getkarishipconfig.jpg](../images/get-kariship-config.jpg)

### Amamba准备

1. 确保 Kairship 实例的 kubeconfig 证书被创建到 Amamba 的流水线凭证中，并且确保已经同步到 Jenkins
2. 确保代码仓库的 token 已经被创建到Amamba的流水线凭证中，并且确保已经同步到 Jenkins (如果代码仓库为公开仓库则不需要，如果为集成进来的 Gitlab，只需要 Gitlab 的连接状态正常即可)
3. 现阶段 Amamba 无法获取 Kairship 创建的多云实例以及对应的多云命名空间(在创建流水线的时候)，现在只能手动编写 JenkinsFile

## 流水线创建

[使用到的 JenkinsFile 的仓库链接](https://github.com/amamba-io/amamba-examples)
根据仓库内的pipelines/guestbook-karisip.jenkinsfile创建对应的流水线，修改对应的参数运行即可。
对于部署到 Kairship 的流水线本质上是和其他流水线相同，关键在于 Amamba 无法获取到对应的 Kairship 的实例和对应的多云命名空间，我们只能根据 Kairship 提供的 kubeconfig 证书使用 kubectl 去部署资源。

## 运行结果

![kairshipresult](../images/kairship-result.png)