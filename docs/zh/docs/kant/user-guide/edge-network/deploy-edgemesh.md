# 部署 EdgeMesh 应用

在使用应用网格能力前，需要先部署 EdgeMesh 应用，本文介绍具体操作流程。

## 前置准备

1. 去除 K8s master 节点的污点

    如果 K8s master 节点上有运行业务应用，并且需要访问集群节点上的其他应用，
    需要先去除 K8s master 节点的污点，执行如下命令。

    ```shell
    kubectl taint nodes --all node-role.kubernetes.io/master-
    ```

    !!! note
    
        如果 K8s master 节点上没有部署需要被代理的应用，可以跳过这一步。

2. 给 Kubernetes API 服务添加过滤标签

    正常情况下，为避免 EdgeMesh 去代理 Kubernetes API 服务，因此需要给它添加过滤标签，
    更多信息请参考[服务过滤](https://edgemesh.netlify.app/zh/advanced/hybird-proxy.html#%E6%9C%8D%E5%8A%A1%E8%BF%87%E6%BB%A4)。

    ```shell
    kubectl label services kubernetes service.edgemesh.kubeedge.io/service-proxy-name=""
    ```

## Helm 安装

操作步骤如下：

1. 选择左侧导航栏的 __容器管理__ -> __集群列表__ ，进入集群列表页面，点击 __集群名称__ ，进入集群详情页。

2. 选择左侧菜单 __Helm 应用__ -> __Helm 模板__ ，在 addon 仓库下找到 __edgemesh__ 插件。

    ![Helm 模板](../../images/deploy-edgemesh-01.png)

3. 点击 __edgemesh__ 条目，进入模板详情页。

4. 在页面右上角选择 EdgeMesh 版本，点击 __安装__ 按钮，进入 EdgeMesh 安装页面。

    ![edgemesh 安装](../../images/deploy-edgemesh-02.png)

5. 填写 edgemesh 基础配置。

    - 名称：小写字母、数字字符或 __-__ 组成，并且必须以字母开头及字母或数字字符结尾。
    - 命名空间：EdgeMesh 应用所在命名空间。如果命名空间没有创建，可以选择 __新建命名空间__ 。
    - 版本：结合实际业务需求，选择想要安装的 EdgeMesh 版本。
    - 失败删除：开启后，将默认同步开启安装等待。将在安装失败时删除安装。
    - 就绪等待：启用后，将等待应用下所有关联资源处于就绪状态才标记应用安装成功。
    - 详细日志：开启安装过程日志的详细输出。

    ![Helm 模板](../../images/deploy-edgemesh-03.png)

6. YAML 参数配置。

!!! note

    在默认的 YAML 配置下，需要补充设置认证密码（PSK）和中继节点（Relay Node），否则会导致部署失败。

**PSK 和 Relay Node 设置说明**

```yaml
  # PSK：是一种认证密码，确保每个 edgemesh-agent 只有当拥有相同的 “PSK 密码” 时才能建立连接，更多信息请参考
  # [PSK](https://edgemesh.netlify.app/zh/guide/security.html)。建议使用 openssl 生成，也可以设置成自定义的随机字符串。

  在节点上执行如下命令生成 PSK：

  kubectl taint nodes --all node-role.kubernetes.io/master-

  # Relay Node：是指在网络通信中转发数据包的节点。它在通信的源节点和目标节点之间起到桥接的作用，
  # 帮助数据包在网络中传输并绕过某些限制或障碍，EdgeMesh 中通常为云上节点，也可以添加多个中继节点。
```

**参考示例**

```yaml
global:
  imageRegistry: docker.m.daocloud.io
agent:
  repository: kubeedge/edgemesh-agent
  tag: v1.14.0
  affinity: {}
  nodeSelector: {}
  tolerations: []
  resources:
    limits:
      cpu: 1
      memory: 256Mi
    requests:
      cpu: 0.5
      memory: 128Mi
  psk: JugH9HP1XBouyO5pWGeZa8LtipDURrf17EJvUHcJGuQ=

  relayNodes:
   - nodeName: masternode ## your relay node name
    advertiseAddress:
    - x.x.x.x ## your relay node ip

  modules:
    edgeProxy:
      enable: true
    edgeTunnel:
      enable: true
```

## 检验部署结果

部署完成后，可以执行以下操作检查 EdgeMesh 应用是否部署成功。

1. 选择左侧导航栏的 __容器管理__ -> __集群列表__ ，进入集群列表页面，点击 __集群名称__ ，进入集群详情页。

1. 选择左侧菜单 __Helm 应用__ -> __Helm 应用__ ，进入 Helm 应用列表页面。

1. 查看 Helm 应用的状态，当前状态为 __已部署__ 表示 EdgeMesh 应用部署成功。

 ![EdgeMesh 部署成功](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kant/images/deploy-edgemesh-12.png)

下一步：[创建服务](service.md)
