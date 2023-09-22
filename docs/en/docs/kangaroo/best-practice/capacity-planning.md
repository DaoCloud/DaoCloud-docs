# Registry Capacity Resource Planning

The entire Harbor architecture can be divided into three layers: Consumer, Service, and Data Access Layer.

- Consumer: This mainly includes Harbor Portal, helm tools, and Docker client tools.
- Service: The service layer consists of core services that provide functionality in Harbor, such as core, registry, and jobserver.
- Data Access: This layer provides persistent storage for data, such as image file data and image metadata.

![Resource Architecture](../images/resource-architecture.png)

Capacity planning is reflected in the service layer and the storage layer:

- Service Layer: This primarily refers to the resources required for running the services, such as CPU and Memory.
- Storage Layer: This mainly includes storage for image file data, metadata DB storage, and Redis cache storage.

In practical scenarios, it is recommended to use estimation and validation methods to determine
if the resource planning is reasonable.

## Example

Let's start by setting an estimation for storing 500GB of image data.

### Service Layer

Different resource configurations can support different service request volumes,
and at least two service replicas should be set up:

| Service                   | CPU  | Memory |
| ------------------------- | ---- | ------ |
| Harbor Services (All)     | 1 Core | 2 Gi   |

### Storage Layer

| Type      | Storage       |
| --------- | ------------- |
| Image File | File System: The utilization should not exceed 85%. For example, if you need 500GB of actual file storage, the file system should have at least 588GB of storage.<br />[MinIO Object Storage](https://min.io/product/erasure-code-calculator): The actual storage usage rate in MinIO depends on the number of services and the erasure code configuration. For example, if the file system requires 588GB of storage and has a 50% utilization rate, then 1176GB of storage needs to be allocated. |
| DB Storage  | DB Storage: For 500GB of image data, approximately 50GB of DB space should be allocated.     |
| Cache Storage | Redis Cache: For 500GB of image data, approximately 5GB of cache space should be allocated.   |

## Validation

We can use load testing tools to validate if the resource planning meets the actual application requirements.

If you're unsure whether the current configuration meets the actual application requirements,
it is recommended to use the following load testing tool for validation.
The load testing tool is called [Harbor Perf](https://github.com/goharbor/perf).

```bash
git clone https://github.com/goharbor/perf
cd perf
export HARBOR_URL=https://admin:password@harbor.domain (username, password, and address)
export HARBOR_VUS=100 (number of virtual users)
export HARBOR_ITERATIONS=200 (number of iterations per virtual user)
export HARBOR_REPORT=true (generate report or not)
go run mage.go
```

## Additional Information

The image situation may vary for each company, and there can be reuse between layers. Additionally, it is important to consider image garbage collection, which may or may not be enabled depending on the setup.

When using Harbor, it is necessary to understand image garbage collection (GC). GC refers to the cleanup process that frees up space by deleting blobs that are no longer referenced when images are deleted from Harbor. By default, space is not automatically released when images are deleted.

To ensure efficient resource utilization, it is recommended to consider the following:

- Disabled GC: If GC is not enabled, continuous storage of images in the repository requires consideration of the storage requirements for existing images as well as the incremental storage and growth rate.
- Periodic GC: Running periodic GC helps alleviate storage pressure on the image repository. However, enabling periodic GC should be based on actual conditions and specific requirements. Consult the native Harbor documentation for instructions on enabling GC.

It is also important to consider whether to use MinIO or a file system for image file storage. The choice depends on factors such as performance, scalability, and specific needs. Proper resource planning should take these considerations into account.
