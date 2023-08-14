# Container Registry FAQ

This page lists some common issues and solutions when using the container registry.

## Middleware deployment is not available in the DCE 5.0 standard package

The DCE 5.0 standard package does not include middleware. Middleware is only available in the Platinum package.

## How to verify if the configured middleware network is connectable

Log in to the target cluster where Harbor is deployed and execute the `ping` command
on any node to test the connectivity to the middleware components.

## Private images not visible in the image space list

There is a bug in versions `v0.7.0-v0.7.3` and `v0.8.0` of the container registry system,
which results in the inability to see private images.

## When using Minio deployed with middleware

When using Minio deployed with middleware, you need to manually create buckets
through the Minio management platform beforehand.

## Minimum supported version of Harbor for repository integration

During repository integration, there are certain version requirements due to
the use of Harbor's functionality. Currently, the known minimum supported version is `2.4.0`.
Earlier versions will not be compatible.

## Offline environment image scanner failure

The image scanner relies on vulnerability data, which is obtained by default from the [CVE official website](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=kubernetes).
In a pure offline environment, vulnerability scanning cannot be performed, and the process will fail.

![trivy](./images/trivy-nodb.png)

## Error occurs when creating Harbor after cluster verification passes in the first step

Currently, only the existence of `CRD` is being verified in the cluster, and the `harbor-operator` service
is not being checked. This may result in failures to create `Harbor` correctly when the `harbor-operator` service does not exist.

## Error occurs after executing `docker login {ip}` locally

```text
Error response from daemon: Get "https://{ip}/v2/": x509: cannot validate certificate for {ip} because it doesn't contain any IP SANs
```

This error occurs because the `registry` is an `https` service that uses an unsigned or insecure certificate.
To resolve this issue, add the corresponding IP to `"insecure-registries"` in the `/etc/docker/daemon.json` configuration file.

```json
"insecure-registries": [
  "{ip}",
  "registry-1.docker.io"
]
```

Then, restart the service with `systemctl restart docker`.

## Failed to start services when passwords contain special chars

