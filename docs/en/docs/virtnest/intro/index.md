---
MTPE: windsonsea
Date: 2024-04-24
hide:
  - toc
---

# What is Virtual Machine (Virtnest)?

Virtnest is a technology based on KubeVirt that allows virtual machines to be managed as
cloud native applications, seamlessly integrating with containers. This enables users to
easily deploy virtual machine applications and enjoy a smooth experience similar to
containerized applications.

Here are the general steps to use Virtnest:

1. [Install the virtnest-agent component](../install/virtnest-agent.md) within the cluster.
2. [Build the required virtual machine images](../vm-image/index.md) and push them to
    Docker Registry or another image repository.
3. [Create virtual machines using the images](../vm/index.md) or [create virtual machines using YAML](../vm/index.md#yaml).
4. [Access the virtual machines](../vm/access.md) via VNC/console.
5. View the list of virtual machines and detailed information about each one.
6. Perform necessary operations such as start/stop, restart, clone, [snapshot](../vm/snapshot.md),
   restore from snapshot, and [live migration](../vm/live-migration.md) as needed.

## Advantages of Virtnest

- Improved resource utilization: Virtnest leverages container images as the foundation for
  creating virtual machines, effectively enhancing resource utilization.
  Containerized virtual machines can run applications and configurations independently
  while sharing the host kernel and hardware resources, reducing resource wastage.

- Rapid deployment and scalability: With Virtnest, virtual machines can be rapidly deployed
  and scaled within Kubernetes clusters. By integrating images and containers, virtual machine
  startup time is reduced, and the number of virtual machines can be dynamically adjusted
  according to demand. This flexibility enhances resource allocation efficiency and system performance.

- Simplified management and operations: Virtnest simplifies the process of managing and operating
  virtual machines within Kubernetes clusters. Administrators can easily handle tasks such as startup,
  shutdown, configuration, and monitoring of virtual machines using cluster management tools.
  The streamlined management process reduces complexity and eases administrative burdens.

- Flexible application deployment: Deploying virtual machines as container images in Kubernetes clusters
  brings significant flexibility to application deployment. Users can conveniently package
  different applications and configurations into container images and quickly deploy them
  in the cluster using Virtnest. This agility enables agile and flexible application deployment.

- Seamless integration with the container ecosystem: Virtnest combines virtual machines with containers,
  seamlessly integrating them into existing container ecosystems within Kubernetes clusters. Users can
  leverage container networking, service discovery, load balancing, and other functionalities while
  seamlessly collaborating with other containerized applications.

With Virtnest, users can fully unleash the potential of Kubernetes clusters for efficient management
of virtualized infrastructure. We are committed to continuously optimizing and enhancing Virtnest's
containerization capabilities, providing users with a superior virtual machine management experience.

!!! note

    The Virtual Machine, __Virtnest__ , is a feature exclusive to the DCE 5.0 Enterprise Package (Standard, Advanced, and Platinum editions).
