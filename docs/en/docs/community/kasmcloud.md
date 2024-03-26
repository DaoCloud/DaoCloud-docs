<div align="center">
  <h1><code>KasmCloud</code></h1>

<strong>Managing and Running Actors, Providers, and Links in Kubernetes</strong>
</div>

## :warning:Warning

**This is a contributor-led experimental project and is not recommended to run in production at this time.**

With each tag, it works fine, but there may be incompatible changes between tags.

## Design

[Combining WasmCloud with Kubernetes](https://docs.google.com/document/d/16p-9czZ6GT_layiabGE6HTyVpbYSALjoyxXhgIfYW0s/edit#heading=h.ymjg4q1g3smk)

<div align="center"><img src="./arch.png" style="width:500px;" /></div>

## Quick Start

1. Deploy Nats

    ```bash
    helm repo add nats https://nats-io.github.io/k8s/helm/charts/
    helm repo update
    helm upgrade --install kasmcloud-nats nats/nats
    ```

2. Deploy KasmCloud CRDs and Webhook Server

    ```bash
    kubectl apply -f ./deploy/crds
    kubectl apply -f ./deploy/webhook
    ```

3. Deploy KasmCloud Host

    ```bash
    kubectl apply -f ./deploy/kasmcloud_host_rbac.yaml

    # Deploy Default KasmCloud Host
    kubectl apply -f ./deploy/kasmcloud_host_default.yaml

    # [Optional] You can also deploy KasmCloud Host in each Kubernetes node.
    kubectl apply -f ./deploy/kasmcloud_host_daemonset.yaml

    # [Optional] You can also deploy as many temporary hosts as you want
    # and change the number of temporary hosts by scaling the Deployment
    kubectl apply -f ./deploy/kasmcloud_host_deployment.yaml
    ```

4. Deploy Actor, Link and Provider Sample

    ```bash
    kubectl apply -f ./sample.yaml
    kubectl get kasmcloud
    ```

    Output is similar to:

    ```console
    NAME                              DESC   PUBLICKEY                                                  REPLICAS   AVAILABLEREPLICAS   CAPS                                                   IMAGE
    actor.kasmcloud.io/echo-default   Echo   MBCFOPM6JW2APJLXJD3Z5O4CN7CPYJ2B4FTKLJUR5YR5MITIU7HD3WD5   10         10                  ["wasmcloud:httpserver","wasmcloud:builtin:logging"]   wasmcloud.azurecr.io/echo:0.3.8

    NAME                                CONTRACTID             LINK   ACTORYKEY                                                  PROVIDERKEY
    link.kasmcloud.io/httpserver-echo   wasmcloud:httpserver   test   MBCFOPM6JW2APJLXJD3Z5O4CN7CPYJ2B4FTKLJUR5YR5MITIU7HD3WD5   VAG3QITQQ2ODAOWB5TTQSDJ53XK3SHBEIFNK4AYJ5RKAX2UNSCAPHA5M

    NAME                                       DESC          PUBLICKEY                                                  LINK   CONTRACTID             IMAGE
    provider.kasmcloud.io/httpserver-default   HTTP Server   VAG3QITQQ2ODAOWB5TTQSDJ53XK3SHBEIFNK4AYJ5RKAX2UNSCAPHA5M   test   wasmcloud:httpserver   ghcr.io/iceber/wasmcloud/httpserver:0.17.0-index
    ```

5. curl echo server

    ```bash
    # other terminal
    kubectl port-forward pod/kasmcloud-host-default 8080:8080

    curl 127.0.0.1:8080
    {"body":[],"method":"GET","path":"/","query_string":""}
    ```

## RoadMap

* Add KasmCloudHost resource
* Add status information for the resource
* Add Kasmcloud Repeater  module
* Add rolling updates for Actor
* Add DaemonSet deployment for Actor
* Blue/Green Deployment for Actors and Providers

## Reference

- [kasmcloud repo](https://github.com/wasmCloud/kasmcloud)
