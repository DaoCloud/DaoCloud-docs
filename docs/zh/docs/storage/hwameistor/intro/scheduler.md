---
hide:
  - toc
---

# 调度器

调度器 (scheduler) 是 HwameiStor 的重要组件之一。
它自动将 Pod 调度到配有 HwameiStor 存储卷的正确节点。
使用调度器后，Pod 不必再使用 NodeAffinity 或 NodeSelector 字段来选择节点。
调度器能处理 LVM 和 Disk 存储卷。

- 安装

    调度器应在集群中以 HA 模式部署，这是生产环境中的最佳实践。

- 通过 hwameistor-operator 安装

    hwameistor-operator 安装后会自动将 HwameiStor 相关组件拉起。
    参阅[通过 hwameistor-operator 安装 HwameiStor](../install/deploy-operator.md)。

- 通过 YAML 部署（针对开发）

    ```bash
    kubectl apply -f deploy/scheduler.yaml
    ```

<details>
    <summary>点击此处查看 scheduler.yaml</summary>
    <pre><code>
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hwameistor-scheduler
  namespace: {{ .Release.Namespace }}
spec:
  replicas: {{ .Values.scheduler.replicas }}
  selector:
    matchLabels:
      app: hwameistor-scheduler
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: hwameistor-scheduler
    spec:
      affinity:
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 1
              preference:
                matchExpressions:
                  - key: node-role.kubernetes.io/master
                    operator: Exists
                  - key: node-role.kubernetes.io/control-plane
                    operator: Exists
      containers:
      - args:
        - -v=2
        - --bind-address=0.0.0.0
        - --leader-elect=false
        - --leader-elect-resource-name=hwameistor-scheduler
        - --leader-elect-resource-namespace={{ .Release.Namespace }}
        - --config=/etc/hwameistor/hwameistor-scheduler-config.yaml
        image: {{ .Values.global.hwameistorImageRegistry }}/{{ .Values.scheduler.imageRepository }}:{{ template "hwameistor.scheudlerImageTag" . }}
        imagePullPolicy: IfNotPresent
        name: hwameistor-kube-scheduler
        resources:
          {{- toYaml .Values.scheduler.resources | nindent 12 }}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /etc/hwameistor/
          name: hwameistor-scheduler-config
          readOnly: true
      volumes:
      - configMap:
          name: hwameistor-scheduler-config 
          items:
          - key: hwameistor-scheduler-config.yaml
            path: hwameistor-scheduler-config.yaml
        name: hwameistor-scheduler-config
      serviceAccountName: hwameistor-admin 
      serviceAccount: hwameistor-admin
      tolerations:
      - key: CriticalAddonsOnly
        operator: Exists
      - effect: NoSchedule
        key: node.kubernetes.io/not-ready
        operator: Exists
      - effect: NoSchedule
        key: node-role.kubernetes.io/master
        operator: Exists
      - effect: NoSchedule
        key: node-role.kubernetes.io/control-plane
        operator: Exists
      - effect: NoSchedule
        key: node.cloudprovider.kubernetes.io/uninitialized
        operator: Exists
    </code></pre>
</details>
