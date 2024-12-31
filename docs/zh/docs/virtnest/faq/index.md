# 虚拟机常见问题

虚拟机（virtnest）包含 apiserver 和 agent 两个部分，遇到问题时应从这两部分进行排查。

## 页面 API 报错

若页面请求 API 报错 500 或 cluster 资源不存在，
首先应检查[全局服务集群](../../kpanda/user-guide/clusters/cluster-role.md#_2)中虚拟机相关服务的日志，
寻找是否 kpanda 的关键词。若存在，需确认 kpanda 相关服务是否运行正常。
