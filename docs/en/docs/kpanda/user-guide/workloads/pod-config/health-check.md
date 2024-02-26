# container health check

Container health check checks the health status of containers according to user requirements. After configuration, if the application in the container is abnormal, the container will automatically restart and recover. Kubernetes provides Liveness checks, Readiness checks, and Startup checks.

- **LivenessProbe** can detect application deadlock (the application is running, but cannot continue to run the following steps). Restarting containers in this state can help improve the availability of applications, even if there are bugs in them.

- **ReadinessProbe** can detect when a container is ready to accept request traffic. A Pod can only be considered ready when all containers in a Pod are ready. One use of this signal is to control which Pod is used as the backend of the Service. If the Pod is not ready, it will be removed from the Service's load balancer.

- **Startup check (StartupProbe)** can know when the application container is started. After configuration, it can control the container to check the viability and readiness after it starts successfully, so as to ensure that these liveness and readiness probes will not affect the start of the application. Startup detection can be used to perform liveness checks on slow-starting containers, preventing them from being killed before they start running.

## Liveness and readiness checks

The configuration of LivenessProbe is similar to that of ReadinessProbe, the only difference is to use __readinessProbe__ field instead of __livenessProbe__ field.

**HTTP GET parameter description:**

| Parameter | Parameter Description |
| ----------------------------------- | ---------------- ----------------------------------------------- |
| Path (Path) | The requested path for access. Such as: /healthz path in the example |
| Port (Port) | Service listening port. Such as: port 8080 in the example |
| protocol | access protocol, Http or Https |
| Delay time (initialDelaySeconds) | Delay check time, in seconds, this setting is related to the normal startup time of business programs. For example, if it is set to 30, it means that the health check will start 30 seconds after the container is started, which is the time reserved for business program startup. |
| Timeout (timeoutSeconds) | Timeout, in seconds. For example, if it is set to 10, it indicates that the timeout waiting period for executing the health check is 10 seconds. If this time is exceeded, the health check will be regarded as a failure. If set to 0 or not set, the default timeout waiting time is 1 second. |
| Timeout (timeoutSeconds) | Timeout, in seconds. For example, if it is set to 10, it indicates that the timeout waiting period for executing the health check is 10 seconds. If this time is exceeded, the health check will be regarded as a failure. If set to 0 or not set, the default timeout waiting time is 1 second. |
| SuccessThreshold (successThreshold) | The minimum number of consecutive successes that are considered successful after a probe fails. The default value is 1, and the minimum value is 1. This value must be 1 for liveness and startup probes. |
| Maximum number of failures (failureThreshold) | The number of retries when the probe fails. Giving up in case of a liveness probe means restarting the container. Pods that are abandoned due to readiness probes are marked as not ready. The default value is 3. The minimum value is 1. |

### Check with HTTP GET request

**YAML example:**

```yaml
apiVersion: v1
kind: Pod
metadata:
   labels:
     test: liveness
   name: liveness-http
spec:
   containers:
   -name: liveness
     image: k8s.gcr.io/liveness
     args:
     - /server
     livenessProbe:
       httpGet:
         path: /healthz # Access request path
         port: 8080 # service listening port
         httpHeaders:
         - name: Custom-Header
           value: Awesome
       initialDelaySeconds: 3 # kubelet should wait 3 seconds before performing the first probe
       periodSeconds: 3 #kubelet performs a liveness detection every 3 seconds
```

According to the set rules, Kubelet sends an HTTP GET request to the service running in the container (the service is listening on port 8080) to perform the detection. The kubelet considers the container alive if the handler under the __/healthz__ path on the server returns a success code. If the handler returns a failure code, the kubelet kills the container and restarts it. Any return code greater than or equal to 200 and less than 400 indicates success, and any other return code indicates failure. The __/healthz__ handler returns a 200 status code for the first 10 seconds of the container's lifetime. The handler then returns a status code of 500.

### Use TCP port check

**TCP port parameter description:**

