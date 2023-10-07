# 网关压力测试报告

本文介绍 DCE 5.0 云原生网关在不同场景下的性能表现，便于您根据需求为网关配置合适的资源。

## 测试环境

开始测试之前，需要部署 DCE 5.0，下载安装测试工具，并准备好用于测试的压力机。

| 对象         | 角色                           |说明
| -------------- | ------------------------------ | ---|
| DCE 5.0 云原生网关|测试对象|采用一主一从的模式，部署位置：172.30.120.211 |
|Locust|测试工具|采用 1+4 的主从分布式运行模式，四台压测机的资源配置均为 8 核 8 G|
|Nginx|用于测试网关性能的演示服务|通过 DCE 5.0 云原生网关访问，访问地址为：http://172.30.120.211:30296/|
| contour |  DCE 5.0 云原生网关的控制面 |版本为 1.23.1|
| envoy |  DCE 5.0 云原生网关的数据面  |版本为 1.24.0|
| 全局管理 | DCE 5.0 云原生网关依赖的组件 |版本为 0.12.1|
| 容器管理 | DCE 5.0 云原生网关依赖的组件 |版本为 0.13.1|
| 微服务引擎 | DCE 5.0 云原生网关依赖的组件 |版本为 0.15.1|

## 性能指标

- 吞吐量（RPS）：每秒处理的请求数。结合 CPU 使用率，判断 DCE 5.0 云原生网关在特定资源配置下每秒可以处理的并发请求数。
  吞吐量越高，说明网关性能越好
- CPU 使用率：测试处理特定数量的并发请求时，DCE 5.0 云原生网关实例的 CPU 使用情况。
  当 CPU 使用量达到 90% 以上时，认为 CPU 接近满载，此时的吞吐量（RPS）是当前配置能够正常处理的最大并发请求数。

## 测试脚本

- 在 Locust Web 机器执行如下命令，收集压测结果

    ```bash
    docker run -p 8089:8089 --network=host -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/gateway-external-nginx.py --master
    ```

- 在 Locust 压测机执行如下命令，模拟用户访问，执行压力测试

    ```bash
    docker run -p 8089:8089 --network=host -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/gateway-external-nginx.py --worker --master-host=172.30.120.210
    ```

- 压测脚本 `gateway-external-nginx.py`

    ```python
    from locust import task
    from locust.contrib.fasthttp import FastHttpUser

    class ShellCard(FastHttpUser):

      host = "http://172.30.120.211:30296" # 被测服务的访问地址
      @task
      def test(self):
        header = {"Host": "external.nginx"}
        self.client.get("/", headers=header)
    ```

## 测试 nginx 吞吐量：三副本，不限制资源

### 测试结果

<table>
  <tr>
    <th>并发用户数</th>
    <th>每秒吞吐量</th>
    <th>CPU 使用量</th>
    <th>分析</th>
  </tr>
  <tr>
    <td>4</td>
    <td>4300</td>
    <td>58%——70%</td>
    <td>资源未充分利用，理论上仍有能力处理更多请求。</td>
  </tr>
  <tr>
    <td>8</td>
    <td>5700</td>
    <td>77%——83%</td>
    <td>仍有少量资源空闲，可以尝试增加并发请求数，测试吞吐量上限。</td>
  </tr>
  <tr>
    <td>12</td>
    <td>6700</td>
    <td>90%——95%</td>
    <td>只有极少量资源空闲，CPU 接近满载，视为达到吞吐量上限。</td>
  </tr>
  <tr>
</table>

!!! success

    综上，当服务部署三副本且不限制资源用量时，DCE 5.0 云原生网关能够处理的最大并发请求数大约为 6000 到 7000，较同类产品而言可谓性能优异。

### 测试过程截图

- 并发用户数为 4

    ![4 个并发用户](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway01.png)

    ![4 个并发用户](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway02.png)

- 并发用户数为 8

    ![8 个并发用户](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway03.png)

    ![8 个并发用户](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway04.png)

- 并发用户数为 12
    
    ![12 个并发用户](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway05.png)

    ![12 个并发用户](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway06.png)

## 探究 contour 资源配置对 envoy 的性能影响

DCE 5.0 云原生网关是在开源项目 contour 和 envoy 的基础上进一步研发优化而来。contour 充当网关的控制平面，envoy 充当数据平面。

创建 DCE 5.0 云原生网关时，系统要求必须为网关配置不低于 1 核 1 G 的资源。因此，本次测试中 contour 的资源限制最低为 1 核 1 G。

此外，为了更好地体现 contour 的资源配置的影响，将 envoy 的资源限制设置为 6 核 3 G，
保证 envoy 自身始终具有较高的性能，不会因为自身资源不足而影响测试结果。

为保证压测机器资源负载正常，默认 Locust users 为 8。

### 测试结果

<table>
  <tr>
    <th>contour 资源规格</th>
    <th>每秒吞吐量</th>
    <th>CPU 使用量</th>
    <th>分析</th>
  </tr>
  <tr>
    <td>1 核 1 G</td>
    <td>3700</td>
    <td>53%——69%</td>
    <td rowspan="3">contour 的资源配置从 1 核 1 G 到 2 核 1 G，再到 3 核 2 G，</br>但网关每秒吞吐量一直维持在 3700 左右，上下变动幅度只有 100。</br>CPU 使用率也维持在 50%——70%左右，整体变化非常小。</td>
  </tr>
  <tr>
    <td>2 核 1 G</td>
    <td>3600</td>
    <td>55%——72%</td>
  </tr>
  <tr>
    <td>3 核 2 G</td>
    <td>3800</td>
    <td>57%——69%</td>
  </tr>
