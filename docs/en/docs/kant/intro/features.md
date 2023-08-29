# Functional Features

Cloud-edge collaboration extends cloud-native capabilities to the edge through an integrated "end-edge-cloud" collaborative architecture, helping enterprises quickly expand secure, flexible, efficient, and reliable edge cloud-native capabilities,
widely applicable to industrial Internet, Internet of Things (IoT), smart factories, smart parks, smart retail, and other fields. The cloud side implements the registration, management, and distribution of applications and configurations of edge nodes, while the edge side is responsible for running edge applications, achieving edge autonomy. Device side supports multi-protocol terminal access and provides standard interfaces to connect with devices.

The functional architecture of the edge computing platform is shown in the following figure:

## Features

Cloud-edge collaboration supports the following functional features:

### Edge Node Management

Supports accessing a massive number of edge nodes, automatically generating configuration information for edge nodes in the platform, and supporting two efficient and convenient management methods: online and offline node management. Edge nodes can be managed, monitored, and operated uniformly on the cloud side.

### Edge Application/Model Management

- The edge computing platform supports deploying edge applications or models quickly to edge nodes in the form of containers.
  Users can package their own edge application programs or models into container images, upload them to the container registry, and then deploy container images to edge nodes for operation through the cloud-edge collaboration platform.
- The cloud-edge collaboration platform supports viewing running data, events, and log information of deployed instances.
- Containers have a more robust ecosystem, helping users' container applications seamlessly transition to other running environments, having better portability,
  and containers have better resource isolation and support CPU scheduling.

### Edge Device Management

The edge computing platform supports terminal devices connected to edge nodes, and terminal devices support access through Modbus protocol. After the terminal device is connected, it can be managed uniformly on the cloud side.

### Data Management

The edge computing platform provides message routing function. Users can configure message routing rules, and the platform forwards edge messages to the corresponding message endpoints according to the configured message routing,
flexibly controlling data routing and improving data security.

### Permission Management

The platform provides three-level permission management for platform/folders/workspaces, ensuring resource sharing and isolation among different roles at multiple levels and fully ensuring resource security.

### Edge Control

- Provides resource scheduling and management operation and maintenance functions for edge nodes.
- Provides full-life-cycle management of applications and models running on edge nodes.
- Provides data collection function and supports device protocol conversion, which can collect data from associated devices connected to edge nodes.
- Provides messaging and data transmission channels, supporting EventBus protocol for transmitting edge messages to cloud-side REST protocols and cloud-side REST protocols to edge-side EventBus/ServiceBus protocols, while also supporting bidirectional transmission of unstructured data such as images, videos, files, etc.
