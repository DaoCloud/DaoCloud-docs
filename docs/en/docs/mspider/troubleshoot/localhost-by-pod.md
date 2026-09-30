# How to Make an Application Listening on localhost in a Cluster Accessible by Other Pods

This page describes how to configure sidecar resources so that an application listening on localhost can be accessed by other Pods in the cluster through a Service.

## Symptom

When an application deployed in the cluster listens on localhost, even if the service port of the application is exposed through a Service, the service cannot be accessed by other Pods in the cluster.

Examples of applications listening on localhost in different languages are as follows:

- Golang: net.Listen("tcp", "localhost:8080")
- Node.js: http.createServer().listen(8080, "localhost")
- Python: socket.socket().bind(("localhost", 8083))

## Problem Cause

When an application in the cluster listens on the localhost network address, since localhost is a local address, it is normal that other Pods in the cluster cannot access it.

## Solution

You can choose any of the following ways to expose the application service.

- Method 1: Change the network address the application listens on

    If you want the service provided by the application to be exposed externally, it is recommended to modify the application code and change the network address the application listens on from localhost to 0.0.0.0.

- Method 2: Use the service mesh to expose a service listening on localhost

    If you do not want to modify the application code and need to expose the application listening on localhost to other Pods in the cluster, you can configure it when creating the sidecar.

    Replace the following fields according to your actual situation.

     | **Field**           | **Description**                              |
     | ------------------ | ------------------------------------- |
     | `{namespace}`      | Replace it with the namespace where the application is deployed.        |
     | `{container_port}` | Replace it with the container port on which the application listens on localhost. |
     | `{port}`           | Replace it with the Service port of the application.           |
     | `{key} : {value}`  | Replace it with the label of the selected application Pod.           |

     ```yaml
     apiVersion: networking.istio.io/v1beta1
     kind: Sidecar
     metadata:
       name: localhost-access
       namespace: { namespace }
     spec:
       ingress:
         - defaultEndpoint: "127.0.0.1:{container_port}"
           port:
             name: tcp
             number: { port }
             protocol: TCP
       workloadSelector:
         labels:
           { key }: { value }
     ```
