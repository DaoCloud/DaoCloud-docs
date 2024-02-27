# 兼容性测试报告 - OpenShift

基于 OpenShift，测试服务网格在创建专有网格时的兼容性。

本次测试报告以 OpenShift 4.11 为例，详细阐述了服务网格接入 OpenShift 专有网格模式时的兼容性测试过程。

## 测试目的

验证 DCE 5.0 服务网格上创建基于原生 istio，从控制面/数据面聚合 OpenShift 单集群模式的专有网格。

## 测试环境

### 服务网格环境

基于 demo-dev.daocloud.io

### OpenShift 环境

准备了 OpenShift 3 个节点：

|           HostName            |      IP      | Kubernetes 版本 | Crictl 版本 |         OS 内核版本          | OS Release |
| :---------------------------: | :----------: | :-------------: | :---------- | :--------------------------: | :--------- |
| master01.mspider.openshift.io | 10.6.157.111 | v1.24.0+3882f8f | 1.24.2      | 4.18.0-372.26.1.el8_6.x86_64 | rhcos      |
| master02.mspider.openshift.io | 10.6.157.112 | v1.24.0+3882f8f | 1.24.2      | 4.18.0-372.26.1.el8_6.x86_64 | rhcos      |
| master03.mspider.openshift.io | 10.6.157.113 | v1.24.0+3882f8f | 1.24.2      | 4.18.0-372.26.1.el8_6.x86_64 | rhcos      |

查看 3 个节点的状况：

```shell
oc get nodes -owide
```

输出类似于：

```none
NAME                          STATUS   ROLES          AGE   VERSION           INTERNAL-IP    EXTERNAL-IP OS-IMAGE                                                       KERNEL-VERSION                CONTAINER-RUNTIME
master01.mspider.openshift.io Ready    master.worker  7d3h  v1.24.0+3882f8f   10.6.157.111   <none>      Red Hat Enterprise Linux CoreOS 411.86.202209211811-0 (Ootpa)  4.18.0-372.26.1.el8_6.x86_64  cri-o://1.24.2-7.rhaos4.11.gitca400e0.el8
master02.mspider.openshift.io Ready    master.worker  7d2h  v1.24.0+3882f8f   10.6.157.112   <none>      Red Hat Enterprise Linux CoreOS 411.86.202209211811-0 (Ootpa)  4.18.0-372.26.1.el8_6.x86_64  cri-o://1.24.2-7.rhaos4.11.gitca400e0.el8
master03.mspider.openshift.io Ready    master.worker  7d2h  v1.24.0+3882f8f   10.6.157.113   <none>      Red Hat Enterprise Linux CoreOS 411.86.202209211811-0 (Ootpa)  4.18.0-372.26.1.el8_6.x86_64  cri-o://1.24.2-7.rhaos4.11.gitca400e0.el8
```

## 测试过程

### 通过容器管理接入 OpenShift

获取 OpenShift 集群的 kubeconfig (～/.kube/config)，在 demo-dev 环境的容器管理中接入集群。

