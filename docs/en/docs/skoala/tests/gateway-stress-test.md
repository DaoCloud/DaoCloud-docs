Gateway Load Test Report

This article introduces the performance of the DCE 5.0 Cloud-Native Gateway in different scenarios, enabling you to configure appropriate resources for the gateway based on your needs.

## Test Environment

Before starting the test, it is necessary to deploy DCE 5.0, download and install the testing tool and prepare stress-testing machines.

| Object | Role | Description |
| --- | --- | --- |
| DCE 5.0 Cloud-Native Gateway | Test Object | Deployed in master-slave mode, located at: 172.30.120.211 |
| Locust | Testing Tool | Running in a 1+4 master-slave distributed mode, with four stress-testing machines' resource configurations at 8 cores and 8 G |
| Nginx | Demo service for testing gateway performance | Accessed through DCE 5.0 Cloud-Native Gateway, access address: http://172.30.120.211:30296/|
| contour | Control plane of DCE 5.0 Cloud-Native Gateway | Version 1.23.1 |
| envoy | Data plane of DCE 5.0 Cloud-Native Gateway | Version 1.24.0 |
| Global Management | Components that DCE 5.0 Cloud-Native Gateway depends on | Version 0.12.1 |
| Container Management | Components that DCE 5.0 Cloud-Native Gateway depends on | Version 0.13.1 |
| Microservice Engine | Components that DCE 5.0 Cloud-Native Gateway depends on | Version 0.15.1 |

## Performance Indicators

- Throughput (RPS): The number of requests processed per second. Combined with CPU utilization, it determines the maximum number of concurrent requests that can be processed per second under a specific resource configuration for the DCE 5.0 Cloud-Native Gateway. The higher the throughput, the better the gateway performance.
- CPU utilization: The CPU usage of the DCE 5.0 Cloud-Native Gateway instance when processing a specific number of concurrent requests during the test. When the CPU usage exceeds 90%, it is considered to be approaching full load, and the throughput (RPS) at this point is the maximum number of concurrent requests that can be processed normally with the current configuration.

## Test Script

- Run the following command on the Locust Web machine to collect the stress-testing results:

    ```
    docker run -p 8089:8089 --network=host -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/gateway-external-nginx.py --master
    ```

- Run the following command on the Locust stress-testing machine to simulate user access and perform stress testing:

    ```
    docker run -p 8089:8089 --network=host -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/gateway-external-nginx.py --worker --master-host=172.30.120.210
    ```

- Stress-testing script `gateway-external-nginx.py`:

    ```
    from locust import task
    from locust.contrib.fasthttp import FastHttpUser

    class ShellCard(FastHttpUser):

      host = "http://172.30.120.211:30296" # Access address of the tested service
      @task
      def test(self):
        header = {"Host": "external.nginx"}
        self.client.get("/", headers=header)
    ```

## Test Nginx Throughput: Three Replicas, No Resource Limitations

### Test Results

<table>
  <tr>
    <th>Number of Concurrent Users</th>
    <th>Throughput (RPS)</th>
    <th>CPU Utilization</th>
    <th>Analysis</th>
  </tr>
  <tr>
    <td>4</td>
    <td>4300</td>
    <td>58%——70%</td>
    <td>The resources are not fully utilized, theoretically capable of handling more requests.</td>
  </tr>
  <tr>
    <td>8</td>
    <td>5700</td>
    <td>77%——83%</td>
    <td>A small amount of resources is still idle, and increasing the number of concurrent requests can be attempted to test the throughput limit.</td>
  </tr>
  <tr>
    <td>12</td>
    <td>6700</td>
    <td>90%——95%</td>
    <td>Only a very small amount of resources is idle, CPU is close to full load, considered to have reached the maximum throughput limit.</td>
  </tr>
</table>

!!! success

    Based on the above, when three replicas of the service are deployed with no resource usage limitations, the DCE 5.0 Cloud-Native Gateway can handle approximately 6,000 to 7,000 concurrent requests, which is excellent performance compared to similar products.

### Test Process Screenshots

- Concurrent Users = 4

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway01.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway02.png)

- Concurrent Users = 8

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway03.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway04.png)

- Concurrent Users = 12
 
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway05.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway06.png)

## Investigating the Impact of Contour Resource Configuration on Envoy Performance

The DCE 5.0 Cloud-Native Gateway is further developed and optimized based on the open-source projects Contour and Envoy. Contour acts as the control plane of the gateway, and Envoy acts as the data plane.

When creating the DCE 5.0 Cloud-Native Gateway, the system requires that the gateway be configured with no less than 1 core and 1 G of resources. Therefore, in this test, the minimum resource limit for Contour is set to 1 core and 1 G.

To better demonstrate the impact of Contour's resource configuration, Envoy's resource limit is set to 6 cores and 3 G to ensure that Envoy itself always has high performance and does not affect the test results due to insufficient resources.

To ensure normal resource load on the stress-testing machine, the Locust users are set to 8 by default.

