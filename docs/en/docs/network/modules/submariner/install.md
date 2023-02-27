---
MTPE: TODO
Revised: Jeanine-tw
Pics: TODO
Date: 2023-02-27
---

# Installing Submariner

This page describes how to install Submariner.

## Prerequisites

- Prepare at least two clusters, either by deploying submariner-k8s-broker in one of them or separately in the other cluster, with submariner-operator deployed in a subcluster of each join. The subclusters should be able to communicate properly with each other and with the clusters deployed by submariner-k8s-broke
- It is better not to restart the subnets of different subclusters, otherwise you need to enable the Globalnet feature, which has some limitations
- The list of supported CNIs is:
    * OpenShift-SDN
    * Weave
    * Flannel
    * Canal
    * Calico(there is a compatibility issue, you need to circumvent it manually, refer to [FAQ](subctl.md))
    * OVN (requires OVN NorthBound DB version > 6.1.0+)
- Kube-proxy mode must be `IPtables`, `IPvs` mode is not supported yet
- The cluster needs to allow `Vxlan` traffic internally and udp/4500 ports outside the cluster
> Submariner is in a relatively early stage, and bugs are common.

## Installation steps

!!! Note

    `submariner-k8s-broker` can be deployed in a single cluster or in a subcluster of Join. This article shows the installation process with `submariner-k8s-broker` deployed in a single cluster as an example.

Make sure your cluster is successfully connected to the `container management` platform, and then perform the following steps to first install `submariner-k8s-broker`. 1:

1. Click `Container Management` -> `Cluster List` in the left navigation bar, and then find the cluster name where you want to install `submariner-k8s-broker`. 2.

2. In the left navigation bar, select `Helm Applications` -> `Helm Templates`, find and click `submariner-k8s-broker`.

    ! [helm](... /... /images/submariner-k8s-broker-helm-repo.png)

3. Select the version you want to install in the version selection, and click Install. 4.

It is recommended to install it under the `submariner-k8s-broker` namespace.

    ! [broker-ns](... /... /images/submariner-k8s-broker-ns.png)

5. The configuration shown below does not need to be changed, just leave the default parameters as they are: !

    ! [config](... /... /images/submariner-k8s-broker-config.png)

6. Successfully install `submariner-k8s-broker` in the Broker cluster.

    ! [broker](... /... /images/submariner-k8s-broker-install.png)

7. Switch to its subcluster: master01 and install `submariner-operator`: !

    ! [operator](... /... /images/submariner-operator-helm-repo.png)

8. Select the version you want to install in the version selection, and click Install. 9.

9. Recommend installing under the `submariner-operator` namespace, turn on Ready to Wait: !

    ! [operator-ns](... /... /images/submariner-operator-ns.png)

