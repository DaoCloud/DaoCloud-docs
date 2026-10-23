# Retain Jenkins Configuration Parameters

The Jenkins configuration file is stored through a ConfigMap.
However, in actual use, you may modify some configuration items, such as the Agent image or the maximum number
of parallel executors. Upgrading through Helm will overwrite your configurations. To balance the difference
between the Jenkins upgrade and your custom configurations, the Workbench provides the feature of retaining
Jenkins configuration parameters.

!!! tip

    Workbench version >= v0.33.0, or installer version >= v0.24.0

## Configuration Steps

1. Click **≡** in the upper left corner to open the navigation bar, select **Container Management** -> **Clusters**, find `kpanda-global-cluster`, and click the name of the cluster.
2. On the cluster details page, click **ConfigMaps and Secrets** -> **ConfigMaps** in sequence, select the namespace `amamba-system`, and search by the name `global-jenkins-casc-config`.
3. Click **Edit YAML** and add the following configuration to the `data` field:

    ```yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: global-jenkins-casc-config
      namespace: amamba-system
    data:
      jenkins.yaml: | # Edit this part
        xxxxx
    ```

    Among them, `jenkins.yaml` must be **in the same format** as the `jenkins.yaml` in the Jenkins CASC configuration item.
    After you complete the modification, its content will be merged into the Jenkins configuration file in the form of `patch`.

!!! tip
    
    The Jenkins CASC configuration item refers to the parameters that Jenkins can configure through a configuration
    file (Configuration as Code). You can go to the namespace where Jenkins is installed and view the
    `jenkins-casc-config` ConfigMap, whose key is `jenkins.yaml`.

!!! note

    If only Jenkins is upgraded, since the upgrade of Jenkins cannot be detected, you need to manually update the
    `amamba.io/casc-sync-at` field in the annotation of this ConfigMap (you can change it to any value) so that
    it can be applied to Jenkins.

## Configuration Examples

Some configuration examples are given below:

- Add an agent

    ```yaml
    jenkins.yaml: |
      jenkins:
        clouds:
          - kubernetes:
              name: "kubernetes"
              templates:
                - name: "new"
                  label: "new"
                  inheritFrom: "nodejs"
                  containers:
                    - name: "nodejs"
                      image: "docker.m.daocloud.io/amambadev/jenkins-agent-nodejs:v0.4.6-20.17.0-ubuntu-podman"
    ```

- Set the maximum number of parallel agents

    ```yaml
    jenkins.yaml: |
      jenkins:
        clouds:
          - kubernetes:
              containerCapStr: "100"
    ```

- Add a shared library configuration:

    ```yaml
    jenkins.yaml: |
      unclassified:
        globalLibraries:
          libraries:
          - defaultVersion: "main"
            name: "amamba-shared-lib"
            retriever:
              modernSCM:
                scm:
                  git:
                    remote: "https://github.com/amamba-io/amamba-shared-lib.git"
    ```
