---
hide:
  - toc
---

# What is Virtual Machine (Virtnest)?

Virtnest is a technology based on KubeVirt that allows virtual machines to be managed as
cloud native applications, seamlessly integrating with containers. This enables users to
easily deploy virtual machine applications and enjoy a smooth experience similar to
containerized applications.

Here are the general steps to use Virtnest:

1. Install the virtnest-agent component within the cluster.
2. Build the required Virtual Machine images.
3. Push the images to a Docker Registry or other image repositories.
4. Create virtual machines using the images/YAML.
5. Access the virtual machines through VNC/console.
6. View the list of virtual machines and their details.
7. Perform operations such as power on/off, restart, clone, snapshot, restore snapshot,
   and live migration as needed.

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
