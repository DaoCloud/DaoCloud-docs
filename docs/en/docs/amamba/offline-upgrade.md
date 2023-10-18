# Offline upgrade

Workbench supports offline upgrade. This guide will walk you through Workbench upgrade process
from an [installation package](../download/modules/amamba.md).

<!--!!! note

    Fetch the latest image of Workbench.
-->

## Load image from installation package

You can load an image in two ways.

### Load with chart-Syncer

If a mirror warehouse exists in the environment, it is recommended to use chart-syncer to synchronize images to the mirror warehouse, which is more efficient and convenient.

1. Create `load-image.yaml` as the chart-syncer profile

    All parameters in the `load-image.yaml` file are mandatory. You need a private container registry and modify configurations as described below. See [Official Doc](https://github.com/bitnami-labs/charts-syncer) for a detailed explanation of the chart-syncer profile.

    === "chart repo installed"

        If chart repo is already install, use the following configuration to synchronize the image directly.

    ```yaml title="load-image.yaml"
    source:
      intermediateBundlesPath: amamba-offline # Relative path to executing chart-syncer command, **not** the relative path between this YAML file and the offline package
    target:
      containerRegistry: 10.16.10.111 # image repo url
      containerRepository: amamba # the specific project in image repo
      repo:
        kind: HARBOR # Can be other supported Helm Chart repos, like ChartMuseum
        url: http://10.16.10.111/chartrepo/amamba #  change to chart repo url
        auth: # username/password
          username: "admin"
          password: "Harbor12345"
      containers:
        auth: # username/password
          username: "admin"
          password: "Harbor12345"
    ```

    === "chart repo not installed"

        Chart-syncer also supports exporting a chart as a `tgz` file in a specified path if chart repo is not installed.

        ```yaml title="load-image.yaml"
        source:
            intermediateBundlesPath: amamba-offline #  Relative path to executing chart-syncer command, **not** the relative path between this YAML file and the offline package
        target:
            containerRegistry: 10.16.10.111 # change to your image repo url
            containerRepository: release.daocloud.io/amamba # change to the project in your image repo
            repo:
              kind: LOCAL
              path: ./local-repo # loca path of chart
            containers:
              auth:
                username: "admin" # your username to access image repo
                password: "Harbor12345" # your password to access image repo
        ```

2. Run this command to sync the image.

    ```bash
    charts-syncer sync --config load-image.yaml
    ```

### Load with Docker/containerd

1. Decompress the `tar` package.

    ```shell
    tar xvf amamba.bundle.tar
    ```

    After the decompression, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the image from local to a Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr image import images.tar
        ```

!!! note
    
    - The image needs to be loaded via Docker or containerd to each node.
    - After the loading is complete, you should tag the image to keep version consistency.

## Start Upgrade

1. Check if the helm repository of Workbench exists. `amamba` is the internal code for Workbench.

    ```shell
    helm repo list | grep amamba
    ```

    If nothing is returned or `Error: no repositories to show` is displayed, run the following command to add the Helm repository for Workbench.

    ```shell
    helm repo add amamba http://{harbor url}/chartrepo/{project}
    ```

2. Update Workbench's Helm repository.

    ```shell
    helm repo update amamba
    ```

    Outdated Helm versions may cause failure. If failed, try `helm update repo`

3. Back up `--set` parameters. Before upgrading the global management version, it is recommended to run the following commands to back up `--set` parameters of the previous version.

    ```shell
    helm get values amamba -n amamab-system -o yaml > amamba.bak.yaml
    ```

4. Select the version of Workbench you want to install (the latest version is recommended).

    ```shell
    helm search  repo amamba-release-ci --versions |head
    ```
    
    The output is similar to:

    ```console
    NAME                       CHART VERSION   APP VERSION  DESCRIPTION                               
    amamba-release-ci/amamba   0.14.0  	       0.14.0  	    Amamba is the entrypoint to DCE 5.0, provides de...
    ```

5. Modify `registry` and `tag` in `amamba.bak.yaml`.

    ??? note "Click to see sample YAML file"

        ```yaml title="amamba.bak.yaml"
        amambaSyncer:
          resources:
            limits:
              cpu: 200m
              memory: 256Mi
            requests:
              cpu: 20m
              memory: 128Mi
        apiServer:
          configMap:
            debug: true
          fromJar:
            image:
              registry: releas-ci.daocloud.io
              repository: docker/library/openjdk
              tag: 11.0-jre-slim
          image:
            registry: release-ci.daocloud.io
            repository: amamba/amamba-apiserver
          resources:
            limits:
              cpu: "2"
              memory: 2Gi
            requests:
              cpu: 20m
              memory: 150Mi
        argo-cd:
          applicationSet:
            enabled: false
            image:
              repository: release-ci.daocloud.io/quay/argoproj/argocd
              tag: v2.4.12
          controller:
            image:
              repository: release-ci.daocloud.io/quay/argoproj/argocd
              tag: v2.4.12
            resources:
              limits:
                cpu: "2"
                memory: 2Gi
              requests:
                cpu: 100m
                memory: 256Mi
          dex:
            enabeld: true
            image:
              repository: release-ci.daocloud.io/ghcr/dexidp/dex
              tag: v2.32.0
            initImage:
              repository: release-ci.daocloud.io/quay/argoproj/argocd
              tag: v2.4.12
            resources:
              limits:
                cpu: 50m
                memory: 64Mi
              requests:
                cpu: 10m
                memory: 16Mi
          enabled: true
          notifications:
            enabled: false
          redis:
            enabled: true
            image:
              repository: release-ci.daocloud.io/docker/library/redis
              tag: 7.0.4-alpine
            metrics:
              enabled: false
            resources:
              limits:
                cpu: 200m
                memory: 128Mi
              requests:
                cpu: 5m
                memory: 16Mi
          repoServer:
            image:
              repository: release-ci.daocloud.io/quay/argoproj/argocd
              tag: v2.4.12
            resources:
              limits:
                cpu: 200m
                memory: 256Mi
              requests:
                cpu: 5m
                memory: 8Mi
          server:
            image:
              repository: release-ci.daocloud.io/quay/argoproj/argocd
              tag: v2.4.12
            resources:
              limits:
                cpu: 250m
                memory: 256Mi
              requests:
                cpu: 5m
                memory: 8Mi
            service:
              nodePortHttp: 31886
              nodePortHttps: 31887
              type: NodePort
        argo-rollouts:
          controller:
            image:
              registry: release-ci.daocloud.io
              repository: quay/argoproj/argo-rollouts
              tag: v1.2.0
            resources:
              limits:
                cpu: 100m
                memory: 128Mi
              requests:
                cpu: 16m
                memory: 128Mi
          dashboard:
            enabled: true
            image:
              registry: release-ci.daocloud.io
              repository: quay/argoproj/kubectl-argo-rollouts
              tag: v1.2.0
            resources:
              limits:
                cpu: 100m
                memory: 128Mi
              requests:
                cpu: 10m
                memory: 16Mi
            service:
              nodePort: 30070
              type: NodePort
          enabled: true
        devopsServer:
          enabled: true
          image:
            registry: release-ci.daocloud.io
            repository: amamba/amamba-devops-server
          resources:
            limits:
              cpu: "2"
              memory: 2Gi
            requests:
              cpu: 50m
              memory: 160Mi
        global:
          amamba:
            imageTag: v0.13-dev-a8ca782a
          imageRegistry: release-ci.daocloud.io
        mysql:
          busybox:
            repository: docker/busybox
            tag: 1.35.0
          image:
            repository: docker/mysql
            tag: 5.7.30
          persistence:
            size: 20Gi
          resources:
            limits:
              cpu: 500m
              memory: 512Mi
            requests:
              cpu: 20m
              memory: 256Mi
        ui:
          image:
            tag: v0.15.0-dev-fd64789e
          resources:
            limits:
              cpu: 100m
              memory: 128Mi
            requests:
              cpu: 5m
              memory: 4Mi
        
        ```

6. Run the following command to upgrade

    ```shell
    helm upgrade amamba . \
      -n amamba-system \
      -f ./amamba.bak.yaml
    ```
