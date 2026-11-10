---
MTPE: windsonsea
date: 2024-07-17
hide:
  - toc
---

# Features

Cloud Edge Collaboration extends cloud-native capabilities to the edge through an integrated
"end-edge-cloud" collaborative architecture. This approach helps enterprises rapidly expand
secure, flexible, efficient, and reliable edge cloud-native capabilities, making it widely
applicable in fields such as industrial Internet, Internet of Things (IoT), smart factories,
smart parks, smart retail, and more. The cloud side handles the registration, management,
and distribution of applications and configurations for edge nodes, while the edge side focuses
on running edge applications, achieving edge autonomy. The device side supports multi-protocol
terminal access and provides standard interfaces for device connectivity.

Cloud Edge Collaboration supports the following features:

| Feature | Description |
| --- | --- |
| **Edge Node Management** | Supports onboarding a vast number of edge nodes with automatically generated node configuration; offers token and certificate management methods; enables unified management, monitoring, and operation of nodes from the cloud. |
| **Edge Application/Model Management** | Packages applications or models as container images, uploads them to a container registry, and deploys them to edge nodes quickly; provides runtime data, events, and logs of deployed instances; containers improve portability and resource isolation and support CPU / GPU scheduling. |
| **Edge Device Management** | Supports connecting end devices to edge nodes over multiple protocols, and manages them uniformly from the cloud once connected. |
| **Edge Mesh** | Implements a closed loop of edge business traffic through service discovery and traffic proxy, solving communication problems between edge services in edge scenarios. |
| **Data Management** | Provides message routing with configurable rules; the platform forwards edge messages to the corresponding endpoints along the configured paths, enabling flexible data routing and stronger data security. |
| **Permission Management** | Offers three-level permission management (platform / folder / workspace) for fine-grained control; ensures resource sharing and isolation among different roles at multiple levels and guarantees resource security. |
| **Edge Control** | Provides resource scheduling, management, and O&M for edge nodes; full lifecycle management of applications and models; data collection with device protocol conversion; messaging and data channels supporting EventBus-to-REST and REST-to-EventBus / ServiceBus forwarding paths; bidirectional transfer of unstructured data such as images, videos, and files. |
