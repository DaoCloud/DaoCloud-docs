# 自定义 Elasticsearch 索引名

随着集群规模和应用数量的增加，为提升日志查询效率，同时满足不同客户对索引管理的需求，Insight 对索引进行了调整。由原来的 All-In-One 索引调整成了默认根据 Kubernetes 集群隔离的方式。

- Insight < 0.23.0
```bash
insight-es-k8s-logs-000001

insight-es-k8s-event-logs-000001

skoala-gw-000002
```

- Insight >= 0.23.0
```bash
insight-es-k8s-logs-b699320e-d929-401c-bab1-810449248520-2023.12.07-000011

insight-es-k8s-event-logs-b699320e-d929-401c-bab1-810449248520-2023.12.07-000011

skoala-gw-b699320e-d929-401c-bab1-810449248520-2023.12.07-000011
```
此次调整主要是在 Elasticsearch 存储侧采用了官方推荐的 [DataStream](https://www.elastic.co/guide/en/elasticsearch/reference/current/data-streams.html) 方式来管理索引。

## 为什么默认根据集群 ID 划分索引？

因为无法形成一个通用的划分规则满足所有客户，所以默认根据集群 ID划分是一个比较稳妥的方式。

如果项目中遇到如下问题，则可以考虑自定义索引名：
- 同一集群的不同 Namespace 下，应用产生的日志量各不相同，无法分开管理。
- 用户希望基于 kubernetes 的 Namespace 或者 Deployment Name 以及其他需求来划分索引。
- ...

## 如何自定义？
根据前面 [DataStream](https://www.elastic.co/guide/en/elasticsearch/reference/current/data-streams.html)  原理，我们只需要保证在数据最终写入 Elasticsearch 的时候 DataStream 或者索引名以 `insight-es-k8s-logs-`, `insight-es-k8s-event-logs-` 为前缀即可。

### 示例：
- 如果是通过 [Fluentbit](https://fluentbit.io/) 写入 Elasticsearch，则可以在 Fluentbit ES Output 中配置：

```bash
    [OUTPUT]
        Name           es
        Alias          es.kubeevent.syslog
        Match_Regex    (?:kubeevent)\.(.*)
        Host           172.16.160.1
        Port           30374
        Index          insight-es-k8s-event-logs-b699320e-d929-401c-bab1-810449248520-myapp-mypod # 👈 自定义 DataStream 或者索引名
        HTTP_User      elastic
        HTTP_Passwd    ${ES_PASSWORD}
        Retry_Limit    3
        Type           _doc
        Trace_Error    on
        Replace_Dots   On
        Time_Key       @timestamp
```

- 如果是通过 [Logstash](https://www.elastic.co/guide/en/logstash/8.13/index.html) 从 Kafka 消费日志数据并写入 Elasticsearch，则可以在 Logstash Pipeline 中配置：

```bash
    output {
      if [kafka_topic] == "insight-event" {
        elasticsearch {
          hosts => ["https://xxx.xxx.xx.xx:32427"] # elasticsearch 地址
          user => 'elastic'                         # elasticsearch 用户名
          ssl => 'true'
          password => 'mypassword'    # elasticsearch 密码
          ssl_certificate_verification => 'false'
          index => "insight-es-k8s-event-logs-mycluster-mynamespace" # 👈 自定义 DataStream 或者索引名
        }
      }
    }
```

- 如果是通过 [Vector](https://vector.dev/docs/) 从 Kafka 消费日志数据并写入 Elasticsearch，则可以在 Vector Sinks 中配置：

```yaml
    sinks:
      insight_es_logs:
        type: elasticsearch
        inputs:
          - insight_logs_remap
        api_version: auto
        auth:
          strategy: basic
          user: elastic
          password: mypassword
        bulk:
          index: insight-es-k8s-event-logs-mycluster-mynamespace # 👈 自定义 DataStream 或者索引名
        endpoints:
          - 'http://x.x.x.x:30141'
        tls:
          verify_certificate: false
          verify_hostname: false
```