10. Configure `submariner-operator` to connect to the Broker cluster:

    ! [operator-broker](... /... /images/submariner-operator-broker.png)

    The above parameter description:

    * ``Broker`` -> ``brokerK8sApiServer``: the address of the Broker Cluster API-Server, which can be obtained by.

        ```shell
        # On the cluster where submariner-k8s-broker is installed
        [root@broker ~]# kubectl -n default get endpoints kubernetes -o jsonpath="{.subsets[0].addresses[0].ip}:{.subsets[0].ports[? (@.name=='https')].port}"
        10.6.172.22:6443
        ```

    * `Broker` -> `brokerK8sCA`: client certificate to access the Broker cluster API-Server, which can be obtained by.

        ```shell
        # On the cluster where submariner-k8s-broker is installed
        [root@broker ~]# kubectl -n submariner-k8s-broker get secrets  -o jsonpath="{.items[?(@.metadata.annotations['kubernetes\.io/service-account\.name']=='submariner-k8s-broker-client')].data['ca\.crt']}"
        LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUMvakNDQWVhZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJek1ESXlNakV3TkRjek5Wb1hEVE16TURJeE9URXdORGN6TlZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBTVFLCmRVUHZoeDNOcFRXeGU0STZNV1I1VFU0VThJeVhBeWF6ZXJRRnhZK3l5Q3F1NnhFOUUwTDRSbUdxS0pyTFRSVWYKQi85YmowcWRaNFRJd2FTTmN3cGVqanYxYllTaVVKV0NsT0dXbTdLWUd4UnhCMEZFbVlCaGovT29HWGJhaEw5eQpqR1A1VjFsYTMxYlhONllSY0duR3hXMCt0QmE0RndhMGlUV3owd2R5dFE4cVpuMXdLUC9QMjNKZ0o1N1pwN3hOCmlLOHV6OENGRjZmTnkyNVJYeEV2cGRQdzEwcnJDM0Npem1mcjNaZHl0cGVFdk44U2V6STByMVNtVHBxSTM4UlEKZzVKdTFvV1NRcENEZjBPV1N5WUxxRno1NmU5dStPc0tyVXFzQkVsUkdKNWhvUGppVW9VN3I2N3lmSGl4TmdTcgpEM1I4aklSQzZITE5OTHE5UG8wQ0F3RUFBYU5aTUZjd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0hRWURWUjBPQkJZRUZDclJxaGJRNnV1aWFlOVJJd3RsdGd0bHhaRzhNQlVHQTFVZEVRUU8KTUF5Q0NtdDFZbVZ5Ym1WMFpYTXdEUVlKS29aSWh2Y05BUUVMQlFBRGdnRUJBSU5QUmtZMEpKSk5jNjFlVUpSOQo2bm9LTFl0cUN6VUxqRDVOZ3BmSy9GK0NvNk45Y0k5c0c1V1FVQ3ZMUVc5MUlFRlhFencvSEswUFBJTy8zVFpICjVQS05TUjR5d2hwSmtyeFRveDEvWWRqK2RWNzNGUnFKTFVuQkw1T3U4SWlKR2RNR0VKc040dnd5amk5TGt3WGMKcC9aUUVieWhLdmRvRWdOaDlhUzMrQzRJSVFnNmVqZTgvYVh6NTVaL2RoN2NZQUhCZWFQYmVwWU1kNklwc3VhTwo5Smx3TmJaSWczNHIzL3hQYjhCNUJOSkp2MXI3eE1YblFlaXc1MFNWaGdpR0JXMFdOdFo4NDVGREY2NHFzVFBsCjhLSjZOQkdjRUVuTHpDSXNhVUwxUHk4bk90K3NWWFNlUlhXV2VlWm84R0krWGpXQjZWL3FscnllSmp6Yy9hUU4KYWdBPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
        ```

    * `Broker` -> `brokerK8sApiServerToken`: the Token to access the Broker Cluster API-Server, which can be obtained by.

        ```shell
        # On the cluster where submariner-k8s-broker is installed
        [root@broker ~]# kubectl -n submariner-k8s-broker get secrets -o jsonpath="{.items[?(@.metadata.annotations['kubernetes\.io/service-account\.name']=='submariner-k8s-broker-client')].data.token}" | base64 --decode
        eyJhbGciOiJSUzI1NiIsImtpZCI6Ik1kUWpXalIwUVV0RmtTcjJXdElvMW1WWHdZbU5Md2pRN0tFeVZSbUpINTgifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJzdWJtYXJpbmVyLWs4cy1icm9rZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlY3JldC5uYW1lIjoic3VibWFyaW5lci1rOHMtYnJva2VyLWNsaWVudC10b2tlbiIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJzdWJtYXJpbmVyLWs4cy1icm9rZXItY2xpZW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiYzM0MzQ0MTItOTEyNi00NmFjLTk5ODUtZDgwYWI3MDAxOTdkIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OnN1Ym1hcmluZXItazhzLWJyb2tlcjpzdWJtYXJpbmVyLWs4cy1icm9rZXItY2xpZW50In0.quC7a3hTctbgaRKHmzAvlP16EspwtTzWzirgj0o2d9XYfVe6bPX29Wg4XHh3ZzetaMYmvj_toukQJcQ6bO1CG7xv4mOFFkLF2ECrQNPGKYa5A2LHgQCFiWteWjU7wcisW3lugMTC6a5OrbK4optvVjseLwqI-BClm8nsgjGocBTrv1qqDp-4aiPkLtgcZRV2bsgE3yLsyc7Mhuncs7gDmI2NuBXoYRGfXtAjd6XIbnXd5Tp5sAV_k92xruNqKDpzQZI32K6I7It1WNQvtGOTYHa9sks0gxgUmQu8Z9Pikke5LCFOMNcBbjwlCCxzg6jKWJH87ReMtenRqcfG2jNeTQ
        ```

        > Note that you need to perform decode

    * `Broker` -> `brokerK8sRemoteNamespace`: namespace of the submariner-k8s-broker component, default is submariner-k8s-broker (refer to step 4).
    * `Broker` -> `enableGloablnet`: Whether to enable the Globalnet feature. You can enable it if subclusters overlap with each other. 11.

