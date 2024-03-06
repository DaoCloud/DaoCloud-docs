# 镜像仓库 FAQ

本页列出使用镜像仓库时常见的一些问题和解决办法。

## DCE5.0标准版本中不能使用中间件部署

DCE 5.0标准版本中没有中间件，中间件属于白金版。

## 如何校验配置的中间件网络是否可连接

登录部署 Harbor 的目标集群，在任意节点中执行 `ping` 命令，测试是否能连接到中间件组件。

## 镜像空间列表看不到私有镜像

镜像仓库在 `v0.7.0-v0.7.3`、`v0.8.0` 版本系统存在一个 bug，会导致看不到私有镜像。

## 在使用中间件部署的 Minio 时

在使用中间件部署的 Minio 时，需要先手动通过 Minio 管理平台创建好 bucket。

## 仓库集成支持的 Harbor 最低版本

在仓库集成时因使用了 `Harbor` 的功能，对版本有一定要求，目前支持的已知最低版本为：`2.4.0`。更早的旧版本将不可用。

## 离线环境镜像扫描器失败

镜像扫描因为依赖漏洞数据，默认是去
[CVE 官网](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=kubernetes)获取漏洞数据。
如果是一个纯离线环境，则不能正常进行漏洞扫描，会执行失败。

![trivy](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/trivy-nodb.png)

## 创建托管 Harbor 时第一步集群校验通过后创建 Harbor 仍然出错

目前只校验了集群中是否有 `CRD`，没有校验 `harbor-operator` 服务，可能会出现不存在 `harbor-operator` 服务的情况，导致不能正确的创建 `Harbor`。

## 本地执行 `docker login {ip}` 之后报错

```text
Error response from daemon: Get "https://{ip}/v2/": x509: cannot validate certificate for {ip} because it doesn't contain any IP SANs
```

出现这个错误是因为 `registry` 是 `https` 服务，是使用了非签名证书或者不安全证书，就会提示这个错误，
解决办法是在 `/etc/docker/daemon.json` 配置文件中 `"insecure-registries"` 加入对应的 IP。

```json
"insecure-registries": [
  "{ip}",
  "registry-1.docker.io"
]
```

之后重启 `systemctl restart docker`。

## 创建托管 harbor 接入外部 PG、Redis，密码含有特殊字符 (!@#$%^&*) 之类的，服务启动失败

目前密码中不能有特殊字符，不然会出现服务启动失败的情况，可以使用大小写字母和数字组合的情况。

## Harbor Operator 安装不成功

`Harbor Operator` 安装不成功需要检查这几点，`cert-manager`是否安装成功，`installCRDs` 是否设置为`true`。
安装`Harbor operator` 的 __helm__ 任务是否成功。

## 创建托管 Harbor 可以使用 redis cluster 模式吗

目前 `Harbor` 仍然不能使用 `redis` cluster 模式。

## 私有镜像在非镜像仓库模块能看到吗？

镜像仓库是严格按照 DEC 5.0 的权限来执行的，在镜像仓库中某个用户必须要属于某个租户，
才能看到当前租户下的私有镜像空间，否则即使管理员也不能看到。

## 私有镜像绑定工作空间后不能查询到

私有镜像绑定工作空间后程序需要异步执行很多逻辑，所以不会马上能看到。
这个过程会受到系统的影响，如果系统响应较快，则异步执行较快，1 分钟内能看到。最长应该不会超过 5 分钟。

## 托管Harbor创建后能访问了但是状态依然不健康

目前托管 Harbor 页面上的状态和仓库集成的状态是二合一的，当两个状态都为健康的时候才是健康，
因此可能出现托管 `Harbor` 已经可以访问了，但是状态依然不健康，这种情况需要等一个服务探测周期，
一个探测周期是 10 分钟，在一个周期后就会恢复如初。

## 创建的托管仓库状态为不健康

![仓库不健康](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/img.png)

- A1：用户输入的数据库、Redis、S3 存储等信息有误，导致无法连接，可通过查看日志文件进行排查。
  现象主要是几个核心服务有 Pod 启动失败，可以通过查看日志进一步确认原因。

    ```shell
    kubectl -n kangaroo-lrf04 get pods
    ```

    ```none
    NAME                                                         READY   STATUS    RESTARTS   AGE
    trust-node-port-harbor-harbor-chartmuseum-57fdfb9cdc-qznwc   1/1     Running   0          20h
    trust-node-port-harbor-harbor-core-855f8df46c-cgqb9          1/1     Running   0          20h
    trust-node-port-harbor-harbor-jobservice-6b958dbc57-ks997    1/1     Running   0          20h
    trust-node-port-harbor-harbor-portal-5cf6bf659b-kj6gd        1/1     Running   0          20h
    trust-node-port-harbor-harbor-registry-5ccbf457c5-qrtx5      2/2     Running   0          20h
    trust-node-port-harbor-harbor-trivy-dbdc8945-xh6rv           1/1     Running   0          20h
    trust-node-port-nginx-deployment-677c74576-7kmh4             1/1     Running   0          20h
    ```

