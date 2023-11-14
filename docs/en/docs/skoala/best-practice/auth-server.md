# The microservice gateway accesses the authentication server

The microservice gateway supports access to a third-party authentication server.

## prerequisite

- [Create a cluster](../../kpanda/user-guide/clusters/create-cluster.md) OR [Integrate a cluster](../../kpanda/user-guide/clusters/integrate-cluster.md)
- [Create a gateway](../gateway/index.md)

## Configuring the authentication Server

### Use the default authentication server

1. Clone the code template of the authentication server to a local directory.

    ```
    git clone https://github.com/projectsesame/envoy-authz-java
    ```
2. Use the default image directly under [ all-in-one-contour.yaml ](https://github.com/projectsesame/envoy-authz-java/blob/main/all-in-one-contour.yaml) and [ all-in-one-contour.yaml ](https://github.com/projectsesame/envoy-authz-java/blob/main/all-in-one-contour.yaml).

    The default image is as follows:
    - release.daocloud.io/skoala/demo/envoy-authz-java:0.1.0
    - release-ci.daocloud.io/skoala/demo/envoy-authz-java:0.1.0

3. The template is simple path identification. If the access path is `/`, the access is authenticated, and other paths are denied.

### Use a custom authentication server

1. Clone the code template of the authentication server to a local directory.

    ```
    git clone https://github.com/projectsesame/envoy-authz-java
    ```
    
    The project is divided into two sub-modules:

    - The API module is envoy"s `protobuf` file definition (no changes required)
    - authz-grpc-server module is the authentication logical processing address of the authentication server (fill in the authentication logic here)
    - release.daocloud.io/skoala/demo/envoy-authz-java:0.1.0

2. Compile the API module using the following command to resolve the problem where the class is not found

    ```
    mvn clean package
    ```

3. After successful compilation, write your own authentication logic in the check method.

    - Check method in envoy – authz – Java/authz – GRPC – server/SRC/main/Java/envoy/projectsesame/IO/authzgrpcserver/AuthzService Java
    - The template is simple path identification. If the access path is `/`, the access is authenticated, and other paths are denied.

4. Once the code is written, package the image using Docker.

    The Dockerfile already exists in the code template repository, and you can use this template directly to build the image.

5. Fill the image address in the `spec/template/spec/containers/image` field under Deployment in the [ all-in-one-contour.yaml ](https://github.com/projectsesame/envoy-authz-java/blob/main/all-in-one-contour.yaml) file.

    <!--![]()screenshots-->-->

## Access authentication server

1. Create the following resources in the cluster where the gateway resides. You can use the `kubectl apply` command to quickly create the following three resources at once based on the [ all-in-one-contour.yaml ](https://github.com/projectsesame/envoy-authz-java/blob/main/all-in-one-contour.yaml) file.

    - Deployment of the authentication server
    - The Service of the authentication server
    - The ExtensionService of the authentication server

2. Create a domain name under the gateway that uses the `https` protocol and fill in basic information.

    <!--![]()screenshots-->-->

3. Enter the security configuration of this domain name and specify the address of the authentication server. The authentication server address is in `namespace/name` format.

    <!--![]()screenshots-->-->

    !!! note

        The `namespace/name` of the authentication server refers to the values of the `namespace` and `name` fields in the `metadata` section of the ExtensionService under the [all-in-one-contour.yaml](https://github.com/projectsesame/envoy-authz-java/blob/main/all-in-one-contour.yaml) file.

4. Create an API under the gateway, and enter the newly created domain name in the path `/`. Enable `Security Auth`, and take the API online.

    <!--![]()screenshots-->

5. You can now access the API through the authentication server.
