# 服务接入 Sentinel 集群流控

为服务接入 Sentinel 集群流控时，需要从服务器和客户端两方面调整配置。

## 集群流控服务器

DCE 5.0 不提供托管的 Sentinel 服务器，所以用户需自己启动 Sentinel 官方提供的集群流控服务器，且该服务器需要满足以下条件：

- 连接 Nacos，以便从 Nacos 读取持久化配置

- 为 Sentinel 服务器命名，以便作为配置前缀来区分多个集群流控服务器的 `NamespaceSet` 和 `ServerTransport` 配置

    ```java
    ReadableDataSource<String, Set<String>> namespaceDs = new NacosDataSource<>(nacosAddress, DEFAULT_GROUP,
                    serverName + NAMESPACESET_POSTFIX,
                    source -> JSON.parseObject(source, new TypeReference<Set<String>>() {}));
            ClusterServerConfigManager.registerNamespaceSetProperty(namespaceDs.getProperty());
            ReadableDataSource<String, ServerTransportConfig> transportConfigDs = new NacosDataSource<>(nacosAddress, DEFAULT_GROUP,
                    serverName + SERVERTRANSPORT_POSTFIX,
                    source -> JSON.parseObject(source, new TypeReference<ServerTransportConfig>() {}));
            ClusterServerConfigManager.registerServerTransportProperty(transportConfigDs.getProperty());
    ```

- 相关的代码实现，可参考 [sentinel-cluster-flow-control-java](https://github.com/projectsesame/sentinel-cluster-flow-control-java)

## 集群流控客户端

由于 Sentinel 官方提供的客户端 `sentinel-cluster-client-default` SDK 只适配内存模式使用。而 DCE 5.0 也为集群流控客户端配置做了持久化，所以官方原始客户端 SDK 已无效。

1. 首先，用户需引入如下代码：

    ```java
    public class SentinelClusterClientInitFunc implements InitFunc {

       private String nacosAddress;
       private Properties properties = new Properties();
       private String groupId;
       private String dataId;

       @Override
       public void init() throws Exception {
           getNacosAddr();

           parseAppName();

           initDynamicRuleProperty();

           initClientConfigProperty();

           initClientServerAssignProperty();

           initStateProperty();
       }

       private void getNacosAddr() {
           nacosAddress = System.getProperty("nacos.address");
           if (StringUtil.isBlank(nacosAddress)){
               throw new RuntimeException("nacos address start param must be set");
           }
           System.out.printf("nacos address: %s\n", nacosAddress);
       }

       private void parseAppName() {
           String[] apps = APPNAME.split("@@");
           System.out.printf("app name: %s\n", APPNAME);
           if (apps.length != 3) {
               throw new RuntimeException("app name format must be set like this: {{namespaceId}}@@{{groupName}}@@{{appName}}");
           } else if (StringUtil.isBlank(apps[1])){
               throw new RuntimeException("group name cannot be empty");
           }
           properties.put(PropertyKeyConst.NAMESPACE, apps[0]);
           properties.put(PropertyKeyConst.SERVER_ADDR, nacosAddress);
           properties.put(PropertyKeyConst.USERNAME, DEFAULT_NACOS_USERNAME);
           properties.put(PropertyKeyConst.PASSWORD, DEFAULT_NACOS_PASSWORD);
           groupId = apps[1];
           dataId = apps[2];
       }

       private void initDynamicRuleProperty() {
           ReadableDataSource<String, List<FlowRule>> ruleSource = new NacosDataSource<>(properties, groupId,
               dataId + FLOW_POSTFIX, source -> JSON.parseObject(source, new TypeReference<List<FlowRule>>() {}));
           FlowRuleManager.register2Property(ruleSource.getProperty());

           ReadableDataSource<String, List<ParamFlowRule>> paramRuleSource = new NacosDataSource<>(properties, groupId,
                   dataId +  PARAM_FLOW_POSTFIX, source -> JSON.parseObject(source, new TypeReference<List<ParamFlowRule>>() {}));
           ParamFlowRuleManager.register2Property(paramRuleSource.getProperty());
       }

       private void initClientConfigProperty() {
           ReadableDataSource<String, ClusterClientConfig> clientConfigDs = new NacosDataSource<>(properties, groupId,
                   dataId + CLUSTER_CLIENT_POSTFIX, source -> JSON.parseObject(source, new TypeReference<ClusterClientConfig>() {}));
           ClusterClientConfigManager.registerClientConfigProperty(clientConfigDs.getProperty());
       }

       private void initClientServerAssignProperty() {
    //       Cluster map format:
    //       [
    //           {
    //               "machineId": "10.64.0.81@8720",
    //                "ip": "10.64.0.81",
    //                "port": 18730,
    //                "clientSet": ["10.64.0.81@8721", "10.64.0.81@8722"]
    //           }
    //       ]
           ReadableDataSource<String, ClusterClientAssignConfig> clientAssignDs = new NacosDataSource<>(properties, groupId,
                   dataId +  CLUSTER_MAP_POSTFIX, source -> {
               List<ClusterGroupDto> groupList = JSON.parseObject(source, new TypeReference<List<ClusterGroupDto>>() {});
               return Optional.ofNullable(groupList)
                   .flatMap(this::extractClientAssignment)
                   .orElse(null);
           });
           ClusterClientConfigManager.registerServerAssignProperty(clientAssignDs.getProperty());
       }

       private void initStateProperty() {
           ReadableDataSource<String, Integer> clusterModeDs = new NacosDataSource<>(properties, groupId,
                   dataId + CLUSTER_MAP_POSTFIX, source -> {
               List<ClusterGroupDto> groupList = JSON.parseObject(source, new TypeReference<List<ClusterGroupDto>>() {});
               return Optional.ofNullable(groupList)
                   .map(this::extractMode)
                   .orElse(ClusterStateManager.CLUSTER_NOT_STARTED);
           });
           ClusterStateManager.registerProperty(clusterModeDs.getProperty());
       }

       private int extractMode(List<ClusterGroupDto> groupList) {
           if (groupList.stream().anyMatch(this::machineEqual)) {
               return ClusterStateManager.CLUSTER_SERVER;
           }

           boolean canBeClient = groupList.stream()
               .flatMap(e -> e.getClientSet().stream())
               .filter(Objects::nonNull)
               .anyMatch(e -> e.equals(getCurrentMachineId()));
           return canBeClient ? ClusterStateManager.CLUSTER_CLIENT : ClusterStateManager.CLUSTER_NOT_STARTED;
       }

       private Optional<ClusterClientAssignConfig> extractClientAssignment(List<ClusterGroupDto> groupList) {
           if (groupList.stream().anyMatch(this::machineEqual)) {
               return Optional.empty();
           }
           for (ClusterGroupDto group : groupList) {
               if (group.getClientSet().contains(getCurrentMachineId())) {
                   String ip = group.getIp();
                   Integer port = group.getPort();
                   return Optional.of(new ClusterClientAssignConfig(ip, port));
               }
           }
           return Optional.empty();
       }

       private boolean machineEqual(ClusterGroupDto group) {
           return getCurrentMachineId().equals(group.getMachineId());
       }

       private String getCurrentMachineId() {
           return HostNameUtil.getIp() + SEPARATOR + TransportConfig.getRuntimePort();
       }

       private static final String SEPARATOR = "@";
    }
    ```

2. 接着在 Spring 容器中通过如下方式加载：

    ```java
    @PostConstruct
    public void initSentinelClusterFlow() throws Exception{
    	new SentinelClusterClientInitFunc().init();
    }
    ```
