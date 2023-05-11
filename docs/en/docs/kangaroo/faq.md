# container registry FAQ

## Harbor Operator installation failed

If the installation of `Harbor Operator` is unsuccessful, you need to check these points, whether `cert-manager` is installed successfully, and whether `installCRDs` is set to `true`.
Whether the `helm` task to install `Harbor operator` was successful.

## Create managed Harbor can use redis cluster mode

Currently `Harbor` still cannot use `redis` cluster mode.

## Can private images be seen in non-container registry modules?

The container registry is implemented strictly according to the authority of DEC 5.0. In the container registry, a user must belong to a certain tenant to see the private registry space under the current tenant, otherwise even the administrator cannot see it.

## After the private image is bound to the workspace, it cannot be queried

After the private image is bound to the workspace, the program needs to execute a lot of logic asynchronously, so it will not be visible immediately.
This process will be affected by the system. If the system responds faster, the asynchronous execution will be faster and can be seen within 1 minute. It should be no longer than 5 minutes.

## Managed Harbor can be accessed after creation, but the status is still unhealthy

Currently, the status on the hosted Harbor page and the status of the registry integration are two in one. When both statuses are healthy, it is healthy.
Therefore, it may happen that the managed `Harbor` is already accessible, but the state is still unhealthy. In this case, you need to wait for a service detection cycle. A detection cycle is 10 minutes, and it will return to the original state after a cycle.

## The status of the created managed registry is unhealthy



- A1: The database, Redis, S3 storage and other information entered by the user are incorrect, resulting in the failure to connect. You can check the log files for troubleshooting. The phenomenon is mainly that several core services have Pod startup failures, and the cause can be further confirmed by viewing the logs.

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

- A2: If the troubleshooting in A1 is correct, check whether the `harborcluster` resource is healthy, and check the `harborcluster` resource status with the following command.

     ```shell
     kubectl -n kangaroo-lrf04 get harborclusters.goharbor.io
     ```

     ```none
     NAME PUBLIC URL STATUS
     trust-node-port https://10.6.232.5:30010 healthy
     ```

- A3: If the troubleshooting in A2 is correct, check whether the `registrysecrets.kangaroo.io` resource is created and the status of `status` on the `kpanda-global-cluster` cluster.

     Tip: The default namespace is kangaroo-system.

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

     - The above A1 and A2 are all troubleshooting on the cluster hosting Harbor, and the target cluster can be viewed through the following page path: `registry Instance` -> `Overview` -> `Deployment Location`
     - The above A3 was verified on `kpanda-global-cluster` cluster.

## After creating a `Project` or uploading an image, it is found that the image space and available storage on the page have not increased

This is because the statistical information on the `Hosted Harbor` home page and registry integration details on the UI page is asynchronously obtained data, and there will be a certain delay, the longest delay is `10` minutes.

## The registry is integrated but the status is unhealthy



First confirm whether the instance is really healthy. If the instance is not healthy, you need to troubleshoot the instance;
If the instance is healthy, check `registrysecrets.kangaroo.io` on the `kpanda-global-cluster` cluster
Whether the resource is created, and check the status of `status`, so that you can initially confirm the problem.

Tip: The default namespace is kangaroo-system.

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

## After the registry is integrated, it cannot be viewed in the instance of the image list page

Please confirm whether the resources integrated in the registry are healthy. If they are unhealthy, they will not be displayed in the instance list on the image list page.
For the confirmation method, please refer to [Unhealthy Confirmation Method after registry Integration](#_2).

## Select a private `Project` image in the `Kpanda` image selector, but when deploying, it prompts that the image pull failed

- A1: You can see the private `Project` in the image selector, which means that `Project` and `Workspace` have been bound,
   At this point, you need to check whether a `secret` named `registry-secret` is generated in the `namespace` of the target cluster for image deployment.

     ```shell
     kubectl -n default get secret registry-secret
     ```

     ```none
     NAME TYPE DATA AGE
     registry-secret kubernetes.io/dockerconfigjson 1 78d
     ```

- A2: If you confirm that the `secret` named `registry-secret` has been generated, you need to confirm whether the `dockerconfigjson` in the `secret` is correct.

     ```shell
     kubectl get secret registry-secret -o jsonpath='{.data.*}'| base64 -d | jq
     ```

     ```none
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
