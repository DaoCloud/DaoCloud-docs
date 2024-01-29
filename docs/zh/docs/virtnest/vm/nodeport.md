# 通过 NodePort 访问虚拟机

本文将介绍如何通过 NodePort 访问虚拟机。

## 现有访问方式的缺陷

1. 虚拟机支持通过 VNC 或者 console 访问，但这两种访问方式都有一个弊端，无法多终端同时在线。

2. 通过 NodePort 形式的 Service，可以帮助解决这个问题。

## 创建 service 的方式

1. 通过容器管理页面

    - 选择目标访问的虚拟机所在集群页面创建服务（Service）
    - 选择访问类型为节点访问（NodePort）
    - 选择命名空间（虚拟机所在 namespace）
    - 标签选择器填写 `vm.kubevirt.io/name:you-vm-name`
    - 端口配置：协议选择 TCP，端口名称自定义，服务端口、容器端口填写 22

2. 创建成功后，就可以通过 `ssh username@nodeip -p port` 来访问虚拟机

## 通过 kubectl 创建 svc

1. 编写 YAML 文件，示例如下：

    ```yaml
    apiVersion: v1
    kind: Service
      metadata:
        name: test-ssh
    spec:
      ports:
      - name: tcp-ssh
        nodePort: 32090
        protocol: TCP
        // 22 端口，不要更改
        port: 22 
        targetPort: 22
      selector:
        // 虚拟机的 name
       vm.kubevirt.io/name: test-image-s3
      type: NodePort
    ```

1. 执行以下命令

    ```sh
    kubectl apply -f you-svc.yaml
    ```

1. 创建成功后，就可以通过 `ssh username@nodeip -p 32090` 来访问虚拟机
