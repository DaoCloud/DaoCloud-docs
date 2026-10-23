# Service Integration with Sentinel Specification

To normally use the [Sentinel traffic governance](../trad-ms/hosted/plugins/sentinel.md) and view
[Sentinel data monitoring](../trad-ms/hosted/monitor/components.md) provided by the DCE microservice engine,
you need to integrate the application with the Sentinel console, and certain specifications
must be met when passing the application parameters.

## Java (No Framework)

!!! note

    - The following operations apply to any version of the Sentinel SDK.
    - When you integrate a service in the following way, the rules created in the UI will not take effect,
      because the client does not connect to Nacos or other storage to obtain the rules, but directly sets
      the rules based on memory.
    - The following method is mainly applicable to the scenario of quickly integrating Sentinel for verification,
      or the scenario where the Spring Cloud framework is not used.

<!-- - You can refer to the code: <https://gitlab.daocloud.cn/ndx/sentinel/-/tree/main/sentinel-demo/daocloud-java> -->

1. Add dependencies in the `pom.xml` file.

    ```xml
    <!-- Add the sentinel core dependency-->
    <dependency>
      <groupId>com.alibaba.csp</groupId>
      <artifactId>sentinel-core</artifactId>
      <version>1.8.6</version>
    </dependency>

    <!-- Add the sentinel console dependency-->
    <dependency>
      <groupId>com.alibaba.csp</groupId>
      <artifactId>sentinel-transport-simple-http</artifactId>
      <version>1.8.6</version>
    </dependency>
    ```

2. Set rules using the Sentinel API.

    ```java
    private static void initFlowRules(){
      List<FlowRule> rules = new ArrayList<>();
      FlowRule rule = new FlowRule();
      rule.setResource("HelloWorld");
      rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
      // Set limit QPS to 20.
      rule.setCount(20);
      rules.add(rule);
      FlowRuleManager.loadRules(rules);
    }
    ```

3. Define resources using the Sentinel API.

    ```java
    public static void main( String[] args ) {
      // Configure rules
      initFlowRules();
   
      while (true) {
      // Since version 1.5.0, the try-with-resources feature can be used directly
      try (Entry entry = SphU.entry("HelloWorld")) {
      // Protected logic
      System.out.println("hello world");
      } catch (BlockException ex) {
      // Logic to handle flow control
      System.out.println("blocked!");
      }
      }
    }
    ```

4. Add the JVM parameter to connect to the Sentinel console, and start the application.

    ```shell
    # ip:port is the address of the Sentinel console
    -Dcsp.sentinel.dashboard.server=10.6.176.50:32196
    ```

5. Open the Sentinel console, find the corresponding application and verify the flow control effect.

    <!--![]()screenshots-->

## Java (SpringCloud) Framework

When integrating microservices of the SpringCloud framework, the following requirements must be met.

### project.name Naming Specification

The `project.name` parameter for integrating an application with the Sentinel console must use the following format:

```java
{{nacos_namespace_id}}@@{{nacos_group}}@@{{appName}}
```

!!! note

    - When this specification is met, the Sentinel governance rules will be pushed to the configuration
      center in the corresponding configuration group under the corresponding namespace.
    - The first part `{{nacos_namespace_id}}` refers to the **ID** of the Nacos namespace, not the name of the namespace.
    - The ID corresponding to the Nacos `public` namespace is the null character "". If you want to integrate
      the application with the `public` namespace, you must use an empty string, for example, `@@A@@appA`.
    - This specification must be met, otherwise unknown errors will be caused.

### Naming Specification of the dataId That Sentinel Writes to the Nacos Configuration Center

- Flow control rules: {{appName}}-flow-rules
- Degrade rules: {{appName}}-degrade-rules
- System rules: {{appName}}-system-rules
- Authority rules: {{appName}}-authority-rules
- Hotspot rules: {{appName}}-param-rules

appName is the last part of the three-part project.name.

### Built-in Communication User Agreed Between Sentinel and Nacos

```yaml
username: skoala
password: 98985ba0-da90-41f6-b6dc-96f2ec49d973
```

### Recommended Integration Method

After the above three conditions are met, it is recommended to use the following method to integrate
microservices of the SpringCloud framework with Sentinel.

!!! note

    - After the above three conditions are met, the DCE microservice engine does not mandate a specific integration method.
    - The DCE microservice engine is fully compatible with relevant open source frameworks, and developers
      can flexibly use an appropriate integration method according to their needs.

