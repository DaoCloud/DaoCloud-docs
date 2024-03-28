# Deploy Second Scheduler scheduler-plugins in a Cluster

This page describes how to deploy a second scheduler scheduler-plugins in a cluster.

## Why do we need scheduler-plugins?

The cluster created through the platform will install the native K8s scheduler, but the native scheduler has many limitations:

- The native scheduler cannot meet scheduling requirements, you can choose to use
  [CoScheduling](https://github.com/kubernetes-sigs/scheduler-plugins/tree/master/pkg/coscheduling),
  [CapacityScheduling](https://github.com/kubernetes-sigs/scheduler-plugins/tree/master/pkg/capacityscheduling)
  and other scheduler-plugins plugins
- In special scenarios, a new scheduler is needed to complete scheduling tasks without affecting the process of the native scheduler
- Distinguish schedulers with different functionalities by switching scheduler names to achieve different scheduling scenarios

This page takes the scenario of using the vgpu scheduler while combining the cosheduling plugin capability of scheduler-plugins as an example to introduce how to install and use scheduler-plugins.

## Install scheduler-plugins

### Prerequisites

- kubean is a new feature introduced in version v0.13.0, please ensure that the version is >= this version when managing the cluster.
- The installation version of scheduler-plugins is v0.27.8, please ensure that the cluster version is compatible with it.
  Refer to the document [Compatibility Matrix](https://github.com/kubernetes-sigs/scheduler-plugins/tree/master?tab=readme-ov-file#compatibility-matrix).

### Installation Process

1. Add the scheduler-plugins parameter in **Create Cluster** -> **Advanced Configuration** -> **Custom Parameters**.

    ```yaml
    scheduler_plugins_enabled:true
    scheduler_plugins_plugin_config:
      - name: Coscheduling
        args:
          permitWaitingTimeSeconds: 10 # default is 60
    ```

    Parameters:

    - `scheduler_plugins_enabled` When set to true, enables the scheduler-plugins capability.
    - You can enable or disable certain plugins by setting the `scheduler_plugins_enabled_plugins` or `scheduler_plugins_disabled_plugins` options.
    See [K8s Official Plugin Names](https://github.com/kubernetes-sigs/scheduler-plugins?tab=readme-ov-file#plugins) for reference.
    - If you need to set parameters for custom plugins, please configure `scheduler_plugins_plugin_config`,
      for example: set the `permitWaitingTimeoutSeconds` parameter for coscheduling.
      See [K8s Official Plugin Configuration](https://github.com/kubernetes-sigs/scheduler-plugins/blob/master/manifests/coscheduling/scheduler-config.yaml) for reference.

    <!-- ![Add scheduler-plugins parameter](../../images/cluster-scheduler-plugin-01.png) -->

2. After successful cluster creation, the system will automatically install the scheduler-plugins and
   controller component loads. You can check the load status in the corresponding cluster's stateless loads.

    <!-- ![Check plugin load status](../../images/cluster-scheduler-plugin-02.png) -->

## Using scheduler-plugins

Here is an example of how to use scheduler-plugins in conjunction with the coscheduling plugin while using the vgpu scheduler.

1. Install vgpu in the Helm template and set the values.yaml parameters.

    - `schedulerName: scheduler-plugins-scheduler`: This is the scheduler name for scheduler-plugins installed by kubean, and currently cannot be modified.
    - `scheduler.kubeScheduler.enabled: false`: Do not install kube-scheduler and use vgpu-scheduler as a separate extender.

    <!-- ![Install vgpu plugin](../../images/cluster-scheduler-plugin-03.png) -->

1. Extend vgpu-scheduler on scheduler-plugins.

    ```bash
    [root@master01 charts]# kubectl get cm -n scheduler-plugins scheduler-config -ojsonpath="{.data.scheduler-config\.yaml}"
    ```

    ```yaml
    apiVersion: kubescheduler.config.k8s.io/v1
    kind: KubeSchedulerConfiguration
    leaderElection:
      leaderElect: false
    profiles:
      # Compose all plugins in one profile
      - schedulerName: scheduler-plugins-scheduler
        plugins:
          multiPoint:
            enabled:
              - name: Coscheduling
              - name: CapacityScheduling
              - name: NodeResourceTopologyMatch
              - name: NodeResourcesAllocatable
            disabled:
              - name: PrioritySort
    pluginConfig:
      - args:
          permitWaitingTimeSeconds: 10
        name: Coscheduling
    ```

    Modify configmap of scheduler-config for scheduler-plugins:

    ```bash
    [root@master01 charts]# kubectl get cm -n scheduler-plugins scheduler-config -ojsonpath="{.data.scheduler-config\.yaml}"
    ```

    ```yaml
    apiVersion: kubescheduler.config.k8s.io/v1
    kind: KubeSchedulerConfiguration
    leaderElection:
      leaderElect: false
    profiles:
      # Compose all plugins in one profile
      - schedulerName: scheduler-plugins-scheduler
        plugins:
          multiPoint:
            enabled:
              - name: Coscheduling
              - name: CapacityScheduling
              - name: NodeResourceTopologyMatch
              - name: NodeResourcesAllocatable
            disabled:
              - name: PrioritySort
    pluginConfig:
      - args:
          permitWaitingTimeSeconds: 10
        name: Coscheduling
    extenders:
      - urlPrefix: "${urlPrefix}"
        filterVerb: filter
        bindVerb: bind
        nodeCacheCapable: true
        ignorable: true
        httpTimeout: 30s
        weight: 1
        enableHTTPS: true
        tlsConfig:
          insecure: true
        managedResources:
          - name: nvidia.com/vgpu
            ignoredByScheduler: true
          - name: nvidia.com/gpumem
            ignoredByScheduler: true
          - name: nvidia.com/gpucores
            ignoredByScheduler: true
          - name: nvidia.com/gpumem-percentage
            ignoredByScheduler: true
          - name: nvidia.com/priority
            ignoredByScheduler: true
          - name: cambricon.com/mlunum
            ignoredByScheduler: true
    ```

1. After installing vgpu-scheduler, the system will automatically create a service (svc), and the urlPrefix specifies the URL of the svc.

    !!! note

        - The svc refers to the pod service load. You can use the following command in the namespace where the nvidia-vgpu plugin is installed to get the external access information for port 443.

            ```shell
            kubectl get svc -n ${namespace}
            ```

        - The urlPrefix format is `https://${ip address}:${port}`

1. Restart the scheduler pod of scheduler-plugins to load the new configuration file.

    !!! note

        When creating a vgpu application, you do not need to specify the scheduler name. The vgpu-scheduler webhook
        will automatically change the scheduler's name to "scheduler-plugins-scheduler" without manual specification.
