# Sidecar traffic passthrough

Traffic passthrough refers to the fact that all or part of the upstream and downstream traffic of the workload is directly sent to the workload itself without being forwarded by the sidecar.

The DCE 5.0 service mesh realizes the controllable sidecar passthrough of workload outbound/inbound traffic, and can implement interception settings for specific ports and IPs.

- Feature setting object: Workload
- Setting parameters: port, IP
- Flow direction: inbound, outbound

Istio applicable fields:

```none
traffic.sidecar.istio.io/excludeOutboundPorts
traffic.sidecar.istio.io/excludeOutboundIPRanges
```

**Operation process for enabling/disabling traffic passthrough**

```mermaid
graph TB

install[The workload has installed<br>a sidecar and restarted] -.Yes.-> config[Click traffic passthrough<br>Enable passthrough<br>Configure flow direction/IP/port parameters]
install -.-> inject[Sidecar injection] -.-> config
config --> restart1[Restart] --> effect[Passthrough setting takes effect]
--> delete[Click traffic passthrough<br>Delete all passthrough entries] --> restart2[Restart] --> disable[Passthrough disabled]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class install,config,inject,restart1,restart2,effect,delete plain;
class effect,disable k8s
```

## Enable traffic passthrough

1. Enter a mesh, click `Sidecar Management` -> `Workload Sidecar Management`.

    ![workload sidecar management](../../images/pn01.png)

1. Click `⋮` on the right side of a load, and select `Traffic passthrough Settings` in the pop-up menu.

    ![click menu item](../../images/pn02.png)

1. After setting the parameters of traffic passthrough, click `OK`.

    ![Traffic passthrough settings](../../images/pn03.png)

1. The screen prompts that the traffic passthrough setting is successful.

    ![Set successfully](../../images/pn04.png)
