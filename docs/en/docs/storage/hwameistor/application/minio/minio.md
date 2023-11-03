---
sidebar_position: 3
sidebar_label: "Minio"
---

#MinIO

## Introduction to MinIO

MinIO is a high-performance, distributed, S3-compatible multicloud object storage system suite. MinIO natively supports Kubernetes and can support all public cloud, private cloud and edge computing environments.
MinIO is a GNU AGPL v3 open source software-defined product that can run well on standard hardware such as x86 and other devices.

![MinIO Architecture](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/minio-design.png)

MinIO's architectural design has been aimed at private cloud standards with high performance requirements from the very beginning, pursuing the ultimate performance on the basis of realizing all the features required by object storage.
MinIO is easy to use, efficient, and high-performance, and can provide cloud native object storage services with elastic scalability in a simpler way.

MinIO performs well in traditional object storage use cases (such as auxiliary storage, disaster recovery, and archiving), and is also unique in storage technologies in machine learning, big data, private cloud, hybrid cloud, etc., including data analysis, high-performance application loads, native cloud applications, etc.

### MinIO architecture design

MinIO is designed for a cloud native architecture that can run as a lightweight container and be managed by an external orchestration service such as Kubernetes.
MinIO's entire service package is approximately less than 100 MB of static binaries, makes efficient use of CPU and memory resources even under heavy load, and can co-host a large number of tenants on shared hardware.
The corresponding architecture diagram is as follows:

![Architecture Diagram](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/architect.png)

MinIO is used as the main storage for cloud native applications. Compared with traditional object storage, cloud native applications require higher throughput and lower latency, and these are the performance metrics that MinIO can achieve. The read/write speed is as high as 183 GB/s and 171 GB/s.

The ultimate high performance of MinIO is inseparable from the underlying storage platform. Local storage has the highest read and write performance among many storage protocols, which undoubtedly provides performance guarantee for MinIO.
HwameiStor is exactly the storage system that meets the requirements of the cloud native era. It has the advantages of high performance, high availability, automation, low cost, and rapid deployment, and can replace expensive traditional SAN storage.

MinIO can run on standard servers with local drives (JBOD/JBOF).
The cluster is a fully symmetric architecture, meaning that all servers are functionally identical, there are no namenodes or metadata servers.

MinIO writes data and metadata together as objects eliminating the need for a metadata database.
MinIO performs all features in an inline, strictly consistent operation, including erasure codes, bit rotrot checks, encryption, and more.

Each MinIO cluster is a collection of distributed MinIO servers, one process per node.
MinIO runs as a single process in user space and uses lightweight coroutines to achieve high concurrency.
Drives are grouped into Scratch Sets (by default, 16 drives per group), and objects are placed on those Scratch Sets using a deterministic hashing algorithm.

MinIO is designed for large-scale, multi-datacenter cloud storage services.
Each tenant runs its own MinIO cluster that is completely isolated from other tenants, allowing tenants to be immune to any disruptions from upgrades, updates, and security incidents.
Each tenant scales independently by federating clusters across geographic regions.

![node-distribution-setup](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/node-setup.png)

### Advantages of using HwameiStor as the base to build MinIO

Using HwameiStor as the base to build a MinIO storage solution to build a smart, stable, and sensitive comprehensive enhanced local storage has the following advantages.

- Automated operation and maintenance management

   It can automatically discover, identify, manage, and allocate disks. Smart scheduling of applications and data based on affinity. Automatically monitor disk status and give timely warning.

- Highly available data

   Use cross-node replicas to synchronize data to achieve high availability. When a problem occurs, the application will be automatically scheduled to the high-availability data node to ensure the continuity of the application.

- Abundant data volume types

   Aggregate HDD, SSD, and NVMe disks to provide low-latency, high-throughput data services.

- Flexible and dynamic linear expansion

   It can be dynamically expanded according to the size of the cluster to flexibly meet the data persistence requirements of the application.

- Rich use cases, widely adapt to enterprise needs, and adapt to high-availability architecture middleware

   Middleware such as Kafka, ElasticSearch, and Redis have their own high-availability architecture, and at the same time have high requirements for IO access to data.
   The LVM-based single-copy local data volume provided by HwameiStor can well meet their requirements.

- Provide highly available data volumes for applications

   OLTP databases such as MySQL require the underlying storage to provide highly available data storage, which can quickly restore data when a problem occurs, and also require high-performance data access.
   The double-copy high-availability data volume provided by HwameiStor can well meet such needs.

