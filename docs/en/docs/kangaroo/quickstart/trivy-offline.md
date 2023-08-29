---
hide:
  - toc
---

# Enable Image Security Scanning in Offline Environment

> Trivy uses the `admin` account to pull the images for scanning.
> Before using it, ensure that you can perform `docker login` using the `admin` account.

## Download Offline Image Package

There are two versions of `trivy`, and currently, both require downloading version `2`.
Version `2` is no longer available in the [https://github.com/aquasecurity/trivy-db](https://github.com/aquasecurity/trivy-db) project.
You can directly download the offline `trivy-db` package, which is packaged as
an [`oci` package](https://github.com/aquasecurity/trivy-db/pkgs/container/trivy-db).

Use the `oras` tool to download it. First, install `oras`.
Please note the following commands are for the `linux` platform:

```shell
export VERSION="1.0.0"
$ curl -LO "https://github.com/oras-project/oras/releases/download/v${VERSION}/oras_${VERSION}_linux_amd64.tar.gz"
$ mkdir -p oras-install/
$ tar -zxf oras_${VERSION}_*.tar.gz -C oras-install/
$ sudo mv oras-install/oras /usr/local/bin/
$ rm -rf oras_${VERSION}_*.tar.gz oras-install/
```

Next, use the `oras` tool to download `trivy-db`:

```shell
$ oras pull ghcr.io/aquasecurity/trivy-db:2
db.tar.gz
$ tar -zxf db.tar.gz
# After extraction, you will have two files
db/metadata.json
db/trivy.db
```

## Enable Offline Scan in Managed Harbor

### Edit in the Kubernetes cluster where Harbor is hosted

```shell
$ kubectl -n {namespace} edit harborclusters.goharbor.io {harbor-name}
# Modify trivy offlineScan and skipUpdate to true
trivy:
    offlineScan: true
    skipUpdate: true
```

## Alternatively, you can make modifications from the DCE 5.0 cluster management page

1. Go to `Clusters`, click the proper cluster name.
2. Select `Custom Resources`.
3. Choose the `harborcluster` resource.
4. Enter the namespace where Harbor is hosted.
5. Select YAML.
6. Edit the YAML:

```yaml
trivy:
    offlineScan: true
    skipUpdate: true
```

## Upload `trivy.db` and `metadata.json` Files

### Create the corresponding directory `/home/scanner/.cache/trivy/db` in the `trivy pod`

1. Go to `Clusters`, click the proper cluster name.
2. Enter the namespace where Harbor is hosted.
3. Locate the `trivy` workload.
4. Click `Console` to enter the container (if there are multiple replicas, set it for each replica).
5. Once inside the container, execute `cd /home/scanner/.cache/trivy`.
6. Execute `mkdir db` to create the directory.

### After creating the directory, upload the offline package

1. Go to `Clusters`, click the proper cluster name.
2. Enter the namespace where Harbor is hosted.
3. Locate the `trivy` workload.
4. Click `Upload File`.
5. In the popup window, enter the upload path as `/home/scanner/.cache/trivy/db` and click `OK`.
6. You will be taken to the file selection page. Upload the `trivy.db` and `metadata.json` files respectively.
