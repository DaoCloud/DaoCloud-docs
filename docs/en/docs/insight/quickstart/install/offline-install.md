# Offline upgrade observability module

This page explains how to install or upgrade the observability module after downloading it from [Download Center](../../../download/index.md).

!!! info

     The word `insight` appearing in the following commands or scripts is the internal development codename of the observability module.

## Load the image from the installation package

You can load the image in one of the following two ways. When there is a container registry in the environment, it is recommended to select chart-syncer to synchronize the image to the container registry. This method is more efficient and convenient.

### chart-syncer synchronously images to the container registry

1. Create load-image.yaml

     !!! note

         All parameters in this YAML file are required. You need a private container registry and modify related configurations.

     === "chart repo installed"

         If the current environment has installed the chart repo, chart-syncer also supports exporting the chart as a tgz file.

         ```yaml
         source:
           intermediateBundlesPath: insight-offline # The relative path to run the charts-syncer command, not the relative path between this YAML file and the offline bundle
         target:
           containerRegistry: 10.16.10.111 # need to be changed to your container registry url
           containerRepository: release.daocloud.io/insight # need to be changed to your container registry
           repo:
             kind: HARBOR # Can also be any other supported Helm Chart repository class
             url: http://10.16.10.111/chartrepo/release.daocloud.io # need to change to chart repo url
             auth:
             username: "admin" # Your container registry username
             password: "Harbor12345" # Your container registry password
           containers:
             auth:
               username: "admin" # Your container registry username
               password: "Harbor12345" # Your container registry password
         ```

     === "chart repo not installed"

         If the chart repo is not installed in the current environment, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

         ```yaml
         source:
           intermediateBundlesPath: insight-offline # The relative path to run the charts-syncer command, not the relative path between this YAML file and the offline bundle
         target:
           containerRegistry: 10.16.10.111 # need to be changed to your container registry url
           containerRepository: release.daocloud.io/insight # need to be changed to your container registry
           repo:
             kind: LOCAL
             path: ./local-repo # chart local path
           containers:
             auth:
               username: "admin" # Your container registry username
               password: "Harbor12345" # Your container registry password
         ```

1. Run the synchronous imageing command.

     ```shell
     charts-syncer sync --config load-image.yaml
     ```

### Docker or containerd direct loading

Unzip and load the image file.

1. Unzip the tar archive.

     ```shell
     tar xvf insight.bundle.tar
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
         ctr image import images.tar
         ```

!!! note
     Each node needs to perform Docker or containerd loading image operation.
     After the loading is complete, the tag image is required to keep the Registry and Repository consistent with the installation.

## upgrade

There are two ways to upgrade. You can choose the corresponding upgrade plan according to the pre-operations:

=== "upgrade via helm repo"

     1. Check whether the global management helm repository exists.

         ```shell
         helm repo list | grep insight
         ```

         If the returned result is empty or as prompted, proceed to the next step; otherwise, skip the next step.

         ```none
         Error: no repositories to show
         ```

     1. Add the globally managed helm repository.

         ```shell
         helm repo add insight http://{harbor url}/chartrepo/{project}
         ```

     1. Update the globally managed helm repository.

         ```shell
         helm repo update insight # If the helm version is too low, it will fail. If it fails, please try to run helm update repo
         ```

     1. Select the version of Global Management you want to install (the latest version is recommended).

         ```shell
         helm search repo insight/insight --versions
         helm search repo insight/insight-agent --versions
         ```

         ```none
         [root@master ~]# helm search repo insight/insight --versions
         NAME CHART VERSION APP VERSION DESCRIPTION
         insight/insight 0.13.1 v0.13.1 A Helm chart for Insight
         insight/insight-agent 0.13.1 v0.13.1 A Helm chart for Insight Agent
         ...
         ```

     1. Back up the `--set` parameter.

         Before upgrading the global management version, it is recommended that you run the following command to back up the `--set` parameter of the old version.

         ```shell
         helm get values insight -n insight-system -o yaml > insight.yaml
         helm get values insight-agent -n insight-system -o yaml > insight-agent.yaml
         ```

     1. Execute `helm upgrade`.

         Before upgrading, it is recommended that you override the `global.imageRegistry` field in insight.yaml and insight-agent.yaml to the address of the currently used container registry.

         ```shell
         export imageRegistry={your image registry}
         ```

         ```shell
         helm upgrade insight insight/insight \
           -n insight-system \
           -f ./insight.yaml \
           --set global.imageRegistry=$imageRegistry \
           --version 0.13.1
         ```

         as well as

         ```shell
         helm upgrade insight-agent insight/insight-agent \
           -n insight-system \
           -f ./insight-agent.yaml \
           --set global.imageRegistry=$imageRegistry \
           --version 0.13.1
         ```

=== "upgrade via chart package"

     1. Back up the `--set` parameter.

         Before upgrading the global management version, it is recommended that you run the following command to back up the `--set` parameter of the old version.

         ```shell
         helm get values insight -n insight-system -o yaml > insight.yaml
         ```

     1. Execute `helm upgrade`.

         Before upgrading, it is recommended that you overwrite `global.imageRegistry` in bak.yaml to the address of the current container registry.

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