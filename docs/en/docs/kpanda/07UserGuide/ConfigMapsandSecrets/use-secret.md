# use key

A secret is a resource object used to store and manage sensitive information such as passwords, OAuth tokens, SSH, TLS credentials, etc. Using keys means you don't need to include sensitive secrets in your application code.

## scenes to be used

You can use keys in Pods in a variety of usage scenarios, mainly including:

- Used as an environment variable of the container to provide some necessary information required during the running of the container.
- Use secrets as pod data volumes.
- Used as the identity authentication credential for the container registry when the kubelet pulls the container image.

## Use the key to set the environment variable of the container

You can use the key as the environment variable of the container through the GUI or the terminal command line.

!!! note

    Key import is to use the key as the value of an environment variable; key key value import is to use a parameter in the key as the value of an environment variable.

### Graphical interface operation

When creating a workload from an image, you can set environment variables for the container by selecting `Key Import` or `Key Key Value Import` on the `Environment Variables` interface.

1. Go to the [Image Creation Workload](../Workloads/CreateDeploymentByImage.md) page.

    ![Create deployment](../../images/secret05.png)

2. Select the `Environment Variables` configuration in `Container Configuration`, and click the `Add Environment Variable` button.

    ![Add environment variable](../../images/secret06.png)

3. Select `Key Import` or `Key Key Value Import` in the environment variable type.

    ![Key Import](../../images/secret07.png)

    - When the environment variable type is selected as `key import`, enter `variable name`, `prefix` name, `key` name in sequence.

    - When the environment variable type is selected as `key key value import`, enter `variable name`, `key` name, `key` name in sequence.

### Command line operation

As shown in the example below, you can set the secret as an environment variable when creating the workload, using the `valueFrom` parameter to refer to the Key/Value in the Secret.

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
            optional: false # This value is the default; means "mysecret"
                            # Must exist and contain a primary key named "username"
      - name: SECRET_PASSWORD
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: password
            optional: false # This value is the default; means "mysecret"
                            # Must exist and contain a primary key named "password"
```

## Use the key as the pod's data volume

### Graphical interface operation

When creating a workload through an image, you can use the key as the data volume of the container by selecting the storage type as "key" on the "data storage" interface.

1. Go to the [Image Creation Workload](../Workloads/CreateDeploymentByImage.md) page.

    ![Create deployment](../../images/secret05.png)

2. In the `Container Configuration`, select the `Data Storage` configuration, and click the `Add` button in the `Node Path Mapping` list.

    ![Create deployment](../../images/secret08.png)

3. Select `Key` in the storage type, and enter `container path`, `subpath` and other information in sequence.

### Command line operation

The following is an example of a Pod that mounts a Secret named `mysecret` via a data volume:

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
      optional: false # Default setting, means "mysecret" must already exist
```

If the Pod contains multiple containers, each container needs its own `volumeMounts` block, but only one `.spec.volumes` setting is required for each Secret.

## Used as the identity authentication credential for the container registry when the kubelet pulls the container image

You can use the key as the identity authentication credential for the container registry through the GUI or the terminal command line.

### Graphical operation

When creating a workload through an image, you can use the key as the data volume of the container by selecting the storage type as "key" on the "data storage" interface.

1. Go to the [Image Creation Workload](../Workloads/CreateDeploymentByImage.md) page.

    ![Create deployment](../../images/secret05.png)

2. In the second step of `Container Configuration`, select the `Basic Information` configuration, and click the `Select Image` button.

    ![Select Image](../../images/secret09.png)

3. Select the name of the private container registry in the drop-down list of `container registry' in the pop-up box. Please see [Create Secret](create-secret.md) for details on private image secret creation.

    ![Select Image](../../images/secret10.png)

4. Enter the image name in the private registry, click `OK` to complete the image selection.

!!! note

    When creating a key, you need to ensure that you enter the correct container registry address, user name, password, and select the correct image name, otherwise you will not be able to obtain the image in the container registry.