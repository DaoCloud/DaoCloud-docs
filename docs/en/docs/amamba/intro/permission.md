---
hide:
  - toc
---

# Apply workbench permission description

[Workbench](./what.md) Three user roles are supported:

- Workspace Admin
- Workspace Editor
- Workspace Viewer

Each role has different rights, as described below.

<!--
mark yes by `&check;` and no by `&cross;`
-->

| Object |operation| Workspace Admin | Workspace Editor | Workspace Viewer |
| -------- | ---------------------------------- | --------------- | ---------------- | ---------------- |
| Application     |Viewing the application list| &check;         | &check;          | &check;          |
|          |View details (Jump to Container Management)| &check;         | &check;          | &check;          |
|          |Viewing application logs (Jump to Observable)| &check;         | &check;          | &check;          |
|          |View Application Monitor (Skip to Observable)| &check;         | &check;          | &check;          |
|          |View RabbitMQ details – Basic information| &check;         | &check;          | &check;          |
|          |View the Service grid (Jump to the Service Grid)| &check;         | &check;          | &check;          |
|          |View the Microservice Engine (Skip to Microservice Engine)| &check;         | &check;          | &check;          |
|          |Create an application| &check;         | &check;          | &cross;          |
|          |Editor YAML| &check;         | &check;          | &cross;          |
|          |Update the number of copies| &check;         | &check;          | &cross;          |
|          |Update container image| &check;         | &check;          | &cross;          |
|          |Editing pipeline| &check;         | &check;          | &cross;          |
|          |Application grouping| &check;         | &check;          | &cross;          |
|          |delete| &check;         | &check;          | &cross;          |
| Namespace |view| &check;         | &check;          | &check;          |
|          |create| &check;         | &cross;          | &cross;          |
|          |Edit tag| &check;         | &cross;          | &cross;          |
|          |Edit resource quota| &check;         | &cross;          | &cross;          |
|          |delete| &check;         | &cross;          | &cross;          |
| Pipeline   |View pipeline| &check;         | &check;          | &check;          |
|          |View running record| &check;         | &check;          | &check;          |
|          |create| &check;         | &check;          | &cross;          |
|          |run| &check;         | &check;          | &cross;          |
|          |delete| &check;         | &check;          | &cross;          |
|          |copy| &check;         | &check;          | &cross;          |
|          |edit| &check;         | &check;          | &cross;          |
|          |Cancel run| &check;         | &check;          | &cross;          |
| Credential     |view| &check;         | &check;          | &check;          |
|          |create| &check;         | &check;          | &cross;          |
|          |edit| &check;         | &check;          | &cross;          |
|          |delete| &check;         | &check;          | &cross;          |
| GitOps |view| &check;         | &check;          | &check;          |
|          |create| &check;         | &check;          | &cross;          |
|          |synchronization| &check;         | &check;          | &cross;          |
|          |edit| &check;         | &check;          | &cross;          |
|          |delete| &check;         | &check;          | &check;          |
| Code Repo |view| &check;         | &check;          | &cross;          |
|          |import| &check;         | &check;          | &cross;          |
|          |delete| &check;         | &check;          | &cross;          |
| Grayscale Release |view| &check;         | &check;          | &check;          |
|          |create| &check;         | &check;          | &cross;          |
|          |release| &check;         | &check;          | &cross;          |
|          |Continue to publish| &check;         | &check;          | &cross;          |
|          |Termination of publication| &check;         | &check;          | &cross;          |
|          |update| &check;         | &check;          | &cross;          |
|          |rollback| &check;         | &check;          | &cross;          |
|          |delete| &check;         | &check;          | &cross;          |
