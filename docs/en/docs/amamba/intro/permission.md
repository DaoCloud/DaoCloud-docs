---
hide:
  - toc
---

# Workbench Permissions

[Workbench](index.md) defines three user roles:

- Workspace Admin
- Workspace Editor
- Workspace Viewer

Each role has different permissions, as described below.

<!--
Permissions are indicated with __✅__ for granted access and __❌__ for denied access.
-->

| Object |Operation| Workspace Admin | Workspace Editor | Workspace Viewer |
| -------- | ---------------------------------- | --------------- | ---------------- | ---------------- |
| Application     |view application list| ✅         | ✅          | ✅          |
|          |view details (Go to Container Management)| ✅         | ✅          | ✅          |
|          |view application logs (Go to Observability)| ✅         | ✅          | ✅          |
|          |view monitoring data (Go to Observability)| ✅         | ✅          | ✅          |
|          |view RabbitMQ details – Basic information| ✅         | ✅          | ✅          |
|          |view service mesh (Go to Service Mesh)| ✅         | ✅          | ✅          |
|          |view Microservice Engine (Go to Microservice Engine)| ✅         | ✅          | ✅          |
|          |create an application| ✅         | ✅          | ❌         |
|          |edit YAML| ✅         | ✅          | ❌         |
|          |update the number of replicas| ✅         | ✅          | ❌         |
|          |update container image| ✅         | ✅          | ❌         |
|          |edit pipeline| ✅         | ✅          | ❌         |
|          |group applications| ✅         | ✅          | ❌         |
|          |delete| ✅         | ✅          | ❌         |
| Namespace |view| ✅         | ✅          | ✅          |
|          |create| ✅         | ❌         | ❌         |
|          |edit tag| ✅         | ❌         | ❌         |
|          |edit resource quota| ✅         | ❌         | ❌         |
|          |delete| ✅         | ❌         | ❌         |
| Pipeline |view pipeline| ✅         | ✅          | ✅          |
|          |view running records| ✅         | ✅          | ✅          |
|          |create| ✅         | ✅          | ❌         |
|          |run| ✅         | ✅          | ❌         |
|          |delete| ✅         | ✅          | ❌         |
|          |copy| ✅         | ✅          | ❌         |
|          |edit| ✅         | ✅          | ❌         |
|          |cancel pipeline running| ✅         | ✅          | ❌         |
| Credential |view| ✅         | ✅          | ✅          |
|          |create| ✅         | ✅          | ❌         |
|          |edit| ✅         | ✅          | ❌         |
|          |delete| ✅         | ✅          | ❌         |
| GitOps |view| ✅         | ✅          | ✅          |
|          |create| ✅         | ✅          | ❌         |
|          |sync| ✅         | ✅          | ❌         |
|          |edit| ✅         | ✅          | ❌         |
|          |delete| ✅         | ✅          | ✅          |
| Code Repo |view| ✅         | ✅          | ❌         |
|          |import| ✅         | ✅          | ❌         |
|          |delete| ✅         | ✅          | ❌         |
| Canary Release |view| ✅         | ✅          | ✅          |
|          |create| ✅         | ✅          | ❌         |
|          |release| ✅         | ✅          | ❌         |
|          |continue to release| ✅         | ✅          | ❌         |
|          |stop release| ✅         | ✅          | ❌         |
|          |update| ✅         | ✅          | ❌         |
|          |rollback| ✅         | ✅          | ❌         |
|          |delete| ✅         | ✅          | ❌         |

!!! note

     For a more detailed introduction to roles and permissions of DCE 5.0, refer to [Role and permission management](../../ghippo/user-guide/access-control/role.md).
