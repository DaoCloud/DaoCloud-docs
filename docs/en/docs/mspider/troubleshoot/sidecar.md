---
hide:
  - toc
---

# Conflict between Namespace Sidecar and Workload Sidecar Configuration

## Description

After modifying the Namespace Sidecar policy, the injection of sidecars into Pods does not take effect immediately upon injection.

## Analysis

The Namespace configuration represents the default sidecar injection policy for sidecars within the current namespace. When a Pod is enabled, it automatically undergoes sidecar injection based on the policy defined in the current namespace. This injection occurs at the start of the Pod on the launching node. If the Namespace sidecar policy is modified while the Pod is running, Istio, in order to ensure the stability of the production environment, does not automatically restart the Pod. Therefore, the user needs to manually restart the Pod.

## Solution

* To address this issue, it is necessary to manually restart the Pod. Please proceed with caution and plan accordingly based on the specific business requirements.
* Use the command `kubectl rollout restart deployment <deployment-name> -n <namespace>` to restart the Pod. Again, exercise caution and plan accordingly based on the specific business requirements.
