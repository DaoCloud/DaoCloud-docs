# Offline upgrade Insight

This page explains how to install or upgrade Insight after
[downloading it from Download Center](../../../download/modules/insight.md).

!!! info

     The word __insight__ appearing in the following commands or scripts is the internal development codename of the observability module.

## Decompression

```shell
tar -xvf insight_v0.25.3_amd64.tar
```

After decompression, two bundle packages can be obtained, namely insight and insight agent.

```shell
$ ll insight_v0.25.3_amd64
总用量 2899996
-rw-r--r-- 1 root root 2367463936 4月   2 18:36 insight_0.25.3.bundle.tar
-rw-r--r-- 1 root root  602125824 4月   2 18:35 insight-agent_0.25.3.bundle.tar
```

## Load the image from the installation package

You can load the image in one of the following two ways. When there is a container registry in the environment, it is recommended to select chart-syncer to synchronize the image to the container registry. This method is more efficient and convenient. Please note that the version of charts-syncer should be greater than or equal to [0.0.22](https://github.com/DaoCloud/charts-syncer/releases/tag/v0.0.22).

### chart-syncer synchronously images to the container registry

1. Create load-image.yaml

    !!! note

        All parameters in this YAML file are required. You need a private container registry and modify related configurations.

    === "chart HARBOR repo installed"

        If the current environment has installed the HARBOR chart repo, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml
        source:
          intermediateBundlesPath: insight-offline # (1)!
        target:
          containerPrefixRegistry: 10.16.10.111 # (2)!
          appendOriginRegistry: true
          repo:
            kind: HARBOR # (3)!
            url: http://10.16.10.111/chartrepo/release.daocloud.io # (4)!
            auth:
            username: "admin" # (5)!
            password: "Harbor12345" # (6)!
          containers:
            auth:
              username: "admin" # (7)!
              password: "Harbor12345" # (8)!
        ```

        1. The relative path to run the charts-syncer command, not the relative path between this YAML file and the offline bundle
        2. need to be changed to your container registry url
        3. Can also be any other supported Helm Chart repository class
        4. need to change to chart repo project url
        5. Your container registry username
        6. Your container registry password
        7. Your container registry username
        8. Your container registry password

    === "chart CHARTMUSEUM repo installed"

        If the current environment has installed the CHARTMUSEUM chart repo, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml
        source:
          intermediateBundlesPath: insight-offline # (1)!
        target:
          containerPrefixRegistry: 10.16.10.111 # (2)!
          appendOriginRegistry: true
          repo:
            kind: CHARTMUSEUM # (3)!
            url: http://10.16.10.111 # (4)!
            auth:
              username: "rootuser" # (5)!
              password: "rootpass123" # (6)!
          containers:
            auth:
              username: "rootuser" # (7)!
              password: "rootpass123" # (8)!
        ```

        1. The relative path to run the charts-syncer command, not the relative path between this YAML file and the offline bundle
        2. need to be changed to your container registry url
        3. Can also be any other supported Helm Chart repository class
        4. need to change to chart repo url
        5. Your container registry username. If chartmuseum disable login verification, auth can be vacant.
        6. Your container registry password
        7. Your container registry username
        8. Your container registry password

    === "chart repo not installed"

        If the chart repo is not installed in the current environment, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml
        source:
          intermediateBundlesPath: insight-offline # (1)!
        target:
          containerPrefixRegistry: 10.16.10.111 # (2)!
          repo:
            kind: LOCAL
            path: ./local-repo # (3)!
          containers:
            auth:
              username: "admin" # (4)!
              password: "Harbor12345" # (5)!
        ```

        1. The relative path to run the charts-syncer command, not the relative path between this YAML file and the offline bundle
        2. need to be changed to your container registry url
        3. chart local path
        4. Your container registry username
        5. Your container registry password

1. Run the synchronous imageing command.

    ```shell
    charts-syncer sync --config load-image.yaml --insecure
    ```

### Docker or containerd direct loading

Unzip and load the image file.

1. Unzip the tar archive.

    ```shell
    tar -xvf insight_0.25.3.bundle.tar
    ```

    After successful decompression, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the image locally to Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    Each node needs to perform Docker or containerd loading image operation.
    After the loading is complete, the tag image is required to keep the Registry and Repository consistent with the installation.

## upgrade

There are two ways to upgrade. You can choose the corresponding upgrade plan according to the pre-operations. Before upgrading, please pay attention to the "Upgrade-note"

=== "upgrade via helm repo"

     1. Check whether the Insight helm repository exists.

        ```shell
        helm repo list | grep insight
        ```

        If the returned result is empty or as prompted, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

     1. Add the Insight helm repository.

        ```shell
        helm repo add insight http://{harbor url}/chartrepo/{project} --insecure-skip-tls-verify
        ```

     1. Update the globally managed helm repository.

        ```shell
        helm repo update insight # (1)!
        ```

        1. If the helm version is too low, it will fail. If it fails, please try to run helm update repo

     1. Select the version of Insight you want to install (the latest version is recommended).

        ```shell
        helm search repo insight/insight --versions
        helm search repo insight/insight-agent --versions
        ```

        ```none
        [root@master ~]# helm search repo insight/insight --versions
        NAME                 CHART VERSION  APP VERSION  DESCRIPTION
        insight/insight        0.25.3         0.25.3       A Helm chart for Insight
        insight/insight-agent  0.25.3         0.25.3       A Helm chart for Insight Agent
        ...
        ```

     1. Back up the `--set` parameter.

        Before upgrading the Insight version, it is recommended that you run the following command to back up the `--set` parameter of the old version.

        ```shell
        helm get values insight -n insight-system -o yaml > insight.yaml
        helm get values insight-agent -n insight-system -o yaml > insight-agent.yaml
        ```

     1. Run `helm upgrade` .

        ```shell
        helm upgrade insight insight/insight \
          -n insight-system \
          -f ./insight.yaml \
          --version 0.25.3
        ```

        as well as

        ```shell
        helm upgrade insight-agent insight/insight-agent \
          -n insight-system \
          -f ./insight-agent.yaml \
          --version 0.25.3
        ```

=== "upgrade via chart package"

     1. Back up the `--set` parameter.

        Before upgrading the Insight version, it is recommended that you run the following command to back up the `--set` parameter of the old version.

        ```shell
        helm get values insight -n insight-system -o yaml > insight.yaml
        ```

     1. Run `helm upgrade` .

        Before upgrading, it is recommended that you overwrite __global.imageRegistry__ in bak.yaml to the address of the current container registry.

        ```shell
        export imageRegistry={your image registry}
        ```

        ```shell
        helm upgrade insight . \
          -n insight-system \
          -f ./insight.yaml \
          --set global.imageRegistry=$imageRegistry
        ```

        as well as

        ```shell
        helm upgrade insight-agent . \
          -n insight-system \
          -f ./insight-agent.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
