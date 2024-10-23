# 边车生命周期

边车的生命周期包括启动、运行和停止。

## 边车启动

我们首先来看一个注入边车的 Pod 在启动时的流程。
首先需要知道，在服务网格中，边车代理是以 Envoy 作为技术实现，
但边车代理容器中并非只有 Envoy 进程在运行。实际上，边车代理容器中还运行着一个叫做 pilot-agent 的进程。
pilot-agent 大概起到以下的这么几种作用：

- 为 Envoy 生成引导配置并启动 Envoy
- 代理容器的健康检查
- 为 Envoy 更新证书
- 终止 Envoy

可以看到其实 pilot-agent 基本就起着对 Envoy 代理进行生命周期管理的作用。
启动 Envoy 是 pilot-agent 的一个很重要的职责，pilot-agent 会为 Envoy
代理准备引导配置（也就是 config_dump 中的 BOOTSTRAP 部分），并启动 Envoy 进程。
随便找一个注入边车的 Pod YAML：

```yaml
apiVersion: v1
kind: Pod
metadata:
---
spec:
  containers:
    - args:
        - proxy
        - sidecar
        - --domain
        - $(POD_NAMESPACE).svc.cluster.local
        - --proxyLogLevel=warning
        - --proxyComponentLogLevel=misc:error
        - --log_output_level=default:info
        - --concurrency
        - "2"
---
name: istio-proxy
```

我们可以看到 pilot-agent 在启动 Envoy 时使用的各项参数。

### HoldApplicationUntilProxyStarts

现在看看我们在 Pod 启动时可以为边车配置什么：对于边车容器来说，我们理想的状态是要确保在业务容器启动之前、边车容器就已经启动完成了。
实际上，我们可以通过两个 Kubernetes 的机制来做到这件事情：

1. 在 Pod 启动时，Pod 中的容器是以在 YAML 中声明的顺序依次启动的。
2. 我们可以[在 Pod YAML 中定义 lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)。
   lifecycle 包含 postStart 和 preStop 两个字段，在启动一个容器后，若容器的声明中包含 lifecycle.postStart，
   则 postStart 中声明的指令会被运行，指令运行完毕后才会启动下一个容器。

边车代理配置项 HoldApplicationUntilProxyStarts 就是用来干这个的。该配置项是一个 bool 的开关，当此项开启时，边车注入器会做两件事情：

1. 保证边车容器的声明顺序位于 Pod 中所有容器的最前。
2. 为边车容器加入带有 postStart 的 lifecycle 声明如下：

```yaml
lifecycle:
  postStart:
    exec:
      command:
      - pilot-agent
      - wait
```

postStart 中声明的指令`pilot-agent wait`，其含义是让 pilot-agent 持续等待、直到 Envoy 进程启动完毕。
通过上述两步，我们就可以保证边车在 Pod 启动时的生命周期，不会影响业务容器的流量。
在服务网格中，HoldApplicationUntilProxyStarts 是默认在全局开启的，我们也推荐默认开启此项，以确保正确的启动生命周期。

然而，在环境中同时有大量 Pod 启动时，可能会因为控制面/ API Server 压力过大而造成 Envoy 启动过慢，
在这种极端情况下、postStart 指令可能持续时间过长并导致整个 Pod 启动失败。在这种情况下，
也可以考虑暂时关闭 HoldApplicationUntilProxyStarts，率先保证 Pod 可以正常启动。

## 边车终止

在 Pod 停止时，情况可能会更复杂一些，对于 Pod 来说，大概会发生下面的这些事情：

1. Kubelet 会同时向 Pod 中的所有容器发送 SIGTERM 信号。
2. 如果某个容器的 lifecycle 中配置了 preStop 字段，则 Kubelet 不会立即发送 SIGTERM 信号，
   而是先执行 preStop 中声明的指令，等待指令完成之后再发送 SIGTERM 信号。
3. 容器接受到 SIGTERM 信号后，会进入自己的停止逻辑。

对于边车容器来说，pilot-agent 会接受到 SIGTERM 信号，并开始处理其停止 Envoy 的逻辑，因此它的停止流程是这样的。

