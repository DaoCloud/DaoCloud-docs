# Hwameistor Local Storage System

Hwameistor is an HA local storage system for cloud native stateful workloads.

HwameiStor creates a local storage resource pool for centrally managing all disks such as HDD, SSD, and NVMe. It uses the CSI architecture to provide distributed services with local volumes, and provides data persistence capabilities for stateful cloud native workloads or components.

HwameiStor is an open source, lightweight, and cost-efficient local storage system that can replace expensive traditional SAN storage. The system architecture of HwameStor is as follows.

![cncf gophers](./images/cncf-gophers.png)

**HwameiStor is a [Cloud Native Computing Foundation](https://cncf.io/) sandbox project.**

HwameiStor is composed of five components:

- Local Disk Manager (LDM): used to simplify the management of disks on nodes. It can abstract the disk on a node into a resource for monitoring and management purposes. It's a daemon that will be deployed on each node, then detect the disk on the node, abstract it into local disk (LD) resources and save it to kubernetes.
- Local Storage: a cloud native local storage system provisions high performance and persistent LVM volume with local access to applications.
- Scheduler: automatically schedule the Pod to a correct node which is associated with HwameiStor volume. With the scheduler, the Pod does not need the NodeAffinity or NodeSelector field to select the node. A scheduler will work for both LVM and Disk volumes.
- admission-controller: a webhook that can automatically verify which pod uses the HwameiStor volume and help to modify the schedulerName to hwameistor-scheduler.
- DRBD (Distributed Replicated Block Device): It is composed of Linux kernel modules and related scripts to build high available clusters. It is implemented by image the entire device over the network, which can be thought of as a kind of network RAID.

[Go to HwameiStor repo](https://github.com/hwameistor/hwameistor){ .md-button }

[Go to HwameiStor website](https://hwameistor.io/){ .md-button }

<p align="center">
<img src="https://landscape.cncf.io/images/left-logo.svg" width="300"/>&nbsp;&nbsp;<img src="https://landscape.cncf.io/images/right-logo.svg" width="350"/>
<br/><br/>
HwameiStor enriches the <a href="https://landscape.cncf.io/?selected=hwamei-stor">CNCF CLOUD NATIVE Landscape.</a>
</p>