<!--- You can refer to the code: https://gitlab.daocloud.cn/ndx/sentinel/-/tree/main/sentinel-demo/daocloud-springcloud-->

1. Add dependencies in the `pom.xml` file.

    For the version correspondence, refer to: [Release Notes](https://github.com/spring-cloud-incubator/spring-cloud-alibaba/wiki/版本说明).

    ```xml
    <!-- Add the Sentinel dependency-->
    <dependency>
      <groupId>com.alibaba.cloud</groupId>
      <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
    </dependency>

    <!-- Add the Sentinel Nacos data source dependency-->
    <dependency>
      <groupId>com.alibaba.csp</groupId>
      <artifactId>sentinel-datasource-nacos</artifactId>
    </dependency>

    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```

2. Add the `application.yaml` configuration file in the project.

    ```yaml title="application.yaml"
    nacos:
      # Nacos address
      address: 10.6.176.50:30760
      # Nacos configuration center namespace
      namespace:
      # Nacos configuration center group
      group: DEFAULT_GROUP

    # Name of the application integrated with the sentinel console
    project:
      name: ${nacos.namespace}@@${nacos.group}@@${spring.application.name}
    spring:
      application:
        name: daocloud-springcloud
      cloud:
        sentinel:
          # Sentinel Nacos data source
          datasource:
            flow:
              nacos:
                server-addr: ${nacos.address}
                dataId: ${spring.application.name}-flow-rules
                groupId: ${nacos.group}
                namespace: ${nacos.namespace}
                # Specified by the microservice engine: the user and password agreed between Nacos and Sentinel
                username: skoala
                password: 98985ba0-da90-41f6-b6dc-96f2ec49d973
                ruleType: flow
            degrade:
              nacos:
                server-addr: ${nacos.address}
                # Specified by the microservice engine: naming convention for Sentinel writing to Nacos
                dataId: ${spring.application.name}-degrade-rules
                groupId: ${nacos.group}
                namespace: ${nacos.namespace}
                # Specified by the microservice engine: the user and password agreed between Nacos and Sentinel
                username: skoala
                password: 98985ba0-da90-41f6-b6dc-96f2ec49d973
                rule-type: degrade
            system:
              nacos:
                server-addr: ${nacos.address}
                # Specified by the microservice engine: naming convention for Sentinel writing to Nacos
                dataId: ${spring.application.name}-system-rules
                groupId: ${nacos.group}
                namespace: ${nacos.namespace}
                # Specified by the microservice engine: the user and password agreed between Nacos and Sentinel
                username: skoala
                password: 98985ba0-da90-41f6-b6dc-96f2ec49d973
                rule-type: system
            authority:
              nacos:
                server-addr: ${nacos.address}
                # Specified by the microservice engine: naming convention for sentinel writing to nacos
                dataId: ${spring.application.name}-authority-rules
                groupId: ${nacos.group}
                namespace: ${nacos.namespace}
                # Specified by the microservice engine: the user and password agreed between nacos and sentinel
                username: skoala
                password: 98985ba0-da90-41f6-b6dc-96f2ec49d973
                rule-type: authority
            param-flow:
              nacos:
                server-addr: ${nacos.address}
                # Specified by the microservice engine: naming convention for sentinel writing to nacos
                dataId: ${spring.application.name}-param-rules
                groupId: ${nacos.group}
                namespace: ${nacos.namespace}
                # Specified by the microservice engine: the user and password agreed between nacos and sentinel
                username: skoala
                password: 98985ba0-da90-41f6-b6dc-96f2ec49d973
                rule-type: param-flow

    ```

3. Write the relevant Web API.

    ```java
    @SpringBootApplication
    @RestController
    @RequestMapping
    public class App {
        public static void main( String[] args ) {
            SpringApplication.run(App.class, args);
        }
   
        @GetMapping("/hello")
        public String hello(){
            return "hello world";
        }
    }
    ```

4. Create a flow control rule in the Sentinel console.

    <!--![]()screenshots-->

5. Start the application and add the JVM parameter to connect to the Sentinel console.

    ```java
    -Dcsp.sentinel.dashboard.server=10.6.176.50:32196
    ```

6. Use a script to access the Web API for which the flow control rule is set. For example:

    ```java
    while true; do curl http://localhost:8080/hello; done
    ```

7. Verify in the Sentinel console whether the rule takes effect.

    <!--![]()screenshots-->
