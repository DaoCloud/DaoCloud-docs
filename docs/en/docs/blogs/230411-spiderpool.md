# Spiderpool: A new option for Calico's fixed application IP

![spiderpool](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/spiderpool.png)

**Calico is a set of open source network and network security solutions**, which is also an implementation of Kubernetes container network solution (CNI: Container Network Interface).
It is implemented based on pure three-layer routing of Linux. In some cases, users can announce the route of the Pod subnet to the gateway through the Calico BGP mode.
Clients from outside the cluster can access the Pod directly via the Pod's IP, while also preserving the client's source IP.

## Current Pain Points

In the Calico Underlay network mode, users also hope that the IP addresses of Deployment or StatefulSet type applications can be fixed or float in a specified IP range, because:

- The IP address of the Pod is often controlled by the firewall policy, and the firewall will only allow specific IP or target access within the IP range
- Traditional microservice applications directly use Pod IP for microservice registration
- In some cases, the service IP is a fixed IP and will not change

Calico can achieve Pod-level IP fixation by injecting annotations into Pods: `cni.projectcalico.org/ipAddrs`, but **we found the following deficiencies in use**:

- Fixed IP only takes effect at the Pod level, and has no effect on Deployment and StatefulSet types;
- The administrator needs to ensure that the annotation IPs of Pods do not overlap to avoid IP conflicts. Especially in large-scale clusters, it is difficult to troubleshoot conflicting IPs;
- The configuration and management of fixed IP addresses are cumbersome and not cloud-native.

## Solution: [Spiderpool](https://github.com/spidernet-io/spiderpool)

In response to the above deficiencies, we try to achieve this requirement through Spiderpool.
Spiderpool is a Kubernetes IPAM plug-in project, which is mainly designed for the IP address management requirements of the Underlay network.
Can be used by any CNI project compatible with third-party IPAM plugins. It mainly has the following characteristics:

- Can automatically allocate fixed IP addresses for Deployment and StatefulSet types, and achieve automatic expansion and contraction of the number of IP addresses with the number of replicas
- Manage and configure IP pools in the form of CRD, greatly reducing operation and maintenance costs
- Support for pods created by third-party controllers
- Support specifying different subnets for Pod multi-NICs

The following will introduce Spiderpool.

## Install Spiderpool

