# Uninstall

Run the following commands in order to uninstall DCE 5.0 from your environment.

!!! warning

    Your data will not be backed up. Please proceed with caution.

```shell
kubectl -n mcamel-system delete mysql mcamel-common-mysql-cluster
kubectl -n mcamel-system delete mysql mcamel-common-kpanda-mysql-cluster
kubectl -n mcamel-system delete elasticsearches mcamel-common-es-cluster-masters
kubectl -n mcamel-system delete redisfailover mcamel-common-redis-cluster
kubectl -n mcamel-system delete tenant mcamel-common-minio-cluster
kubectl -n ghippo-system delete gateway ghippo-gateway
kubectl -n istio-system delete requestauthentications ghippo
helm -n mcamel-system uninstall eck-operator mysql-operator redis-operator minio-operator
helm -n ghippo-system uninstall ghippo
helm -n insight-system uninstall insight-agent insight
helm -n ipavo-system uninstall ipavo
helm -n kpanda-system uninstall kpanda
helm -n istio-system uninstall istio-base istio-ingressgateway istiod
kubectl delete namespace mcamel-system ghippo-system insight-system ipavo-system kpanda-system istio-system
```
