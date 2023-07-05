# Sentinel 应用监控接入文档

1. 应用 sentinel metric exporter sdk 版本 >=  [v2.0.0-alpha](https://github.com/alibaba/Sentinel/releases/tag/2.0.0-alpha)

   ```xml
   <dependency>
     <groupId>com.alibaba.csp</groupId>
     <artifactId>sentinel-metric-exporter</artifactId>
     <version>v2.0.0-alpha</version>
   </dependency>
   ```

   原因可参考：https://github.com/alibaba/Sentinel/pull/2976

2. 应用启动添加 javaagent 参数（-javaagent:/jmx_prometheus_javaagent-0.17.0.jar=12345:/prometheus-jmx-config.yaml），且 jmx 端口固定为：12345

   jmx 使用可参考：https://docs.daocloud.io/en/insight/user-guide/quickstart/jvm-monitor/jmx-exporter/

3. 应用创建 kubernetes service，核心包括

   - labels 字段，固定为：skoala.io/type: sentinel

   - port 字段，固定为：name: jmx-metrics，port: 12345，targetPort: 12345

   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     labels:
       skoala.io/type: sentinel
     name: sentinel-demo
     namespace: skoala-jia
   spec:
     ports:
     - name: jmx-metrics
       port: 12345
       protocol: TCP
       targetPort: 12345
     selector:
       app.kubernetes.io/name: sentinel-demo
   ```

   原因可参考系统 ServiceMonitor CR定义：

   ```yaml
   apiVersion: monitoring.coreos.com/v1
   kind: ServiceMonitor
   metadata:
     labels:
       release: insight-agent
       operator.insight.io/managed-by: insight
     name: sentinel-service-monitor
   spec:
     endpoints:
       - port: jmx-metrics
         scheme: http
     jobLabel: jobLabel
     namespaceSelector:
       any: true
     selector:
       matchLabels:
         skoala.io/type: sentinel
   ```

