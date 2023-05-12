# Use configuration items

Configuration item (ConfigMap) is an API object of Kubernetes, which is used to save non-confidential data into key-value pairs, and can store configurations that other objects need to use.
When used, the container can use it as an environment variable, a command-line argument, or a configuration file in a storage volume. By using configuration items, configuration data and application code can be separated, providing a more flexible way to modify application configuration.

!!! note

     Configuration items do not provide confidentiality or encryption. If the data to be stored is confidential, please use [secret](use-secret.md), or use other third-party tools to ensure the privacy of the data instead of configuration items.
     In addition, when using configuration items in containers, the container and configuration items must be in the same cluster namespace.

## scenes to be used

You can use configuration items in Pods. There are many usage scenarios, mainly including:

- Use configuration items to set the environment variables of the container

- Use configuration items to set the command line parameters of the container

- Use configuration items as container data volumes

## Set the environment variables of the container

You can use the configuration item as the environment variable of the container through the graphical interface or the terminal command line.

!!! note

     The configuration item import is to use the configuration item as the value of the environment variable; the configuration item key value import is to use a certain parameter in the configuration item as the value of the environment variable.

### Graphical interface operation

When creating a workload through an image, you can set environment variables for the container by selecting `Import Configuration Items` or `Import Configuration Item Key Values` on the `Environment Variables` interface.

1. Go to the [Image Creation Workload](../workloads/create-deployment.md) page, in the `Container Configuration` step, select the `Environment Variables` configuration, and click the `Add Environment Variable` button.

     

2. Select `Configuration Item Import` or `Configuration Item Key Value Import` in the environment variable type.

     - When the environment variable type is selected as `configuration item import`, enter `variable name`, `prefix` name, `configuration item` name in sequence.

     - When the environment variable type is selected as `configuration item key-value import`, enter `variable name`, `configuration item` name, and `key` name in sequence.

### Command line operation

You can set configuration items as environment variables when creating a workload, using the valueFrom parameter to refer to the Key/Value in the ConfigMap.

```yaml
apiVersion: v1
kind: Pod
metadata:
   name: configmap-pod-1
spec:
   containers:
     - name: test-container
       image: busybox
       command: [ "/bin/sh", "-c", "env" ]
       env:
         - name: SPECIAL_LEVEL_KEY
           valueFrom: # (1)
             configMapKeyRef:
               name: kpanda-configmap # (2)
               key: SPECIAL_LEVEL # (3)
   restartPolicy: Never
```

1. Use `valueFrom` to specify the value of the env reference configuration item
2. Referenced configuration file name
3. Referenced configuration item key

## Set the command line parameters of the container

You can use configuration items to set the command or parameter value in the container, and use the environment variable substitution syntax `$(VAR_NAME)` to do so. As follows.

```yaml
apiVersion: v1
kind: Pod
metadata:
   name: configmap-pod-3
spec:
   containers:
     - name: test-container
       image: busybox
       command: [ "/bin/sh", "-c", "echo $(SPECIAL_LEVEL_KEY) $(SPECIAL_TYPE_KEY)" ]
       env:
         - name: SPECIAL_LEVEL_KEY
           valueFrom:
             configMapKeyRef:
               name: kpanda-configmap
               key: SPECIAL_LEVEL
         - name: SPECIAL_TYPE_KEY
           valueFrom:
             configMapKeyRef:
               name: kpanda-configmap
               key: SPECIAL_TYPE
   restartPolicy: Never
```

After the Pod runs, the output is as follows.

```none
Hello Kpanda
```

## Used as container data volume

You can use the configuration item as the environment variable of the container through the graphical interface or the terminal command line.

### Graphical operation

When creating a workload through an image, you can use the configuration item as the data volume of the container by selecting the storage type as "Configuration Item" on the "Data Storage" interface.

1. Go to the [Image Creation Workload](../workloads/create-deployment.md) page, in the `Container Configuration` step, select the `Data Storage` configuration, and click `Add in the `Node Path Mapping` list ` button.

     

2. Select `Configuration Item` in the storage type, and enter `container path`, `subpath` and other information in sequence.

### Command line operation

To use a ConfigMap in a Pod's storage volume.

Here is an example Pod that mounts a ConfigMap as a volume:

```yaml
apiVersion: v1
kind: Pod
metadata:
   name: mypod
spec:
   containers:
   -name: mypod
     image: redis
     volumeMounts:
     - name: foo
       mountPath: "/etc/foo"
       readOnly: true
   volumes:
   - name: foo
     configMap:
       name: myconfigmap
```

If there are multiple containers in a Pod, each container needs its own `volumeMounts` block, but you only need to set one `spec.volumes` block per ConfigMap.

!!! note

     When a configuration item is used as a data volume mounted on a container, the configuration item can only be read as a read-only file.