</table>

!!! success

    这说明 contour 的资源配置对 envoy 的性能几乎没有影响。

### 测试过程截图

- contour 资源 1 核 1 G

    ![1c1g](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway07.png)

    ![1c1g](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway08.png)

- contour 资源 2 核 1 G

    ![2c1g](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway09.png)

    ![2c1g](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway10.png)

- contour 资源 3 核 2 G
    
    ![3c2g](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway11.png)

    ![3c2g](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway12.png)

## 探究 envoy 资源配置对吞吐量的影响

envoy 固定为 1 副本，contour 配置为 1 核 1 G，被测试服务 nginx 配置为 3 副本，不限制资源用量。

### 测试结果

<table>
  <tr>
    <th>envoy 资源规格</th>
    <th>并发用户数</th>
    <th>每秒吞吐量</th>
    <th>CPU 使用量</th>
    <th>分析</th>
  </tr>
  <tr>
    <td rowspan="3">1 核 1 G</td>
    <td>4</td>
    <td>1016</td>
    <td>18%——22%</td>
    <td rowspan="3">当 envoy 的资源配置不变时，即使并发用户数成倍增加，网关吞吐量也变化不大。</td>
  </tr>
  <tr>
    <td>8</td>
    <td>1181</td>
    <td>19%——20%</td>
  </tr>
  <tr>
    <td>16</td>
    <td>1090</td>
    <td>19%——22%</td>
  </tr>
  <tr>
    <td rowspan="2">2 核 1 G</td>
    <td>4</td>
    <td>2103</td>
    <td>28%——41%</td>
    <td rowspan="2">并发用户数为 4 时，当资源配置从 1 核增加到 2 核，吞吐量也增加了 1000 左右。</td>
  </tr>
  <tr>
    <td>8</td>
    <td>2284</td>
    <td>38%——47%</td>
  </tr>
  <tr>
    <td rowspan="2">3 核 1 G</td>
    <td>8</td>
    <td>3355</td>
    <td>59%——70%</td>
    <td rowspan="2">并发用户数为 8 时，当资源配置从 1 核增加到 3 核，吞吐量也增加了 2000 左右。</td>
  </tr>
  <tr>
    <td>12</td>
    <td>3552</td>
    <td>52%——59%</td>
  </tr>
  <tr>
    <td rowspan="2">4 核 2 G</td>
    <td>8</td>
    <td>3497</td>
    <td>58%——80%</td>
    <td rowspan="4">并发用户数为 12 时，当资源配置从 3 核增加到 5 核，吞吐量也增加了 1000 左右。</td>
  </tr>
  <tr>
    <td>12</td>
    <td>4250</td>
    <td>78%——86%</td>
  </tr>
  <tr>
    <td rowspan="2">5 核 2 G</td>
    <td>8</td>
    <td>3573</td>
    <td>60%——81%</td>
    <td rowspan="2"></td>
  </tr>
  <tr>
    <td>12</td>
    <td>4698</td>
    <td>68%——78%</td>
  </tr>
  <tr>
    <td rowspan="2">6 核 2 G</td>
    <td>12</td>
    <td>4574</td>
    <td>78%——85%</td>
    <td rowspan="2">当配置为 6 核 2 G 时，吞吐量为 5400 左右，CPU 使用量也到达了 90% 以上，接近满载。</td>
  </tr>
  <tr>
    <td>16</td>
    <td>5401</td>
    <td>90%以上</td>
  </tr>
</table>

!!! success

    综上：
    
    - envoy 的 CPU 配置对吞吐量起决定性因素。
    - 在当前压测资源下，通过 envoy 访问 nginx 的吞吐量能够达到直接访问 nginx 的吞吐量的 80% 以上。

### 测试过程截图

#### 当 envoy 配置为 1 核 1 G

- 并发用户数为 4

    ![4](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway13.png)

    ![4](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway14.png)

- 并发用户数为 8

    ![8](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway15.png)

    ![8](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway16.png)

- 并发用户数为 16

    ![16](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway17.png)

    ![16](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway18.png)

#### 当 envoy 配置为 2 核 1 G

- 并发用户数为 4

    ![4](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway19.png)

    ![4](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway20.png)

- 并发用户数为 8

    ![8](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway21.png)

    ![8](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway22.png)

#### 当 envoy 配置为 3 核 1 G

- 并发用户数为 8

    ![8](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway23.png)

    ![8](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway24.png)

- 并发用户数为 12

    ![12](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway25.png)

    ![12](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway26.png)

#### 当 envoy 配置为 4 核 2 G

- 并发用户数为 8

    ![8](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway27.png)

    ![8](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway28.png)

- 并发用户数为 12

    ![12](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway29.png)

    ![12](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway30.png)

#### 当 envoy 配置为 5 核 2 G

- 并发用户数为 8

    ![8](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway31.png)

    ![8](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway32.png)

- 并发用户数为 12

    ![12](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway33.png)

    ![12](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway34.png)

#### 当 envoy 配置为 6 核 2 G

- 并发用户数为 12

    ![12](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway35.png)

    ![12](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway36.png)

- 并发用户数为 16

    ![16](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway37.png)

    ![16](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/test-gateway38.png)
