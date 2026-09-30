# Sidecar Lifecycle

The lifecycle of a sidecar includes startup, running, and termination.

## Sidecar Startup

Let's first look at the startup process of a Pod with an injected sidecar.
First, you need to know that in the service mesh, the sidecar proxy is technically implemented with Envoy,
but the sidecar proxy container does not only run the Envoy process. In fact, a process called pilot-agent also runs in the sidecar proxy container.
pilot-agent roughly plays the following roles:

- Generates the bootstrap configuration for Envoy and starts Envoy
- Health check of the proxy container
- Updates certificates for Envoy
- Terminates Envoy

As you can see, pilot-agent basically plays the role of managing the lifecycle of the Envoy proxy.
Starting Envoy is a very important responsibility of pilot-agent. pilot-agent prepares the bootstrap configuration for the Envoy
proxy (that is, the BOOTSTRAP part in config_dump) and starts the Envoy process.
Take any Pod YAML with an injected sidecar:

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

We can see the various parameters used by pilot-agent when starting Envoy.

### HoldApplicationUntilProxyStarts

Now let's see what we can configure for the sidecar when a Pod starts: for the sidecar container, our ideal state is to ensure that the sidecar container has already started before the business container starts.
In fact, we can achieve this through two Kubernetes mechanisms:

1. When a Pod starts, the containers in the Pod start in the order declared in the YAML.
2. We can [define a lifecycle in the Pod YAML](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/).
   The lifecycle contains the postStart and preStop fields. After a container is started, if the container declaration contains lifecycle.postStart,
   the instructions declared in postStart will be run, and the next container will only be started after the instructions finish running.

The sidecar proxy configuration item HoldApplicationUntilProxyStarts is used for this. This configuration item is a boolean switch. When it is enabled, the sidecar injector will do two things:

1. Ensure the sidecar container is declared first among all containers in the Pod.
2. Add a lifecycle declaration with postStart to the sidecar container as follows:

```yaml
lifecycle:
  postStart:
    exec:
      command:
      - pilot-agent
      - wait
```

The instruction `pilot-agent wait` declared in postStart means to let pilot-agent keep waiting until the Envoy process has finished starting.
Through the above two steps, we can ensure the lifecycle of the sidecar when the Pod starts, without affecting the traffic of the business container.
In the service mesh, HoldApplicationUntilProxyStarts is enabled globally by default, and we also recommend enabling it by default to ensure a correct startup lifecycle.

However, when a large number of Pods start at the same time in the environment, Envoy may start too slowly due to excessive pressure on the control plane/API Server.
In this extreme case, the postStart instruction may last too long and cause the entire Pod to fail to start. In this case,
you can also consider temporarily disabling HoldApplicationUntilProxyStarts to ensure the Pod can start normally first.

## Sidecar Termination

When a Pod stops, the situation may be a bit more complicated. For a Pod, roughly the following things happen:

1. Kubelet sends a SIGTERM signal to all containers in the Pod at the same time.
2. If the preStop field is configured in the lifecycle of a container, Kubelet will not send the SIGTERM signal immediately,
   but will first execute the instructions declared in preStop, and then send the SIGTERM signal after the instructions are completed.
3. After receiving the SIGTERM signal, the container enters its own termination logic.

For the sidecar container, pilot-agent will receive the SIGTERM signal and start processing its logic to stop Envoy, so its termination process is as follows.