- Automated operation and maintenance of traditional storage software

   MinIO, Ceph and other storage software need to use the disk on the Kubernetes node, which can be used in PVC/PV mode.
   Automatically use HwameiStor's single-copy local volume through the CSI driver, quickly respond to the deployment, expansion, migration and other requirements of the business system, and realize automatic operation and maintenance based on Kubernetes.

## test environment

Follow the steps below to deploy the Kubernetes cluster, HwameiStor local storage, and MinIO in sequence.

### Deploy the Kubernetes cluster

This test uses three virtual machine nodes to deploy a Kubernetes cluster: 1 Master + 2 Worker nodes, and the kubelet version is 1.22.0.

![k8s-cluster](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/k8s-cluster.png)

### Deploy HwameiStor local storage

Deploy HwameiStor local storage on Kubernetes.

![View HwameiStor local storage](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-get-hwamei-pod.png)

Each of the two Worker nodes is configured with five disks (SDB, SDC, SDD, SDE, SDF) for HwameiStor local disk management.

![lsblk](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/lsblk01.png)

![lsblk](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/lsblk02.png)

View local storage node status.

![get-lsn](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-get-lsn.png)

The storageClass is created.

![get-sc](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-get-sc.png)

## Distributed multi-tenant source deployment and installation (minio operator)

This section explains how to deploy minio operator, how to create tenants, and how to configure HwameiStor local volumes.

### Deploy the minio operator

Follow the steps below to deploy minio operator.

1. Copy the minio operator repository to the local.

     ```sh
     git clone <https://github.com/minio/operator.git>
     ```

     ![helm-repo-list](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/helm-repo-list.png)

     ![ls-operator](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/ls-opeartor.png)

2. Enter the helm operator directory: `/root/operator/helm/operator`.

     ![ls-pwd](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/ls-pwd.png)

3. Deploy the minio-operator instance.

     ```sh
     helm install minio-operator \
     --namespace minio-operator \
     --create-namespace \
     --generate-name .
     --set persistence.storageClass=local-storage-hdd-lvm .
     ```

4. Check the running status of the minio-operator resource.

     ![get-all](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-get-all.png)

### Create a tenant

Follow the steps below to create a tenant.

1. Go to `/root/operator/examples/kustomization/base` directory. Modify tenant.yaml as follows.

     ![git-diff-yaml](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/git-diff-tenant-yaml.png)

2. Enter the `/root/operator/helm/tenant/` directory. Modify the `values.yaml` file as follows.

     ![git-diff-values.yaml](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/git-diff-values-yaml.png)

3. Go to `/root/operator/examples/kustomization/tenant-lite` directory. Modify the `kustomization.yaml` file as follows.

     ![git-diff-kustomization-yaml](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/git-diff-kustomization-yaml.png)

4. Modify the `tenant.yaml` file as follows.

     ![git-diff-tenant-yaml02](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/git-diff-tenant-yaml02.png)

5. Modify the `tenantNamePatch.yaml` file as follows.

     ![git-diff-tenant-name-patch-yaml](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/git-diff-tenant-name-patch -yaml.png)

6. Create a tenant:

     ```sh
     kubectl apply –k .
     ```

7. Check the tenant minio-t1 resource status:

     ![kubectl-get-all-nminio-tenant](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-get-all-nminio-tenant.png )

8. If you want to create a new tenant, you can create a new `tenant` directory under the `/root/operator/examples/kustomization` directory (this case is `tenant-lite-2`) and make corresponding modifications to the corresponding files .

     ![pwd-ls-ls](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/pwd-ls-ls.png)

9. Execute `kubectl apply –k .` to create a new tenant `minio-t2`.

     ![kubectl-get-all-nminio](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-get-all-minio.png)

### Configure HwameiStor local volume

Run the following commands in sequence to configure a local volume.

```sh
kubectl get statefulset.apps/minio-t1-pool-0-nminio-tenant-oyaml
```

![local-storage-hdd-lvm](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/local-storage-hdd-lvm.png)

```sh
kubectl get pvc –A
```

![kubectl-get-pvc](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-get-pvc.png)

```sh
kubectl get pvc export-minio6-0 -nminio-6 -oyaml
```

![kubectl-get-pvc-export-oyaml](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-get-pvc-export-oyaml.png )

```sh
kubectl get pv
```

![kubectl-get-pv](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-get-pv.png)

