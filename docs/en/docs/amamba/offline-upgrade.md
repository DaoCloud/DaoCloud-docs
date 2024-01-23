# Offline Upgrade

Workbench supports offline upgrades. You need to load the images from the
[installation package](../download/modules/amamba.md) and then run the corresponding commands for the upgrade.

## Loading Images from the Installation Package

There are two ways to load the images from the installation package.

### Sync Images via charts-syncer

If you have an image repository in your environment, it is recommended to use
charts-syncer to sync the images to the repository, which is more efficient and convenient.

1. Create the __load-image.yaml__ file.

    > Note: All parameters in this YAML file are required. You need to have a private image repository and modify the relevant configurations.

    ```yaml title="load-image.yaml"
    source:
      intermediateBundlesPath: ghippo-offline # The relative path to run the charts-syncer command, not the relative path between this YAML file and the offline package.
    target:
      containerRegistry: 10.16.10.111 # The URL of the image repository
      containerRepository: amamba # The specific project in the image repository
      repo:
        kind: HARBOR # It can also be any other supported Helm Chart repository type, such as ChartMuseum.
        url: http://10.16.10.111/chartrepo/amamba # Modify it to the chart repo URL
        auth: # Username/password
          username: "admin"
          password: "Harbor12345"
      containers:
        auth: # Username/password
          username: "admin"
          password: "Harbor12345"
    ```

    !!! note "If the chart repo is not installed in the current environment, you can also export the chart as a __tgz__ file using chart-syncer and place it in the specified path."

        ```yaml title="load-image.yaml"
        source:
            intermediateBundlesPath: amamba-offline # The relative path to run the charts-syncer command, not the relative path between this YAML file and the offline package.
        target:
            containerRegistry: 10.16.10.111 # Modify it to your image repository URL
            containerRepository: release.daocloud.io/amamba # Modify it to your image repository
            repo:
              kind: LOCAL
              path: ./local-repo # Local path to the chart
            containers:
              auth:
                username: "admin" # Your image repository username
                password: "Harbor12345" # Your image repository password
        ```

2. Run the following command to sync the images.

    ```bash
    charts-syncer sync --config load-image.yaml
    ```

### Load Images Directly via Docker or containerd

1. Run the following command to extract the images.

    ```shell
    tar xvf amamba.bundle.tar
    ```

    After successful extraction, you will have three files: __images.tar__ , __hints.yaml__ , and __original-chart__ .

1. Run the following command to load the images from the local directory into Docker or containerd.

    > Note: Perform the following steps on **each node** in the cluster. After loading the images,
    > make sure to tag them to ensure consistency with the Registry and Repository used during installation.

    ```shell
    docker load -i images.tar # for Docker
    ctr -n k8s.io image import images.tar # for containerd
    ```

## Upgrade

1. Check if the Helm repository for Workbench exists:

    ```shell
    helm repo list | grep amamba
    ```

    If the result is empty or shows an __Error: no repositories to show__ message,
    run the following command to add the Helm repository for Workbench:

    ```shell
    helm repo add amamba http://{harbor url}/chartrepo/{project}
    ```

2. Update the Helm repository for Workbench:

    ```shell
    helm repo update amamba
    ```

    Note that a low version of Helm can cause the update to fail.
    If it fails, try executing __helm update repo__ .

3. Back up the __--set__ parameters. Before upgrading the global management version,
   it is recommended to back up the __--set__ parameters of the old version using the following command:

    ```shell
    helm get values ghippo -n ghippo-system -o yaml > amamba.bak.yaml
    ```

4. Choose the desired version of Workbench to install (it is recommended to install the latest version):

    ```shell
    helm search repo amamba-release-ci --versions | head
    ```

    The output will be similar to:

    ```console
    NAME                       CHART VERSION   APP VERSION  DESCRIPTION                               
    amamba-release-ci/amamba   0.14.0  	       0.14.0  	    Amamba is the entrypoint to DCE 5.0, provides de...
    ```

5. Modify the __registry__ and __tag__ in the __amamba.bak.yaml__ file.

    ??? note "Click to view an example YAML file"

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

6. Run the following commands to upgrade.

    ```shell
    helm upgrade amamba . \
      -n amamba-system \
      -f ./amamba.bak.yaml
    ```
