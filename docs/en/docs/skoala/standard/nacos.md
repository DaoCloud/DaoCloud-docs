# Service Integration with Nacos SDK

This article explains how traditional microservices in different frameworks can integrate with the native Nacos SDK.

## Java (No Framework)

1. Add the dependency in your `pom.xml` file. The latest version currently is `2.2.2`.

   ```xml
   <dependency>
       <groupId>com.alibaba.nacos</groupId>
       <artifactId>nacos-client</artifactId>
       <version>${latest.version}</version>
   </dependency>
   ```

2. Add the code for service registration and discovery in your service:

    ```java
    // Add configuration variables: serverAddr (Nacos address, e.g., 192.168.0.0:8848) and namespace (Nacos namespace)
    Properties properties = new Properties();
    properties.setProperty("serverAddr", System.getProperty("serverAddr"));
    properties.setProperty("namespace", System.getProperty("namespace"));

    NamingService naming = NamingFactory.createNamingService(properties);

    // Register an instance: provide the service name, IP, port, and group
    naming.registerInstance("sentinel-demo", "11.11.11.11", 8888, "DEFAULT");

    System.out.println(naming.getAllInstances("sentinel-demo"));

    naming.deregisterInstance("sentinel-demo", "11.11.11.11", 8888, "DEFAULT");

    System.out.println(naming.getAllInstances("sentinel-demo"));

    // Subscribe to a service to receive event notifications on changes
    naming.subscribe("sentinel-demo", new EventListener() {
        @Override
        public void onEvent(Event event) {
            System.out.println(((NamingEvent)event).getServiceName());
            System.out.println(((NamingEvent)event).getInstances());
        }
    });
    ```

