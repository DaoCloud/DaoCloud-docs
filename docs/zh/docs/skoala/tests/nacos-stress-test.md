# Nacos 压力测试报告

本文通过 JVM 虚拟机测试托管 Nacos 注册配置中心在不同资源规格下的性能表现，便于您根据实际的业务场景为 Nacos 提供合适的资源配额。

## 性能指标

TPS：通常指服务器每秒处理的事务数 (Transactions Per Second)。在本文中具体指 Nacos 服务器每秒可以处理多少个服务注册请求。

## 测试命令

```console
java -jar -Xms2g -Xmx2g -Dnacos.server=10.6.222.21:30168 -Dthead.count=100 -Dservice.count=500 nacos-client-1.0-SNAPSHOT-jar-with-dependencies.jar
```

- `-Xms2g`：JVM 的初始内存
- `-Xmx2g`：JVM 可使用的最大内存
- `-Dnacos.server`：Nacos 注册配置中心的访问地址
- `-Dthead.count`：线程数，对应测试结果中的`并发数`
- `-Dservice.count`：每个线程的请求数，对应测试结果中的`服务数`
- `nacos-client-1.0-SNAPSHOT-jar-with-dependencies.jar`：压测使用的 Jar 包，实际测试过程中在本地将其重命名为 `nacos-benchmark.jar`

## 测试过程截图

![process](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-nacos01.png)

## 测试结果

<table>
  <tr>
    <th>规格</th>
    <th>节点数</th>
    <th>并发数</th>
    <th>服务数</th>
    <th>执行时间(毫秒)</th>
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

## 探究 JVM 资源配置对 Nacos 的性能影响

为探究 JVM 的资源配置对托管 Nacos 注册配置中心的性能影响，在 Nacos 申请资源为 `2 Core 4 GiB` 时，为 JVM 也配置相同的资源，即 `2 Core 4 GiB`。

这种情况下得出的测试结果如下：

<table>
  <tr>
    <th>规格</th>
    <th>节点数</th>
    <th>并发数</th>
    <th>服务数</th>
    <th>执行时间(毫秒)</th>
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

    TPS 与调整前的数据不相上下。这说明，调整 JVM 对 Nacos 的性能基本没有影响。