- A2：如果 A1 排查无误，排查 `harborcluster` 资源是否健康，如下命令查看 `harborcluster` 资源状态。

    ```shell
    kubectl -n kangaroo-lrf04 get harborclusters.goharbor.io
    ```

    ```none
    NAME              PUBLIC URL                 STATUS
    trust-node-port   https://10.6.232.5:30010   healthy
    ```

- A3：如果 A2 排查无误，在 `kpanda-global-cluster` 集群上排查 `registrysecrets.kangaroo.io`
  资源是否创建，以及 `status` 情况。

    提示: namespace 默认为 kangaroo-system。

    ```shell
    kubectl -n kangaroo-system get registrysecrets.kangaroo.io
    ```

    ```none
    NAME                        AGE
    inte-bz-harbor-1            34d
    ```

    ```shell
    kubectl -n kangaroo-system describe registrysecrets.kangaroo.io inte-bz-harbor-1
    ```

!!! tip

    - 上述 A1、A2 都在托管 Harbor 所在的集群上排查问题，目标集群通过如下页面路径查看： __仓库实例__ -> __概览__ -> __部署位置__ 
    - 上述 A3 在 `kpanda-global-cluster` 集群上验证。

## 创建 `Project` 或上传镜像后发现页面上的镜像空间和可用存储未增加

这是因为 UI 页面上在`托管 Harbor` 首页、仓库集成详情中的统计信息是异步获取的数据，会有一定的延迟，最长延迟为 `10` 分钟。

## 仓库集成后但状态为不健康

![仓库集成不健康](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/img_1.png)

首先确认实例是否真的健康，如果实例不健康，则需要排查实例的问题；
如果实例健康，则通过在 `kpanda-global-cluster` 集群上排查 `registrysecrets.kangaroo.io`
资源是否创建，并排查 `status` 情况，这样可以初步确认问题所在。

提示：namespace 默认为 kangaroo-system。

```shell
kubectl -n kangaroo-system get registrysecrets.kangaroo.io
```

```none
NAME                     AGE
trust-test-xjw           34d
```

```shell
kubectl -n kangaroo-system get registrysecrets.kangaroo.io trust-test-xjw -o yaml
```

```yaml
apiVersion: kangaroo.io/v1alpha1
kind: RegistrySecret
metadata:
  name: trust-test-xjw
  namespace: kangaroo-system
spec:
  ....
status:
  state:
    lastTransitionTime: "2023-03-29T03:27:31Z"
    message: 'Get "https://harbor.kangaroo.daocloud.io": dial tcp: lookup harbor.kangaroo.daocloud.io
      on 10.233.0.3:53: no such host'
    reason: RegistryHealthCheckFail
    status: "False"
    type: HealthCheckFail
```

## 仓库集成后，在镜像列表页面实例中不可查看

请确认仓库集成的资源是否健康，如果不健康是不会在镜像列表页面的实例列表中显示的。
确认方式请参考[仓库集成后不健康的确认方法](#_2)。

## 在 `Kpanda` 镜像选择器中选中一个私有 `Project` 镜像但部署时提示镜像拉取失败

- A1：能在镜像选择器中看到私有 `Project` 表明 `Project` 和 `Workspace` 已经进行了绑定，
  此时需要去镜像部署的目标集群 `namespace` 中确认是否生成名为 `registry-secret` 的 __secret__ 。

    ```shell
    kubectl -n default get secret registry-secret
    ```

    ```none
    NAME              TYPE                             DATA   AGE
    registry-secret   kubernetes.io/dockerconfigjson   1      78d
    ```

- A2：如果确认已经生成名为 `registry-secret` 的 __secret__ ，则需要确认 `secret` 中的 __dockerconfigjson__ 是否正确。

    ```shell
    kubectl get secret registry-secret -o jsonpath='{.data.*}'| base64 -d | jq
    ```

    ```json
    {
      "auths": {
        "127.0.0.1:5000": {
          "auth": "YWRtaW46SGFyYm9yMTIzNDU="
        }
      }
    }
    ```

    ```shell
    echo "YWRtaW46SGFyYm9yMTIzNDU=" | base64 -d
    ```

    ```none
    admin:Harbor12345
    ```
