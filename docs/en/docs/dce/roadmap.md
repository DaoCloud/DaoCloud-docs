---
hide:
  - toc
---

# DCE 5.0 Product Features Roadmap

This page lists the roadmap for the features of various modules in DCE 5.0 over the coming months.

!!! tip

    For development records from the past few years, refer to the [DCE 5.0 Release Notes](./dce-rn/20240830.md).
    If you have any suggestions or ideas, feel free to [submit an Issue](https://github.com/DaoCloud/DaoCloud-docs/issues).

<div class="grid cards" markdown>

-   :material-microsoft-azure-devops:{ .lg .middle } __Workbench__

    ---

    - Improve R&D efficiency by displaying more dimensional statistical analysis on the overview panel
    - Save application templates (Helm Chart)
    - Add more custom steps and custom templates

    [:octicons-arrow-right-24: View Workbench Release Notes](../amamba/intro/release-notes.md)

-   :octicons-container-16:{ .lg .middle } __Containers__

    ---

    - Support GPU Volcano scheduling policy
    - Promote [Hami](../community/hami.md) to implement vGPU quotas, support secondary scheduling of GPU nodes, dynamic application for GPU resources, etc.
    - Support DRA networking

    [:octicons-arrow-right-24: View Container Release Notes](../kpanda/intro/release-notes.md)

-   :material-train-car-container:{ .lg .middle } __Virtual Machines__

    ---

    - Provide a virtual machine dashboard to intuitively reflect the status and resource usage of virtual machines
    - Support configuration for the liveliness and availability health checks of virtual machines
    - Support virtual machine backups

    [:octicons-arrow-right-24: View Virtual Machine Release Notes](../virtnest/intro/release-notes.md)

-   :material-engine:{ .lg .middle } __Microservices__

    ---

    - Version management for microservice gateway APIs
    - Provide instance-level black and white lists for microservice gateways

    [:octicons-arrow-right-24: View Microservices Release Notes](../skoala/intro/release-notes.md)

-   :material-monitor-dashboard:{ .lg .middle } __Insight__

    ---

    - Display full-link span data
    - Support custom log collection configuration and log de-sensitization
    - Alerts support sending to different users based on various labels such as cluster and namespace levels

    [:octicons-arrow-right-24: View Insight Release Notes](../insight/intro/release-notes.md)

-   :material-slot-machine:{ .lg .middle } __AI Lab__

    ---

    - Multi-modal large model agent workflow orchestration
    - LLMOps model inference service gateway

    [:octicons-arrow-right-24: View AI Lab Release Notes](../baize/intro/release-notes.md)

-   :fontawesome-brands-edge:{ .lg .middle } __Cloud Edge Collaboration__

    ---

    - Support CSI storage standards
    - Edge nodes support lightweight Pod operation capabilities (viewing and restarting Pods)
    - kantadm supports pre-container runtime initialization

    [:octicons-arrow-right-24: View Cloud-Edge Collaboration Release Notes](../kant/intro/release-notes.md)

-   :fontawesome-solid-user-group:{ .lg .middle } __Global Management__

    ---

    - In public cloud mode, create users under folders
    - Build a new version of the License Secret system

    [:octicons-arrow-right-24: View Global Management Release Notes](../ghippo/intro/release-notes.md)

</div>
