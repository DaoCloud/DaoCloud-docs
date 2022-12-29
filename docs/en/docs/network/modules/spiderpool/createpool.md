---
hide:
   - toc
---

# Create subnet and IP pool

This chapter describes how to create subnets and IP pools before creating workloads to use IP pools.

### Prerequisites

1. [SpiderPool successfully deployed. ](../../modules/spiderpool/install.md)
2. [Multus with Macvlan /SRI-OV has been successfully deployed. ](../../modules/multus-underlay/install.md)

### Interface operation

1. Log in to the platform UI, click `Container Management` to enter the `Cluster List`, select the cluster to be used to enter `Cluster Details` and select `Network Configuration` to enter the network configuration page.

    ![networkconfig01](../../images/networkconfig01.jpg)

2. Enter `Network Configuration` to confirm whether the subnet to be used has been created.

       - If the subnet to be used has been created by default, you can directly `create an IP pool`.
       - If the subnet to be used is not created by default, you can enter the page and click `Create Subnet`.

       ![Create Subnet](../../images/subnetcreate.jpg)

    ​ Parameter description:

    ​ - `IPv4/IPv6 Type`: the subnet type of the subnet to be created
    ​ - `Subnet`: The subnet segment that has been planned. If it is used with Macvlan, it corresponds to the network segment corresponding to the network interface/subinterface. Please confirm with the network administrator in advance
    ​ - `Gateway`: Enter the gateway corresponding to the subnet, please confirm with your network colleagues in advance
    ​ - `VLAN ID`: Enter the VLAN ID corresponding to the subnet

3. Click `Next` to enter `IP Selection`, enter the IP segment to be used (the above-mentioned IP in the subnet), and click `OK` to complete the creation of the subnet.

     ![Complete subnet creation](../../images/subnetcreate02.jpg)

     **Create IP pool** (optional)

     - If you need to strictly control IP, you can complete the creation of IP pool in advance.
     - If coarse-grained control of IP resources is adopted, there is no need to create an IP pool in advance.

4. Click the `subnet name` to be used to enter the subnet details page.

     ![Subnet Details](../../images/subnetlist.jpg)

5. Click `Create IP Pool` to enter the creation page, and enter the following parameters.

     - `Gateway`: `Gateway` inherits `Subnet Gateway` by default and can be modified.
     - `Custom Routing`: When users have special routing requirements, they can be customized based on IP pool granularity.
     - `Workload Affinity`: Enter a workload label (such as `app: workload01`). After the IP pool is created, it can only be selected by the corresponding workload to achieve the effect of a fixed IP pool.
     - `Node Affinity`: Enter the node label (such as `node:controller-1`). After the IP pool is created, the workload Pod needs to be scheduled to the corresponding node to use the created IP pool.
     - `Namespace Affinity`: After enabling it, you can select the corresponding namespace. After selecting, only workloads in the corresponding namespace can use the created IP pool.

     `Note`: When creating, do not add any affinity. The created IP pool is `shared IP pool`.

     ![Shared IP Pool](../../images/createippool01.jpg)

6. Click `Add IP`, select `IP start address` and `IP number` to join the IP pool, click `OK` to complete the IP addition, and click again to complete the creation of the IP pool.

     `Get IP rules`: Obtain the corresponding number of IPs in turn from the `IP start address`, if the IP segments are not consecutive IPs, skip the intermediate IPs and obtain them sequentially.

     ![Add IP](../../images/createippool02.jpg)

7. After the creation is complete [the workload can use the IP Pool](../../modules/spiderpool/usage.md)

### YAML creation

**YAML Create Subnet**

```yaml
apiVersion: spiderpool.spidernet.io/v1
kind: SpiderSubnet
metadata:
   name: default-v4-subnet
spec:
   gateway: 172.30.120.1
   ipVersion: 4
   ips:
   - 172.30.120.126-172.30.120.127 #The subnet IP has been planned, and the IP segment can be entered
       #Such as: 72.30.120.126-172.30.120.127 segment or a single IP such as: 172.30.120.126
   subnet: 172.30.120.0/21
   vlan: 0
```

Use Pod annotation `ipam.spidernet.io/ippool`

**YAML create IPPool**

```yaml
apiVersion: spiderpool.spidernet.io/v1
kind: SpiderIPPool
metadata:
   name: standard-ipv4-ippool
spec:
   ipVersion: 4
   subnet: 172.30.120.0/21
   ips:
   - 172.30.120.126-172.30.120.127 # Added to the IP in the subnet, you can enter the IP segment
          # Such as: 172.30.120.126-172.30.120.127 segment or a single IP such as: 172.30.120.126
```