```yaml
clusters:
- cluster:
    insecure-skip-tls-verify: true
    server: https://10.6.157.130:6443
  name: mspider
contexts:
- context:
    cluster: mspider
    user: admin
  name: admin
current-context: admin
preferences: {}
users:
- name: admin
  user:
    client-certificate-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURaekNDQWsrZ0F3SUJBZ0lJV0wzelp0MFErbGt3RFFZSktvWklodmNOQVFFTEJRQXdOakVTTUJBR0ExVUUKQ3hNSmIzQmxibk5vYVdaME1TQXdIZ1lEVlFRREV4ZGhaRzFwYmkxcmRXSmxZMjl1Wm1sbkxYTnBaMjVsY2pBZQpGdzB5TWpFd01qWXhNekE1TWpaYUZ3MHpNakV3TWpNeE16QTVNalphTURBeEZ6QVZCZ05WQkFvVERuTjVjM1JsCmJUcHRZWE4wWlhKek1SVXdFd1lEVlFRREV3eHplWE4wWlcwNllXUnRhVzR3Z2dFaU1BMEdDU3FHU0liM0RRRUIKQVFVQUE0SUJEd0F3Z2dFS0FvSUJBUUNtZ2RKcUNCTCtGcmRmQmVseGU2dkNnbWpZMXJqN09rV1dDTHVUVWVJWgoyaWg1NHBWUVByUzVkQVEvbUVaME1NcTVBSmQ4dE1maWpVcFlnQkU4d1pmeU0wZEM0d3h0empXWnZvQWhSejZUCjFuRDFvd1RsZndJMDJjZ0lkZUpJSlJEa2tsV3JQUjVRZU0wbytLdWYrN1dFUDVSSW82bWVxVEtuUHBuMmRyaWwKQUxPSFIvQWFiaklqVG51YUM2QWNlSzdyN1VobGtQQ2pRK3dKdVI1cld5eW9HVFBTMlc4MVd6Mm9UNi9UQ05UVQpYTDhncWFoa2dlWGpYZkl0bzYweVVpNnV3K1dMNk1oc0NhVlpXZG1TaDVRMzZZdTlSZEFKazduaHlVR3JkNXRYCmplRm9LM0gyZjcycmwrOGdrcTdlVjNVYjRPY2pyU2VUUTIvNlY5NjhwQzcxQWdNQkFBR2pmekI5TUE0R0ExVWQKRHdFQi93UUVBd0lGb0RBZEJnTlZIU1VFRmpBVUJnZ3JCZ0VGQlFjREFRWUlLd1lCQlFVSEF3SXdEQVlEVlIwVApBUUgvQkFJd0FEQWRCZ05WSFE0RUZnUVVEdW1uRWkxWjRlLytlcjJXcEY4bTBLODhGcE13SHdZRFZSMGpCQmd3CkZvQVVBM1VjTVdYYjh5aE54TVgrOUhBcWpneTBYMnN3RFFZSktvWklodmNOQVFFTEJRQURnZ0VCQUYvL1BvM3MKSWp5N2tva1p2OU1LUDJvMm9ubWdhY0owNklIay9VbTVIbC8rMVE5WmhDeDJWSDNtWnIyME5kQ0M5Rm03OFovZwpoK3lDVi9hbGRXTnAxUXhyaWJUbGpscmNsek55L20vYWRmMUhKSGoram1mdEJFeCtmNkVEdFFQZ3BUZUlCbk01CnhzMDFSUldwVTBKVnVsYU5RclphNHUyYVZnc3h3djYzdEEyeXlzblpxbGFqWktNZjU3TEhNTjBKdE10K3FyTDMKS1p1R1pqblVvcDk3SFh0VDVBZ01jU1R1V0UyME9QR0tldFVuTVI3cldza2pvSlU5VWNSelBTQ1FGTWZCam53VQpNLzNRM0lYTmNVay9mSDdxZk1DV2pGL29sNWNXMnhZOTN4ekF0bTVFWVpUei9VRk4wOEFzS09qMS9hRWVBaHlICkFhclV5UHBEYTlwUkpJWT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=
    client-key-data: LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0NBUUVBcG9IU2FnZ1MvaGEzWHdYcGNYdXJ3b0pvMk5hNCt6cEZsZ2k3azFIaUdkb29lZUtWClVENjB1WFFFUDVoR2REREt1UUNYZkxUSDRvMUtXSUFSUE1HWDhqTkhRdU1NYmM0MW1iNkFJVWMrazladzlhTUUKNVg4Q05ObklDSFhpU0NVUTVKSlZxejBlVUhqTktQaXJuL3UxaEQrVVNLT3BucWt5cHo2WjluYTRwUUN6aDBmdwpHbTR5STA1N21ndWdISGl1NisxSVpaRHdvMFBzQ2JrZWExc3NxQmt6MHRsdk5WczlxRSt2MHdqVTFGeS9JS21vClpJSGw0MTN5TGFPdE1sSXVyc1BsaStqSWJBbWxXVm5aa29lVU4rbUx2VVhRQ1pPNTRjbEJxM2ViVjQzaGFDdHgKOW4rOXE1ZnZJSkt1M2xkMUcrRG5JNjBuazBOditsZmV2S1F1OVFJREFRQUJBb0lCQUJ5dHo2Z2pxK0hIMTkydQpEdjlVNWNpaTNadzduN0RsNEladkNwL2RRcXhoUHdkL1YyaHk1SDNzMWE1K2MrUWZZMHRxSnExOEZkR1h0RzU1CjRINHVlaFZsYjZpOW9xNW5EaVJsQTN5MzRMZG1BQjdPN1ZENkIwOURFNGtoaE5BWVVraU1TK1VxcWNZQ2lKTysKQVJHVk1UYU9IT1JHRERrZnUzSEMvcEhNOFJDNlB3dzJxV1BCazZJKzJWbHdGZTNDMUZGTGpHL0IxQkFPaUZkYQpibUxkMU85cEt4QVMvODlBSzJYd0RBY1MwWk0zaDRTTkl5LzIvcVY0MHRHUFFhaG5RWEJKcGpNRy9ZQWV0U3JkClVES3VnSkF6azVvT2Q0Z1pVSlNzZFYvK3lCQlJlc2Zta3FpTTdxQXArZVpzbkxUUERYZy8zcDlCcXd2eHJUKzcKb3BGaFVTRUNnWUVBeVEyZFZaRHZHcWljTzFXSVF1VFZYbFBsdjd4dTl2aklic1pxZWV3K1FlVXBnYkFoOXFQMApwbDJsaGtFR1VIZjZzeUdnb3BUTnRaci9IYzVCUXRSbzJGbzl4Z25QZkxTQ21ZMS9FbTQyd3UzUmhJNVNZOU1ICmZWYVFTeS9vRTRrQ3Y1ZmpTSmM2dkZ1aHVYTllFWkhraWRmSHFValFDazduRTErY2lxT01YNWNDZ1lFQTFBTSsKVitXWXIvb0JSaEVpck9vbVF1U1l1d1lRcHhKaVF1UFBzUk9jR3VkRUFXU2V6SVVRV2RSTERETEl6cHhuUHhGQgpGMHRrQnY4VmhrMk9uS0dRazAweVZnTlhnOHlvMnBlNk8zQ0w1QUdiMTdPMlBvWmJ4Mkozc1JNa3Fuc015US92CkJVbUJ6YXVTTWEwVXprREFoU0xHaU01V253dDNMOEpEaUE0ZWQxTUNnWUFWUFAzd3l3V25FRWFvc2VsWi82aFcKZFpCZ2g3eEZGSlMvdHZBS2Z4MDRnc2Uycm05NENXdlBvemJZRHNobStiV2U5Sjl1YlQrcHZuelNuallncENXTApMVVUzUlZRSXZWektjYnNKckdEV2lKN0lYT3h4SlJxMmI4MkFVOGcxUUJUdFBsTkJHTkNZa3lscldMYmw3RDV6CkhUczNNN3plU2VWNUUzR0s1Nm50Y3dLQmdRRExNQVNheHE4cjBFVlNPbS9xR2tuckNCeWIrVGNTZDVyMmtsQmwKVys3YkZkTm1KbUhPanFSYUF3eWR0em9lVVdUZDI1SnZXZENXcC9lZ0RFcG1NSzFYanI5MEVhWFk2ZGJXRUYzcQpRM1crWWhCU2pLaFhpZnNCdm93Smg5ZzNEdEQxRFRFODl2TFJBdUtNZTEyYVFoS0FSaERSNGpiQUhJUHdvSlNLCkcwWDFnd0tCZ0J3cERlNmJWMGc2aEQzN1VVOStpQnBTblVnWWNzLzZBVlJOR0k5RDhreFFIb1JESnNWT2ZVV1QKaERDWDF2aUFpU0hEUStmSzlIZUhOWVk5Z05iRmdRakpDdlAxbHFRYU9IZnltUGliWUo5OVgxWnZ5eWlqNjJkbQo1a3gvMnhwOGJPanM0U2hCY21JcGc5TjFZODl1UWtpTlJ4MEl0NUdFRWJweFNXQ1U4TGEyCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0tCg==
```

