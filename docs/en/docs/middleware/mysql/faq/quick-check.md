# MySQL Health Check

> If you encounter an issue that is not covered in the "Troubleshooting" section, you can quickly jump to the bottom of the page and submit your problem.

To perform a regular health check on MySQL, you can use a single command to quickly view the overall status of the MySQL instance:

```none
kubectl get pod -n mcamel-system -Lhealthy,role | grep mysql
```

The output is similar to:

```
mcamel-common-mysql-cluster-auto-2023-03-28t00-00-00-backujgg9m 0/1 Completed 0 27h
mcamel-common-mysql-cluster-auto-2023-03-29t00-00-00-backusgf59 0/1 Completed 0 3h43m
mcamel-common-mysql-cluster-mysql-0 4/4 Running 6 (11h ago) 25h yes master
mcamel-common-mysql-cluster-mysql-1 4/4 Running 690 (11h ago) 4d20h yes replica
mcamel-mysql-apiserver-9797c7f76-bvf5n 2/2 Running 0 22h
mcamel-mysql-ui-7ffd9dd8db-d5jfm 2/2 Running 0 25m
mysql-operator-0 2/2 Running 109 (47m ago) 2d21h
```

As shown above, if the status of the active and standby nodes ( __master__ __replica__ ) is __yes__ , it means that MySQL is in a normal state.
