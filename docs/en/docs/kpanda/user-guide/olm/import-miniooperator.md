# Importing MinIo Operator Offline

This guide explains how to import the MinIo Operator offline in an environment without internet access.

## Prerequisites

- The current cluster is connected to the container management and the Global cluster has installed the `kolm` component (search for helm templates for kolm).
- The current cluster has the `olm` component installed with a version of 0.2.4 or higher (search for helm templates for olm).
- Ability to execute Docker commands.
- Prepare a container registry.

## Steps

1. Set the environment variables in the execution environment and use them in the subsequent steps by running the following command:

    ```bash
    export OPM_IMG=10.5.14.200/quay.m.daocloud.io/operator-framework/opm:v1.29.0 
    export BUNDLE_IMG=10.5.14.200/quay.m.daocloud.io/operatorhubio/minio-operator:v5.0.3 
    ```

    How to get the above image addresses:

    Go to `Container Management` -> Select the current cluster -> `Helm Applications` -> View the `olm` component -> `Plugin Settings`, and find the images needed for the opm, minio, minio bundle, and minio operator in the subsequent steps.


    ```bash
    Using the screenshot as an example, the four image addresses are as follows:

    # opm image
    10.5.14.200/quay.m.daocloud.io/operator-framework/opm:v1.29.0

    # minio image
    10.5.14.200/quay.m.daocloud.io/minio/minio:RELEASE.2023-03-24T21-41-23Z

    # minio bundle image
    10.5.14.200/quay.m.daocloud.io/operatorhubio/minio-operator:v5.0.3

    # minio operator image
    10.5.14.200/quay.m.daocloud.io/minio/operator:v5.0.3
    ```

2. Run the opm command to get the operators included in the offline bundle image.

    ```bash
    # Create the operator directory
    $ mkdir minio-operator && cd minio-operator 

    # Get the operator yaml
    $ docker run --user root -v $PWD/minio-operator:/minio-operator ${OPM_IMG} alpha bundle unpack --skip-tls-verify -v -d ${BUNDLE_IMG} -o ./minio-operator

    # Expected result
    .
    └── minio-operator
        ├── manifests
        │   ├── console-env_v1_configmap.yaml
        │   ├── console-sa-secret_v1_secret.yaml
        │   ├── console_v1_service.yaml
        │   ├── minio-operator.clusterserviceversion.yaml
        │   ├── minio.min.io_tenants.yaml
        │   ├── operator_v1_service.yaml
        │   ├── sts.min.io_policybindings.yaml
        │   └── sts_v1_service.yaml
        └── metadata
            └── annotations.yaml

    3 directories, 9 files
    ```

3. Replace all image addresses in the `minio-operator/manifests/minio-operator.clusterserviceversion.yaml` file with the image addresses from the offline container registry.

    Before replacement:


    After replacement:


4. Generate a Dockerfile for building the bundle image.

    ```bash
    $ docker run --user root -v $PWD:/minio-operator -w /minio-operator ${OPM_IMG} alpha bundle generate --channels stable,beta -d /minio-operator/minio-operator/manifests -e stable -p minio-operator  

    # Expected result
    .
    ├── bundle.Dockerfile
    └── minio-operator
        ├── manifests
        │   ├── console-env_v1_configmap.yaml
        │   ├── console-sa-secret_v1_secret.yaml
        │   ├── console_v1_service.yaml
        │   ├── minio-operator.clusterserviceversion.yaml
        │   ├── minio.min.io_tenants.yaml
        │   ├── operator_v1_service.yaml
        │   ├── sts.min.io_policybindings.yaml
        │   └── sts_v1_service.yaml
        └── metadata
            └── annotations.yaml

    3 directories, 10 files
    ```

5. Build the bundle image and push it to the offline registry.

    ```bash
    # Set the new bundle image
    export OFFLINE_BUNDLE_IMG=10.5.14.200/quay.m.daocloud.io/operatorhubio/minio-operator:v5.0.3-offline 

    $ docker build . -f bundle.Dockerfile -t ${OFFLINE_BUNDLE_IMG}  

    $ docker push ${OFFLINE_BUNDLE_IMG}
    ```

6. Generate a Dockerfile for building the catalog image.

    ```bash
    $ docker run --user root -v $PWD:/minio-operator -w /minio-operator ${OPM_IMG} index add  --bundles ${OFFLINE_BUNDLE_IMG} --generate --binary-image ${OPM_IMG} --skip-tls-verify

    # Expected result
    .
    ├── bundle.Dockerfile
    ├── database
    │   └── index.db
    ├── index.Dockerfile
    └── minio-operator
        ├── manifests
        │   ├── console-env_v1_configmap.yaml
        │   ├── console-sa-secret_v1_secret.yaml
        │   ├── console_v1_service.yaml
        │   ├── minio.min.io_tenants.yaml
        │   ├── minio-operator.clusterserviceversion.yaml
        │   ├── operator_v1_service.yaml
        │   ├── sts.min.io_policybindings.yaml
        │   └── sts_v1_service.yaml
        └── metadata
            └── annotations.yaml

    4 directories, 12 files
    ```

7. Build the catalog image.

    ```bash
    # Set the new catalog image  
    export OFFLINE_CATALOG_IMG=10.5.14.200/release.daocloud.io/operator-framework/system-operator-index:v0.1.0-offline

    $ docker build . -f index.Dockerfile -t ${OFFLINE_CATALOG_IMG}  

    $ docker push ${OFFLINE_CATALOG_IMG}
    ```

8. Go to Container Management and update the built-in catsrc image for the helm application `olm` (enter the catalog image specified in the construction of the catalog image, `${catalog-image}`).

9. After the update is successful, the `minio-operator` component will appear in the Operator Hub.