在容器管理中查看接入集群的状态：

![接入 openshift](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/os01.png)

### 创建专有网格

1. 登录 global-cluster 节点，查看服务网格同步容器管理接入集群的状态。

    ![查看集群接入状态](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/os02.png)

1. 完成创建网格时的配置后，点击 __确定__ 。

    > 对于控制面集群，请选择通过容器管理接入的 openshift4-mspider 集群

    ![创建网格](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/os03.png)

1. OpenShift 集群成功接入网格

    ![成功接入网格](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/os04.png)

1. 查看各个组件是否健康

    ![组件状况](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/os05.png)

    ![组件状况](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/os06.png)

#### 接入时遇到的问题

1. 提示错误 __istio-operator RS CreateFailed__ 

    ![RS CreateFailed](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/os07.png)

    原因分析：OpenShift（安全上下文约束）SCC 对创建 Pod 有权限限制

    解决办法：增加 SCC 用户命名空间权限 "privileged"

    ```sh
    oc adm policy add-scc-to-user privileged -z istio-operator
    oc adm policy add-scc-to-user privileged -z istio-system
    oc adm policy add-scc-to-group privileged system:authenticated
    ```

    重启 istio-operator rs 解决问题。

2. 提示错误 __message: no running Istio pods in "istio-system"__ 

    原因分析：字面提示是 istio-system 命名空间下缺少 istiod/istio-ingressgateway service pod。
    实际是网格全局边车资源限制中的内存资源参数格式错误；正确格式为 500Mi

    ![资源参数格式](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/os08.png)

    解决办法：修改 yaml 文件，添加 Mi 单位

    ```shell
    kubectl edit gm -n mspider-system openshift -oyaml
    ```

    ![修改单位](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/os09.png)

