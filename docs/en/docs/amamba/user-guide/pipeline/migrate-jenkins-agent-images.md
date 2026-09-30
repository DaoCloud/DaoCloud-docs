# Migrate Jenkins Agent Images

> This article applies to:
> - Jenkins v0.5.0 and above
> - Workbench v0.35 and above
> - DCE installer v0.27 and above

Since Jenkins was upgraded to **v0.4.8**, we have streamlined the Jenkins chart to avoid a long
installation time caused by an oversized image when installing DCE. This speeds up the installation
and improves the stability of the system. Starting from v0.4.8, the Jenkins chart is divided into two:

- A slim Jenkins, which contains the core features of Jenkins. Among them, the Jenkins Agent images only include:

    - base
    - nodejs (16.20.2)
    - python (3.8.19)
    - golang (1.22.6)
    - maven (jdk8)
  
    In addition, images for the CentOS system are **no longer** provided.

- jenkins-full: the full version of Jenkins. In addition to the images above, it also contains Agent images
  of different versions. For example, Python includes images of 3.8.19, 2.7.9, 3.11.9, and other versions.
  For the specific Agent image versions, refer to the
  [Agent version list](https://github.com/amamba-io/jenkins-agent/blob/main/version.yaml).

To ensure the compatibility of the DCE upgrade, after Jenkins is upgraded, although the name does not
change, the list of available images has changed (the images still exist in the image repository), so
you need to manually modify the mapping of the Agent images.

If you only use base, golang, nodejs, maven, and python, you **do not** need to perform the following
operations. This article only applies to users who use non-default Agent images.
If you use an Agent with a version number such as go-v1.17.13, follow the steps below 👇 to migrate.

## Migration Steps

The available Jenkins Agent images are mapped through a ConfigMap. The modification steps are as follows:

1. In the DCE UI, click **≡** in the upper left corner to open the navigation bar, select __Container Management__ -> __Clusters__, find and click the cluster name `kpanda-global-cluster`.
1. In the left navigation bar, select __Storage and Secrets__ -> __ConfigMaps__, select the namespace `amamba-system` cluster, and search for the name `global-jenkins-casc-config`.
1. Enter the details, click **Edit YAML** in the upper right corner. The YAML path is data -> jenkins.yaml -> jenkins -> clouds -> kubernetes -> templates.

    > If the corresponding key does not exist, you need to create one. For the format, refer to the ConfigMap `jenkins-casc-config` in the namespace where Jenkins is installed.

1. The label field indicates the agent label name used in the UI or Jenkinsfile.

    ![label field](../../images/agent-image.png)

1. Select the agent label you need to modify, and change the `image` of the corresponding container
   (such as go, python, etc.) in the `containers` field to the image of the corresponding version.

For example, the agent label used before the upgrade is `go-1.17.13`, and the corresponding image is
`https://my-regiestry.com/go-v1.17.13`. After the upgrade, there is only a template with the label `go`
in the ConfigMap, so you need to change the image corresponding to `go` to `https://my-regiestry.com/go-v1.17.13`.

```yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: global-jenkins-casc-config
      namespace: amamba-system
    data:
      jenkins.yaml: |
        jenkins:
          clouds:
          - kubernetes:
              templates:
              - containers:
                - args: ""
                  image: amambadev/jenkins-agent-go:v0.4.6-1.17.13-ubuntu-podman  # change it to the image address of the corresponding agent version
                  name: go                  
                - args: ^${computer.jnlpmac} ^${computer.name}
                  image: docker.m.daocloud.io/jenkins/inbound-agent:4.10-2        # the jnlp configuration does not need to be changed
                  name: jnlp
                label: go   # the corresponding label
                name: go
```
