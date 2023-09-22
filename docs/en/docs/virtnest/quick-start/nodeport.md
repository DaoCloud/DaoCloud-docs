# Accessing Virtual Machine via NodePort

This article explains how to access a virtual machine using NodePort.

## Limitations of Existing Access Methods

1. Virtual machines support access via VNC or console, but both methods have a limitation: they do not allow multiple terminals to be simultaneously online.

2. Using a NodePort-formatted Service can help solve this problem.

## Creating a Service

1. Using the Container Management Page

    - Select the cluster page where the target virtual machine is located and create a Service.
    - Select the access type as NodePort.
    - Choose the namespace (the namespace where the virtual machine resides).
    - Fill in the label selector as `vm.kubevirt.io/name: your-vm-name`.
    - Port Configuration: Choose TCP for the protocol, provide a custom port name, and set the service port and container port to 22.

2. After successful creation, you can access the virtual machine by using `ssh username@nodeip -p port`.

## Creating the Service via kubectl

1. Write the YAML file as follows:

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
        port: 22
        targetPort: 22
      selector:
        vm.kubevirt.io/name: test-image-s3
      type: NodePort
    ```

2. Execute the following command:

    ```sh
    kubectl apply -f your-svc.yaml
    ```

3. After successful creation, you can access the virtual machine by using `ssh username@nodeip -p 32090`.