### Test Results

<table>
  <tr>
    <th>Contour Resource Specification</th>
    <th>Throughput (RPS)</th>
    <th>CPU Utilization</th>
    <th>Analysis</th>
  </tr>
  <tr>
    <td>1 core 1G</td>
    <td>3700</td>
    <td>53%——69%</td>
    <td rowspan="3">Contour's resource configuration ranges from 1 core 1 G to 2 cores 1 G, and then to 3 cores 2 G, but the maximum throughput of the gateway has been maintained at around 3700, with a fluctuation range of only 100. CPU utilization has also remained at around 50% to 70%, with very small overall changes.</td>
  </tr>
  <tr>
    <td>2 cores 1G</td>
    <td>3600</td>
    <td>55%——72%</td>
  </tr>
  <tr>
    <td>3 cores 2G</td>
    <td>3800</td>
    <td>57%——69%</td>
  </tr>
</table>

!!! success

    This indicates that Contour's resource configuration has almost no impact on Envoy's performance.

### Test Process Screenshots

- contour: 1 core 1 G

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway07.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway08.png)

- contour: 2 core 1 G

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway09.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway10.png)

- contour: 3 core 2 G
    
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway11.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway12.png)

## Investigating the Impact of Envoy Resource Configuration on Throughput

Envoy is fixed to 1 replica, Contour is configured with 1 core and 1 G, and the tested service Nginx is configured with 3 replicas with no resource usage limitations.

### Test Results

<table>
  <tr>
    <th>Envoy Resource Specification</th>
    <th>Concurrent Users</th>
    <th>Throughput (RPS)</th>
    <th>CPU Utilization</th>
    <th>Analysis</th>
  </tr>
  <tr>
    <td rowspan="3">1 core 1G</td>
    <td>4</td>
    <td>1016</td>
    <td>18%——22%</td>
    <td rowspan="3">When Envoy's resource configuration remains unchanged, even if the number of concurrent users doubles, the gateway throughput does not change much.</td>
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
    <td rowspan="2">2 cores 1G</td>
    <td>4</td>
    <td>2103</td>
    <td>28%——41%</td>
    <td rowspan="2">With 4 concurrent users, when the resource configuration is increased from 1 core to 2 cores, the throughput also increases by about 1000.</td>
  </tr>
  <tr>
    <td>8</td>
    <td>2284</td>
    <td>38%——47%</td>
  </tr>
  <tr>
    <td rowspan="2">3 cores 1G</td>
    <td>8</td>
    <td>3355</td>
    <td>59%——70%</td>
    <td rowspan="2">With 8 concurrent users, when the resource configuration is increased from 1 core to 3 cores, the throughput also increases by about 2000.</td>
  </tr>
  <tr>
    <td>12</td>
    <td>3552</td>
    <td>52%——59%</td>
  </tr>
  <tr>
    <td rowspan="2">4 cores 2G</td>
    <td>8</td>
    <td>3497</td>
    <td>58%——80%</td>
    <td rowspan="4">With 12 concurrent users, when the resource configuration is increased from 3 cores to 5 cores, the throughput also increases by about 1000.</td>
  </tr>
  <tr>
    <td>12</td>
    <td>4250</td>
    <td>78%——86%</td>
  </tr>
  <tr>
    <td rowspan="2">5 cores 2G</td>
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
    <td rowspan="2">6 cores 2G</td>
    <td>12</td>
    <td>4574</td>
    <td>78%——85%</td>
    <td rowspan="2">When configured with 6 cores and 2 G, the throughput is about 5400, and CPU usage also reaches over 90%, close to full load.</td>
  </tr>
  <tr>
    <td>16</td>
    <td>5401</td>
    <td>Above 90%</td>
  </tr>
</table>

!!! success

    In conclusion:

    - Envoy's CPU configuration is the determining factor for throughput.
    - Under current stress test resources, the throughput of accessing Nginx through Envoy can reach over 80% of directly accessing Nginx.

### Test Process Screenshots

#### Envoy 1 core 1G

- Concurrent Users = 4

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway13.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway14.png)

- Concurrent Users = 8

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway15.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway16.png)

- Concurrent Users = 16

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway17.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway18.png)

#### Envoy 2 core 1 G

- Concurrent Users = 4

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway19.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway20.png)

- Concurrent Users = 8

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway21.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway22.png)

#### Envoy 3 core 1 G

- Concurrent Users = 8

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway23.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway24.png)

- Concurrent Users = 12
    
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway25.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway26.png)

#### Envoy 4 core 2 G

- Concurrent Users = 8

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway27.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway28.png)

- Concurrent Users = 12

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway29.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway30.png)

#### Envoy 5 core 2 G

- Concurrent Users = 8

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway31.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway32.png)

- Concurrent Users = 12

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway33.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway34.png)

#### Envoy 6 core 2 G

- Concurrent Users = 12

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway35.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway36.png)

- Concurrent Users = 16

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway37.png)
    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/test-gateway38.png)
