# MySQL 健康检查

> 如果您发现遇到的问题，未包含在 __故障排查__ 内，可以快速跳转到页面底部，提交您的问题。

常规的 MySQL 健康状态检查，可以通过一句命令快速查看 MySQL 实例的整体状态:

```none
kubectl get pod -n mcamel-system -Lhealthy,role | grep mysql
```

输出类似于：

```
mcamel-common-mysql-cluster-auto-2023-03-28t00-00-00-backujgg9m   0/1     Completed          0               27h              
mcamel-common-mysql-cluster-auto-2023-03-29t00-00-00-backusgf59   0/1     Completed          0               3h43m            
mcamel-common-mysql-cluster-mysql-0                               4/4     Running            6 (11h ago)     25h     yes       master
mcamel-common-mysql-cluster-mysql-1                               4/4     Running            690 (11h ago)   4d20h   yes       replica
mcamel-mysql-apiserver-9797c7f76-bvf5n                            2/2     Running            0               22h              
mcamel-mysql-ui-7ffd9dd8db-d5jfm                                  2/2     Running            0               25m              
mysql-operator-0                                                  2/2     Running            109 (47m ago)   2d21h  
```

如上所示，如果主备节点（ __master__ 和 __replica__ ）的状态均为 __yes__ ，说明 MySQL 为正常状态。