11. configure `submariner-operator`.

    ![operator-install1](../../images/submariner-operator-install1.png)

    The above configuration notes:

    * `IPsec Configuration` -> `ceIPSecPSK`: Pre-shared key required for establishing IPsec tunnels. If higher security is required, it can be obtained using the following.

        ```shell
        [root@broker ~]# LC_CTYPE=C tr -dc 'a-zA-Z0-9' < /dev/urandom | fold -w 64 | head -n 1
        ZSMhkWz6EfO7zacMLCeYoKruYIm6iq1roNQKS8rKW8cQGJiYwDaYQNrzbbdP2azl
        ```

    * `Submariner` -> `clusterId`: Used to identify this subcluster, the fill specification needs to satisfy DNS-1123 Label.
    * `Submariner` -> `clusterCidr`: Fill in the CIDR of the subcluster Pod.

        ![operator-install2](../../images/submariner-opearator-install2.png)

    * `Submariner` -> `serviceCidr`: Fill in the CIDR of the subcluster Service.
    * `Submariner` -> `globalCidr`: Enables the globalnet feature.

        > Note: If you are not using the globalnet feature, do not configure this field.

    * `Image Configuration` -> `cableDriver`: tunnel mode, support `libreswan` (default), `wireguard`, `vxlan`.
    * `Image Configuration` -> `natEnabled`: whether to turn on the NAT feature between gateway nodes. If gateway nodes of different subclusters need to communicate across the public network, then enable it.

12. After the installation of subcluster master1 is complete.

    ![opearator-install-3](../../images/submariner-opearator-install-3.png)

13. After the installation is complete, you need to manually set one of the nodes of subcluster master1 as a gateway node and add the tag "submariner.io/gateway: true": !

    ![gateway](../../images/submariner-operator-gateway-label.png)

    ```shell
    root@controller-node-1:~# kubectl  get po -n submariner-operator
    NAME                                                     READY   STATUS      RESTARTS       AGE
    helm-operation-upgrade-submariner-operator-q79sp-9bkzl   0/1     Completed   0              31h
    submariner-gateway-jpclp                                 1/1     Running     18 (30m ago)   31h
    submariner-lighthouse-agent-589676874b-dn75z             1/1     Running     0              31h
    submariner-lighthouse-coredns-5d675b4897-tm752           1/1     Running     0              32h
    submariner-lighthouse-coredns-5d675b4897-wxr8z           1/1     Running     0              32h
    submariner-metrics-proxy-2ptmn                           2/2     Running     0              31h
    submariner-operator-75ccdf484-6862g                      1/1     Running     0              32h
    submariner-routeagent-kh4hp                              1/1     Running     0              31h
    ```

The subcluster master1 join is finished, install submariner in another subcluster in the same way.

## Caution

- After installation, you need to tag at least one node with "submariner.io/gateway: true". The Gateway component will only be installed if this tag is present.
- If the cluster CNI is Calico, some additional work is required to resolve compatibility issues with Calico, see [usage](usage.md).
