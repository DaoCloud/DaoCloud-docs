# kubernetes cluster compatibility test

✅: Test passed; ❌: Test failed.

!!! note

     The test functions in the table are not comprehensive.

| case | | test method| K8s 1.26 |k8s 1.23.0 ~ 1.23.13 | k8s 1.24.0 ~ 1.24.7 | k8s 1.25.0 ~ 1.25.3 | 1.18 |Remarks |
| ------------ | ------------------------ | ----------- ----- | --------- | --------- | --------- | --------- | ----- | --------- |--------- |--------- |--------- |---- ----- |
| Collect and query web application metrics | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Add custom metric collection | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Query real-time metrics | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Instantaneous index query | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Instantaneous metric api field function verification | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Query metrics over a period of time | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Query api field function verification of metrics within a period of time | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Batch query cluster CPU, memory usage, total cluster CPU, cluster memory usage, total number of cluster nodes | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Batch query node CPU, memory usage, total node CPU, node memory usage | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Batch query cluster CPU, memory usage, total cluster CPU, cluster memory usage, and total number of cluster nodes within a period of time | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Batch query to query metrics api field function verification within a period of time | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅ | |
| Query Pod log | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Query SVC log | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Query statefulset logs | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Query Deployment Logs | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Query NPD log | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Log Filtering | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Log fuzzy query-workloadSearch | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Log fuzzy query-podSearch | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Log fuzzy query-containerSearch | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Log Accurate Query-cluster | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Log precise query-namespace | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |
| Log query api field function verification | | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅| ✅| ✅| | |