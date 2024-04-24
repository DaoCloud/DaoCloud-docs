# ArgoCD High Availability Solution

ArgoCD mainly includes the following components:

- argocd-repo-server

    The argocd-repo-server is responsible for cloning Git repositories and keeping them up to date.
    Repositories are cloned to /tmp (or a path specified by the TMPDIR environment variable).
    If the Pod has too many repositories or if the repositories contain a large number of files,
    the Pod may run out of disk space. To avoid this problem, please install a persistent volume.

- argocd-controller

    It is used to fetch the generated Manifests and requests the Kubernetes API server to get the actual state of the argocd-application-controller from the argocd-repo-server cluster.
    Each controller replica uses two separate queues to handle the coordination (milliseconds) and synchronization (seconds) of applications.
    Manifest generation usually takes the most time during coordination, and if manifest generation takes too long, application coordination will fail and result in an error. As a solution,
    you can increase the deployment value --repo-server-timeout-seconds and consider expanding the scale of the argocd-repo-server deployment.
    If the controller manages too many clusters, it will use too much memory, and you can shard the clusters across multiple controller replicas.
    To enable sharding, increase the number of replicas in the argocd-application-controller StatefulSet environment variable and duplicate the number of replicas ARGOCD_CONTROLLER_REPLICAS.
    By default, the controller updates cluster information every 10 seconds. If there are issues with your cluster network that cause longer update times, you can try modifying the environment variable ARGO_CD_UPDATE_CLUSTER_INFO_TIMEOUT to increase the timeout (in seconds).

- argocd-server

    This is stateless and is least likely to cause issues. To ensure there is no downtime during upgrades,
    consider increasing the number of replicas to 3 or more, and replicate this number in the environment variable ARGOCD_API_SERVER_REPLICAS.
    The environment variable ARGOCD_GRPC_MAX_SIZE_MB allows you to specify the maximum size of server response messages
    (in megabytes). The default value is 200. For an ArgoCD instance managing over 3000 applications,
    you might need to increase this value.

- argocd-dex-server

    Using argocd-dex-server in-memory database, data will be inconsistent across two or more instances.

## Installation

Below is the content of a values.yaml file for an HA installation mode,
based on official documentation modified environment variables
(just a necessary example, actual installation is recommended to install persistent volumes).

```yaml title="values.yaml"
argo-cd:
  crds:
    install: false # Set to false if argo-cd was installed previously
    keep: false
  configs:
    params:
      reposerver.parallelism.limit: 4
      controller.status.processors: 20 # Set as needed
      controller.operation.processors: 10 # Set as needed
      controller.repo.server.timeout.seconds: 60 # If managing many repositories, consider increasing this value
      timeout.reconciliation: 180s # Polling time
  repoServer:
    replicas: 2
    autoscaling:
      enabled: true
      minReplicas: 2
      maxReplicas: 5
    env:
      - name: ARGOCD_GIT_ATTEMPTS_COUNT
        value: "3"
      - name: ARGOCD_EXEC_TIMEOUT
        value: "2m30s"
    extraArgs:
      - --repo-cache-expiration=1h
  controller:
    replicas: 2 # Consider increasing deployment size if managing many repositories
    env: 
      - name: WORKQUEUE_BUCKET_SIZE
        value: "500"
      - name: ARGOCD_RECONCILIATION_JITTER
        value: "60"
      - name: ARGO_CD_UPDATE_CLUSTER_INFO_TIMEOUT
        value: "60" # In seconds
      - name: ARGOCD_CLUSTER_CACHE_LIST_PAGE_SIZE
        value: "500"
      - name: ARGOCD_CLUSTER_CACHE_LIST_PAGE_BUFFER_SIZE
        value: "5"
  server:
    autoscaling:
      enabled: true
      minReplicas: 2 # Should not be 1
      maxReplicas: 5
    env:
      - name: ARGOCD_API_SERVER_REPLICAS
        value: "2" # Recommended to be consistent with minReplicas, not less than minReplicas
      - name: ARGOCD_GRPC_MAX_SIZE_MB
        value: "200"
  dex: # Argo's own in-memory storage component, HA mode will cause data inconsistency, can set replica count to 1
    enabled: true
  redis-ha:
    enabled: true
```

Field explanations are as follows:

| Field | Recommended Value | Description |
|-------|-------------------|-------------|
| argo-cd.configs.params.reposerver.parallelism.limit | 10 | Configures the number of manifests the management tool can operate on simultaneously; insufficient memory or system threads can cause git repository fetch failures |
| argo-cd.configs.params.controller.status.processors | 20 | Configures the controller's queue for coordinating apps (processing time in milliseconds) default length is 20 (recommended length per 1000 apps is 50) |
| argo-cd.configs.params.controller.operation.processors | 10 | Configures the controller's queue for syncing apps (processing time in seconds) default length is 10 (recommended length per 1000 apps is 25) |
| argo-cd.configs.params.controller.repo.server.timeout.seconds | 60 | Configures the timeout to prevent queue overflow during manifest generation |
| argo-cd.configs.params.timeout.reconciliation | 180s | Configures the polling cycle for the controller's git repository |
| argo-cd.reposerver.env[0].name: ARGOCD_GIT_ATTEMPTS_COUNT | 3 | Configures the number of retries for failed git repository requests |
| argo-cd.reposerver.env[1].name: ARGOCD_EXEC_TIMEOUT | 2m30s | Configures the execution timeout for the reposerver processing git or helm repositories |
| argo-cd.reposerver.extraArgs[0]: --repo-cache-expiration=1h | 1h | Configures the cache expiration time for the reposerver |
| argo-cd.controller.env[0].name: WORKQUEUE_BUCKET_SIZE | 500 | Configures the queue length for the controller handling concurrent events |
| argo-cd.controller.env[1].name: ARGOCD_RECONCILIATION_JITTER | 60 | Configures the jitter time to prevent spikes in storage server components when an app sync times out, in seconds |
| argo-cd.controller.env[2].name: ARGO_CD_UPDATE_CLUSTER_INFO_TIMEOUT | 60 | Configures the interval for the controller updating cluster information (increase this variable when cluster network issues cause long update times or when cluster updates are infrequent) |
| argo-cd.controller.env[3].name: ARGOCD_CLUSTER_CACHE_LIST_PAGE_SIZE | 500 | Configures the page size for the controller retrieving cluster resources (ARGOCD_CLUSTER_CACHE_LIST_PAGE_SIZE*ARGOCD_CLUSTER_CACHE_LIST_PAGE_BUFFER_SIZE should be greater than the estimated maximum resource count in the cluster) |
| argo-cd.controller.env[4].name: ARGOCD_CLUSTER_CACHE_LIST_PAGE_BUFFER_SIZE | 5 | Can increase the buffer size appropriately to prevent controller memory overflow errors (in MB) |
| argo-cd.server.env[1].name: ARGOCD_GRPC_MAX_SIZE_MB | 200 | In MB, allows the maximum size of server response messages, set to a larger value if managing many projects (set to 200+ if 3000 projects) |

## References

- [Argo CD Official High Availability Configuration Steps](https://argo-cd.readthedocs.io/en/stable/operator-manual/high_availability/)
