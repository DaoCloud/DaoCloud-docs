# Pipeline Issues

This page provides solutions to some common issues you may encounter when using the pipeline feature.

## Error when running a pipeline

High network communication delay can lead to pipeline running errors, if Jenkins and
the application are deployed in different data centers. The error message is similar to:

```console
E0113 01:47:27.690555 50 request.go:1058] Unexpected error when reading response body: net/http: request canceled (Client.Timeout or context cancellation while reading body)
error: unexpected error when reading response body. Please retry. Original error: net/http: request canceled (Client.Timeout or context cancellation while reading body)
```

**Solution:**

In the pipeline's Jenkinsfile, change the deployment command from __kubectl apply -f__ to
__kubectl apply -f. --request-timeout=30m__ .

## Update __podTemplate__ image of built-in Labels

The Workbench module declares 7 labels with the podTemplate CRD: __base__ , __maven__ , __mavenjdk11__ ,
__go__ , __go16__ , __node.js__ , and __python__ . You can specify an Agent label to use the corresponding
podTemplate for your applications. If these build-in images cannot satisfy your need, update or
add images with the following steps.

1. Go to the __Container Management__ module and click the name of the cluster where the Jenkins component is running.

2. In the left navigation bar, click __ConfigMaps & Secrets__ -> __ConfigMaps__ .

3. Search for __jenkins-casc-config__ and click __Edit YAML__ in the Actions column.

    ![screen](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/faq01.png)

4. Under __data__ -> __jenkins.yaml__ -> __jenkins.clouds.kubernetes.templates__ , select the podTemplate whose image you want to change.

    ![screen](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/faq02.png)

5. Once you have made the necessary updates, go to __Workloads__ section and restart Jenkins deployment.

## Modify dependency source in __settings.xml__ in Maven?

When use Maven as the pipeline build environment, most users need to modify __settings.xml__
file to change the dependency source. You can follow these steps:

1. Go to the Container Management module and click the name of the cluster where the Jenkins component is running.

2. In the left navigation bar, click __ConfigMaps & Secrets__ -> __ConfigMaps__ .

3. Search for __amamba-devops-agent__ and click __Edit YAML__ in the Actions column.

4. Modify the __MavenSetting__ under the __data__ section as per your requirement.

    ![screen](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/faq03.png)

5. Once you have made the necessary updates, go to __Workloads__ and restart Jenkins.

## Unable to access private image repositories when building images through Jenkins

### Podman runtime

1. Go to the Container Management module and click the name of the cluster where the Jenkins component is running.

2. In the left navigation bar, click __ConfigMaps & Secrets__ -> __ConfigMaps__ .

3. Search for __insecure-registries__ and click __Edit YAML__ in the Actions column.

4. Configure under the __registries.conf__ file in the __data__ section.

    Pay attention to the formatting and indentation when making modifications.
    Each registry should have a separate __[[registry]]__ section, as shown in the image below:

    ![faq-ci1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/faq04.png)

    !!! note

        The value of the __registries__ keyword should be the complete domain name or
        IP address of the container registry, without adding the __http__ or __https__ prefix.
        If the container registry uses a non-standard port number, you can add a colon __:__
        followed by the port number after the address.

        ```toml
        [registries]
        location = "registry.example.com:5000"
        insecure=true

        [registries]
        location = "192.168.1.100:8080"
        insecure=true
        ```

    Refer to [Podman documentation](https://podman-desktop.io/docs/containers/registries/insecure-registry).

### Cluster runtime is Docker

1. Open the Docker configuration file. On most Linux distributions, the configuration file
   is located at __/etc/docker/daemon.json__ . If it doesn't exist, please create this configuration file.

2. Add the repository address to the __insecure-registries__ field.

    ```json
    {
      "insecure-registries": ["10.16.10.120:4443"]
    }
    ```

3. After saving, restart Docker by executing the following commands:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    ```

!!! note

    Refer to [Docker documentation](https://docs.docker.com/engine/reference/commandline/dockerd/#configuration-reload-behavior).