1. If a preStop instruction is declared in the lifecycle of the sidecar container, the preStop instruction will be executed first.
2. After the preStop instruction is completed, Kubelet sends a SIGTERM signal to the sidecar container.
3. After receiving the stop signal, pilot-agent enters the termination logic. At this time, pilot-agent will first post a request to this path of the Envoy process:
   `localhost:15000/drain_listeners?inboundonly&graceful`. After receiving this request,
   Envoy will stop listening on all inbound ports and no longer accept new connections and requests, but it can still continue to process existing requests.
   The graceful parameter in the request path can [make Envoy interrupt listening in as graceful a way as possible](https://github.com/envoyproxy/envoy/pull/11639).
4. pilot-agent will then sleep for a period of time (this interval can be customized by the sidecar proxy configuration item terminationDrainDuration)
5. After the sleep ends, pilot-agent will forcibly stop the Envoy process, and the Sidecar container is officially stopped.

### TerminationDrainDuration

As just mentioned, when a Pod stops, after sending a request to Envoy to stop accepting new requests, pilot-agent will sleep for a period of time before stopping the Envoy process.
The significance of this sleep period is that during this period, the Envoy process will not accept new requests but can still process existing requests. This period can serve as a "buffer time"
to let pilot-agent wait for Envoy to finish processing all existing requests before stopping, so that these existing requests will not be discarded out of thin air.
The sidecar proxy configuration item "sidecar proxy termination wait duration (TerminationDrainDuration)" is used to configure this sleep duration, and the default configuration is 5s.

In actual use, this TerminationDrainDuration often needs to be adjusted according to business needs. If, after receiving the SIGTERM signal,
the business container still needs a relatively long time to process existing requests, you often need to appropriately extend TerminationDrainDuration.
Otherwise, an awkward situation may occur where pilot-agent has finished sleeping but the existing requests have not been processed yet, and these existing requests will still be discarded.

### EXIT_ON_ZERO_ACTIVE_CONNECTIONS

From the above description, we can find that configuring TerminationDrainDuration itself still has certain limitations, because the lifecycle of Envoy
is still completely unrelated to the lifecycle of the business container. We can set a reasonable
TerminationDrainDuration based on observation of the business and production experience, but we can never guarantee that after pilot-agent sleeps for this period, the existing requests have really all been processed.
In the new version of the service mesh, the sidecar proxy provides a configuration item EXIT_ON_ZERO_ACTIVE_CONNECTIONS, which is passed in as an environment variable of the sidecar container.
The service mesh supports EXIT_ON_ZERO_ACTIVE_CONNECTIONS starting from version 1.15.3.104. You can find its corresponding option "wait for the number of sidecar connections to reach zero when terminating the Pod" on the console.
This configuration item is disabled by default. After it is enabled, step 4 in the above sidecar proxy stop process will change.
Originally:

> pilot-agent will then sleep for a period of time (this interval can be customized by the sidecar proxy configuration item terminationDrainDuration)

After EXIT_ON_ZERO_ACTIVE_CONNECTIONS is enabled:

> pilot-agent will first sleep for a period of time (this interval is changed to be set by the environment variable MINIMUM_DRAIN_DURATION, with a default of 5s),
> and after waking up, it will check every 1s whether there are still active connections on Envoy (this check is implemented by sending a stats query request
> `GET localhost:15000/stats?usedonly&filter=downstream_cx_active` to the Envoy management port;
> refer to [Istio PR 35059](https://github.com/istio/istio/pull/35059),
> [Envoy Listener statistic parameters](https://www.envoyproxy.io/docs/envoy/latest/configuration/listeners/stats)

It can be found that after EXIT_ON_ZERO_ACTIVE_CONNECTIONS is enabled, the biggest difference is that after pilot-agent wakes up, it will continuously query the current connection status of Envoy
at a period of 1s, and stop Envoy when there are no active connections. The number of active connections is undoubtedly a good indicator for judging when to stop
Envoy, at least better than the original crude sleep for TerminationDrainDuration. It should be noted that after EXIT_ON_ZERO_ACTIVE_CONNECTIONS is enabled, because the stop logic of pilot-agent changes,
the TerminationDrainDuration we set will no longer work. For the stop logic of pilot-agent, refer to the following:

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

### Customize preStop and postStart in the lifecycle

Note that the TerminationDrainDuration and EXIT_ON_ZERO_ACTIVE_CONNECTIONS we just discussed are all discussed in the ideal environment we assume.
The so-called assumed ideal environment means that we assume that neither the sidecar container nor the business container declares preStop in its lifecycle, and that the business container, like the sidecar container, enters the termination process after receiving SIGTERM.
However, in actual business processes, business containers often have a wide variety of lifecycles and cannot be generalized as an ideal situation. The most typical situation is, for example:
the business container defines its own lifecycle and needs to execute a preStop instruction before stopping, and during this period it still receives requests from the outside.
At this time, if the sidecar container does not set preStop and directly enters the termination process, requests coming during this period may fail to connect because Envoy has stopped listening.
When facing such situations, we can customize the lifecycle of the sidecar and implement the stop lifecycle logic of the sidecar by ourselves through the preStop declared in it,
so as to ensure as much as possible that the sidecar container can be well synchronized with the lifecycle of the business container. The service mesh provides a configuration item to customize the lifecycle of the sidecar container.
You can directly write a lifecycle in json format to override the lifecycle field of the sidecar container. As for the content of the custom lifecycle, you need to specify and write it according to the specific business situation.
By default, if you have enabled HoldApplicationUntilProxyStarts, the sidecar injector will add the following lifecycle to the sidecar container by default:

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

In addition to the postStart mentioned above, a preStop with sleep 15 is also added by default, to ensure as much as possible that the sidecar terminates after the business container.
Of course, this preStop cannot directly adapt to all business scenarios, and it can be overridden through a custom lifecycle.
