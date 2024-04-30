# 常见问题

Virtnest 包含 apiserver 和 agent 两个部分，遇到问题时应从这两部分进行排查。

## 页面 api 报错：
若页面请求 API 报错 500 或 cluster 资源不存在，首先应检查 global 集群中 virtnest 相关服务的日志，寻找是否有 kpanda 的关键词。若存在，需确认 kpanda 相关服务是否运行正常。



## VM无法正常使用：
若创建的 VM 无法正常使用，原因多样。以下是排查方向：

### VM 创建失败：
VM 创建失败时，应在目标集群中查看 VM 的详细信息：

`kubectl -n your-namespace describe vm your-vm`


如果详细信息涉及存储，如 PVC、PV、SC 等，请检查 SC 状态。问题未解决时，应咨询开发人员。

如果详细信息涉及设备，如 KVM、GPU 等，请核实目标集群节点是否完成了[依赖条件](../install/install-dependency.md)检查。若所有依赖已安装，应咨询开发人员。

### VM 创建成功但无法使用：
若 VM 创建成功但无法使用，应在 DCE 页面检查 VM 的 VNC 页面是否正常。若显示但仅限启动信息，请检查[依赖条件](../install/install-dependency.md)。依赖条件齐全后，应联系开发人员。

若 VNC 页面显示异常，应使用命令 

`kubectl -n your-namespace describe vm your-vm` 查看 VM 详细信息。

当详细信息涉及存储信息，如 PVC、PV、SC 等，应检查 SC 状态。问题未解决时，应联系开发人员。