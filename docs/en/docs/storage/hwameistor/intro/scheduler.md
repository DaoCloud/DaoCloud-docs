# Scheduler

The scheduler is one of the important components of HwameiStor. It automatically schedules Pods to the correct nodes with HwameiStor storage volumes. With the scheduler, Pods no longer have to use the NodeAffinity or NodeSelector fields to select nodes. The scheduler can handle LVM and Disk storage volumes.

## Install

The scheduler should be deployed in HA mode in the cluster, which is a best practice in production environments.

## Deploy via Helm Chart

The scheduler must be used with local disks and a local disk manager. It is recommended to install via [Helm Chart](../install/deploy-helm.md).

## Deploy via YAML (for development)

```bash
kubectl apply -f deploy/scheduler.yaml
```

<details>
    <summary>Click here to view scheduler.yaml</summary>
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
