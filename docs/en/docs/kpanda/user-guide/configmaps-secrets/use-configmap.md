# Use ConfigMaps

ConfigMap (ConfigMap) is an API object of Kubernetes, which is used to save non-confidential data into key-value pairs, and can store configurations that other objects need to use.
When used, the container can use it as an environment variable, a command-line argument, or a configuration file in a storage volume. By using ConfigMaps, configuration data and application code can be separated, providing a more flexible way to modify application configuration.

!!! note

     ConfigMaps do not provide confidentiality or encryption. If the data to be stored is confidential, please use [secret](use-secret.md), or use other third-party tools to ensure the privacy of the data instead of ConfigMaps.
     In addition, when using ConfigMaps in containers, the container and ConfigMaps must be in the same cluster namespace.

## scenes to be used

You can use ConfigMaps in Pods. There are many  use cases, mainly including:

- Use ConfigMaps to set the environment variables of the container

- Use ConfigMaps to set the command line parameters of the container

- Use ConfigMaps as container data volumes

## Set the environment variables of the container

You can use the ConfigMap as the environment variable of the container through the graphical interface or the terminal command line.

!!! note

     The ConfigMap import is to use the ConfigMap as the value of the environment variable; the ConfigMap key value import is to use a certain parameter in the ConfigMap as the value of the environment variable.

### Graphical interface operation

When creating a workload through an image, you can set environment variables for the container by selecting __Import ConfigMaps__ or __Import ConfigMap Key Values__ on the __Environment Variables__ interface.

1. Go to the [Image Creation Workload](../workloads/create-deployment.md) page, in the __Container Configuration__ step, select the __Environment Variables__ configuration, and click the __Add Environment Variable__ button.

     

2. Select __ConfigMap Import__ or __ConfigMap Key Value Import__ in the environment variable type.

     - When the environment variable type is selected as __ConfigMap import__ , enter __variable name__ , __prefix__ name, __ConfigMap__ name in sequence.

     - When the environment variable type is selected as __ConfigMap key-value import__ , enter __variable name__ , __ConfigMap__ name, and __Secret__ name in sequence.

### Command line operation

You can set ConfigMaps as environment variables when creating a workload, using the valueFrom parameter to refer to the Key/Value in the ConfigMap.

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

1. Use __valueFrom__ to specify the value of the env reference ConfigMap
2. Referenced configuration file name
3. Referenced ConfigMap key

## Set the command line parameters of the container

You can use ConfigMaps to set the command or parameter value in the container, and use the environment variable substitution syntax __$(VAR_NAME)__ to do so. As follows.

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

You can use the ConfigMap as the environment variable of the container through the graphical interface or the terminal command line.

### Graphical operation

When creating a workload through an image, you can use the ConfigMap as the data volume of the container by selecting the storage type as "ConfigMap" on the "Data Storage" interface.

1. Go to the [Image Creation Workload](../workloads/create-deployment.md) page, in the __Container Configuration__ step, select the __Data Storage__ configuration, and click __Add in the __ Node Path Mapping __ list __ button.

     

2. Select __ConfigMap__ in the storage type, and enter __container path__ , __subpath__ and other information in sequence.

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

If there are multiple containers in a Pod, each container needs its own __volumeMounts__ block, but you only need to set one __spec.volumes__ block per ConfigMap.

!!! note

     When a ConfigMap is used as a data volume mounted on a container, the ConfigMap can only be read as a read-only file.