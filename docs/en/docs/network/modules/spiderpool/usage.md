---
hide:
   - toc
---

# Workloads use IP pools

This section mainly introduces the combination of Multus and the Underlay CNI plug-in to configure multiple NICs for the workload Pod, and to allocate and fix the IP of the Underlay network through Spiderpool. Mainly include:

- Pod set multi-container NIC
- Workloads use IP pools
- Workloads use fixed IP pools
- Workloads use auto-created fixed IP pools

## Prerequisites

1. [SpiderPool successfully deployed](../../modules/spiderpool/install.md).
2. [Multus with Macvlan/SRI-OV successfully deployed](../../modules/multus-underlay/install.md).
3. If you use manual selection of IP pool, please complete [IP subnet and IP pool created](../../modules/spiderpool/createpool.md) in advance. If you use automatic creation of a fixed IP pool, you only need to complete [IP pool created](../../modules/spiderpool/createpool.md) in advance.

## Steps

1. Log in to the platform UI, click `Container Management` to enter the `Cluster List`, click the corresponding cluster name to enter the `Cluster Details`, select the `Stateless Load` list, and click `Image Creation`.

     ![Image creation](../../images/useippool.jpg)

2. Enter the workload creation page, complete the input of `basic information`, `container configuration`, `service configuration` and other information, enter `advanced configuration` and click to configure `container NIC`.

     ![Container NIC](../../images/useippool02.jpg)

3. Enter the `Container Configuration` page, complete the input of relevant parameters, and click `Confirm` to complete the creation.

     `Network card information`: If the created application container needs to use multiple network cards (such as one for east-west communication and one for north-south communication), you can add multiple network cards.

     - eth0 (default NIC): Overlay CNI, Calico/Cilium is the default.

     - net1: Underlay CNI configuration can be selected, such as Macvlan/SRI-OV, the example in this article is Macvlan

     `IP Pool Configuration`: Rules for Underlay CNI IP allocation

     - `Create a fixed IP pool`: After enabling it, you only need to select the corresponding subnet for the newly added container NICs (net1, net2, net3). When the workload is deployed, a fixed IP pool is automatically created. After deployment, the container NIC can only use this IP addresses in the pool.
     - `Elastic IP`: After it is enabled, the number of IPs in the IP pool will change according to the number of elastic IPs set. The maximum number of available IPs is equal to the number of Pod copies + the number of elastic IPs. When the Pod expands, the IP pool will expand accordingly.
     - `Custom Routing`: When the application creates special routing requirements, you can add custom routes.
     - `Network card IP pool`: Select the subnet or the corresponding IP pool to be used by the corresponding network card.

     **Manually select an existing IP pool**

     To manually select an IP pool, you need to create an IP pool in advance. You can select the range of the IP pool as `shared IP pool`, add the current `application affinity IP pool`, and add the current `namespace affinity IP pool`.

     ![Manually select IP pool](../../images/useippool05.jpg)

     **Automatically create fixed IP pool**

     You only need to select the corresponding subnet to automatically create a fixed IP pool

     ![Automatically create fixed IP pool](../../images/useippool03.jpg)

     ![Automatically create fixed IP pool](../../images/useippool04.jpg)

4. After creating the workload, you can click the corresponding workload `workload01` to view the IP used by the workload Pod.

     ![View IP](../../images/useippool06.jpg)

     ![useippool07](../../images/useippool07.jpg)

## YAML usage

1. Use the Pod annotation `ipam.spidernet.io/ippool` to choose to allocate IP from the IP pool `testingippool` to create this Deployment.

     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: workload01
     spec:
       replicas: 3
       selector:
         matchLabels:
           app: workload01
       template:
         metadata:
           annotations:
             ipam.spidernet.io/ippool: |-
               {
                 "ipv4": ["testingippool"]
               }
           labels:
             app: workload01
         spec:
           containers:
           -name: workload01
             image: busybox
             imagePullPolicy: IfNotPresent
             command: ["/bin/sh", "-c", "trap : TERM INT; sleep infinity & wait"]
     ```

2. The Pods controlled by the Deployment `workload01` are assigned IP addresses from the IP pool `testingippool` and run successfully.

     ```bash
     kubectl get se
     NAME INTERFACE IPV4POOL IPV4 IPV6POOL IPV6 NODE CREATETION TIME
     workload01-6967dcd8df-8b6zp eth0 standard-ipv4-ippool 172.18.41.47/24 spider-worker 7s
     standard-ippool-deploy-6967dcd8df-cvq79 eth0 standard-ipv4-ippool 172.18.41.50/24 spider-worker 7s
     standard-ippool-deploy-6967dcd8df-s58x9 eth0 standard-ipv4-ippool 172.18.41.41/24 spider-worker 7s
     ```
