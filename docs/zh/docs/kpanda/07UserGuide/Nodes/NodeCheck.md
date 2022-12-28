# 创建集群节点可用性检查

在创建集群或为已有集群添加节点时，请参阅下表，检查节点配置，以避免因节点配置错误导致集群创建或扩容失败。

| 检查项          | 描述                                   |
| -------------- | -------------------------------------- |
| 操作系统        | 参考[支持的架构及操作系统](#支持的架构及操作系统)         |
| SELinux        | 关闭                                   |
| 防火墙	      | 关闭                                   |
| 架构一致性       | 节点间 CPU 架构一致（如均为 ARM 或 X86）   |
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
| X86  | CentOS 7.x                                                 | 推荐 |
| X86  | Redhat 7.x                                                 | 推荐 |
| X86  | Redhat 8.x                                                 | 推荐 |
| X86  | Flatcar Container Linux by Kinvolk                         |      |
| X86  | Debian Bullseye, Buster, Jessie, Stretch                   |      |
| X86  | Ubuntu 16.04, 18.04, 20.04, 22.04                          |      |
| X86  | Fedora 35, 36                                              |      |
| X86  | Fedora CoreOS                                              |      |
| X86  | openSUSE Leap 15.x/Tumbleweed                              |      |
| X86  | Oracle Linux 7, 8, 9                                       |      |
| X86  | Alma Linux 8, 9                                            |      |
| X86  | Rocky Linux 8, 9                                           |      |
| X86  | Amazon Linux 2                                             |      |
| X86  | Kylin Linux Advanced Server release V10 (Sword) - SP2 海光 |      |
| X86  | UOS Linux                                                  |      |
| X86  | openEuler                                                  |      |