1. 如果边车容器的 lifecycle 中声明了 preStop 指令，则会先执行 preStop 指令。
2. preStop 指令执行完毕后，Kubelet 向边车容器发送 SIGTERM 信号。
3. pilot-agent 收到停止信号后，进入停止逻辑，此时，pilot-agent 会首先向 Envoy 进程的这个路径
   post 一个请求：`localhost:15000/drain_listeners?inboundonly&graceful`，在接收到这个请求后，
   Envoy 会停止所有入向端口的监听，不再接收新的连接和请求，但仍然可以继续处理存量的请求。
   请求路径中的 graceful 参数则可以[令 Envoy 以尽可能优雅的方式来中断监听](https://github.com/envoyproxy/envoy/pull/11639)。
4. pilot-agent 随后会 sleep 一段时间（这个时间间隔可以由边车代理配置项 terminationDrainDuration 来自定义）
5. 在 sleep 结束后，pilot-agent 会强制停止 Envoy 进程，Sidear 容器正式停止。

### TerminationDrainDuration

刚才提到，在 Pod 停止时、向 Envoy 发送请求停止接收新的请求后，pilot-agent 会 sleep 一段时间后再停止 Envoy 进程。
sleep 这段时间的意义在于：Envoy 进程在这段时间之内不会接收新的请求，但仍然可以处理存量的请求，这段时间就可以成为一段“缓冲时间”，
让 pilot-agent 等待 Envoy 处理完所有存量请求后再行停止，这样就不会让这些存量请求被凭空丢弃了。
边车代理配置项 “边车代理终止等待时长（TerminationDrainDuration）”就是用来配置这一段睡眠时长的，默认配置为 5s。

在实际使用中，往往需要根据业务需求调整这个 TerminationDrainDuration，如果在收到 SIGTERM 信号后，
业务容器还需要一段比较长的时间来处理存量的请求，则往往需要适当延长 TerminationDrainDuration，
否则可能发生 pilot-agent 已经 sleep 完了，存量请求还没处理完的尴尬情况，此时存量请求还是会被丢弃。

### EXIT_ON_ZERO_ACTIVE_CONNECTIONS

经过上面的描述，我们可以发现配置 TerminationDrainDuration 本身还是有一定的局限性的，因为 Envoy
的生命周期和业务容器的生命周期还是完全没有关系的。我们可以根据对业务的观察和生产经验来设定一个合理的
TerminationDrainDuration，但我们永远无法保证 pilot-agent 睡过了这段时间之后、存量的请求就真的都处理完了。
在新版本的服务网格中，边车代理提供了一个配置项 EXIT_ON_ZERO_ACTIVE_CONNECTIONS，该配置项是以边车容器的环境变量的形式传入的。
服务网格在 1.15.3.104 版本开始支持 EXIT_ON_ZERO_ACTIVE_CONNECTIONS，您可以在控制台上找到它对应的选项“终止 Pod 时等待边车连接数归零”。
此配置项默认关闭。在开启此项后，上述边车代理停止流程中的第 4 步将会发生变化。
原先：

> pilot-agent 随后会 sleep 一段时间（这个时间间隔可以由边车代理配置项 terminationDrainDuration 来自定义）

开启 EXIT_ON_ZERO_ACTIVE_CONNECTIONS 后：

> pilot-agent 会首先 sleep 一段时间（这个时间间隔改为由环境变量 MINIMUM_DRAIN_DURATION 来设定，默认为 5s），
> 睡醒后每隔 1s 时间，检测一次 Envoy 上是否还存在活跃的连接（这个检测是通过向 Envoy 的管理端口发送 stats 查询请求
> `GET localhost:15000/stats?usedonly&filter=downstream_cx_active`来实现的，
> 参考 [Istio PR 35059](https://github.com/istio/istio/pull/35059),
> [Envoy Listener 统计参数](https://www.envoyproxy.io/docs/envoy/latest/configuration/listeners/stats)

可以发现，在开启 EXIT_ON_ZERO_ACTIVE_CONNECTIONS 后，最大的区别在于 pilot-agent 睡醒后会以 1s
为周期不断查询当前 Envoy 的连接状态，当没有活跃的连接后再停止 Envoy。活跃连接数无疑是一个判断何时停止
Envoy 的良好指标，至少比原先粗暴地 sleep TerminationDrainDuration 的效果要来得好。
需要注意的是，当开启 EXIT_ON_ZERO_ACTIVE_CONNECTIONS 后，由于 pilot-agent 的停止逻辑发生改变，
我们设定的 TerminationDrainDuration 也就不好使了，pilot-agent 的停止逻辑参考如下：

```go
func (a *Agent) terminate() {
    log.Infof("Agent draining Proxy")
    e := a.proxy.Drain()
    if e != nil {
        log.Warnf("Error in invoking drain listeners endpoint %v", e)
    }
    // If exitOnZeroActiveConnections is enabled, always sleep minimumDrainDuration then exit
    // after min(all connections close, terminationGracePeriodSeconds-minimumDrainDuration).
    // exitOnZeroActiveConnections is disabled (default), retain the existing behavior.
    if a.exitOnZeroActiveConnections {
        log.Infof("Agent draining proxy for %v, then waiting for active connections to terminate...", a.minDrainDuration)
        time.Sleep(a.minDrainDuration)
        log.Infof("Checking for active connections...")
        ticker := time.NewTicker(activeConnectionCheckDelay)
        for range ticker.C {
            ac, err := a.activeProxyConnections()
            if err != nil {
                log.Errorf(err.Error())
                a.abortCh <- errAbort
                return
            }
            if ac == -1 {
                log.Info("downstream_cx_active are not available. This either means there are no downstream connection established yet" +
                         " or the stats are not enabled. Skipping active connections check...")
                a.abortCh <- errAbort
                return
            }
            if ac == 0 {
                log.Info("There are no more active connections. terminating proxy...")
                a.abortCh <- errAbort
                return
            }
            log.Infof("There are still %d active connections", ac)
        }
    } else {
        log.Infof("Graceful termination period is %v, starting...", a.terminationDrainDuration)
        time.Sleep(a.terminationDrainDuration)
        log.Infof("Graceful termination period complete, terminating remaining proxies.")
        a.abortCh <- errAbort
    }
    log.Warnf("Aborted proxy instance")
}
```

### 自定义 lifecycle 中的 preStop 与 postStart

需要注意到，我们在刚才讨论的 TerminationDrainDuration 与 EXIT_ON_ZERO_ACTIVE_CONNECTIONS 都是在我们假设的理想环境中讨论的。
所谓假设的理想环境，即是指我们假设边车容器与业务容器的 lifecycle 中都没有声明 preStop，且业务容器也和边车容器一样，在接到 SIGTERM 后就进入停止流程了。
然而在实际的业务流程中，业务容器往往有着五花八门的生命周期，不能以理想状况一概而论。最典型的状况就比如：
业务容器定义了自己的 lifecycle，需要在停止之前执行 preStop 指令，并且在这期间仍然接收了来自外部的请求。
此时如果边车容器不设定 preStop，直接进入停止流程，则在这段时间内过来的请求可能无法连接，因为 Envoy 已经停止监听了。
在面对类似这样的情况时，我们可以自定义边车的 lifecycle，通过声明里面的 preStop 来自行实现边车的停止生命周期逻辑，
尽可能保证边车容器能够和业务容器的生命周期有比较好的同步。服务网格提供了对边车容器的 lifecycle 进行自定义的配置项，
您可以直接编写 json 格式的 lifecycle 来对边车容器的 lifecycle 字段进行覆写。至于自定义 lifecycle 的内容则需要根据具体的业务情况来指定编写了。
在默认情况下，如果您开启了 HoldApplicationUntilProxyStarts，则边车注入器默认会为边车容器加入以下的 lifecycle：

```yaml
lifecycle:
  postStart:
    exec:
      command:
        - pilot-agent
        - wait
  preStop:
    exec:
      command:
        - /bin/sh
        - -c
        - sleep 15
```

除了上面提过的 postStart 外，还会默认加入一个 sleep 15 的 preStop，来尽可能地保证边车在业务容器之后终止。
当然，这个 preStop 无法直接适应所有的业务场景，可以通过自定义的 lifecycle 来覆盖它。
