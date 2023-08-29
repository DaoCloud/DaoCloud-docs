# Nacos Stress Test Report

This article aims to evaluate the performance of Nacos registry and configuration center under different resource specifications, using JVM virtual machine testing. It will assist you in determining appropriate resource quotas for Nacos based on your actual business scenarios.

## Performance Metrics

TPS: Transactions Per Second, typically refers to the number of transactions processed by a server per second. In the context of this article, it specifically indicates the number of service registration requests that Nacos server can handle per second.

## Test Command

```
java -jar -Xms2g -Xmx2g -Dnacos.server=10.6.222.21:30168 -Dthread.count=100 -Dservice.count=500 nacos-client-1.0-SNAPSHOT-jar-with-dependencies.jar
```

- `-Xms2g`: Initial memory allocation for the JVM.
- `-Xmx2g`: Maximum memory allocation for the JVM.
- `-Dnacos.server`: Access address of the Nacos registry and configuration center.
- `-Dthread.count`: Number of threads, corresponding to `concurrency` in the test results.
- `-Dservice.count`: Number of requests per thread, corresponding to `services` in the test results.
- `nacos-client-1.0-SNAPSHOT-jar-with-dependencies.jar`: Jar package used for stress testing. In actual testing, rename it as `nacos-benchmark.jar` locally.

## Screenshots of the Test Process

![process](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-nacos01.png)

## Test Results

<table>
  <tr>
    <th>Resource</th>
    <th>Node</th>
    <th>Concurrency</th>
    <th>Services</th>
    <th>Execution Time (ms)</th>
    <th>TPS</th>
  </tr>
  <tr>
    <td rowspan="3">1 Core 2 GiB</td>
    <td rowspan="3">1</td>
    <td>30</td>
    <td>1000</td>
    <td>17086</td>
    <td>1755.8</td>
    <td></td>
  </tr>
  <tr>
    <td>50</td>
    <td>1000</td>
    <td>23315</td>
    <td>2144.5</td>
  </tr>
  <tr>
    <td>100</td>
    <td>500</td>
    <td>26194</td>
    <td>1908.4</td>
  </tr>
  <tr>
    <td rowspan="3">2 Core 4 GiB</td>
    <td rowspan="3">1</td>
    <td>30</td>
    <td>1000</td>
    <td>8794</td>
    <td>3409.1</td>
  </tr>
  <tr>
    <td>50</td>
    <td>1000</td>
    <td>15460</td>
    <td>3225.8</td>
  </tr>
  <tr>
    <td>100</td>
    <td>500</td>
    <td>15699</td>
    <td>3184.7</td>
  </tr>
  <tr>
  <tr>
    <td rowspan="3">4 Core 8 GiB</td>
    <td rowspan="3">1</td>
    <td>50</td>
    <td>1000</td>
    <td>11843</td>
    <td>4221.9</td>
  </tr>
  <tr>
    <td>80</td>
    <td>1000</td>
    <td>14510</td>
    <td>5513.4</td>
  </tr>
  <tr>
    <td>100</td>
    <td>500</td>
    <td>9501</td>
    <td>5262.6</td>
  </tr>
  <tr>
    <td rowspan="3">8 Core 16 GiB</td>
    <td rowspan="3">1</td>
    <td>50</td>
    <td>2000</td>
    <td>14391</td>
    <td>6948.8</td>
  </tr>
  <tr>
    <td>80</td>
    <td>2000</td>
    <td>18695</td>
    <td>8558.4</td>
  </tr>
    <tr>
    <td>100</td>
    <td>1000</td>
    <td>11686</td>
    <td>8557.2</td>
  </tr>
</table>

## Investigating the Impact of JVM Resource Configuration on Nacos Performance

To investigate the impact of JVM resource configuration on the performance of hosting Nacos registry and configuration center, we allocated the same resources to JVM as Nacos, which is `2 Core 4 GiB`.

The test results under this configuration are as follows:

<table>
  <tr>
    <th>Specification</th>
    <th>Nodes</th>
    <th>Concurrency</th>
    <th>Services</th>
    <th>Execution Time (ms)</th>
    <th>TPS</th>
  </tr>
  <tr>
    <td rowspan="6">2 Core 4 GiB</td>
    <td rowspan="3">1</td>
    <td>30</td>
    <td>1000</td>
    <td>11003</td>
    <td>2727.3</td>
    <td></td>
  </tr>
  <tr>
    <td>50</td>
    <td>1000</td>
    <td>15006</td>
    <td>3333.3</td>
  </tr>
  <tr>
    <td>100</td>
    <td>500</td>
    <td>13963</td>
    <td>3580.9</td>
  </tr>
</table>

!!! success

The TPS remains consistent with the previous results even after adjusting the JVM. This indicates that adjusting the JVM has minimal impact on the performance of Nacos.
