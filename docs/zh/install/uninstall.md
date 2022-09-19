# 卸载

卸载 DCE 5.0 将会从您的集群中上移除，卸载过程中不会进行任何备份，请谨慎操作。请执行以下命令：

```shell
kubectl -n mcamel-system delete mysql mcamel-common-mysql-cluster
kubectl -n mcamel-system delete elasticsearches mcamel-common-es-cluster-masters
kubectl -n mcamel-system delete redisfailover mcamel-common-redis-cluster
kubectl -n ghippo-system delete gateway ghippo-gateway
kubectl -n istio-system delete requestauthentications ghippo
helm -n mcamel-system  uninstall eck-operator mysql-operator redis-operator
helm -n ghippo-system  uninstall ghippo
helm -n insight-system uninstall insight-agent insight
helm -n ipavo-system   uninstall ipavo
helm -n kpanda-system  uninstall kpanda
helm -n istio-system   uninstall istio-base istio-ingressgateway istiod
```
