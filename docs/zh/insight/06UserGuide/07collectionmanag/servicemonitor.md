# 配置服务发现规则

可观测 Insight 支持通过`容器管理`创建 CRD ServiceMonitor 的方式来满足您自定义服务发现的采集需求。
用户可以通过使用 ServiceMonitor 自行定义 Pod 发现的 Namespace 范围以及通过 `matchLabel` 来选择监听的 Service。

## 前提条件

集群已安装 Helm 应用 `insight-agent` 且处于`运行中`状态。

## 操作步骤

1. 选择左侧导航栏的`采集管理`，查看全部集群采集插件的状态。

  ![集群列表](../../images/collectmanage02.png)

2. 点击列表`集群名称`进入采集配置详情。

  ![集群列表](../../images/service-discover.png)

3. 点击链接跳转到`容器管理` 中创建 Service Monitor。

	``` ruby
	apiVersion: monitoring.coreos.com/v1 
		kind: ServiceMonitor 
		metadata: 
			name: micrometer-demo 
			namespace: default 
		spec: 
			endpoints: 
				- interval: 15s 
				path: /actuator/prometheus 
				port: metrics 
			namespaceSelector: 
				any: true 
			selector:
				matchLabels: 
					micrometer-prometheus-discovery: 'true'
	```

在这段YAML文件中，各代码段的含义如下：
-   `metadata` 下的 `name` 和 `namespace` 将指定 ServiceMonitor 所需的一些关键元信息。
-   `spec` 的 `endpoints` 为服务端点，代表Prometheus所需的采集Metrics的地址。`endpoints` 为一个数组，同时可以创建多个` endpoints` 。每个 `endpoints` 包含三个字段，每个字段的含义如下：
    -   `interval`：指定Prometheus对当前 `endpoints` 采集的周期。单位为秒，在本次示例中设定为`15s`。
    -   `path`：指定Prometheus的采集路径。在本次示例中，指定为 `/actuator/prometheus`。
    -   `port`：指定采集数据需要通过的端口，设置的端口为采集的 Service 端口所设置的`name`。
- `spec`的`namespaceSelector`为需要发现的Service的范围。`namespaceSelector`包含两个互斥字段，字段的含义如下：
		-   `any`：有且仅有一个值`true`，当该字段被设置时，将监听所有符合Selector过滤条件的Service的变动。
		-   `matchNames`：数组值，指定需要监听的 `namespace` 的范围。例如，只想监听default和kpanda-system 两个命名空间中的Service，那么 `matchNames` 设置如下：

	```ruby
	namespaceSelector: 
		matchNames: 
		- default 
		- kpanda-system
	```

- `spec`的`selector`用于选择Service。
