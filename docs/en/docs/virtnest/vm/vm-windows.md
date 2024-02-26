# Creating a Windows Virtual Machine

This document will explain how to create a Windows virtual machine via the command line.

## Prerequisites

1. Before creating a Windows virtual machine, ensure that your environment is ready by following the [dependencies and prerequisites for installing the virtual machine module](../install/install-dependency.md).
2. Follow the official documentation for the installation process: [How to install during Windows install](https://kubevirt.io/user-guide/virtual_machines/windows_virtio_drivers/#how-to-install-during-windows-install).
3. If the virtual machine does not have network access, manually load the Windows network drivers during boot-up. Refer to the official documentation: [How to install after Windows installation?](https://kubevirt.io/user-guide/virtual_machines/windows_virtio_drivers/#how-to-install-after-windows-install).
4. It is recommended to access the Windows virtual machine using VNC.

## Uploading the Windows Operating System Image File

1. Start the CDI upload service

    ```shell
    cat << EOF | kubectl  -n virtnest-system apply  -f -
    apiVersion: v1
    kind: Service
    metadata:
    labels:
        cdi.kubevirt.io: cdi-uploadproxy
    name: cdi-uploadproxy-nodeport
    spec:
    ports:
    - nodePort: 31001
        port: 443
        protocol: TCP
        targetPort: 8443
    selector:
        cdi.kubevirt.io: cdi-uploadproxy
    type: NodePort
    EOF
    ```

2. CDI certificate configuration

    ```shell
    # Replace 10.6.136.25 with the node IP
    echo | openssl s_client -showcerts -connect 10.6.136.25:31001 2>/dev/null \
            | openssl x509 -inform pem -noout -text \
            | sed -n -e '/Subject.*CN/p' -e '/Subject Alternative/{N;p}'
    echo "10.6.136.25  cdi-uploadproxy" >> /etc/hosts
    
    kubectl patch cdi cdi \
        --type merge \
        --patch '{"spec":{"config":{"uploadProxyURLOverride":"https://cdi-uploadproxy:31001"}}}'
    
    kubectl get secret -n virtnest-system cdi-uploadproxy-server-cert \
        -o jsonpath="{.data['tls\.crt']}" \
        | base64 -d > cdi-uploadproxy-server-cert.crt
    
    sudo cp cdi-uploadproxy-server-cert.crt /etc/pki/ca-trust/source/anchors
    
    sudo update-ca-trust
    ```

3. Install the tools

    ```shell
    (
    set -x; cd "$(mktemp -d)" &&
    OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
    ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
    KREW="krew-${OS}_${ARCH}" &&
    curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
    tar zxvf "${KREW}.tar.gz" &&
    ./"${KREW}" install krew
    )
    
    echo 'export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"' >> ~/.bashrc && bash --login
    
    kubectl krew install virt
    ```

4. Download the Windows ISO from the [Windows website](https://www.microsoft.com/en-us/evalcenter/download-windows-server-2012-r2)

    ```shell
    wget -O win.iso 'https://go.microsoft.com/fwlink/p/?LinkID=2195443&clcid=0x409&culture=en-us&country=US'
    ```

5. Upload the Windows ISO and create a boot disk

    ```shell
    kubectl virt image-upload -n virt-demo pvc iso-win \  
    --image-path=/root/win.iso \  
    --access-mode=ReadWriteOnce \
    --size=25G \  
    --uploadproxy-url=https://cdi-uploadproxy:31001 \  
    --force-bind \
    --insecure \
    --wait-secs=240 \
    --storage-class=local-path  
    ```

6. Create a data disk

    ```shell
    kubectl apply -n virt-demo  -f - <<EOF
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
    name: winhd
    namespace: virt-demo
    spec:
    accessModes:
        - ReadWriteOnce
    resources:
        requests:
        storage: 20Gi
    storageClassName: local-path
    EOF
    ```

## Creating the Windows Virtual Machine

??? note "Click to view the YAML example for creating a Windows virtual machine"

    ```yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
    annotations:
        kubevirt.io/latest-observed-api-version: v1
        kubevirt.io/storage-observed-api-version: v1
    labels:
        virtnest.io/os-family: Windows
        virtnest.io/os-version: 2012.r2
    name: vm-windows
    namespace: virt-demo
    spec:
    running: true
    template:
        metadata:
        creationTimestamp: null
        labels:  
            app: vm-windows
            version: v1
            kubevirt.io/domain: vm-windows
        spec:
        architecture: amd64
        domain:
            cpu:
            cores: 4
            sockets: 1
            threads: 1
            devices:
            disks:
                - bootOrder: 1
                cdrom:
                    bus: sata
                name: cdromiso
                - bootOrder: 2
                disk:
                    bus: virtio
                name: harddrive
                - bootOrder: 3
                cdrom:
                    bus: sata
                name: virtiocontainerdisk
            interfaces:
                - name: default
                passt: {}  
                ports:
                    - name: http
                    port: 80  
            machine:
            type: q35
            resources:
            requests:
                memory: 2G
        networks:
            - name: default
            pod: {}
        volumes:
            - name: cdromiso
            persistentVolumeClaim:
                claimName: iso-win  
            - name: harddrive
            persistentVolumeClaim:
                claimName: winhd  
            - containerDisk:
                image: kubevirt/virtio-container-disk
            name: virtiocontainerdisk
    ```

## Accessing the Windows Virtual Machine

1. Once created successfully, access the virtual machine list page to verify that the virtual machine is running properly.

    <!-- Add image later -->

2. Click VNC to access the virtual machine.

    <!-- Add image later -->
