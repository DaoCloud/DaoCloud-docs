# Import Custom Helm Apps into Built-in Addons

This article explains how to import Helm appss into the system's built-in addons in both offline and online environments.

## Offline Environment

An offline environment refers to an environment that cannot connect to the internet or is a closed private network environment.

### Prerequisites

- [charts-syncer](https://github.com/DaoCloud/charts-syncer) is available and running.
  If not, you can [click here to download](https://github.com/DaoCloud/charts-syncer/releases).
- The Helm Chart has been adapted for [charts-syncer](https://github.com/DaoCloud/charts-syncer).
  This means adding a __.relok8s-images.yaml__ file to the Helm Chart. This file should include all the images used in the Chart,
  including any images that are not directly used in the Chart but are used similar to images used in an Operator.

!!! note

    - Refer to [image-hints-file](https://github.com/vmware-tanzu/asset-relocation-tool-for-kubernetes#image-hints-file) for instructions on how to write a Chart.
      It is required to separate the registry and repository of the image because the registry/repository needs to be replaced or modified when loading the image.
    - The installer's fire cluster has [charts-syncer](https://github.com/DaoCloud/charts-syncer) installed.
      If you are importing a custom Helm apps into the installer's fire cluster, you can skip the download and proceed to the adaptation.
      If [charts-syncer](https://github.com/DaoCloud/charts-syncer) binary is not installed, you can [download it immediately](https://github.com/DaoCloud/charts-syncer/releases).

### Sync Helm Chart

1. Go to __Container Management__ -> __Helm Apps__ -> __Helm Repositories__ , search for the addon, and obtain the built-in repository address and username/password (the default username/password for the system's built-in repository is rootuser/rootpass123).


1. Sync the Helm Chart to the built-in repository addon of the container management system

    * Write the following configuration file, modify it according to your specific configuration, and save it as __sync-dao-2048.yaml__ .

        ```yaml
        source:  # helm charts source information
          repo:
            kind: HARBOR # It can also be any other supported Helm Chart repository type, such as CHARTMUSEUM
            url: https://release-ci.daocloud.io/chartrepo/community #  Change to the chart repo URL
            #auth: # username/password, if no password is set, leave it blank
              #username: "admin"
              #password: "Harbor12345"
        charts:  # charts to sync
          - name: dao-2048 # helm charts information, if not specified, sync all charts in the source helm repo
            versions:
              - 1.4.1
        target:  # helm charts target information
          containerRegistry: 10.5.14.40 # image repository URL
          repo:
            kind: CHARTMUSEUM # It can also be any other supported Helm Chart repository type, such as HARBOR
            url: http://10.5.14.40:8081 #  Change to the correct chart repo URL, you can verify the address by using helm repo add $HELM-REPO
            auth: # username/password, if no password is set, leave it blank
              username: "rootuser"
              password: "rootpass123"
          containers:
            # kind: HARBOR # If the image repository is HARBOR and you want charts-syncer to automatically create an image repository, fill in this field
            # auth: # username/password, if no password is set, leave it blank
              # username: "admin"
              # password: "Harbor12345"
 
        # leverage .relok8s-images.yaml file inside the Charts to move the container images too
        relocateContainerImages: true
        ```

    * Execute the charts-syncer command to sync the Chart and its included images

        ```sh
        charts-syncer sync --config sync-dao-2048.yaml --insecure --auto-create-repository
        ```

        The expected output is:

        ```console
        I1222 15:01:47.119777    8743 sync.go:45] Using config file: "examples/sync-dao-2048.yaml"
        W1222 15:01:47.234238    8743 syncer.go:263] Ignoring skipDependencies option as dependency sync is not supported if container image relocation is true or syncing from/to intermediate directory
        I1222 15:01:47.234685    8743 sync.go:58] There is 1 chart out of sync!
        I1222 15:01:47.234706    8743 sync.go:66] Syncing "dao-2048_1.4.1" chart...
        .relok8s-images.yaml hints file found
        Computing relocation...
 
        Relocating dao-2048@1.4.1...
        Pushing 10.5.14.40/daocloud/dao-2048:v1.4.1...
        Done
        Done moving /var/folders/vm/08vw0t3j68z9z_4lcqyhg8nm0000gn/T/charts-syncer869598676/dao-2048-1.4.1.tgz
        ```

1. Once the previous step is completed, go to __Container Management__ -> __Helm Apps__ -> __Helm Repositories__ , find the corresponding addon,
   click __Sync Repository__ in the action column, and you will see the uploaded Helm apps in the Helm template.

1. You can then proceed with normal installation, upgrade, and uninstallation.



## Online Environment

The Helm Repo address for the online environment is __release.daocloud.io__ .
If the user does not have permission to add Helm Repo, they will not be able to import custom Helm appss into the system's built-in addons.
You can add your own Helm repository and then integrate your Helm repository into the platform using the same steps as syncing Helm Chart in the offline environment.
