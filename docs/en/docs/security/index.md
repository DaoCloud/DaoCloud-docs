---
MTPE: Jeanine-tw
Revised: NA
Pics: NA
Date: 2023-01-04
---

# Cloud Native Security

DCE 5.0 provides a fully automated security implementation for containers, Pods, images, runtimes, and microservices.
The following table lists some of the security features that have been implemented or are in the process of being implemented.

| Security Features | Specific Items | Description |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Image security | Trusted image Distribution | Key pairs and signature information are required to achieve secure transport of images. It's allowed to select a key for mirror signing during mirror transmission. |
| Runtime security | Event correlation analysis | Support correlation and risk analysis of security events detected at runtime to enhance attack traceability. Support converge alerts, reduce invalid alerts, and improve event response efficiency. |
| - | Container decoy repository | The container decoy repository is equipped with common decoys including but not limited to: unauthorized access vulnerabilities, code execution vulnerabilities, local file reading vulnerabilities, remote command execution RCE vulnerabilities, and other container decoys. |
| - | Container decoy deployment | Support custom decoy containers, including service names, service locations, etc. |
| - | Container decoy alerting | Support alerting on suspicious behavior in container decoys. |
| - |  Offset detection | While scanning the image, learn all the binary information in the image and form a "whitelist" to allow only the binaries in the "whitelist" to run after the container is online, which ensures that the container can not run unauthorized (such as illegal download) executable files. |
| Micro-isolation | Intelligent recommendation of isolation policies | Support for recording historical access traffic to resources, and intelligent policy recommendation based on historical access traffic when configuring isolation policies for resources. |
| - | Tenant isolation | Support isolation control of tenants in Kubernetes clusters, with the ability to set different network security groups for different tenants, and supports tenant-level security policies to achieve inter-tenant network access and isolation. |
| Microservices security | Service and API security scanning |Supports automatic, manual and periodic scanning of services and APIs within a cluster. Support all traditional web scanning items including XSS vulnerabilities, SQL injection, command/code injection, directory enumeration, path traversal, XML entity injection, poc, file upload, weak password, jsonp, ssrf, arbitrary jump, CRLF injection and other risks. For vulnerabilities found in the container environment, support vulnerability type display, url display, parameter display, danger level display, test method display, etc.|
