# 通知模板使用说明

## 模板语法（Go Template）说明

告警通知模板采用了 [Go Template](https://pkg.go.dev/text/template) 语法来渲染模板。

模板会基于下面的数据进行渲染。

```json
{
    "status": "firing",
    "labels": {
        "alertgroup": "test-group",           // 告警策略名称
        "alertname": "test-rule",          // 告警规则名称
        "cluster": "35b54a48-b66c-467b-a8dc-503c40826330",
        "customlabel1": "v1",
        "customlabel2": "v2",
        "endpoint": "https",
        "group_id": "01gypg06fcdf7rmqc4ksv97646",
        "instance": "10.6.152.85:6443",
        "job": "apiserver",
        "namespace": "default",
        "prometheus": "insight-system/insight-agent-kube-prometh-prometheus",
        "prometheus_replica": "prometheus-insight-agent-kube-prometh-prometheus-0",
        "rule_id": "01gypg06fcyn2g9zyehbrvcdfn",
        "service": "kubernetes",
        "severity": "critical",
        "target": "35b54a48-b66c-467b-a8dc-503c40826330",
        "target_type": "cluster"
   },
    "annotations": {
        "customanno1": "v1",
        "customanno2": "v2",
        "description": "这是一条测试规则，10.6.152.85:6443 down",
        "value": "1"
    },
    "startsAt": "2023-04-20T07:53:54.637363473Z",
    "endsAt": "0001-01-01T00:00:00Z",
    "generatorURL": "http://vmalert-insight-victoria-metrics-k8s-stack-df987997b-npsl9:8080/vmalert/alert?group_id=16797738747470868115&alert_id=10071735367745833597",
    "fingerprint": "25c8d93d5bf58ac4"
}
```

### 使用说明

1. `.` 字符

    在当前作用域下渲染指定对象。

    示例 1: 取顶级作用域下的所有内容，即示例代码中上下文数据的全部内容。

    ```go
    {{ . }}
    ```

2. 判断语句 `if / else`

    使用 if 检查数据，如果不满足可以执行 else。

    ```go
    {{if .Labels.namespace }}命名空间：{{ .Labels.namespace }} \n{{ end }}
    ```

3. 循环函数 `for`

    for 函数用于重复执行代码内容。

    示例 1: 遍历 labels 列表，获取告警的所有 label 内容。

    ```go
    {{ for .Labels}} \n {{end}}
    ```

## 函数说明 FUNCTIONS

Insight 的”通知模板“和”短信模板“支持 70 多个 [sprig](http://masterminds.github.io/sprig/) 函数，以及自研的函数。

### Sprig 函数

Sprig 内置了 70 多种常见的模板函数帮助渲染数据。以下列举常见函数：

* [时间操作](http://masterminds.github.io/sprig/date.html)
* [字符串操作](http://masterminds.github.io/sprig/strings.html)
* [类型转换操作](http://masterminds.github.io/sprig/conversion.html)
* [整数的数学计算](http://masterminds.github.io/sprig/math.html)

更多细节可以查看[官方文档](http://masterminds.github.io/sprig/)。

### 自研函数

#### toClusterName

`toClusterName` 函数根据“集群唯一标示 Id”查询“集群名”；如果查询不到对应的集群，将直接返回传入的集群的唯一标示。

```go
func toClusterName(id string) (string, error)
```

**示例：**

```go-templates
{{ toClusterName "clusterId" }}
{{ "clusterId" | toClusterName }}
```

#### toClusterId

`toClusterId` 函数根据“集群名”查询“集群唯一标示 Id”；如果查询不到对应的集群，将直接返回传入的集群名。

```go
func toClusterId(name string) (string, error)
```

**示例：**

```go-templates
{{ toClusterId "clusterName" }}
{{ "clusterName" | toClusterId }}
```

#### toDateInZone

`toDateInZone` 根据字符串时间转换成所需的时间，并进行格式化。

```go
func toDateInZone(fmt string, date interface{}, zone string) string
```

**示例 1**：

```go-templates
{{ toDateInZone "2006-01-02T15:04:05" "2022-08-15T05:59:08.064449533Z" "Asia/Shanghai" }}
```

将获得返回值 `2022-08-15T13:59:08`。此外，也可以通过 sprig 内置的函数达到 `toDateInZone` 的效果：

```go-templates
{{ dateInZone "2006-01-02T15:04:05" (toDate "2006-01-02T15:04:05Z07:00" .StartsAt) "Asia/Shanghai" }}
```

**示例 2**：

```go-templates
{{ toDateInZone "2006-01-02T15:04:05" .StartsAt "Asia/Shanghai" }}


## 阈值模板说明

Insight 内置 Webhook 告警模板如下，其他如邮件、企业微信等内容相同，只是对换行进行相应调整。

```text
规则名称：{{ .Labels.alertname }} \n
策略名称：{{ .Labels.alertgroup }} \n
告警级别：{{ .Labels.severity }} \n
集群：{{ .Labels.cluster }} \n
{{if .Labels.namespace }}命名空间：{{ .Labels.namespace }} \n{{ end }}
{{if .Labels.node }}节点：{{ .Labels.node }} \n{{ end }}
资源类型：{{ .Labels.target_type }} \n
{{if .Labels.target }}资源名称：{{ .Labels.target }} \n{{ end }}
触发值：{{ .Annotations.value }} \n
发生时间：{{ .StartsAt }} \n
{{if ne "0001-01-01T00:00:00Z" .EndsAt }}结束时间：{{ .EndsAt }} \n{{ end }}
描述：{{ .Annotations.description }} \n
```

### 邮箱主题参数

由于 Insight 在发送告警消息时，会对同一时间同一条规则产生的消息进行合并发送，
所以 email 主题不同于上面四种模板，只会使用告警消息中的 commonLabels 内容对模板进行渲染。默认模板如下: 

```go
[{{ .status }}] [{{ .severity }}] 告警：{{ .alertname }}
```

其他可作为邮箱主题的字段如下: 

```text
{{ .status }} 告警消息的触发状态
{{ .alertgroup }} 告警所属的策略名称
{{ .alertname }} 告警所属的规则名称
{{ .severity }} 告警级别
{{ .target_type }} 告警资源类型
{{ .target }} 告警资源对象
{{ .规则其他自定义 label key }}
```
