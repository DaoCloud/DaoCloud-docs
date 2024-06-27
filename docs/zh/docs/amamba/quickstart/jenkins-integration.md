# 在物理机/虚拟机上集成 Jenkins

## 风险

由于 Jenkins 部署在物理机或虚拟机中，集成之后会有一些基于 K8s 的功能可能无法使用。

- 由于应用工作台将流水线放在 WorkspaceID 同名的文件夹下，这会导致已经存在的流水线无法被发现和展示在工作台的界面中
- 所有基于 casc 的配置都会失效，包括 SonarQube 集成、全局邮件配置
- 如果 Jenkins 不是使用 KubernetesCloud 运行，那么相关的语法会失效，需要手动调整 Jenkinsfile

## 插件

### 必需的插件

安装 Jenkins 时会自动安装以下依赖的插件：

- [Folders Plugin](https://plugins.jenkins.io/cloudbees-folder)
- [Pipeline: REST API Plugin](https://plugins.jenkins.io/pipeline-rest-api/)
- [Pipeline: Declarative](https://plugins.jenkins.io/pipeline-model-definition/)
- [Pipeline: Declarative Extension Points API](https://plugins.jenkins.io/pipeline-model-extensions)
- [Pipeline: Model API](https://plugins.jenkins.io/pipeline-model-api)
- [Git](https://plugins.jenkins.io/git)
- [Blue Ocean](https://plugins.jenkins.io/blueocean)
- [Generic Webhook Trigger](https://plugins.jenkins.io/generic-webhook-trigger)
- [Sonar(SonarQube Scanner for Jenkins)](https://plugins.jenkins.io/sonar)
- [generic-event](https://plugins.jenkins.io/generic-event)

### 可选的插件

- [Kubernetes 插件](https://plugins.jenkins.io/kubernetes)：如果希望流水线运行在 K8s 集群上，则需要安装此插件
- [Docker 插件](https://plugins.jenkins.io/docker-plugin)：如果希望流水线以容器的形式与物理机隔离运行，则需要安装此插件
- [Chinese 插件](https://plugins.jenkins.io/localization-zh-cn)：这是中文社区提供的汉化插件

## 配置节点

有关物理机节点的准备工作，请参阅 [Using Jenkins agents](https://www.jenkins.io/doc/book/using/using-agents/)。

## Jenkins 配置

### EventDispatcher

首先确保 generic-event 插件正常安装并且已经启用。  
查看 amamba-devops-server：

```shell
# 获取 amamba-devops-server 的 svc
kubectl get svc amamba-devops-server -n amamba-system

NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)            AGE
amamba-devops-server   ClusterIP   10.233.45.104   <none>        80/TCP,15090/TCP   230d
```

要确保 Jenkins 可以正常和 amamba-devops-server 通信，通过 NodePort 或 LB 暴露出来，然后 host 填对应 IP。

!!! note

    此操作不太安全，这个服务不适合直接暴露出去。

将 amamba-devops-server 的地址填入到 Jenkins 系统管理配置的 Event Receiver 输入框中，可参考以下格式。

```text
http://<hostIP:Port>/apis/internel.amamba.io/devops/pipeline/v1alpha1/webhooks/jenkins
```

### SonarQube

有关 Sonarqube 的配置信息，参阅 [Jenkins 接入 Sonarqube](https://docs.daocloud.io/amamba/user-guide/pipeline/install-jenkins.html#jenkins_2)。

## 邮件配置

获取 Ghippo 的邮件配置。

```shell
kubectl get ghippoconfig smtp -n ghippo-system -o yaml
```

下面是一个简单的样例：

```yaml
apiVersion: ghippo.io/v1alpha1
kind: GhippoConfig
metadata:
  labels:
    k8slens-edit-resource-version: v1alpha1
  name: smtp
spec:
  from: test@163.com
  host: smtp.163.com
  password: test
  port: 25
  ssl: false
  starttls: false
  user: test@163.com
```

在 Jenkins 里配置邮件服务。  
进入系统管理系统配置，输入管理员邮件地址 `test@163.com`，设置 SMTP 邮件服务器 `smtp.163.com`，
选择 SMTP 认证填入用户名和密码，设置 SMTP 端口，进入用户设置页面，设置邮件地址 `test@163.com`。
