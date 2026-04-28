# Security Vulnerabilities

This page lists some major security vulnerabilities that have appeared in the cloud native community in recent years.

- [2022 Kubernetes Security Vulnerabilities Review - What Can We Learn?](https://www.armosec.io/blog/kubernetes-vulnerabilities-2022/)

    This article summarizes major Kubernetes security vulnerabilities and solutions in 2022, such as CRI-O runtime container escape vulnerability, ArgoCD authentication bypass, etc.
    It introduces some vulnerability prevention measures: implementing security configuration files, following the principle of least privilege when assigning roles and permissions, continuously scanning K8s manifest files, codebases, and clusters, regularly updating software packages on clusters, using container sandbox projects, etc.

- [Istio High-Risk Vulnerability: Users with Localhost Access Can Impersonate Any Workload](https://github.com/istio/istio/security/advisories/GHSA-6c6p-h79f-g6p4)

    If a user has localhost access to the Istiod control plane, they can impersonate any workload identity within the service mesh.
    Affected versions are 1.15.2. Currently, patched version [1.15.3](https://github.com/istio/istio/releases/tag/1.15.3) has been released.

- [Istio High-Risk Vulnerability: Golang Regex Library Causes DoS Attack](https://github.com/istio/istio/security/advisories/GHSA-86vr-4wcv-mm9w)

    There is a request processing error vulnerability in Istiod. When Kubernetes validating or mutating webhook services are exposed, attackers can send custom or oversized messages causing the control plane to crash.
    Currently, [Istio](https://github.com/istio/istio/releases) has released patched versions 1.15.2, 1.14.5, and 1.13.9. Versions below 1.14.4, 1.13.8, or 1.12.9 are affected.

- [CrowdStrike Discovers New Cryptojacking Campaign Targeting Docker and Kubernetes Infrastructure](https://www.crowdstrike.com/blog/new-kiss-a-dog-cryptojacking-campaign-targets-docker-and-kubernetes/)