```sh
kubectl get pvc data0-minio-t1-pool-0-0-nminio-tenant-oyaml
```

![kubectl-get-pvc-oyaml](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-get-pvc-oyaml.png)

```sh
kubectl get lv
```

![kubectl-get-lv](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-get-lv.png)

```sh
kubect get lvr
```

![kubectl-get-lvr](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-get-lvr.png)

## HwameiStor and MinIo test verification

After completing the above configurations, basic functional tests and multi-tenant isolation tests were performed.

### Basic functional testing

The steps of the basic feature test are as follows.

1. Log in to `minio console: 10.6.163.52:30401/login` from the browser.

     ![minio-opeartor-console-login](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/minio-opeartor-console-login.png)

2. Obtain the JWT through `kubectl minio proxy -n minio-operator`.

     ![minio-opeartor-console-login](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/kubectl-minio-proxy-jwt.png)

3. Browse and manage the created tenant information.

     ![tenant01](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/tenant01.png)

     ![tenant02](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/tenant02.png)

     ![tenant03](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/tenant03.png)

     ![tenant04](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/tenant04.png)

     ![tenant05](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/tenant05.png)

     ![tenant06](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/tenant06.png)

4. Log in to the minio-t1 tenant (username minio, password minio123).

     ![login-minio](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/login-minio-t1-01.png)

     ![login-minio](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/login-minio-t1-02.png)

5. Browse bucket bk-1.

     ![view-bucket-1](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/view-bucket-01.png)

     ![view-bucket-1](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/view-bucket-02.png)

     ![view-bucket-1](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/view-bucket-03.png)

6. Create a new bucket bk-1-1.

     ![create-bucket-1-1](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-bucket-1-1.png)

     ![create-bucket-1-1](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-bucket-1-2.png)

     ![create-bucket-1-1](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-bucket-1-3.png)

7. Create the path path-1-2.

     ![create-path-1-2](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-path-1-2-01.png)![create-path-1-2](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-path-1-2-02.png)

8. Uploaded files successfully.

    ![upload-file](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/upload-file-success.png)

    ![upload-file](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/upload-file-success-02.png)

    ![upload-file](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/upload-file-success-03.png)

9. Uploaded folder successfully.

    ![upload-folder](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/upload-folder-success-01.png)

    ![upload-folder](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/upload-folder-success-02.png)

    ![upload-folder](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/upload-folder-success-03.png)

    ![upload-folder](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/upload-folder-success-04.png)

10. Create a read-only user:

    ![create-user](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-readonly-user-01.png)

    ![create-user](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-readonly-user-02.png)

### Multi-tenant isolation test

Perform the following steps for multi-tenant isolation testing.

1. Log in to the minio-t2 tenant.

     ![login-t2](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/login-minio-t2-01.png)

     ![login-t2](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/login-minio-t2-02.png)

2. At this time, only the content of minio-t2 can be seen, and the content of minio-t1 is blocked.

     ![only-t2](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/only-t2.png)

3. Create buckets.

     ![create-bucket](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-bucket01.png)

     ![create-bucket](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/createbucket02.png)

4. Create paths.

     ![create-path](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-path01.png)

     ![create-path](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-path02.png)

5. Upload the file.

     ![upload-file](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/upload-file01.png)

     ![upload-file](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/upload-file02.png)

6. Create users.

     ![create-user](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-user01.png)

     ![create-user](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-user02.png)

     ![create-user](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-user03.png)

     ![create-user](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-user04.png)

     ![create-user](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/create-user05.png)

7. Configure user policy.

     ![user-policy](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/user-policy01.png)

     ![user-policy](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/user-policy02.png)

8. Delete the bucket.

     ![delete-bucket](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/delete-bk01.png)

     ![delete-bucket](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/delete-bk02.png)

     ![delete-bket](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/delete-bk03.png)

     ![delete-bucket](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/delete-bk04.png)

     ![delete-bucket](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/delete-bk05.png)

     ![delete-bucket](https://docs.daocloud.io/daocloud-docs-images/docs/storage/hwameistor/application/minio/delete-bk06.png)

## in conclusion

In this test, MinIO distributed object storage was deployed on the Kubernetes 1.22 platform and connected to HwameiStor local storage. In this environment, the basic ability test, system security test and operation and maintenance management test have been completed.

All tests have passed successfully, confirming that HwameiStor can perfectly adapt to the MinIO storage solution.
