# 备份恢复

备份恢复是

kubernetes 的组件包括 apiserver、controller manager、scheduler， proxy，etcd。 数据都存储在 etcd 中，只有 apiserver 和 etcd 通信，其他组件都直接和 apiserver 通信


etcd 中存放敏感数据，所以访问etcd 时需要使用公钥和私钥，cert，key，cacert
