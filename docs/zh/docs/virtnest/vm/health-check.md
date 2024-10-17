# 健康检查

当配置虚拟机的存活（Liveness）和就绪（Readiness）探针时，与 Kubernetes 的配置过程相似。本文将介绍如何通过 YAML 为虚拟机配置健康检查参数。

但是需要注意：需要在虚拟机创建成功并且处于关机状态下，修改 YAML 进行配置。

## 配置 HTTP Liveness Probe

1. 在 spec.template.spec 中配置 livenessProbe.httpGet。
2. 修改 cloudInitNoCloud 以启动一个 HTTP 服务器。

    ??? note "点击查看 YAML 示例配置"
    
        ```yaml
        apiVersion: kubevirt.io/v1
        kind: VirtualMachine
        metadata:
          annotations:
            kubevirt.io/latest-observed-api-version: v1
            kubevirt.io/storage-observed-api-version: v1
            virtnest.io/alias-name: ''
            virtnest.io/image-secret: ''
            virtnest.io/image-source: docker
            virtnest.io/os-image: release-ci.daocloud.io/virtnest/system-images/ubuntu-22.04-x86_64:v1
          creationTimestamp: '2024-10-15T02:39:45Z'
          finalizers:
            - kubevirt.io/virtualMachineControllerFinalize
          generation: 1
          labels:
            virtnest.io/os-family: Ubuntu
            virtnest.io/os-version: '22.04'
          name: test-probe
          namespace: amamba-team
          resourceVersion: '254032135'
          uid: 6d92779d-7415-4721-8c7b-a2dde163d758
        spec:
          dataVolumeTemplates:
            - metadata:
                creationTimestamp: null
                name: test-probe-rootdisk
                namespace: amamba-team
              spec:
                pvc:
                  accessModes:
                    - ReadWriteOnce
                  resources:
                    requests:
                      storage: 10Gi
                  storageClassName: hwameistor-storage-lvm-hdd
                source:
                  registry:
                    url: >-
                  docker://release-ci.daocloud.io/virtnest/system-images/ubuntu-22.04-x86_64:v1
          runStrategy: Halted
          template:
            metadata:
              creationTimestamp: null
            spec:
              architecture: amd64
              domain:
                cpu:
                  cores: 1
                  sockets: 1
                  threads: 1
                devices:
                  disks:
                    - bootOrder: 1
                      disk:
                        bus: virtio
                      name: rootdisk
                    - disk:
                        bus: virtio
                      name: cloudinitdisk
                  interfaces:
                    - masquerade: {}
                      name: default
                machine:
                  type: q35
                memory:
                  guest: 2Gi
                resources:
                  requests:
                    memory: 2Gi
              networks:
                - name: default
                  pod: {}
              livenessProbe:
                initialDelaySeconds: 120
                periodSeconds: 20
                httpGet:
                  port: 1500
                timeoutSeconds: 10
              volumes:
                - dataVolume:
                    name: test-probe-rootdisk
                  name: rootdisk
                - cloudInitNoCloud:
                    userData: |
                      #cloud-config
                      ssh_pwauth: true
                      disable_root: false
                      chpasswd: {"list": "root:dangerous", expire: False}
                      runcmd:
                        - sed -i "/#\?PermitRootLogin/s/^.*$/PermitRootLogin yes/g" /etc/ssh/sshd_config
                        - systemctl restart ssh.service
                        - dhclient -r && dhclient
                        - apt-get update && apt-get install -y ncat
                        - ["systemd-run", "--unit=httpserver", "ncat", "-klp", "1500", "-e", '/usr/bin/echo -e HTTP/1.1 200 OK\nContent-Length: 12\n\nHello World!']
                  name: cloudinitdisk
        ```

3. 根据操作系统（如 Ubuntu/Debian 或 CentOS），userData 的配置可能有所不同。主要区别：
   
    - 包管理器：

        Ubuntu/Debian 使用 apt-get 作为包管理器。
        CentOS 使用 yum 作为包管理器。
   
    - SSH 服务重启命令：  

        Ubuntu/Debian 使用 systemctl restart ssh.service。
        CentOS 使用 systemctl restart sshd.service（注意 CentOS 7 及之前版本使用 service sshd restart）。

    - 安装的软件包：

        Ubuntu/Debian 安装 ncat。
        CentOS 安装 nmap-ncat（因为 ncat 在 CentOS 的默认仓库中可能不可用）。

## 配置 TCP Liveness Probe

在 spec.template.spec 中配置 livenessProbe.tcpSocket。

