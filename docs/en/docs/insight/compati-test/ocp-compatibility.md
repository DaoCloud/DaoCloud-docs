# Openshift 4.x Cluster Compatibility Test

✅: Test passed; ❌: Test failed.

!!! note

    The table does not cover all test scenarios.

| Test Case                                                                                                     | Test Method | OCP 4.10 (K8s 1.23.0) | Remarks |
| ------------------------------------------------------------------------------------------------------------- | ----------- | --------------------- | ------- |
| Collect and query web application metrics                                                                     | Manual      | ✅                    | -       |
| Add custom metric collection                                                                                  | Manual      | ✅                    | -       |
| Query real-time metrics                                                                                       | Manual      | ✅                    | -       |
| Instantaneous index query                                                                                     | Manual      | ✅                    | -       |
| Instantaneous metric API field verification                                                                   | Manual      | ✅                    | -       |
| Query metrics over a period of time                                                                           | Manual      | ✅                    | -       |
| Metric API field verification within a period of time                                                         | Manual      | ✅                    | -       |
| Batch query cluster CPU, memory usage, total cluster CPU, cluster memory usage, total number of cluster nodes | Manual      | ✅                    | -       |
| Batch query node CPU, memory usage, total node CPU, node memory usage                                         | Manual      | ✅                    | -       |
| Batch query cluster metrics within a period of time                                                           | Manual      | ✅                    | -       |
| Metric API field verification within a period of time                                                         | Manual      | ✅                    | -       |
| Query Pod log                                                                                                 | Manual      | ✅                    | -       |
| Query SVC log                                                                                                 | Manual      | ✅                    | -       |
| Query statefulset logs                                                                                        | Manual      | ✅                    | -       |
| Query Deployment Logs                                                                                         | Manual      | ✅                    | -       |
| Query NPD log                                                                                                 | Manual      | ✅                    | -       |
| Log Filtering                                                                                                 | Manual      | ✅                    | -       |
| Log fuzzy query - workloadSearch                                                                              | Manual      | ✅                    | -       |
| Log fuzzy query - podSearch                                                                                   | Manual      | ✅                    | -       |
| Log fuzzy query - containerSearch                                                                             | Manual      | ✅                    | -       |
| Log Accurate Query - cluster                                                                                  | Manual      | ✅                    | -       |
| Log Accurate Query - namespace                                                                                | Manual      | ✅                    | -       |
| Log query API field verification                                                                              | Manual      | ✅                    | -       |
| Alert Rule - CRUD operations                                                                                  | Manual      | ✅                    | -       |
| Alert Template - CRUD operations                                                                              | Manual      | ✅                    | -       |
| Notification Method - CRUD operations                                                                         | Manual      | ✅                    | -       |
| Link Query                                                                                                    | Manual      | ✅                    | -       |
| Topology Query                                                                                                | Manual      | ✅                    | -       |

The table above represents the Openshift 4.x cluster compatibility test. It includes various test cases, their corresponding test method (manual), and the test results for the OCP version 4.10 (with Kubernetes version 1.23.0).

Please note that this is not an exhaustive list, and additional test scenarios may exist.
