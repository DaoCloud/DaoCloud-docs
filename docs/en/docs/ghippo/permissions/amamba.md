---
hide:
  - toc
---

# Workbench permission description

[Workbench](../../amamba/intro/index.md) supports three user roles:

- Workspace Admin
- Workspace Editor
- Workspace Viewer

Each role has different permissions, which are described below.

<!--
You have permission to use `&check;`, but you don't have permission to use `&cross;`
-->

| Menu Objects | Actions | Workspace Admin | Workspace Editor | Workspace Viewer |
| -------- | ----------------------------------- | ----- ---------- | ---------------- | ---------------- |
| Apps | View App List | &check; | &check; | &check; |
| | View details (jump to container management) | &check; | &check; | &check; |
| | View application logs (jump to observables) | &check; | &check; | &check; |
| | View application monitoring (jump to observables) | &check; | &check; | &check; |
| | View RabbitMQ Details - Basic Information | &check; | &check; | &check; |
| | View service mesh (jump to service mesh) | &check; | &check; | &check; |
| | View microservice engine (jump to microservice engine) | &check; | &check; | &check; |
| | Create App | &check; | &check; | &cross; |
| | Edit YAML | &check; | &check; | &cross; |
| | Update replica count | &check; | &check; | &cross; |
| | Update container image | &check; | &check; | &cross; |
| | Edit Pipeline | &check; | &check; | &cross; |
| | App Grouping | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |
| Namespace | View | &check; | &check; | &check; |
| | Create | &check; | &cross; | &cross; |
| | Edit Tab | &check; | &cross; | &cross; |
| | Edit Resource Quota | &check; | &cross; | &cross; |
| | delete | &check; | &cross; | &cross; |
| Pipeline | View Pipeline | &check; | &check; | &check; |
| | View running records | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | run | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |
| | Copy | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | cancel run | &check; | &check; | &cross; |
| Credentials | View | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |
| Continuous Deployment | View | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | sync | &check; | &check; | &cross; |
| | edit | &check; | &check; | &cross; |
| | delete | &check; | &check; | &check; |
| Code repository | View | &check; | &check; | &cross; |
| | import | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |
| Grayscale release | View | &check; | &check; | &check; |
| | Create | &check; | &check; | &cross; |
| | Post | &check; | &check; | &cross; |
| | Continue posting | &check; | &check; | &cross; |
| | End of publication | &check; | &check; | &cross; |
| | Update | &check; | &check; | &cross; |
| | rollback | &check; | &check; | &cross; |
| | delete | &check; | &check; | &cross; |

!!! note

    For a complete introduction to role and access management, please refer to [Role and Access Management](../user-guide/access-control/role.md).