??? note "点击查看 YAML 示例配置"

    ```yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      annotations:
        kubevirt.io/latest-observed-api-version: v1
        kubevirt.io/storage-observed-api-version: v1
        virtnest.io/alias-name: ''
        virtnest.io/image-secret: ''
        virtnest.io/image-source: docker
        virtnest.io/os-image: release-ci.daocloud.io/virtnest/system-images/ubuntu-22.04-x86_64:v1
      creationTimestamp: '2024-10-15T02:39:45Z'
      finalizers:
        - kubevirt.io/virtualMachineControllerFinalize
      generation: 1
      labels:
        virtnest.io/os-family: Ubuntu
        virtnest.io/os-version: '22.04'
      name: test-probe
      namespace: amamba-team
      resourceVersion: '254032135'
      uid: 6d92779d-7415-4721-8c7b-a2dde163d758
    spec:
      dataVolumeTemplates:
        - metadata:
            creationTimestamp: null
            name: test-probe-rootdisk
            namespace: amamba-team
          spec:
            pvc:
              accessModes:
                - ReadWriteOnce
              resources:
                requests:
                  storage: 10Gi
              storageClassName: hwameistor-storage-lvm-hdd
            source:
              registry:
                url: >-
              docker://release-ci.daocloud.io/virtnest/system-images/ubuntu-22.04-x86_64:v1
      runStrategy: Halted
      template:
        metadata:
          creationTimestamp: null
        spec:
          architecture: amd64
          domain:
            cpu:
              cores: 1
              sockets: 1
              threads: 1
            devices:
              disks:
                - bootOrder: 1
                  disk:
                    bus: virtio
                  name: rootdisk
                - disk:
                    bus: virtio
                  name: cloudinitdisk
              interfaces:
                - masquerade: {}
                  name: default
            machine:
              type: q35
            memory:
              guest: 2Gi
            resources:
              requests:
                memory: 2Gi
          networks:
            - name: default
              pod: {}
          livenessProbe:
            initialDelaySeconds: 120
            periodSeconds: 20
            tcpSocket:
              port: 1500
            timeoutSeconds: 10
          volumes:
            - dataVolume:
                name: test-probe-rootdisk
              name: rootdisk
            - cloudInitNoCloud:
                userData: |
                  #cloud-config
                  ssh_pwauth: true
                  disable_root: false
                  chpasswd: {"list": "root:dangerous", expire: False}
                  runcmd:
                    - sed -i "/#\?PermitRootLogin/s/^.*$/PermitRootLogin yes/g" /etc/ssh/sshd_config
                    - systemctl restart ssh.service
                    - dhclient -r && dhclient
                    - apt-get update && apt-get install -y ncat
                    - ["systemd-run", "--unit=httpserver", "ncat", "-klp", "1500", "-e", '/usr/bin/echo -e HTTP/1.1 200 OK\nContent-Length: 12\n\nHello World!']
              name: cloudinitdisk
    ```

## 配置 Readiness Probes

在 spec.template.spec 中配置 readiness。

??? note "点击查看 YAML 示例配置"

    ```yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      annotations:
        kubevirt.io/latest-observed-api-version: v1
        kubevirt.io/storage-observed-api-version: v1
        virtnest.io/alias-name: ''
        virtnest.io/image-secret: ''
        virtnest.io/image-source: docker
        virtnest.io/os-image: release-ci.daocloud.io/virtnest/system-images/ubuntu-22.04-x86_64:v1
      creationTimestamp: '2024-10-15T02:39:45Z'
      finalizers:
        - kubevirt.io/virtualMachineControllerFinalize
      generation: 1
      labels:
        virtnest.io/os-family: Ubuntu
        virtnest.io/os-version: '22.04'
      name: test-probe
      namespace: amamba-team
      resourceVersion: '254032135'
      uid: 6d92779d-7415-4721-8c7b-a2dde163d758
    spec:
      dataVolumeTemplates:
        - metadata:
            creationTimestamp: null
            name: test-probe-rootdisk
            namespace: amamba-team
          spec:
            pvc:
              accessModes:
                - ReadWriteOnce
              resources:
                requests:
                  storage: 10Gi
              storageClassName: hwameistor-storage-lvm-hdd
            source:
              registry:
                url: >-
              docker://release-ci.daocloud.io/virtnest/system-images/ubuntu-22.04-x86_64:v1
      runStrategy: Halted
      template:
        metadata:
          creationTimestamp: null
        spec:
          architecture: amd64
          domain:
            cpu:
              cores: 1
              sockets: 1
              threads: 1
            devices:
              disks:
                - bootOrder: 1
                  disk:
                    bus: virtio
                  name: rootdisk
                - disk:
                    bus: virtio
                  name: cloudinitdisk
              interfaces:
                - masquerade: {}
                  name: default
            machine:
              type: q35
            memory:
              guest: 2Gi
            resources:
              requests:
                memory: 2Gi
          networks:
            - name: default
              pod: {}
          readiness:
            initialDelaySeconds: 120
            periodSeconds: 20
            httpGet:
              port: 1500
            timeoutSeconds: 10
          volumes:
            - dataVolume:
                name: test-probe-rootdisk
              name: rootdisk
            - cloudInitNoCloud:
                userData: |
                  #cloud-config
                  ssh_pwauth: true
                  disable_root: false
                  chpasswd: {"list": "root:dangerous", expire: False}
                  runcmd:
                    - sed -i "/#\?PermitRootLogin/s/^.*$/PermitRootLogin yes/g" /etc/ssh/sshd_config
                    - systemctl restart ssh.service
                    - dhclient -r && dhclient
                    - apt-get update && apt-get install -y ncat
                    - ["systemd-run", "--unit=httpserver", "ncat", "-klp", "1500", "-e", '/usr/bin/echo -e HTTP/1.1 200 OK\nContent-Length: 12\n\nHello World!']
              name: cloudinitdisk
    ```
