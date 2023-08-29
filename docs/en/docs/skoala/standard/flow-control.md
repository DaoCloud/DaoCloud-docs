# Service Integration with Sentinel Cluster Flow Control

When integrating a service with the Sentinel cluster flow control, configuration adjustments need to be made on both the server and client sides.

## Sentinel Cluster Flow Control Server

DCE 5.0 does not provide a managed Sentinel server, so users need to start the Sentinel cluster flow control server provided by the official Sentinel. The server should meet the following requirements:

- Connect to Nacos to read persistent configurations.

- Name the Sentinel server so that it can be used as a configuration prefix to differentiate the `NamespaceSet` and `ServerTransport` configurations of multiple cluster flow control servers.

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

- For the relevant code implementation, you can refer to [sentinel-cluster-flow-control-java](https://github.com/projectsesame/sentinel-cluster-flow-control-java).

## Sentinel Cluster Flow Control Client

Since the official Sentinel client SDK `sentinel-cluster-client-default` is only compatible with in-memory mode, and DCE 5.0 also provides persistence for cluster flow control client configuration, the original official client SDK is no longer applicable.

1. First, you need to import the following code:

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

2. Next, you can load it in the Spring container using the following approach:

    ```java
    @PostConstruct
    public void initSentinelClusterFlow() throws Exception{
    	new SentinelClusterClientInitFunc().init();
    }
    ```
