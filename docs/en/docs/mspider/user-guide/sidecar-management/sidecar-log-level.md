---
date: 2023-07-28
status: new
hide:
   - toc
---

# Change Sidecar Log Level

The sidecar log is used to record the operation of the workload's sidecar. By controlling the log level, you can control the output of the sidecar log, thereby reducing log output, storage, and transmission.

When deploying a mesh instance, DCE 5.0 supports configuring the global default sidecar log level. By default, all workload sidecars will use this configuration.

## Sidecar Log Level Configuration

- Global Default Sidecar Log Level: By default, the log level of all sidecar logs can be configured in the sidecar information of the mesh instance.
- Temporary Modification of Workload Sidecar Log Level: This applies to modifying the log level of an individual workload's sidecar temporarily within the sidecar container.

### Global Default Sidecar Log Level

!!! warning

    The global default sidecar log level can only be modified by the mesh administrator.

1. Log in to the console, go to the mesh instance details page, and click __Edit Sidecar Information__
   to access the sidecar information modification page.

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/sidecar-log-level-01.png)

2. On the sidecar information modification page, you can modify the global default sidecar log level.
   After making the changes, click the __Save__ button to save the modifications.

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/sidecar-log-level-02.png)

### Temporary Modification of Workload Sidecar Log Level

In most cases, when analyzing temporary issues, you may need to modify the sidecar log level of a specific workload.
DCE service mesh supports temporary modification of the sidecar log level within the sidecar container of the workload.

![image](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/sidecar-log-level-03.png)

To update the configuration of the sidecar container, you need to use __kubectl__ .
Access the cluster console, open the terminal, and run the following command:

```shell
kubectl -n <namespace> exec -it <pod-name>  -c istio-proxy -- curl -X POST localhost:15000/logging?level=<log level>
```

- __<namespace>__ : The namespace where the workload is located.
- __<pod-name>__ : The name of the pod for the workload.
- __<log level>__ : The sidecar log level. Possible values are __trace__ , __debug__ , __info__ , __warning__ , __error__ , __critical__ , __off__ , etc.
- __istio-proxy__ : The name of the sidecar container. No need to modify.
- __localhost:15000__ : The listening address of the sidecar container. No need to modify.

For example, if you want to change the sidecar log level of the workload __productpage-v1-5b4f8f9b9f-8q9q2__
in the __default__ namespace to __debug__ , you would run the following command:

```shell
kubectl -n default exec -it productpage-v1-5b4f8f9b9f-8q9q2  -c istio-proxy -- curl -X POST localhost:15000/logging?level=debug
```

After executing the command, you can click the Logs button to verify if the sidecar log level has been successfully modified.

![image](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/sidecar-log-level-04.png)
