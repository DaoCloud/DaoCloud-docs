# 创建 Windows 虚拟机

本文将介绍如何通过命令行创建 Windows 虚拟机。

## 前提条件

1. 创建 Windows 虚拟机之前，需要先参考[安装虚拟机模块的依赖和前提](../install/install-dependency.md)确定您的环境已经准备就绪。
2. 创建过程建议参考官方文档：[安装 windows 的文档](https://kubevirt.io/2022/KubeVirt-installing_Microsoft_Windows_11_from_an_iso.html)、[安装 Windows 相关驱动程序](https://kubevirt.io/user-guide/virtual_machines/windows_virtio_drivers/#how-to-install-during-windows-install)。
4. Windows 虚拟机建议使用 VNC 的访问方式。

## 导入 ISO 镜像

​		创建 Windows 虚拟机需要导入 ISO 镜像的主要原因是为了安装 Windows 操作系统。与 Linux 操作系统不同，Windows 操作系统安装过程通常需要从安装光盘或 ISO 镜像文件中引导。因此，在创建 Windows 虚拟机时，需要先导入 Windows 操作系统的安装 ISO 镜像文件，以便虚拟机能够正常安装。

以下介绍两个导入 ISO 镜像的办法：

1. （推荐）制作 Docker 镜像，建议参考 [构建镜像](../vm-image/index.md)

2. （不推荐）使用 virtctl 将镜像导入到 PVC 中

   可参考如下命令

      ```sh
      virtctl image-upload -n <命名空间> pvc <PVC 名称> \ 
      --image-path=<IOS 文件路径> \ 
      --access-mode=ReadWriteOnce \ 
      --size=6G \ --uploadproxy-url=<https://cdi-uploadproxy ClusterIP 和端口> \ 
      --force-bind \ 
      --insecure \ 
      --wait-secs=240 \ 
      --storage-class=<SC>
      ```

      例如：

      ```sh
      virtctl image-upload -n <命名空间> pvc <PVC 名称> \ 
      --image-path=<IOS 文件路径> \ 
      --access-mode=ReadWriteOnce \ 
      --size=6G \ --uploadproxy-url=<https://cdi-uploadproxy ClusterIP 和端口> \ 
      --force-bind \ 
      --insecure \ 
      --wait-secs=240 \ 
      --storage-class=<SC>
      ```

## YAML 创建 Windows 虚拟机

使用 yaml 创建 Windows 虚拟机，更加灵活并且更易编写喝维护。以下介绍三种参考的 yaml：

1.（推荐）使用 Virtio 驱动 + Docker 镜像的方式

  - 如果你需要使用存储能力-挂载磁盘，请安装 [viostor 驱动程序](https://kubevirt.io/user-guide/virtual_machines/windows_virtio_drivers/#how-to-install-during-windows-install)。

  - 如果你需要使用网络能力，请安装 [NetKVM 驱动程序](https://kubevirt.io/user-guide/virtual_machines/windows_virtio_drivers/#how-to-install-after-windows-install)。

  ??? note "点击查看完整 YAML"

      ```yaml
      apiVersion: kubevirt.io/v1
      kind: VirtualMachine
      metadata:
        annotations:
          kubevirt.io/latest-observed-api-version: v1
          kubevirt.io/storage-observed-api-version: v1
        labels:
          virtnest.io/os-family: Windows
          virtnest.io/os-version: '10'
        name: windows10-virtio
        namespace: default
      spec:
        dataVolumeTemplates:
          - metadata:
              name: win10-system-virtio
              namespace: default
            spec:
              pvc:
                accessModes:
                  - ReadWriteOnce
                resources:
                  requests:
                    storage: 32Gi
                storageClassName: local-path
              source:
                blank: {}
        running: true
        template:
          metadata:
            labels:
              app: windows10-virtio
              version: v1
              kubevirt.io/domain: windows10-virtio
          spec:
            architecture: amd64
            domain:
              cpu:
                cores: 8
                sockets: 1
                threads: 1
              devices:
                disks:
                  - bootOrder: 1
                    # 请使用 virtio
                    disk:
                      bus: virtio
                    name: win10-system-virtio
                    # ISO 镜像请使用 sata
                  - bootOrder: 2
                    cdrom:
                      bus: sata
                    name: iso-win10
                   # containerdisk 请使用 sata
                  - bootOrder: 3
                    cdrom:
                      bus: sata
                    name: virtiocontainerdisk
                interfaces:
                  - name: default
                    masquerade: {}
              machine:
                type: q35
              resources:
                requests:
                  memory: 8G
            networks:
              - name: default
                pod: {}
            volumes:
              - name: iso-win10
                persistentVolumeClaim:
                  claimName: iso-win10
              - name: win10-system-virtio
                persistentVolumeClaim:
                  claimName: win10-system-virtio
              - containerDisk:
                  image: kubevirt/virtio-container-disk
                name: virtiocontainerdisk
      ```
2. （不推荐）使用 Virtio 驱动和 virtctl 工具的组合方式，将镜像导入到 Persistent Volume Claim（PVC）中。

    ```yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      annotations:
        kubevirt.io/latest-observed-api-version: v1
        kubevirt.io/storage-observed-api-version: v1
      labels:
        virtnest.io/os-family: Windows
        virtnest.io/os-version: '10'
      name: windows10-virtio
      namespace: default
    spec:
      dataVolumeTemplates:
        - metadata:
            name: win10-system-virtio
            namespace: default
          spec:
            pvc:
              accessModes:
                - ReadWriteOnce
              resources:
                requests:
                  storage: 32Gi
              storageClassName: local-path
            source:
              blank: {}
      running: true
      template:
        metadata:
          labels:
            app: windows10-virtio
            version: v1
            kubevirt.io/domain: windows10-virtio
        spec:
          architecture: amd64
          domain:
            cpu:
              cores: 8
              sockets: 1
              threads: 1
            devices:
              disks:
                - bootOrder: 1
                  # 请使用 virtio
                  disk:
                    bus: virtio
                  name: win10-system-virtio
                  # ISO 镜像请使用 sata
                - bootOrder: 2
                  cdrom:
                    bus: sata
                  name: iso-win10
                 # containerdisk 请使用 sata
                - bootOrder: 3
                  cdrom:
                    bus: sata
                  name: virtiocontainerdisk
              interfaces:
                - name: default
                  masquerade: {}
            machine:
              type: q35
            resources:
              requests:
                memory: 8G
          networks:
            - name: default
              pod: {}
          volumes:
            - name: iso-win10
              persistentVolumeClaim:
                claimName: iso-win10
            - name: win10-system-virtio
              persistentVolumeClaim:
                claimName: win10-system-virtio
            - containerDisk:
                image: kubevirt/virtio-container-disk
              name: virtiocontainerdisk
    ```

3. （不推荐）不使用 Virtio 驱动的情况下，使用 virtctl 工具将镜像导入到 Persistent Volume Claim（PVC）中。虚拟机可能使用其他类型的驱动或默认驱动来操作磁盘和网络设备。

    ```yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      annotations:
        kubevirt.io/latest-observed-api-version: v1
        kubevirt.io/storage-observed-api-version: v1
      labels:
        virtnest.io/os-family: Windows
        virtnest.io/os-version: '10'
      name: windows10
      namespace: default
    spec:
      dataVolumeTemplates:
        # 创建系统盘，你创建多个 PVC（磁盘）
        - metadata:
            name: win10-system
            namespace: default
          spec:
            pvc:
              accessModes:
                - ReadWriteOnce
              resources:
                requests:
                  storage: 32Gi
              storageClassName: local-path
            source:
              blank: {}
      running: true
      template:
        metadata:
          labels:
            app: windows10
            version: v1
            kubevirt.io/domain: windows10
        spec:
          architecture: amd64
          domain:
            cpu:
              cores: 8
              sockets: 1
              threads: 1
            devices:
              disks:
                - bootOrder: 1
                  # 无 virtio 驱动，请使用 sata
                 cdrom:
                    bus: sata
                  name: win10-system
                  # ISO 镜像，请使用 sata
                - bootOrder: 2
                  cdrom:
                    bus: sata
                  name: iso-win10
              interfaces:
                - name: default
                  masquerade: {}
            machine:
              type: q35
            resources:
              requests:
                memory: 8G
          networks:
            - name: default
              pod: {}
          volumes:
            - name: iso-win10
              persistentVolumeClaim:
                claimName: iso-win10
            - name: win10-system
              persistentVolumeClaim:
                claimName: win10-system
    ```

## 云桌面

1. Windows 版本的虚拟机大多数情况是需要远程桌面控制访问的，建议使用 [Microsoft Remote Desktop](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac#get-the-remote-desktop-client) 控制您的虚拟机。

2. 请注意：
   -  你的 Windows 版本需支持远程桌面控制，才能使用 [Microsoft Remote Desktop](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac#get-the-remote-desktop-client)。
   -  关闭 Windows 的防火墙。

## 增加数据盘

Windows 虚拟机添加数据盘的方式和 Linux 虚拟机一致。你可以参考下面的 YAML 示例：

  ```sh
  apiVersion: kubevirt.io/v1
  kind: VirtualMachine
  <...>
  spec:
    dataVolumeTemplates:
      # 添加一块数据盘
      - metadata:
          name: win10-disk
          namespace: default
        spec:
          pvc:
            accessModes:
              - ReadWriteOnce
            resources:
              requests:
                storage: 16Gi
            storageClassName: hwameistor-storage-lvm-hdd
          source:
            blank: {}
    template:
      spec:
        domain:
          devices:
            disks:
              - bootOrder: 1
                disk:
                  bus: virtio
                name: win10-system
              # 添加一块数据盘
              - bootOrder: 2
                disk:
                  bus: virtio
                name: win10-disk
            <....>
        volumes:
          <....>
          # 添加一块数据盘
          - name: win10-disk
            persistentVolumeClaim:
              claimName: win10-disk
  ```
## 快照、克隆、实时迁移

这些能力和 Linux 虚拟机一致，可直接参考配置 Linux 虚拟机的方式。

## 访问 Windows 虚拟机

1. 创建成功后，进入虚拟机列表页面，发现虚拟机正常运行。

    ![运行成功](../images/window01.png)

2. 点击控制台访问（VNC），可以正常访问。

    ![访问](../images/windows-vnc.png)