| Parameter | Parameter Description |
| -------------------------------- | ----------------- ----------------------------------------------- |
| Port (Port) | Service listening port. Such as: port 8080 in the example |
| Delay time (initialDelaySeconds) | Delay check time, in seconds, this setting is related to the normal startup time of business programs. For example, if it is set to 30, it means that the health check will start 30 seconds after the container is started, which is the time reserved for business program startup. |
| Timeout (timeoutSeconds) | Timeout, in seconds. For example, if it is set to 10, it indicates that the timeout waiting period for executing the health check is 10 seconds. If this time is exceeded, the health check will be regarded as a failure. If set to 0 or not set, the default timeout waiting time is 1 second. |

For a container that provides TCP communication services, based on this configuration, the cluster establishes a TCP connection to the container according to the set rules. If the connection is successful, it proves that the detection is successful, otherwise the detection fails. If you choose the TCP port detection method, you must specify the port that the container listens to.

**YAML example:**

```yaml
apiVersion: v1
kind: Pod
metadata:
   name: goproxy
   labels:
     app: goproxy
spec:
   containers:
   - name: goproxy
     image: k8s.gcr.io/goproxy:0.1
     ports:
     - containerPort: 8080
     readinessProbe:
       tcpSocket:
         port: 8080
       initialDelaySeconds: 5
       periodSeconds: 10
     livenessProbe:
       tcpSocket:
         port: 8080
       initialDelaySeconds: 15
       periodSeconds: 20

```

This example uses both readiness and liveness probes. The kubelet sends the first readiness probe 5 seconds after the container is started. Attempt to connect to port 8080 of the __goproxy__ container. If the probe is successful, the Pod will be marked as ready and the kubelet will continue to run the check every 10 seconds.

In addition to the readiness probe, this configuration includes a liveness probe. The kubelet will perform the first liveness probe 15 seconds after the container is started. The readiness probe will attempt to connect to the __goproxy__ container on port 8080. If the liveness probe fails, the container will be restarted.

### Run command check

**YAML example:**

```yaml
apiVersion: v1
kind: Pod
metadata:
   labels:
     test: liveness
   name: liveness-exec
spec:
   containers:
   -name: liveness
     image: k8s.gcr.io/busybox
     args:
     - /bin/sh
     - -c
     - touch /tmp/healthy; sleep 30; rm -f /tmp/healthy; sleep 600
     livenessProbe:
       exec:
         command:
         - cat
         - /tmp/healthy
       initialDelaySeconds: 5 # kubelet waits 5 seconds before performing the first probe
       periodSeconds: 5 #kubelet performs a liveness detection every 5 seconds
```

The __periodSeconds__ field specifies that the kubelet performs a liveness probe every 5 seconds, and the __initialDelaySeconds__ field specifies that the kubelet waits for 5 seconds before performing the first probe. According to the set rules, the cluster periodically executes the command __cat /tmp/healthy__ in the container through the kubelet to detect. If the command executes successfully and the return value is 0, the kubelet considers the container to be healthy and alive. If this command returns a non-zero value, the kubelet will kill the container and restart it.

### Protect slow-starting containers with pre-start checks

Some applications require a long initialization time at startup. You need to use the same command to set startup detection. For HTTP or TCP detection, you can set the __failureThreshold * periodSeconds__ parameter to a long enough time to cope with the long startup time scene.

**YAML example:**

```yaml
ports:
- name: liveness-port
   containerPort: 8080
   hostPort: 8080

livenessProbe:
   httpGet:
     path: /healthz
     port: liveness-port
   failureThreshold: 1
   periodSeconds: 10

startupProbe:
   httpGet:
     path: /healthz
     port: liveness-port
   failureThreshold: 30
   periodSeconds: 10
```

With the above settings, the application will have up to 5 minutes (30 * 10 = 300s) to complete the startup process. Once the startup detection is successful, the survival detection task will take over the detection of the container and respond quickly to the container deadlock. If the start probe has been unsuccessful, the container is killed after 300 seconds and further disposition is performed according to the __restartPolicy__ .