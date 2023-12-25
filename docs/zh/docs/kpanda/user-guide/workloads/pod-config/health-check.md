# 容器的健康检查

容器健康检查根据用户需求，检查容器的健康状况。配置后，容器内的应用程序入如果异常，容器会自动进行重启恢复。Kubernetes 提供了存活（Liveness）检查、就绪（Readiness）检查和启动（Startup）检查。

- **存活检查（LivenessProbe）** 可探测到应用死锁（应用程序在运行，但是无法继续执行后面的步骤）情况。 重启这种状态下的容器有助于提高应用的可用性，即使其中存在缺陷。

- **就绪检查（ReadinessProbe）** 可探知容器何时准备好接受请求流量，当一个 Pod 内的所有容器都就绪时，才能认为该 Pod 就绪。 这种信号的一个用途就是控制哪个 Pod 作为 Service 的后端。 若 Pod 尚未就绪，会被从 Service 的负载均衡器中剔除。

- **启动检查（StartupProbe）** 可以了解应用容器何时启动，配置后，可控制容器在启动成功后再进行存活性和就绪态检查， 确保这些存活、就绪探测器不会影响应用的启动。 启动探测可以用于对慢启动容器进行存活性检测，避免它们在启动运行之前就被杀掉。

## 存活和就绪检查

存活检查（LivenessProbe）的配置和就绪检查（ReadinessProbe）的配置参数相似， 唯一区别是要使用 __readinessProbe__ 字段，而不是 __livenessProbe__ 字段。

**HTTP GET 参数说明：**

| 参数                             | 参数说明                                                     |
| -------------------------------- | ------------------------------------------------------------ |
| 路径（ Path）                    | 访问的请求路径。如： 示例中的 /healthz  路径                 |
| 端口(Port)                       | 服务监听端口。 如： 示例中的 8080 端口                     |
| 协议                             | 访问协议，Http 或者Https                                     |
| 延迟时间（initialDelaySeconds）  | 延迟检查时间，单位为秒，此设置与业务程序正常启动时间相关。例如，设置为30，表明容器启动后30秒才开始健康检查，该时间是预留给业务程序启动的时间。 |
| 超时时间（timeoutSeconds）       | 超时时间，单位为秒。例如，设置为10，表明执行健康检查的超时等待时间为10秒，如果超过这个时间，本次健康检查就被视为失败。若设置为0或不设置，默认超时等待时间为1秒。 |
| 超时时间（timeoutSeconds）       | 超时时间，单位为秒。例如，设置为10，表明执行健康检查的超时等待时间为10秒，如果超过这个时间，本次健康检查就被视为失败。若设置为0或不设置，默认超时等待时间为1秒。 |
| 成功阈值（successThreshold）     | 探测失败后，被视为成功的最小连续成功数。默认值是 1，最小值是 1。存活和启动探测的这个值必须是 1。 |
| 最大失败次数（failureThreshold） | 当探测失败时重试的次数。存活探测情况下的放弃就意味着重新启动容器。就绪探测情况下的放弃 Pod 会被打上未就绪的标签。默认值是 3。最小值是 1。 |

### 使用 HTTP GET 请求检查

**YAML 示例：**

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: liveness
  name: liveness-http
spec:
  containers:
  - name: liveness
    image: k8s.gcr.io/liveness
    args:
    - /server
    livenessProbe:
      httpGet:
        path: /healthz  # 访问的请求路径
        port: 8080  # 服务监听端口
        httpHeaders:
        - name: Custom-Header
          value: Awesome
      initialDelaySeconds: 3  # kubelet 在执行第一次探测前应该等待 3 秒
      periodSeconds: 3   #kubelet 每隔 3 秒执行一次存活探测
```

按照设定的规则，Kubelet 向容器内运行的服务（服务在监听 8080 端口）发送一个 HTTP GET 请求来执行探测。如果服务器上 __/healthz__ 路径下的处理程序返回成功代码，则 kubelet 认为容器是健康存活的。 如果处理程序返回失败代码，则 kubelet 会杀死这个容器并将其重启。返回大于或等于 200 并且小于 400 的任何代码都标示成功，其它返回代码都标示失败。 容器存活期间的最开始 10 秒中， __/healthz__ 处理程序返回 200 的状态码。 之后处理程序返回 500 的状态码。

### 使用 TCP 端口检查

**TCP 端口参数说明：**

| 参数                            | 参数说明                                                     |
| ------------------------------- | ------------------------------------------------------------ |
| 端口(Port)                      | 服务监听端口。 如： 示例中的 8080 端口                     |
| 延迟时间（initialDelaySeconds） | 延迟检查时间，单位为秒，此设置与业务程序正常启动时间相关。例如，设置为30，表明容器启动后30秒才开始健康检查，该时间是预留给业务程序启动的时间。 |
| 超时时间（timeoutSeconds）      | 超时时间，单位为秒。例如，设置为10，表明执行健康检查的超时等待时间为10秒，如果超过这个时间，本次健康检查就被视为失败。若设置为0或不设置，默认超时等待时间为1秒。 |

对于提供TCP通信服务的容器，基于此配置，按照设定规则集群对该容器建立TCP连接，如果连接成功，则证明探测成功，否则探测失败。选择TCP端口探测方式，必须指定容器监听的端口。

**YAML 示例：**

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

此示例同时使用就绪和存活探针。kubelet 在容器启动 5 秒后发送第一个就绪探测。 尝试连接 __goproxy__ 容器的 8080 端口， 如果探测成功，这个 Pod 会被标记为就绪状态，kubelet 将继续每隔 10 秒运行一次检测。

除了就绪探测，这个配置包括了一个存活探测。 kubelet 会在容器启动 15 秒后进行第一次存活探测。 就绪探测会尝试连接 __goproxy__ 容器的 8080 端口。 如果存活探测失败，容器会被重新启动。

### 执行命令检查

**YAML 示例:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: liveness
  name: liveness-exec
spec:
  containers:
  - name: liveness
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
      initialDelaySeconds: 5 # kubelet 在执行第一次探测前等待 5 秒
      periodSeconds: 5  #kubelet 每 5 秒执行一次存活探测
```

 __periodSeconds__ 字段指定了 kubelet 每 5 秒执行一次存活探测， __initialDelaySeconds__ 字段指定 kubelet 在执行第一次探测前等待 5 秒。按照设定规则，集群周期性的通过 kubelet 在容器内执行命令 __cat /tmp/healthy__ 来进行探测。 如果命令执行成功并且返回值为 0，kubelet 就会认为这个容器是健康存活的。 如果这个命令返回非 0 值，kubelet 会杀死这个容器并重新启动它。

### 使用启动前检查保护慢启动容器

有些应用在启动时需要较长的初始化时间，需要使用相同的命令来设置启动探测，针对 HTTP 或 TCP 检测，可以通过将 __failureThreshold * periodSeconds__ 参数设置为足够长的时间来应对启动需要较长时间的场景。

**YAML 示例：**

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

如上设置，应用将有最多 5 分钟（30 * 10 = 300s）的时间来完成启动过程， 一旦启动探测成功，存活探测任务就会接管对容器的探测，对容器死锁作出快速响应。 如果启动探测一直没有成功，容器会在 300 秒后被杀死，并且根据 __restartPolicy__ 来 执行进一步处置。
