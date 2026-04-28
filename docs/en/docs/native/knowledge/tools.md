# Tool Recommendations

This page lists some commonly used tools in the cloud native community to improve K8s user experience.

- [Exploring Kubernetes Solutions for "Noisy Neighbor" Scenarios](https://mp.weixin.qq.com/s/g28ett0Z5LR0sHTyOljCRg)

    A noisy neighbor problem occurs when one tenant's performance degrades due to another tenant's activities.
    Although Kubernetes provides CPU Manager, Device Plugin Manager, and Topology Manager to coordinate resource allocation and ensure optimal performance for critical workloads, it doesn't fundamentally solve the problem.
    Intel's RDT (Resource Allocation Technology) supports limiting non-critical workload access to shared resources by configuring corresponding RDT classes for three Kubernetes QoS levels.

- [How to Play with Application Resource Configuration in the FinOps Era](https://mp.weixin.qq.com/s/2ulduH_zKKcCsB64sVI0bg)

    Kubernetes schedules based on resource quotas applied by applications, so how to reasonably configure application resource specifications becomes the key to improving cluster utilization.
    The article shares how to correctly configure application resources based on the FinOps open source project Crane and how to promote resource optimization practices within the enterprise.

- [A New Way to Help Go Teams Use OpenTelemetry](https://gethelios.dev/blog/helping-go-teams-implement-opentelemetry-a-new-approach/)

    Implementing OTel in Go to send data to observability platforms is not simple. Go instrumentation requires a lot of manual operations.
    The Helios team developed a [new OTel Go instrumentation method](https://app.gethelios.dev/get-started) that combines Go AST and agent libraries, making it easy to implement and maintain.
    Also, for end users, this method is non-intrusive and easy to understand.

- [Why is the Experience of Debugging Applications in Kubernetes So Bad?](https://mp.weixin.qq.com/s/maI6Nu6r431LtGzrgq_6rg)

    What developers want: fast inner development loop, ability to use familiar IDE tools for local debugging; early bug detection to avoid entering Outer Loop too soon; in internal environments, collaboration between teams should not interfere with each other.
    To solve these pain points, the article introduces three tools: Kubernetes local development tool [Telepresence](https://github.com/telepresenceio/telepresence), cloud native collaborative development testing solution [KT-Connect](https://github.com/alibaba/kt-connect), and IDE-based cloud native application development tool [Nocalhost](https://github.com/nocalhost/nocalhost).

- [Building End-to-End Non-Intrusive Open Source Observability Solutions on K8s](https://mp.weixin.qq.com/s/HUFawiyv55Hi0aEoEPl6rA)

    [Odigos](https://github.com/keyval-dev/odigos) is an open source observability control plane that allows enterprises to create observability pipelines in minutes, integrating many third-party projects and open standards, reducing complexity of multiple observability software platforms and open source software solutions.
    It also allows applications to provide traces, metrics, and logs in minutes, importantly without modifying any code, completely non-intrusive.
