# Progressive Gray Release with Argo Rollout

This article describes how to implement progressive gray release based on open source [Argo Rollout](https://argoproj.github.io/argo-rollouts/).

## Prerequisites

- The images in the example need to be accessed over the Internet: `argoproj/rollouts-demo:yellow` and `argoproj/rollouts-demo:blue`.

- Only applicable to DCE 5.0 platform deployed via installer with metallb.

- Istio and Argo Rollout components need to be installed in the cluster for using gray release capabilities.

## Operating Steps

The whole process is divided into four steps: first, build the application based on the container image, then configure the Istio-related resources, create the gray release task, and finally verify the effect.

### Build Application Based on Container Image

For specific operating steps, please refer to [Building Microservice Applications Based on Git Repositories](../user-guide/wizard/create-app-git.md) and [Deploying Java Applications Based on Jar Packages](../user-guide/wizard/jar-java-app.md).

**Note**:

- Container image: argoproj/rollouts-demo:blue

- Service port: named `http`, container port is `8082`, and service port is `8082`.

    <!--![]()screenshots-->

- When filling in advanced configurations, it is necessary to enable gray release.

    <!--![]()screenshots-->

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
      # 新增以下内容
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
Create a gray release task in the application console. For more detailed instructions on creating, please refer to Creating Canary Release Tasks.

1. Select the application that enables gray release.

    <!--![]()screenshots-->

2. Modify the publishing rule (for a clearer demonstration effect)

    <!--![]()screenshots-->

3. Click "Create and Update Application", and fill in the image address argoproj/rollouts-demo:yellow in the pop-up dialog box.

    <!--![]()screenshots-->

### Verify Effect

Access the address: http://{istio-ingressgateway LB IP}:8082, and the following access effect will be obtained.

This interface will concurrently call http://{istio-ingressgateway LB IP}:8082/color to obtain color information and fill it into the grid.
In the gray release object, the specified colors are blue, yellow, which will be displayed according to the defined traffic ratio of 1:9.


<!--![]()screenshots-->

At this time, you can choose to continue publishing the application in the gray release module of the application console to adjust the traffic ratio until the final successful release.

<!--![]()screenshots-->

