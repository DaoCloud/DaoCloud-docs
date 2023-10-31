# Progressive Gray Release with Argo Rollout

This article describes how to implement progressive gray release based on open source [Argo Rollout](https://argoproj.github.io/argo-rollouts/).

## Prerequisites

- The images in the example need to be accessed over the Internet: `argoproj/rollouts-demo:yellow` and `argoproj/rollouts-demo:blue`.

- Only applicable to DCE 5.0 platform deployed via installer with metallb.

- Istio and Argo Rollout components need to be installed in the cluster for using gray release capabilities.

## Operating Steps

The whole process is divided into four steps: first, build the application based on the container image, then configure the Istio-related resources, create the gray release task, and finally verify the effect.

### Building the Application Based on Container Image

1. Select `Container Image` as the entry point in the wizard.

2. Fill in the basic information:

3. Fill in the container configuration. For example:

    - Container image: `argoproj/rollouts-demo:blue`
    - Service port: Name is `http`, container port is `8082`, and service port is `8082`.


4. Fill in the advanced configuration and enable `Enable Mesh`.

5. After creation, an application record will be generated in `Overview` -> `Native Apps`.

### Configuration of Istio-related Resources

Create the following resources in the [Service Mesh](../../mspider/intro/index.md) module or console.

1. Create Gateway

    ```yaml title="gateway.yaml"
    apiVersion: networking.istio.io/v1beta1
    kind: Gateway
    metadata:
      name: rollout-demo
      namespace: rollout-demo # (1)
    spec:
      selector:
        istio: ingressgateway
      servers:
      - hosts:
        - '*'
        port:
          name: http
          number: 8082
          protocol: HTTP
    ```

    1. Namespace where the application is deployed.

2. Deploy Gateway

    ```shell
    vi gateway.yaml
    kubectl apply -f gateway.yaml
    ```

3. Modify VirtualService

    ```shell
    kubectl edit vs {# application name #} -n {# application namespace #}
    ```

    Only need to modify the prompted fields, and other fields do not need to be modified.

    ```yaml
    apiVersion: networking.istio.io/v1beta1
    kind: VirtualService
    metadata:
      creationTimestamp: "2022-11-07T10:46:23Z"
      generation: 84
      name: demo01
      namespace: default
      resourceVersion: "5741370"
      uid: 8109f754-aa9d-49f1-b8a9-d4daf5108032
    spec:
      gateways:
      - rollout-demo # (1)
      hosts:
      - '*' # (2)
      http:
      - name: primary
        route:
        - destination:
            host: demo01
            subset: stable
          weight: 100
        - destination:
            host: demo01
            subset: canary
          weight: 0
    ```

    1. Modify here, you need to add a new gateway, which points to the name of the gateway created in the previous step.
    2. Modify here, the original host was the name of the virtual service, which needs to be deleted and changed to `‘*’`.

4. Configure istio-ingressgateway gateway

    ```shell
    kubectl edit svc istio-ingressgateway -n istio-system
    ```

    Only need to modify the prompted fields, and other fields do not need to be modified.

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      labels:
        app: istio-ingressgateway
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/name: istio-ingressgateway
        app.kubernetes.io/version: 1.15.0
        helm.sh/chart: gateway-1.15.0
        istio: ingressgateway
      name: istio-ingressgateway
      namespace: istio-system
      resourceVersion: "5775680"
      uid: 53bd7344-ba45-4547-b695-aca2c4dd713d
    spec:
      allocateLoadBalancerNodePorts: true
      clusterIP: 100.66.222.131
      clusterIPs:
      - 100.66.222.131
      externalTrafficPolicy: Cluster
      internalTrafficPolicy: Cluster
      ipFamilies:
      - IPv4
      ipFamilyPolicy: SingleStack
      ports:
      - name: status-port
        nodePort: 32384
        port: 15021
        protocol: TCP
        targetPort: 15021
      # Add this content
      - name: rollout-demo
        port: 8082
        protocol: TCP
        targetPort: 8082
      # --------------
      selector:
        app: istio-ingressgateway
        istio: ingressgateway
      sessionAffinity: None
      type: LoadBalancer
    ```

5. Create AuthorizationPolicy Resource

    The purpose of this step is to ensure that js-related resources can be accessed normally when accessing through a browser.

    ```yaml
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: demo01
      namespace: istio-system
    spec:
      rules:
      - to:
        - operation:
            paths:
            - /*
      - from:
        - source:
            requestPrincipals:
            - '*'
      selector:
        matchLabels:
          app: istio-ingressgateway
    status:
      loadBalancer:
        ingress:
        - ip: 10.29.135.48
    ```

### Create Gray Release Task

To create a canary release task in the application workspace, follow these steps. For more detailed instructions, you can refer to the [Creating Canary Release Tasks](../user-guide/release/canary.md) guide.

1. Select the application for which you want to enable canary release.



2. Set up the release rules. Choose "Istio" as the traffic management type and "Weight Based" as the traffic routing type.


3. Click `Create and Update App`. In the pop-up dialog, enter the image address: `argoproj/rollouts-demo:yellow`.

### Verify Effect

Access the address: `http://{istio-ingressgateway LB IP}:8082`, and the following access effect will be obtained.

This interface will concurrently call `http://{istio-ingressgateway LB IP}:8082/color` to obtain color information and fill it into the grid.
In the gray release object, the specified colors are blue, yellow, which will be displayed according to the defined traffic ratio of 1:9.

<!--![]()screenshots-->

At this time, you can choose to continue publishing the application in the gray release module of the application console to adjust the traffic ratio until the final successful release.

<!--![]()screenshots-->
