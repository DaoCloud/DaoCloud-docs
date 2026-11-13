# Microservice Gateway Access to Authentication Server

The microservice gateway supports integration with third-party authentication servers.

## Prerequisites

- [Create a Cluster](../../kpanda/user-guide/clusters/create-cluster.md) or
  [Integrate a Cluster](../../kpanda/user-guide/clusters/integrate-cluster.md)
- [Create a Gateway](../gateway/index.md)

## Select an Authentication Server

### Default Authentication Server

1. Clone the authentication server's code template to your local machine.

    ```git
    git clone https://github.com/projectsesame/envoy-authz-java
    ```

2. Use [envoy-authz-java.yaml](https://github.com/projectsesame/envoy-authz-java/blob/main/envoy-authz-java.yaml) and the default image in the repository.

    ```bash
    kubectl apply -f envoy-authz-java.yaml
    ```

    The default image is release.daocloud.io/skoala/demo/envoy-authz-java:0.1.0

3. The template performs simple path-based authorization, allowing access only to the `/` path and denying access to other paths.

### Custom Authentication Server

1. Clone the authentication server's code template to your local machine.

    ```git
    git clone https://github.com/projectsesame/envoy-authz-java
    ```

    This project has two submodules:

    - The API module defines Envoy's `protobuf` files (no need to modify)
    - The authz-grpc-server module handles the authentication logic of the server (customize the authentication logic here)
    - release.daocloud.io/skoala/demo/envoy-authz-java:0.1.0

2. Compile the API module using the following command to resolve any missing dependencies.

    ```bash
    mvn clean package
    ```

3. After successful compilation, write your custom authentication logic in the check method.

    - The check method is located in `envoy-authz-java/authz-grpc-server/src/main/java/envoy/projectsesame/io/authzgrpcserver/AuthzService.java`
    - The template performs simple path-based authorization, allowing access only to the `/` path and denying access to other paths.

4. After writing the code, package the server into a Docker image.

    The Dockerfile is already available in the code template repository, which can be used to build the image.

5. Update the image address in the [envoy-authz-java.yaml](https://github.com/projectsesame/envoy-authz-java/blob/main/all-in-one-contour.yaml) file under Deployment in the spec/template/spec/containers/image field.

    ![Fill in image url](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/jwt04.png)

## Integrate Authentication Server

1. Create the following resources within the cluster where the gateway is located. Use the `kubectl apply` command to quickly create the following three resources based on the [envoy-authz-java.yaml](https://github.com/projectsesame/envoy-authz-java/blob/main/envoy-authz-java.yaml) file:

    - Authentication Server Deployment
    - Authentication Server Service
    - Authentication Server ExtensionService

2. Integrate an Auth plugin in the Plugin Center.

    Fill in the access address with the application deployed in step 1 and ensure that the application uses the GRPC protocol.

    <!--![]()screenshots-->

## Configure Authentication Server

### Configure Gateway

!!! note

    Both HTTP and HTTPS domains support secure authentication. If using HTTPS domains, ensure that the gateway is configured for HTTPS.

1. Configure the authentication server in the gateway.

    <!--![]()screenshots-->

2. Create an `HTTP` or `HTTPS` domain. For example, when creating an HTTP domain, the domain is automatically configured for secure authentication and cannot be disabled.

    <!--![]()screenshots-->

3. Create an API under the gateway, associate it with the newly created domain, set the path match to `/`, and deploy the API. By default, the API inherits the domain's security authentication configuration, but you can customize the plugin's activation and additional parameters.

    <!--![]()screenshots-->

4. You can now access this API through the authentication server.

    - Access `/`.

        ```bash
        curl -H 'header: true' http://gateway.test:30000/
        ```

        The response should indicate successful access.

        ```bash
        adservice-springcloud: hello world!
        ```

    - Access `/test1`.

        ```bash
        curl -H 'header: true' http://gateway.test:30000/test1
        ```

        The response should indicate access denied.

        ```bash
        No permission
        ```

### Configure Domain or API

!!! note

    Only HTTPS domains support secure authentication. Ensure that the gateway is configured for HTTPS.

1. Create an `HTTPS` domain and manually configure secure authentication.

    <!--![]()screenshots-->

2. Create an API under the gateway, associate it with the newly created domain, set the path match to `/`, and deploy the API. By default, the API inherits the domain's security authentication configuration, but you can customize the plugin's activation and additional parameters.

    <!--![]()screenshots-->

3. You can now access this API through the authentication server.

    - Access `/`.

        ```bash
        curl -k -H 'header: true' https://gateway.test:30001/
        ```

        The response should indicate successful access.

        ```none
        adservice-springcloud: hello world!
        ```

    - Access `/test1`.

        ```bash
        curl -k -H 'header: true' https://gateway.test:30001/test1
        ```

        The response should indicate access denied.

        ```none
        No permission
        ```
