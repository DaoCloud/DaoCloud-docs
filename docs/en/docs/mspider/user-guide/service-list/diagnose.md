---
hide:
  - toc
---

# One-click Diagnosis and Repair

DCE 5.0 Service Mesh provides built-in one-click diagnosis and repair functionality for managed services, which can be operated through a graphical user interface.

1. Enter a specific Service Mesh and click `Service Management` -> `Service List`.
   In the `Diagnosis Config` column, next to services with an `Abnormal` status,
   the word `Diagnose` will appear. Click `Diagnose`.

    ![Diagnose](../images/diagnose01.png)

2. A diagnosis popup will appear on the right-hand side. Follow the built-in checklist for inspection.
   Green checkmarks indicate that the item has <span style="color:green">Passed</span>, while red crosses indicate items that is <span style="color:red">Not Passed</span> and need to be repaired.

    Check the items that have <span style="color:red">Not Passed</span> and click the `One-Click Repair` button.
    You can click `Rediagnose` to refresh the checklist, and the repair is usually
    completed within a few minutes.

    ![Repair](../images/diagnose02.png)

3. After successful repair, all items in the checklist will turn gray and display as
   <span style="color:green">Passed</span>. Click `Next`.

    ![Next](../images/diagnose03.png)

4. A list of items that require `Manual Repair` will be displayed.
   You can click `View Troubleshooting Guide` to read the proper documentation page and manually repair the items.

    ![Manual repair](../images/diagnose04.png)

!!! note

    For the services in the following system namespaces, it is not recommended to use one-click repair:

| Category             | Namespace          | Purpose                        |
| -------------------- | ------------------ | ----------------------------- |
| Istio System Namespace | istio-system       | Hosts Istio control plane components and resources |
|                      | istio-operator     | Deploys and manages Istio Operator |
| K8s System Namespace   | kube-system        | Control plane components      |
|                      | kube-public        | Cluster configurations, certificates, etc. |
|                      | kube-node-lease    | Monitors and maintains node activity |
| DCE 5.0 System Namespace | amamba-system      | Application workplace         |
|                      | ghippo-system      | Global management             |
|                      | insight-system     | Observability                 |
|                      | ipavo-system       | Homepage dashboard            |
|                      | kairship-system    | Multicloud orchestration       |
|                      | kant-system        | Cloud-edge collaboration       |
|                      | kangaroo-system    | Container registry              |
|                      | kcoral-system      | Application backup             |
|                      | kubean-system      | Cluster lifecycle management  |
|                      | kpanda-system      | Container management          |
|                      | local-path-storage | Local storage                 |
|                      | mcamel-system      | Middleware                    |
|                      | mspider-system     | Service mesh                  |
|                      | skoala-system      | Microservice engine            |
|                      | spidernet-system   | Network module                |
