# Offline upgrade

The application workbench supports offline upgrade. You need to load the image from the installation package first, and then run the corresponding command to upgrade.

## Load the image from the installation package

You can load an image in two ways.

### Image synchronization through chart-Syncer

If a mirror warehouse exists in the environment, it is recommended to use chart-syncer to synchronize images to the mirror warehouse, which is more efficient and convenient.

1. Create the `load-image.yaml` file.

    > Note: The parameters in this YAML file are mandatory. You need a private mirror repository and modify the configuration.

    ```yaml title="load-image.yaml"
    source:
      intermediateBundlesPath: ghippo-offline # relative path to run `charts-syncer`，not the path of this YAML file to offline package
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

    !!!!!!!!! note "If chart repo is not installed in your current environment, you can also export chart to a `tgz` file via chart-syncer and store it in the specified path."

        ```yaml title="load-image.yaml"
        source:
            intermediateBundlesPath: amamba-offline #  relative path to run `charts-syncer`，not the path of this YAML file to offline package
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

2. Run the following command to synchronize a mirror.

    ```bash
    charts-syncer sync --config load-image.yaml
    ```

### Load the image directly via Docker or containerd

1. Run the following command to decompress the image.

    ```shell
    tar xvf amamba.bundle.tar
    ```

    Decompression after success will get three file: `images.tar`, `hints.yaml`, `original-chart`.

1. Run the following command to load the image locally to Docker or containerd.

    > Note: You need to perform the following operations on ** Each node ** in the cluster. After the loading is complete, label the image to ensure that Registry and Repository are consistent with those during installation.

    ```shell
    docker load -i images.tar # for Docker
    ctr image import images.tar # for containerd
    ```

## upgrade

1. Check that the Helm repository for the application workbench exists.

    ```shell
    helm repo list | grep amamba
    ```

    If nothing is returned or `Error: no repositories to show` is displayed, run the following command to add the Helm repository for the application workbench.

    ```shell
    heml repo add amamba http://{harbor url}/chartrepo/{project}
    ```

2. Update the Helm repository for the application workbench.

    ```shell
    # outdated Helm versions may cause failure. If failed, try `helm update repo`
    helm repo update amamba
    ```

3. Backup `--set` Parameter. Before upgrading the global management version, you are advised to run the following commands to back up `--set` parameters of the previous version.

    ```shell
    helm get values ghippo -n ghippo-system -o yaml > amamba.bak.yaml
    ```

4. Select the version of the application workbench you want to install (the latest version is recommended).

    ```shell
    $ helm search  repo amamba-release-ci --versions |head
    NAME                                   CHART VERSION      	APP VERSION        	DESCRIPTION                               
    amamba-release-ci/amamba                0.14.0  	        0.14.0  	         Amamba is the entrypoint to DCE 5.0, provides de...
    ```

5. Modify `registry` and `tag` in `amamba.bak.yaml`.

    ????? note "Click to view sample YAML file"

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