3. If you need to add more features of Nacos, you can refer to [more usage methods](https://github.com/nacos-group/nacos-examples/tree/master/nacos-client-example).

## Java (Spring Boot) Framework

1. Add the dependencies in your `pom.xml` file:

    ```xml
    <dependency>
        <groupId>com.alibaba.boot</groupId>
        <artifactId>nacos-config-spring-boot-starter</artifactId>
        <version>${latest.version}</version>
    </dependency>
    ```

    !!! note

        - Version [0.2.x.RELEASE](https://mvnrepository.com/artifact/com.alibaba.boot/nacos-config-spring-boot-starter) corresponds to Spring Boot 2.x.
        - Version [0.1.x.RELEASE](https://mvnrepository.com/artifact/com.alibaba.boot/nacos-config-spring-boot-starter) corresponds to Spring Boot 1.x.

2. Add the `bootstrap.yaml` configuration file in your project:

    ```yaml
    spring:
      application:
        name: demo
    nacos:
      config:
        data-id: test # Nacos configuration data ID
        server-addr: 127.0.0.1:8848 # Nacos server address
        group: DEFAULT_GROUP # Configuration file group
        namespace: public # Namespace ID
        type: yaml # Nacos configuration file type
        auto-refresh: true # Enable dynamic configuration refresh
      discovery:
        server-addr: 127.0.0.1:8848 # Nacos server address
        group: DEFAULT_GROUP # Group for application registration
        namespace: public # Nacos namespace
    ```

3. Service Registration: No additional code is needed. Simply start the project and you will see the service listed in the service registry.
4. Add codes for Nacos configuration feature in service.

    1. Login to the Nacos console and add a configuration file.
    2. Add the following code to your controller:

      ```java
      @RestController
      @RequestMapping("config")
      public class Controller {
          @NacosValue(value = "${a.test}", autoRefreshed = true)
          private String name;

          @GetMapping("get")
          public String get() {
              return this.name;
          }
      }
      ```

5. If you need to add more features of Nacos, you can refer to [more usage methods](https://github.com/nacos-group/nacos-examples/tree/master/nacos-spring-boot-example).

## Java (Spring Cloud) Framework

1. Add the dependencies in your `pom.xml` file.

   Please refer to the version compatibility table: [Version Compatibility](https://github.com/spring-cloud-incubator/spring-cloud-alibaba/wiki/版本说明)

    ```xml
    <dependency>
        <groupId>com.alibaba.cloud</groupId>
        <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
        <version>${latest.version}</version>
    </dependency>

    <dependency>
        <groupId>com.alibaba.cloud</groupId>
        <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        <version>${latest.version}</version>
    </dependency>
    ```

2. Add the `bootstrap.yaml` configuration file in your project:

    ```yaml
    spring:
      application:
        name: demo

    ---
    spring:
      cloud:
        nacos:
          config:
            enabled: true
            server-addr: 127.0.0.1:8848 # Nacos server address
            name: test # Nacos configuration data ID
            group: DEFAULT_GROUP # Configuration file group
            namespace: public # Namespace ID
            file-extension: yaml # Configuration file extension
          discovery:
            enabled: true
            server-addr: 127.0.0.1:8848 # Nacos server address
            namespace: public # Namespace ID
            group: DEFAULT_GROUP # Application group name
    ```

    Note: Make sure to adjust the `server-addr`, `group`, and `namespace` values according to your Nacos setup.

3. Add the code for Nacos service registration in your service:

    Add the `@EnableDiscoveryClient` annotation on your startup class to enable service registration with Nacos.

    ```java
    @SpringBootApplication
    @EnableDiscoveryClient
    public class NacosProviderApplication {

      public static void main(String[] args) {
        SpringApplication.run(NacosProviderApplication.class, args);
      }
    }
    ```

4. Add the code for dynamic configuration:

    1. Add a configuration file in the Nacos console.

    2. Add the `@RefreshScope` and `@Value` annotations to your controller.

        Using the `@RefreshScope` annotation from Spring Cloud enables auto-configuration.

        ```java
        @RestController
        @RequestMapping("config")
        @RefreshScope
        public class Controller {
            @Value(value = "${a.test}")
            private String name;

            @GetMapping("get")
            public String get() {
                return this.name;
            }
        }
        ```

        Now, whenever the configuration is updated in the Nacos server, the `value` field will reflect the updated value without restarting the application.

5. If you need to add more features of Nacos, you can refer to [more usage methods](https://github.com/nacos-group/nacos-examples/tree/master/nacos-spring-cloud-example).

## Go Framework

To add the Nacos SDK to a Go microservice framework, you need to meet the following prerequisites:

- Go version 1.15 or above
- Nacos version 2.x or above

Here are the steps to add the Nacos SDK:

1. Get the dependencies

    ```go
    $ go get -u github.com/nacos-group/nacos-sdk-go/v2
    ```

2. Add the code for service registration in your service:

    ```go
    // Create ServerConfig, configure Nacos server address
    sc := []constant.ServerConfig{
      *constant.NewServerConfig("127.0.0.1", 8848, constant.WithContextPath("/nacos")),
    }

    // Create ClientConfig, configure client connection settings
    cc := *constant.NewClientConfig(
      constant.WithNamespaceId("public"), // Namespace ID
      constant.WithTimeoutMs(5000), // Timeout duration
      constant.WithLogDir("/tmp/nacos/log"), // Log directory
      constant.WithCacheDir("/tmp/nacos/cache"), // Nacos service cache directory
      constant.WithLogLevel("debug"), // Log level
    )

    // Create NacosClient by providing ServerConfig and ClientConfig
    client, err := clients.NewNamingClient(
      vo.NacosClientParam{
        ClientConfig:  &cc,
        ServerConfigs: sc,
      },
    )

    // Register service
    registerServiceInstance(client, vo.RegisterInstanceParam{
      Ip:          "10.0.0.10",
      Port:        8848,
      ServiceName: "demo.go",
      GroupName:   "group-a",
      ClusterName: "cluster-a",
      Weight:      10,
      Enable:      true,
      Healthy:     true,
      Ephemeral:   true,
      Metadata:    map[string]string{"idc": "shanghai"},
    })

    // Deregister service
    deRegisterServiceInstance(client, vo.DeregisterInstanceParam{
      Ip:          "10.0.0.10",
      Port:        8848,
      ServiceName: "demo.go",
      GroupName:   "group-a",
      Cluster:     "cluster-a",
      Ephemeral:   true, // must be true
    })
    ```

    Make sure to adjust the IP address, port, service name, group name, cluster name, and other parameters according to your setup.

3. Configuration Loading

    ```go
    // Create ServerConfig, configure Nacos server address
    sc := []constant.ServerConfig{
      *constant.NewServerConfig("127.0.0.1", 8848, constant.WithContextPath("/nacos")),
    }

    // Create ClientConfig, configure client connection settings
    cc := *constant.NewClientConfig(
      constant.WithNamespaceId("public"), // Namespace ID
      constant.WithTimeoutMs(5000), // Timeout duration
      constant.WithLogDir("/tmp/nacos/log"), // Log directory
      constant.WithCacheDir("/tmp/nacos/cache"), // Nacos service cache directory
      constant.WithLogLevel("debug"), // Log level
    )

    // Create NacosClient by providing ServerConfig and ClientConfig
    client, err := clients.NewNamingClient(
      vo.NacosClientParam{
        ClientConfig:  &cc,
        ServerConfigs: sc,
      },
    )

    // Get config
    content, err := client.GetConfig(vo.ConfigParam{
      DataId: "test-data",
      Group:  "test-group",
    })
    fmt.Println("GetConfig, config: " + content)

    // Listen for config change, key = dataId + group + namespaceId
    err = client.ListenConfig(vo.ConfigParam{
      DataId: "test-data",
      Group:  "test-group",
      OnChange: func(namespace, group, dataId, data string) {
        fmt.Println("Config changed, group: " + group + ", dataId: " + dataId + ", content: " + data)
      },
    })
    ```

    Make sure to adjust the `DataId` and `Group` values according to your setup.

4. To add more features of Nacos, you can refer to [more usage methods](https://github.com/nacos-group/nacos-sdk-go).

## Python Framework

1. Get the dependencies

    ```sh
    pip install nacos-sdk-python
    ```

2. Add codes

    ```python
    import nacos

    # Nacos server address
    SERVER_ADDRESSES = "127.0.0.1:8848"
    # Namespace ID
    NAMESPACE = "public"

    client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE)

    # Register service
    client.add_naming_instance("test.service1", "1.0.0.7", 8080, "testCluster2", 0.2, "{}", False, True)
    # Send heartbeat
    client.send_heartbeat("test.service", "1.0.0.7", 8080, "testCluster2", 0.1, "{}")


    # Get config
    data_id = "dev-config"
    group = "DEFAULT_GROUP"

    # Global service configuration
    server_config = json.loads(client.get_config(data_id, group))

    # When the service configuration changes
    def config_update(data):
        global server_config
        server_config = json.loads(data['content'])
        print('new data->', server_config)

    # Listen for service configuration changes
    client.add_config_watcher(data_id, group, config_update)
    ```

3. If you need to add more features of Nacos, please refer to [more usage methods](https://github.com/nacos-group/nacos-sdk-python).

## Node.js Framework

1. Add dependencies

    User version of `2.x` or higher

    ```shell
    npm install nacos --save
    ```

2. Add code for service discovery

    ```js
    'use strict';

    const NacosNamingClient = require('nacos').NacosNamingClient;
    const logger = console;

    const client = new NacosNamingClient({
      logger,
      serverList: '127.0.0.1:8848', // Nacos server address
      namespace: 'public', // Namespace ID
    });
    await client.ready();

    const serviceName = 'nodejs.test.domain';

    // Register service
    await client.registerInstance(serviceName, {
      ip: '1.1.1.1',
      port: 8080,
    });
    await client.registerInstance(serviceName, {
      ip: '2.2.2.2',
      port: 8080,
    });

    // Subscribe to service
    client.subscribe(serviceName, hosts => {
      console.log(hosts);
    });

    // Deregister service
    await client.deregisterInstance(serviceName, {
      ip: '1.1.1.1',
      port: 8080,
    });
    ```

3. Add codes for dynamic configuration

    ```js
    import {NacosConfigClient} from 'nacos';   // ts
    const NacosConfigClient = require('nacos').NacosConfigClient; // js


    const configClient = new NacosConfigClient({
      serverAddr: '127.0.0.1:8848',
      namespace: 'public', //namespace ID
    });

    // get config file
    const content= await configClient.getConfig('test', 'DEFAULT_GROUP'); //dataID: test,group: DEFAULT_GROUP
    console.log('getConfig = ',content);

    // listen to config changes
    configClient.subscribe({
      dataId: 'test',
      group: 'DEFAULT_GROUP',
    }, content => {
      console.log(content);
    });
    ```

4. If you need to add more features of Nacos, please refer to [more usage methods](https://github.com/nacos-group/nacos-sdk-nodejs).

## C++ Framework

1. Download Dependencies

    Download the project [source code](https://github.com/nacos-group/nacos-sdk-cpp) and follow the instructions below:

    ```sh
    cd nacos-sdk-cpp
    cmake .
    make
    ```

    After executing the command, you will get a `libnacos-cli.so` and a `nacos-cli.out` file.

2. Run `make install` to install `libnacos-cli` into the `lib` directory.

3. Add code logic for service registration in your service code.

    ```c++
    #include <iostream>
    #include <unistd.h>
    #include "Nacos.h"

    using namespace std;
    using namespace nacos;

    int main() {
        Properties configProps;
        configProps[PropertyKeyConst::SERVER_ADDR] = "127.0.0.1"; // nacos server ip
        configProps[PropertyKeyConst::NAMESPACE] = "public"; // namespace ID
        NacosServiceFactory *factory = new NacosServiceFactory(configProps);
        ResourceGuard <NacosServiceFactory> _guardFactory(factory);
        NamingService *namingSvc = factory->CreateNamingService();
        ResourceGuard <NamingService> _serviceFactory(namingSvc);
        Instance instance;
        instance.clusterName = "DEFAULT";
        instance.ip = "127.0.0.1";
        instance.port = 2333;
        instance.instanceId = "1";
        instance.ephemeral = true;

        // Simulate Registering 5 Services
        try {
            for (int i = 0; i < 5; i++) {
                NacosString serviceName = "TestNamingService" + NacosStringOps::valueOf(i);
                instance.port = 2000 + i;
                namingSvc->registerInstance(serviceName, instance);
            }
        }
        catch (NacosException &e) {
            cout << "encounter exception while registering service instance, raison:" << e.what() << endl;
            return -1;
        }
        sleep(30);
        // deregister services
        try {
            for (int i = 0; i < 5; i++) {
                NacosString serviceName = "TestNamingService" + NacosStringOps::valueOf(i);

                namingSvc->deregisterInstance(serviceName, "127.0.0.1", 2000 + i);
                sleep(1);
            }
        }
        catch (NacosException &e) {
            cout << "encounter exception while registering service instance, raison:" << e.what() << endl;
            return -1;
        }
        sleep(30);

        return 0;
    }
    ```

4. Add codes for dynamic configuration

    ```c++
    #include <iostream>
    #include "Nacos.h"

    using namespace std;
    using namespace nacos;

    class MyListener : public Listener {
    private:
        int num;
    public:
        MyListener(int num) {
            this->num = num;
        }

        void receiveConfigInfo(const NacosString &configInfo) {
            cout << "===================================" << endl;
            cout << "Watcher" << num << endl;
            cout << "Watched Key UPDATED:" << configInfo << endl;
            cout << "===================================" << endl;
        }
    };

    int main() {
        Properties props;
        props[PropertyKeyConst::SERVER_ADDR] = "127.0.0.1:8848"; //nacos地址
        props[PropertyKeyConst::NAMESPACE] = "public"; // 命名空间ID
        NacosServiceFactory *factory = new NacosServiceFactory(props);
        ResourceGuard <NacosServiceFactory> _guardFactory(factory);
        ConfigService *n = factory->CreateConfigService();
        ResourceGuard <ConfigService> _serviceFactory(n);

        MyListener *theListener = new MyListener(1);//You don't need to free it, since it will be deleted by the function removeListener
        n->addListener("dqid", "DEFAULT_GROUP", theListener);//dataID is "dqid", and group is "DEFAULT_GROUP". config changes will be watched

        cout << "Input a character to continue" << endl;
        getchar();
        cout << "remove listener" << endl;
        n->removeListener("dqid", NULLSTR, theListener);//cancel listener
        getchar();

        return 0;
    }
    ```

5. If you need to add more features of Nacos, please refer to [more usage methods](https://github.com/nacos-group/nacos-sdk-cpp/blob/master/README.md).
