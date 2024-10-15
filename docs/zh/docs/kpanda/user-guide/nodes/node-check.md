# 创建集群节点可用性检查

在创建集群或为已有集群添加节点时，请参阅下表，检查节点配置，以避免因节点配置错误导致集群创建或扩容失败。

| 检查项          | 描述                                   |
| -------------- | -------------------------------------- |
| 操作系统        | 参考[支持的架构及操作系统](#_2)         |
| SELinux        | 关闭                                   |
| 防火墙	      | 关闭                                   |
| 架构一致性       | 节点间 CPU 架构一致（如均为 ARM 或 x86）   |
| 主机时间         | 所有主机间同步误差小于 10 秒。             |
| 网络联通性       | 节点及其 SSH 端口能够正常被平台访问。       |
| CPU            | 可用 CPU 资源大于 4 Core                |
| 内存            | 可用内存资源大于 8 GB                     |

## 支持的架构及操作系统

| 架构 | 操作系统                                                   | 备注 |
| ---- | ---------------------------------------------------------- | ---- |
| ARM  | Kylin Linux Advanced Server release V10 (Sword)  SP2       | 推荐 |
| ARM  | UOS Linux                                                  |      |
| ARM  | openEuler                                                  |      |
| x86  | CentOS 7.x                                                 | 推荐 |
| x86  | Redhat 7.x                                                 | 推荐 |
| x86  | Redhat 8.x                                                 | 推荐 |
| x86  | Flatcar Container Linux by Kinvolk                         |      |
| x86  | Debian Bullseye, Buster, Jessie, Stretch                   |      |
| x86  | Ubuntu 16.04, 18.04, 20.04, 22.04                          |      |
| x86  | Fedora 35, 36                                              |      |
| x86  | Fedora CoreOS                                              |      |
| x86  | openSUSE Leap 15.x/Tumbleweed                              |      |
| x86  | Oracle Linux 7, 8, 9                                       |      |
| x86  | Alma Linux 8, 9                                            |      |
| x86  | Rocky Linux 8, 9                                           |      |
| x86  | Amazon Linux 2                                             |      |
| x86  | Kylin Linux Advanced Server release V10 (Sword) - SP2 海光 |      |
| x86  | UOS Linux                                                  |      |
| x86  | openEuler                                                  |      |
