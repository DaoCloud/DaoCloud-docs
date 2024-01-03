# Types of Security Scans

DCE 5.0 Container Management provides three types of security scans:

- Compliance Scan: Conducts security scans on cluster nodes based on [CIS Benchmark](https://github.com/aquasecurity/kube-bench/tree/main/cfg).
- Authorization Scan: Checks for security and compliance issues in the Kubernetes cluster, records and verifies authorized access, object changes, events, and other activities related to the Kubernetes API.
- Vulnerability Scan: Scans the Kubernetes cluster for potential vulnerabilities and risks, such as unauthorized access, sensitive information leakage, weak authentication, container escape, etc.

## Compliance Scan

The object of compliance scanning is the cluster node. The scan result lists the scan items and results and provides repair suggestions for any failed scan items. For specific security rules used during scanning, refer to the [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes).

The focus of the scan varies when checking different types of nodes.

- Scan the control plane node (Controller)

    - Focus on the security of system components such as __API Server__ , __controller-manager__ , __scheduler__ , __kubelet__ , etc.
    - Check the security configuration of the Etcd database.
    - Verify whether the cluster's authentication mechanism, authorization policy, and network security configuration meet security standards.

- Scan worker nodes

    - Check if the configuration of container runtimes such as kubelet and Docker meets security standards.
    - Verify whether the container image has been trusted and verified.
    - Check if the network security configuration of the node meets security standards.

!!! tip

    To use compliance scanning, you need to create a [scan configuration](cis/config.md) first, and then create a [scan policy](cis/policy.md) based on that configuration. After executing the scan policy, you can [view the scan report](cis/report.md).

## Authorization Scan

Authorization scanning focuses on security vulnerabilities caused by authorization issues. Authorization scans can help users identify security threats in Kubernetes clusters, identify which resources need further review and protection measures. By performing these checks, users can gain a clearer and more comprehensive understanding of their Kubernetes environment and ensure that the cluster environment meets Kubernetes' best practices and security standards.

Specifically, authorization scanning supports the following operations:

- Scans the health status of all nodes in the cluster.

- Scans the running state of components in the cluster, such as __kube-apiserver__ , __kube-controller-manager__ , __kube-scheduler__ , etc.

- Scans security configurations: Check Kubernetes' security configuration.

    - API security: whether unsafe API versions are enabled, whether appropriate RBAC roles and permission restrictions are set, etc.
    - Container security: whether insecure images are used, whether privileged mode is enabled, whether appropriate security context is set, etc.
    - Network security: whether appropriate network policy is enabled to restrict traffic, whether TLS encryption is used, etc.
    - Storage security: whether appropriate encryption and access controls are enabled.
    - Application security: whether necessary security measures are in place, such as password management, cross-site scripting attack defense, etc.

- Provides warnings and suggestions: Security best practices that cluster administrators should perform, such as regularly rotating certificates, using strong passwords, restricting network access, etc.

!!! tip

    To use authorization scanning, you need to create a scan policy first. After executing the scan policy, you can view the scan report. For details, refer to [Security Scanning](audit.md).

## Vulnerability Scan

Vulnerability scanning focuses on scanning potential malicious attacks and security vulnerabilities, such as remote code execution, SQL injection, XSS attacks, and some attacks specific to Kubernetes. The final scan report lists the security vulnerabilities in the cluster and provides repair suggestions.

!!! tip

    To use vulnerability scanning, you need to create a scan policy first. After executing the scan policy, you can view the scan report. For details, refer to [Vulnerability Scan](hunter.md).