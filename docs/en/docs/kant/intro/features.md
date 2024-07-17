---
MTPE: windsonsea
date: 2024-07-17
hide:
  - toc
---

# Features

Cloud Edge Collaboration extends cloud-native capabilities to the edge through an integrated "end-edge-cloud" collaborative architecture. This approach helps enterprises rapidly expand secure, flexible, efficient, and reliable edge cloud-native capabilities, making it widely applicable in fields such as industrial Internet, Internet of Things (IoT), smart factories, smart parks, smart retail, and more. The cloud side handles the registration, management, and distribution of applications and configurations for edge nodes, while the edge side focuses on running edge applications, achieving edge autonomy. The device side supports multi-protocol terminal access and provides standard interfaces for device connectivity.

The functional architecture of the edge computing platform includes the following features:

## Edge Node Management

- Supports the integration of a vast number of edge nodes.
- Automatically generates configuration information for edge nodes within the platform.
- Offers two efficient and convenient management methods: online and offline node management.
- Allows for uniform management, monitoring, and operation of edge nodes from the cloud.

## Edge Application/Model Management

- Facilitates the rapid deployment of edge applications or models to edge nodes in the form of containers.
- Users can package their edge applications or models into container images, upload them to a container registry, and deploy these images to edge nodes via the Cloud Edge Collaboration platform.
- Supports the viewing of running data, events, and log information for deployed instances.
- Containers offer a robust ecosystem, aiding in the seamless transition of container applications to various running environments, enhancing portability.
- Containers provide better resource isolation and support CPU scheduling.

## Edge Device Management

- Supports the connection of end devices to edge nodes, with access through the Modbus protocol.
- Once connected, end devices can be uniformly managed from the cloud.

## Data Management

- Provides a message routing function, allowing users to configure message routing rules.
- The platform forwards edge messages to corresponding message endpoints based on the configured routing rules, enabling flexible data routing and enhancing data security.

## Permission Management

- Offers three-level permission management for platform/folders/workspaces.
- Ensures resource sharing and isolation among different roles at multiple levels, fully guaranteeing resource security.

## Edge Control

- Provides resource scheduling, management, and maintenance functions for edge nodes.
- Offers full life-cycle management of applications and models running on edge nodes.
- Includes data collection functions and supports device protocol conversion, enabling data collection from devices connected to edge nodes.
- Provides messaging and data transmission channels, supporting the EventBus protocol for transmitting edge messages to cloud-side REST protocols and vice versa.
- Supports bidirectional transmission of unstructured data such as images, videos, and files.
