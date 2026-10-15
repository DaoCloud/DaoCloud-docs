# Health Check

When configuring liveness and readiness probes for a virtual machine, the process is similar to that of Kubernetes. This article explains how to configure health check parameters for a virtual machine through YAML.

However, note that you must modify the YAML configuration after the virtual machine is created successfully and is powered off.

## Configure an HTTP Liveness Probe

1. Configure `livenessProbe.httpGet` in `spec.template.spec`.
2. Modify `cloudInitNoCloud` to start an HTTP server.

    ??? note "Click to view the YAML example"

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

3. The `userData` configuration may differ depending on the operating system (such as Ubuntu/Debian or CentOS). The main differences are:

    - Package manager:

        Ubuntu/Debian uses `apt-get` as the package manager.
        CentOS uses `yum` as the package manager.

    - SSH service restart command:

        Ubuntu/Debian uses `systemctl restart ssh.service`.
        CentOS uses `systemctl restart sshd.service` (note that CentOS 7 and earlier versions use `service sshd restart`).

    - Package to install:

        Ubuntu/Debian installs `ncat`.
        CentOS installs `nmap-ncat` (because `ncat` may not be available in the default CentOS repositories).

## Configure a TCP Liveness Probe

Configure `livenessProbe.tcpSocket` in `spec.template.spec`.

??? note "Click to view the YAML example"

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

## Configure Readiness Probes

Configure `readiness` in `spec.template.spec`.

??? note "Click to view the YAML example"

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
