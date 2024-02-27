# 配置服务发现规则

可观测 Insight 支持通过 __容器管理__ 创建 CRD ServiceMonitor 的方式来满足您自定义服务发现的采集需求。
用户可以通过使用 ServiceMonitor 自行定义 Pod 发现的 Namespace 范围以及通过 __matchLabel__ 来选择监听的 Service。

## 前提条件

集群已安装 Helm 应用 __insight-agent__ 且处于 __运行中__ 状态。

## 操作步骤

1. 选择左侧导航栏的 __采集管理__ ，查看全部集群采集插件的状态。

    ![集群列表](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/collectmanage02.png)

2. 点击列表中的某个集群名称进入采集配置详情。

    ![集群列表](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/service-discover.png)

3. 点击链接跳转到 __容器管理__ 中创建 Service Monitor。

	```yaml
	apiVersion: monitoring.coreos.com/v1
	kind: ServiceMonitor
	metadata:
	  name: micrometer-demo # (1)
	  namespace: insight-system # (2)
	    labels: 
	      operator.insight.io/managed-by: insight
	spec:
	  endpoints: # (3)
	    - honorLabels: true
	        interval: 15s
	        path: /actuator/prometheus
	        port: http
	  namespaceSelector: # (4)
	    matchNames:
	      - insight-system  # (5)
	  selector: # (6)
	    matchLabels:
              micrometer-prometheus-discovery: "true"
	```

	1. 指定 ServiceMonitor 的名称
	2. 指定 ServiceMonitor 的命名空间
	3. 这是服务端点，代表 Prometheus 所需的采集 Metrics 的地址。 __endpoints__ 为一个数组，
	   同时可以创建多个 __endpoints__ 。每个 __endpoints__ 包含三个字段，每个字段的含义如下：

	    - __interval__ ：指定 Prometheus 对当前 __endpoints__ 采集的周期。单位为秒，在本次示例中设定为 __15s__ 。
	    - __path__ ：指定 Prometheus 的采集路径。在本次示例中，指定为 __/actuator/prometheus__ 。
	    - __port__ ：指定采集数据需要通过的端口，设置的端口为采集的 Service 端口所设置的 __name__ 。

	4. 这是需要发现的 Service 的范围。 __namespaceSelector__ 包含两个互斥字段，字段的含义如下：

	    - __any__ ：有且仅有一个值 __true__ ，当该字段被设置时，将监听所有符合 Selector 过滤条件的 Service 的变动。
	    - __matchNames__ ：数组值，指定需要监听的 __namespace__ 的范围。例如，只想监听 default 和 insight-system
		  两个命名空间中的 Service，那么 __matchNames__ 设置如下：

		    ```yaml
			namespaceSelector:
			  matchNames:
			    - default
			    - insight-system
			```

	5. 此处匹配的命名空间为需要暴露指标的应用所在的命名空间
	6. 用于选择 Service
