# Kubernetes Cluster Compatibility Test

✅: Test passed; ❌: Test failed.

!!! note

    The table does not cover all test scenarios.

| Test Case                                                                                                     | Test Method | K8s 1.26 | K8s 1.23.0 ~ 1.23.13 | K8s 1.24.0 ~ 1.24.7 | K8s 1.25.0 ~ 1.25.3 | K8s 1.22 | K8s 1.21 | K8s 1.20 | K8s 1.19 | K8s 1.18 | Remarks |
| ------------------------------------------------------------------------------------------------------------- | ----------- | -------- | -------------------- | ------------------- | ------------------- | -------- | -------- | -------- | -------- | -------- | ------- |
| Collect and query web application metrics                                                                     | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Add custom metric collection                                                                                  | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Query real-time metrics                                                                                       | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Instantaneous index query                                                                                     | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Instantaneous metric API field verification                                                                   | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Query metrics over a period of time                                                                           | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Metric API field verification within a period of time                                                         | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Batch query cluster CPU, memory usage, total cluster CPU, cluster memory usage, total number of cluster nodes | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Batch query node CPU, memory usage, total node CPU, node memory usage                                         | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Batch query cluster metrics within a period of time                                                           | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Metric API field verification within a period of time                                                         | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Query Pod log                                                                                                 | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Query SVC log                                                                                                 | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Query statefulset logs                                                                                        | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Query Deployment Logs                                                                                         | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Query NPD log                                                                                                 | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Log Filtering                                                                                                 | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Log fuzzy query - workloadSearch                                                                              | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Log fuzzy query - podSearch                                                                                   | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Log fuzzy query - containerSearch                                                                             | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Log Accurate Query - cluster                                                                                  | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Log Accurate Query - namespace                                                                                | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |
| Log query API field verification                                                                              | E2E         | ✅       | ✅                   | ✅                  | ✅                  | ✅       | ✅       | ✅       | ✅       | ✅       | -       |

Please note that this is not an exhaustive list and there may be additional test scenarios.

The purpose of these tests is to verify the functionality and compatibility of features such as metric collection, real-time metric querying, log querying for various resources (Pods, Services, StatefulSets, Deployments, NPD), and log filtering. The tests have been conducted on Kubernetes versions 1.26, 1.23.0 to 1.23.13, 1.24.0 to 1.24.7, 1.25.0 to 1.25.3, 1.22, 1.21, 1.20, 1.19, and 1.18.