The following is the author's reference
[Spiderpool official document](https://spidernet-io.github.io/spiderpool/usage/get-started-calico/#configure-calico-bgp-optional) built a set
The Calico BGP mode is matched with the Spiderpool environment, and the topology of the network environment is as follows:

![spiderpool](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/spiderpool01.png)

Create a SpiderSubnet instance according to your own environment: nginx-subnet-v4, and experience Spiderpool's fixed IP and other features.

```none
[root@master ~]# kubectl get ss
NAME VERSION SUBNET ALLOCATED-IP-COUNT TOTAL-IP-COUNT
nginx-subnet-v4 4 10.244.0.0/16 0 25602
```

## Automatically fix the IP pool for the application

This feature supports automatically creating an IP pool from the SpiderSubnet(10.244.0.0/16) subnet and binding it to the application Pod. It also supports features such as fixed Pod IP and automatic expansion and contraction of the number of IP pools according to the number of replicas.

Using the Spiderpool automatic pool function, create two copies of the Nginx Deployment application:

```shell
   cat <<EOF | kubectl create -f -
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx
   spec:
     replicas: 2
     selector:
       matchLabels:
         app: nginx
     template:
       metadata:
         annotations:
           ipam.spidernet.io/subnet: '{"ipv4":["nginx-subnet-v4"]}'
           ipam.spidernet.io/ippool-ip-number: '+3'
         labels:
           app: nginx
       spec:
         containers:
         -name: nginx
           image: nginx
           imagePullPolicy: IfNotPresent
           ports:
           - name: http
             containerPort: 80
             protocol: TCP
```

- ipam.spidernet.io/subnet: Spiderpool randomly selects some IPs from the "nginx-subnet-v4" subnet to create a fixed IP pool and bind it to the application
- ipam.spidernet.io/ippool-ip-number: '+3' indicates that the total number of IPs in the IP pool is three more than the number of replicas, which solves the problem that temporary IPs are available when the application rolls out

When the application Deployment is created, an IP pool named auto-nginx-v4-eth0-452e737e5e12 is automatically created in Spiderpool,
and bound to the application. The IP range is: 10.244.100.90-10.244.100.95, and the number of pool IPs is 5:

```none
[root@master1 ~]# kubectl get po -o wide
NAME READY STATUS RESTARTS AGE IP NODE NOMINATED NODE READINESS GATES
nginx-644659db67-6lsmm 1/1 Running 0 12s 10.244.100.93 worker5 <none> <none>
nginx-644659db67-n7ttd 1/1 Running 0 12s 10.244.100.91 master1 <none> <none>

[root@master1 ~]# kubectl get sp
NAME VERSION SUBNET ALLOCATED-IP-COUNT TOTAL-IP-COUNT DEFAULT DISABLE
auto-nginx-v4-eth0-452e737e5e12 4 10.244.0.0/16 2 5 false false

[root@master ~]# kubectl get sp auto-nginx-v4-eth0-452e737e5e12 -o jsonpath='{.spec.ips}'
["10.244.100.90-10.244.100.95"]
```

The IP of the Pod is fixed in the automatic pool: auto-nginx-v4-eth0-452e737e5e12(10.244.100.90-10.244.100.95), and the IP of the restarted Pod is also fixed in this range:

```none
[root@master1 ~]# kubectl get po -o wide
NAME READY STATUS RESTARTS AGE IP NODE NOMINATED NODE READINESS GATES
nginx-644659db67-szgcg 1/1 Running 0 23s 10.244.100.90 worker5 <none> <none>
nginx-644659db67-98rcg 1/1 Running 0 23s 10.244.100.92 master1 <none> <none>
```

Expand the copy, the IP address of the new copy is automatically allocated from the automatic pool: auto-nginx-v4-eth0-452e737e5e12(10.244.100.90-10.244.100.95), and the IP pool automatically expands with the number of copies:

```none
[root@master1 ~]# kubectl scale deploy nginx --replicas 3 # scale pods
deployment.apps/nginx scaled

[root@master1 ~]# kubectl get po -o wide
NAME READY STATUS RESTARTS AGE IP NODE NOMINATED NODE READINESS GATES
nginx-644659db67-szgcg 1/1 Running 0 1m 10.244.100.90 worker5 <none> <none>
nginx-644659db67-98rcg 1/1 Running 0 1m 10.244.100.92 master1 <none> <none>
nginx-644659db67-brqdg 1/1 Running 0 10s 10.244.100.94 master1 <none> <none>

[root@master1 ~]# kubectl get sp
NAME VERSION SUBNET ALLOCATED-IP-COUNT TOTAL-IP-COUNT DEFAULTDISABLE
auto-nginx-v4-eth0-452e737e5e12 4 10.244.0.0/16 3 6 false false
```

## Manually specify the IP pool

In some cases, users want to directly apply IP allocation from a fixed IP range instead of being randomly allocated by Spiderpool. The following will demonstrate this function:

Create IP pool:

```shell
cat << EOF | kubectl apply -f -
apiVersion: spiderpool.spidernet.io/v2beta1
kind: SpiderIPPool
metadata:
   name: nginx-v4-ippool
   spec:
     ipVersion: 4
     subnet: 10.244.0.0/16
     ips:
     - 10.244.120.10-10.244.120.20
```

spec.subnet indicates which subnet the IP pool belongs to

spec.ips Fixed IP address range, the range is 10.244.120.10-10.244.120.20, a total of 10 IPs

Manually specify the IP pool via the annotation `ipam.spidernet.io/ippool`: nginx-v4-ippool, create an application: nginx-m:

```shell
   cat <<EOF | kubectl create -f -
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx-m
   spec:
     replicas: 2
     selector:
       matchLabels:
         app: nginx
     template:
       metadata:
         annotations:
          ipam.spidernet.io/ippool: '{"ipv4":["nginx-v4-ippool"]}'
         labels:
           app: nginx
       spec:
         containers:
         -name: nginx
           image: nginx
           imagePullPolicy: IfNotPresent
           ports:
           - name: http
             containerPort: 80
             protocol: TCP
```

Spiderpool allocates two IPs from the nginx-v4-ippool pool and binds them to the application. Regardless of whether the Pod is restarted or expanded, the IP is still allocated from the pool to achieve the effect of a fixed IP:

```none
[root@master1 ~]# kubectl get po -o wide | grep nginx-m
NAME READY STATUS RESTARTS AGE IP NODE NOMINATED NODE READINESS GATES
nginx-m-7c879df6bc-26dcq 1/1 Running 0 23s 10.244.120.12 worker5 <none> <none>
nginx-m-7c879df6bc-nwdtp 1/1 Running 0 23s 10.244.120.14 master1 <none> <none>

[root@master1 ~]# kubectl get sp
NAME VERSION SUBNET ALLOCATED-IP-COUNT TOTAL-IP-COUNT DEFAULT DISABLE
auto-nginx-v4-eth0-452e737e5e12 4 10.244.0.0/16 3 6 false false
nginx-v4-ippool 4 10.244.0.0/16 2 11 false false
```

## in conclusion

After testing: clients outside the cluster can directly access through the IP of Nginx Pod normally, and the internal communication of Nginx Pod within the cluster also communicates normally across nodes (including across Calico subnets).
In the Calico underlay scenario, we can use Spiderpool to easily help us realize the fixed IP requirements of Deployment and other types of applications, which also provides a new option for this scenario.

For more features, please refer to [Spiderpool Official Documentation](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/).

[Learn about DCE 5.0 Cloud Native Networking](../network/intro/index.md){ .md-button }

[Download DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/index.md){ .md-button .md-button--primary }
[Free Trial](../dce/license0.md){ .md-button .md-button--primary }
