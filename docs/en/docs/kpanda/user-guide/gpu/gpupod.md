# Relationship Between Pods and GPU Cards

This document explains how to view the relationship between Pods and GPU cards after GPU resources are used by containers.

## Prerequisites

* GPU cards and their corresponding driver plugins are installed on the cluster.
* GPU support is enabled in the cluster.
* Applications have been properly deployed using GPU resources.

## Steps

1. Go to the target cluster, expand the **Workloads** menu, and navigate to the **Pods** list.
   In the search bar, select a **GPU type** to filter the list and see which Pods are currently using GPU resources.

    <!-- ![gpupod1](../gpu/images/gpupod1.png) -->

2. If you already know which Pod is using GPU resources, you can search by **Pod name** to view details in the list and the Pod's detail page, including GPU type and resource usage.

    <!-- ![gpupod2](../gpu/images/gpupod2.png)
    ![gpupod3](../gpu/images/gpupod3.png) -->
