# use key

A secret is a resource object used to store and manage sensitive information such as passwords, OAuth tokens, SSH, TLS credentials, etc. Using keys means you don't need to include sensitive secrets in your application code.

## scenes to be used

You can use keys in Pods in a variety of  use cases, mainly including:

- Used as an environment variable of the container to provide some necessary information required during the running of the container.
- Use secrets as pod data volumes.
- Used as the identity authentication credential for the container registry when the kubelet pulls the container image.

## Use the key to set the environment variable of the container

You can use the key as the environment variable of the container through the GUI or the terminal command line.

!!! note

     Key import is to use the key as the value of an environment variable; key key value import is to use a parameter in the key as the value of an environment variable.

### Graphical interface operation

When creating a workload from an image, you can set environment variables for the container by selecting __Key Import__ or __Key Key Value Import__ on the __Environment Variables__ interface.

1. Go to the [Image Creation Workload](../workloads/create-deployment.md) page.

     

2. Select the __Environment Variables__ configuration in __Container Configuration__ , and click the __Add Environment Variable__ button.

     

3. Select __Key Import__ or __Key Key Value Import__ in the environment variable type.

     

     - When the environment variable type is selected as __Key Import__ , enter __Variable Name__ , __Prefix__ , and __Secret__ in sequence.

     - When the environment variable type is selected as __key key value import__ , enter __variable name__ , __Secret__ , __Secret__ name in sequence.

### Command line operation

As shown in the example below, you can set the secret as an environment variable when creating the workload, using the __valueFrom__ parameter to refer to the Key/Value in the Secret.

```yaml
apiVersion: v1
kind: Pod
metadata:
   name: secret-env-pod
spec:
   containers:
   -name: mycontainer
     image: redis
     env:
       - name: SECRET_USERNAME
         valueFrom:
           secretKeyRef:
             name: mysecret
             key: username
             optional: false # (1)
       - name: SECRET_PASSWORD
         valueFrom:
           secretKeyRef:
             name: mysecret
             key: password
             optional: false # (2)

```

1. This value is the default; means "mysecret", which must exist and contain a primary key named "username"
2. This value is the default; means "mysecret", which must exist and contain a primary key named "password"

## Use the key as the pod's data volume

### Graphical interface operation

When creating a workload through an image, you can use the key as the data volume of the container by selecting the storage type as "key" on the "data storage" interface.

1. Go to the [Image Creation Workload](../workloads/create-deployment.md) page.

     

2. In the __Container Configuration__ , select the __Data Storage__ configuration, and click the __Add__ button in the __Node Path Mapping__ list.

     

3. Select __Secret__ in the storage type, and enter __container path__ , __subpath__ and other information in sequence.

### Command line operation

The following is an example of a Pod that mounts a Secret named __mysecret__ via a data volume:

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
     secret:
       secretName: mysecret
       optional: false # (1)
```

1. Default setting, means "mysecret" must already exist

If the Pod contains multiple containers, each container needs its own __volumeMounts__ block, but only one __.spec.volumes__ setting is required for each Secret.

## Used as the identity authentication credential for the container registry when the kubelet pulls the container image

You can use the key as the identity authentication credential for the Container registry through the GUI or the terminal command line.

### Graphical operation

When creating a workload through an image, you can use the key as the data volume of the container by selecting the storage type as "key" on the "data storage" interface.

1. Go to the [Image Creation Workload](../workloads/create-deployment.md) page.

     

2. In the second step of __Container Configuration__ , select the __Basic Information__ configuration, and click the __Select Image__ button.

     

3. Select the name of the private container registry in the drop-down list of `container registry' in the pop-up box. Please see [Create Secret](create-secret.md) for details on private image secret creation.

     

4. Enter the image name in the private registry, click __OK__ to complete the image selection.

!!! note

     When creating a key, you need to ensure that you enter the correct container registry address, username, password, and select the correct mirror name, otherwise you will not be able to obtain the mirror image in the container registry.