Failure to start services when creating Harbor and accessing external PG and Redis with passwords containing special characters (!@#$%^&*)

Currently, passwords cannot contain special characters; otherwise, the services will fail to start.
You can use a combination of uppercase and lowercase letters and numbers instead.

## Harbor Operator installation failed

If the installation of `Harbor Operator` is unsuccessful, you should check the following:

- Ensure that `cert-manager` has been successfully installed.
- Verify that the `installCRDs` setting is set to `true`.
- Confirm that the `helm` job for installing the `Harbor operator` was successful.

## Can I use redis cluster mode when creating a managed Harbor?

Currently, `Harbor` does not support the use of `redis` cluster mode.

## Can private images be seen in a module other than container registry?

The container registry strictly follows the authority of DCE 5.0.
To view private registry space under the current tenant, users must belong to a specific tenant.
Even administrators cannot view it without belonging to the tenant.

## Unable to query private images after binding to workspace

After binding a private image to a workspace, the program executes several asynchronous logic processes,
and it may not be immediately visible. The process duration is dependent on the system's speed and
may take up to 5 minutes to appear.

## Managed Harbor accessible but status remains unhealthy

Currently, the status on the managed Harbor page and the status of the registry integration are combined.
When both statuses are healthy, the Harbor is considered healthy. It's possible that the managed `Harbor`
is already accessible, but the state remains unhealthy. In this case, wait for a service detection cycle,
which occurs every 10 minutes, and it will return to the original state after the cycle.

## The status of managed registry you created just now is unhealthy

- A1: Incorrect user entries for the database, Redis, S3 storage, or other information may
  result in a connection failure. Troubleshoot by checking log files. You may notice that
  several core services have Pod startup failures. Review the logs to determine the cause of the failure.

    ```shell
    kubectl -n kangaroo-lrf04 get pods
    ```

    ```none
    NAME READY STATUS RESTARTS AGE
    trust-node-port-harbor-harbor-chartmuseum-57fdfb9cdc-qznwc 1/1 Running 0 20h
    trust-node-port-harbor-harbor-core-855f8df46c-cgqb9 1/1 Running 0 20h
    trust-node-port-harbor-harbor-jobservice-6b958dbc57-ks997 1/1 Running 0 20h
    trust-node-port-harbor-harbor-portal-5cf6bf659b-kj6gd 1/1 Running 0 20h
    trust-node-port-harbor-harbor-registry-5ccbf457c5-qrtx5 2/2 Running 0 20h
    trust-node-port-harbor-harbor-trivy-dbdc8945-xh6rv 1/1 Running 0 20h
    trust-node-port-nginx-deployment-677c74576-7kmh4 1/1 Running 0 20h
    ```

- A2: If the troubleshooting in A1 is correct, check whether the `harborcluster` resource is
  healthy, and check the `harborcluster` resource status with the following command.

    ```shell
    kubectl -n kangaroo-lrf04 get harborclusters.goharbor.io
    ```

    ```none
    NAME PUBLIC URL STATUS
    trust-node-port https://10.6.232.5:30010 healthy
    ```

- A3: If the troubleshooting in A2 is correct, check whether the `registrysecrets.kangaroo.io`
  resource is created and the status of `status` on the `kpanda-global-cluster` cluster.

    Tip: The default namespace is `kangaroo-system`.

    ```shell
    kubectl -n kangaroo-system get registrysecrets.kangaroo.io
    ```

    ```none
    NAME AGE
    inte-bz-harbor-1 34d
    ```

    ```shell
    kubectl -n kangaroo-system describe registrysecrets.kangaroo.io inte-bz-harbor-1
    ```

!!! tip

    - The above A1 and A2 are all troubleshooting on the cluster hosting Harbor,
      and the target cluster can be viewed through the following page path: 
      `registry Instance` -> `Overview` -> `Deployment Location`.
    - The above A3 was verified on `kpanda-global-cluster` cluster.

## Issue with registry space and storage after creating a Project or uploading an image

If you have created a `Project` or uploaded an image, but found that there has been no increase
in the registry space or available storage on the page, this might be due to the asynchronous nature
of obtaining statistical information on the `managed Harbor` home page and registry integration details
on the UI page. The data retrieval process can take up to `10` minutes, causing a certain delay before
any changes are reflected.

## Registry integration status is unhealthy

If you encounter an issue where the registry integration status is unhealthy, follow these steps:

1. First, check whether the instance is healthy. If it's not, then troubleshoot the instance.
2. If the instance is healthy, verify whether the resource `registrysecrets.kangaroo.io`
   on the `kpanda-global-cluster` cluster has been created or not.
3. Check the status of the resource `status` to identify the problem initially.

**Note:** Ensure to check the default namespace, which is `kangaroo-system`.

```shell
kubectl -n kangaroo-system get registrysecrets.kangaroo.io
```

```none
NAME AGE
trust-test-xjw 34d
```

```shell
kubectl -n kangaroo-system get registrysecrets.kangaroo.io trust-test-xjw -o yaml
```

```yaml
apiVersion: kangaroo.io/v1alpha1
kind: RegistrySecret
metadata:
   name: trust-test-xjw
   namespace: kangaroo-system
spec:
   ....
status:
   state:
     lastTransitionTime: "2023-03-29T03:27:31Z"
     message: 'Get "https://harbor.kangaroo.daocloud.io": dial tcp: lookup harbor.kangaroo.daocloud.io
       on 10.233.0.3:53: no such host'
     reason: RegistryHealthCheckFail
     status: "False"
     type: HealthCheckFail
```

## After integrating the registry, it cannot be viewed in the instance list page of the image

Please confirm if the resources integrated into the registry are healthy. If they are unhealthy,
they won't appear in the instance list on the image page. For the confirmation method,
please refer to [Unhealthy Confirmation Method after Registry Integration](#registry-integration-status-is-unhealthy).

## Selecting a Private `Project` Image in the `Kpanda` Image Selector results in a failed image pull prompt during deployment

- A1: If you can see the private `Project` in the image selector, which means that `Project`
  and `Workspace` have already been bound. At this point, check if a `secret` named `registry-secret`
  has been generated in the target cluster's `namespace` for image deployment.

    ```shell
    kubectl -n default get secret registry-secret
    ```

    ```none
    NAME TYPE DATA AGE
    registry-secret kubernetes.io/dockerconfigjson 1 78d
    ```

- A2: If you confirm that the `secret` named `registry-secret` has been generated,
  you need to confirm whether the `dockerconfigjson` in the `secret` is correct.

    ```shell
    kubectl get secret registry-secret -o jsonpath='{.data.*}'| base64 -d | jq
    ```

    ```json
    {
      "auths": {
        "127.0.0.1:5000": {
          "auth": "YWRtaW46SGFyYm9yMTIzNDU="
        }
      }
    }
    ```

    ```shell
    echo "YWRtaW46SGFyYm9yMTIzNDU=" | base64 -d
    ```

    ```none
    admin:Harbor12345
    ```
