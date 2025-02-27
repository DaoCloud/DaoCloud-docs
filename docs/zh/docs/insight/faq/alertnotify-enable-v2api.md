# Insight 告警通知开启  v1alpha2

Insight 引入了新的模板体系，新的模板体系在渲染的数据结构上做了调整，因此和旧版本（v1alpha1）存在兼容性的问题。
为了避免产生兼容性的问题，默认不启用。用户需要主动开启。
需要特别注意的是，开启时，需要立即迁移模板到 v1alpha2 语法，否则将产生“使用已保存的原消息模板无法正常发送告警消息”错误的问题。（运维实践：记住备份旧模板数据）

本文接下来将介绍：

- [开启新模板](#v1alpha2)
- [迁移至新模板](#_1)

## 启用 v1alpha2

### 方法 1：(推荐) 通过 helm 命令 upgrade

1. 在 Helm upgrade 的执行命令中增加如下参数：

    ```shell
    --set server.alerting.notifyTemplate.version="v1alpha2"
    ```

2. 除 #1 之外亦可编辑 helm 的 values 文件，如下：

    ```diff
    server:
      alerting:
        notifyTemplate:
    -     version: v1alpha1
    +     version: v1alpha2
    ```

### 方法 2：临时调整配置文件（configmap）

1. 编辑 insight-server 的配置文件（configmap）insight-server-config，调整配置文件如下：

    ```diff
    alerting:
      notifyTemplate:
    -   version: v1alpha1
    +   version: v1alpha2
    ```

2. 编辑保存之后，重启 insight-server 即可。

## 模板迁移

模板的迁移主要是因为数据结构从 AmAlert 调整为 AMHookRequest，新的模板语句可以渲染和展示更多的有用信息。

### 数据架构

这是 v1alpha2 的模板里使用的结构：

```go
type AMHookRequest struct {
	Version           string            `protobuf:"bytes,1,opt,name=version,proto3" json:"version,omitempty"`
	GroupKey          string            `protobuf:"bytes,2,opt,name=groupKey,proto3" json:"groupKey,omitempty"`
	Status            string            `protobuf:"bytes,3,opt,name=status,proto3" json:"status,omitempty"`
	Receiver          string            `protobuf:"bytes,4,opt,name=receiver,proto3" json:"receiver,omitempty"`
	GroupLabels       map[string]string `protobuf:"bytes,5,rep,name=groupLabels,proto3" json:"groupLabels,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	CommonLabels      map[string]string `protobuf:"bytes,6,rep,name=commonLabels,proto3" json:"commonLabels,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	CommonAnnotations map[string]string `protobuf:"bytes,7,rep,name=commonAnnotations,proto3" json:"commonAnnotations,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	ExternalURL       string            `protobuf:"bytes,8,opt,name=externalURL,proto3" json:"externalURL,omitempty"`
	Alerts            []*AmAlert        `protobuf:"bytes,9,rep,name=alerts,proto3" json:"alerts,omitempty"`
	TruncatedAlerts   int64             `protobuf:"varint,10,opt,name=truncatedAlerts,proto3" json:"truncatedAlerts,omitempty"`
}
```

这是 v1alpha1 的模板里使用的结构：

```go
type AmAlert struct {
	Status       string            `protobuf:"bytes,1,opt,name=status,proto3" json:"status,omitempty"`
	Labels       map[string]string `protobuf:"bytes,2,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	Annotations  map[string]string `protobuf:"bytes,3,rep,name=annotations,proto3" json:"annotations,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	StartsAt     string            `protobuf:"bytes,4,opt,name=startsAt,proto3" json:"startsAt,omitempty"`
	EndsAt       string            `protobuf:"bytes,5,opt,name=endsAt,proto3" json:"endsAt,omitempty"`
	GeneratorURL string            `protobuf:"bytes,6,opt,name=generatorURL,proto3" json:"generatorURL,omitempty"`
	Fingerprint  string            `protobuf:"bytes,7,opt,name=fingerprint,proto3" json:"fingerprint,omitempty"`
}
```

可以注意到，最大的差别是，旧结构仅仅是新结构的 `.Alerts`  字段，新结构提供更丰富的 CommonLabels，CommonAnnotations 等信息。

## 示例

以邮件通知模板为例，下面是新旧模板的 diff。可以看到，第二行新增了 `{{range .Alerts}}` 语法，只需将原有模板包裹在 `range` 关键字中即可。
需要特别注意的是，邮件的标题和正文**共享相同的数据结构**，不再进行特殊处理，从而降低心智负担。

```diff
+<b style="font-weight: bold">[{{ .Alerts | len -}}] {{.Status}}</b><br />
+{{range .Alerts}}
ruleName: {{ .Labels.alertname }} <br />
groupName: {{ .Labels.alertgroup }} <br />
severity: {{ .Labels.severity }} <br />
cluster: {{ .Labels.cluster | toClusterName }} <br />
{{if .Labels.namespace }} namespace: {{ .Labels.namespace }} <br /> {{ end }}
{{if .Labels.node }} node: {{ .Labels.node }} <br /> {{ end }}
targetType: {{ .Labels.target_type }} <br />
{{if .Labels.target }} target: {{ .Labels.target }} <br /> {{ end }}
value: {{ .Annotations.value }} <br />
startsAt: {{ .StartsAt }} <br />
{{if ne "0001-01-01T00:00:00Z" .EndsAt }} EndsAt: {{ .EndsAt }} <br /> {{ end }}
description: {{ .Annotations.description }} <br />
+<br />
+{{end}}
```

旧模板的写法：

```
[{{ .status }}] [{{ .severity }}] alert: {{ .alertname }}
```

新模板里，可以注意到 severity 调整为 CommonLabels.severity，这才是原始的无额外处理的数据结构。

```
[{{ .Status }}] [{{ .CommonLabels.severity }}] alert: {{ .CommonLabels.alertname }}
```

### 更多示例

飞书、钉钉和企业微信的通知模板。

```diff
+[{{ .Alerts | len -}}] {{.Status}}
+{{range .Alerts}}
Rule Name:   {{ .Labels.alertname }}
Group Name:  {{ .Labels.alertgroup }}
Severity:    {{ .Labels.severity }}
Cluster:     {{ .Labels.cluster | toClusterName }}
{{if .Labels.namespace }}Namespace:  {{ .Labels.namespace }}
{{ end }}{{if .Labels.node }}Node:  {{ .Labels.node }}
{{ end }}Target Type: {{ .Labels.target_type }}
{{if .Labels.target }}Target:  {{ .Labels.target }} 
{{ end }}Value:       {{ .Annotations.value }}
Starts At:   {{ .StartsAt }}
{{if ne "0001-01-01T00:00:00Z" .EndsAt }}Ends At:     {{ .EndsAt }}
{{ end }}Description: {{ .Annotations.description }}
+{{end}}
```