3. 注入边车时提示 __pod Init:CrashLoopBackOff__ 

    激活 ocp iptables

    ```yaml
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: dsm-init
      namespace: openshift-sdn
    spec:
      revisionHistoryLimit: 10
      selector:
        matchLabels:
          app: dsm-init
      template:
        metadata:
          labels:
            app: dsm-init
            type: infra
        spec:
          containers:
          - command:
            - /bin/sh
            - -c
            - |
              #!/bin/sh
              set -x
              iptables -t nat -A OUTPUT -m tcp -p tcp -m owner ! --gid-owner 1337 -j REDIRECT --to-ports 15006
              iptables -t nat -D OUTPUT -m tcp -p tcp -m owner ! --gid-owner 1337 -j REDIRECT --to-ports 15006
              while true; do sleep 100d; done
            image: release.daocloud.io/mspider/proxyv2:1.15.0
            name: dsm-init
            resources:
              requests:
                cpu: 100m
                memory: 20Mi
            securityContext:
              privileged: true
          dnsPolicy: ClusterFirst
          hostNetwork: true
          hostPID: true
          nodeSelector:
            kubernetes.io/os: linux
          priorityClassName: system-node-critical
          restartPolicy: Always
          schedulerName: default-scheduler
          securityContext: {}
          serviceAccount: sdn
          serviceAccountName: sdn
    ```

    运行命令：

    ```shell
    kubectl edit gm -n mspider-system openshift -oyaml
    ```

    添加： `istio.custom_params.components.cni.enabled: "true"` 

### 部署 bookinfo 应用测试

创建 bookinfo namespace，部署 bookinfo 应用时需要对命名空间添加 SCC。

```shell
oc adm policy add-scc-to-user privileged -z bookinfo
```

1. 启用命名空间边车注入

    ![启用命名空间边车注入](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/os10.png)

    ![查看命名空间边车](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/os11.png)

1. 终端查看 bookinfo 命名空间 Labels

    ```shell
    oc describe ns bookinfo |grep "istio-injection-enabled"
    ```

    屏幕输出类似于：

    ```none
    Labels: istio-injection-enabled
    ```

1. 部署 bookinfo 应用

    ```shell
    oc apply -f https://raw.githubusercontent.com/istio/istio/release-1.15/samples/bookinfo/platform/kube/bookinfo.yaml -n bookinfo
    ```

    ![部署 bookinfo](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/os12.png)

    ```shell
    oc get pod -n bookinfo
    ```
