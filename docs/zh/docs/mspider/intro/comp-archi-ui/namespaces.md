---
hide:
  - toc
---

# 系统命名空间

DCE 5.0 服务网格自带了一些系统命名空间，请勿将业务应用和服务部署到这些命名空间，这些命名空间及其作用如下所述。

| 分类                 | 命名空间           | 作用                            |
| -------------------- | ------------------ | ------------------------------- |
| Istio 系统命名空间   | istio-system       | 承载 Istio 控制平面组件及其资源 |
|                      | istio-operator     | 部署和管理 Istio Operator       |
| K8s 系统命名空间     | kube-system        | 控制平面组件                    |
|                      | kube-public        | 集群配置和证书等                |
|                      | kube-node-lease    | 监测和维护节点的活动            |
| DCE 5.0 系统命名空间 | amamba-system      | 应用工作台                      |
|                      | ghippo-system      | 全局管理                        |
|                      | insight-system     | 可观测性                        |
|                      | ipavo-system       | 首页仪表盘                      |
|                      | kairship-system    | 多云编排                        |
|                      | kant-system        | 云边协同                        |
|                      | kangaroo-system    | 镜像仓库                        |
|                      | kcoral-system      | 应用备份                        |
|                      | kubean-system      | 集群生命周期管理                |
|                      | kpanda-system      | 容器管理                        |
|                      | local-path-storage | 本地存储                        |
|                      | mcamel-system      | 中间件                          |
|                      | mspider-system     | 服务网格                        |
|                      | skoala-system      | 微服务引擎                      |
|                      | spidernet-system   | 网络模块                        |
|                      | virtnest-system    | 虚拟机模块                      |
|                      | baize-system       | 智能算力模块                    |
