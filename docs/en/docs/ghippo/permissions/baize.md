---
MTPE: windsonsea
Date: 2024-07-24
hide:
  - toc
---

# AI Lab Permissions

[AI Lab](../../baize/intro/index.md) supports four user roles:

- Admin / Baize Owner: Has full permissions (create, read, update, delete) for all features in the `Developer` and `Operator`.
- Workspace Admin: Has full permissions (create, read, update, delete) for all features in the authorized workspace's `Developer`.
- Workspace Editor: Has update and read permissions for all features in the authorized workspace's `Developer`.
- Workspace Viewer: Has read permissions for all features in the authorized workspace's `Developer`.

Each role has different permissions, as detailed below.

<!--
Use `&check;` for permission granted, and `&cross;` for permission denied.
-->

| Menu Object | Operation | Admin / Baize Owner | Workspace Admin | Workspace Editor | Workspace Viewer |
|---------------|-------------|-----------------------|-------------------|--------------------|--------------------|
| **Developer** | | | | | |
| Overview | View Overview | &check; | &check; | &check; | &check; |
| Notebooks | View Notebooks | &check; | &check; | &check; | &check; |
| | View Notebooks Details | &check; | &check; | &check; | &cross; |
| | Create Notebooks | &check; | &check; | &cross; | &cross; |
| | Update Notebooks | &check; | &check; | &check; | &cross; |
| | Clone Notebooks | &check; | &check; | &cross; | &cross; |
| | Stop Notebooks | &check; | &check; | &check; | &cross; |
| | Start Notebooks | &check; | &check; | &check; | &cross; |
| | Delete Notebooks | &check; | &check; | &cross; | &cross; |
| Jobs | View Jobs | &check; | &check; | &check; | &check; |
| | View Job Details | &check; | &check; | &check; | &check; |
| | Create Job | &check; | &check; | &cross; | &cross; |
| | Clone Job | &check; | &check; | &cross; | &cross; |
| | View Job Load Details | &check; | &check; | &check; | &cross; |
| | Delete Job | &check; | &check; | &cross; | &cross; |
| Job Analysis | View Job Analysis | &check; | &check; | &check; | &check; |
| | View Job Analysis Details | &check; | &check; | &check; | &check; |
| | Delete Job Analysis | &check; | &check; | &cross; | &cross; |
| Datasets | View Datasets | &check; | &check; | &check; | &cross; |
| | Create Dataset | &check; | &check; | &cross; | &cross; |
| | Resync Dataset | &check; | &check; | &check; | &cross; |
| | Update Credentials | &check; | &check; | &check; | &cross; |
| | Delete Dataset | &check; | &check; | &cross; | &cross; |
| Runtime Env | View Runtime Env | &check; | &check; | &check; | &check; |
| | Create Runtime Env | &check; | &check; | &cross; | &cross; |
| | Update Runtime Env | &check; | &check; | &check; | &cross; |
| | Delete Runtime Env | &check; | &check; | &cross; | &cross; |
| Inference Services | View Inference Services | &check; | &check; | &check; | &check; |
| | View Inference Services Details | &check; | &check; | &check; | &check; |
| | Create Inference Service | &check; | &check; | &cross; | &cross; |
| | Update Inference Service | &check; | &check; | &check; | &cross; |
| | Stop Inference Service | &check; | &check; | &check; | &cross; |
| | Start Inference Service | &check; | &check; | &check; | &cross; |
| | Delete Inference Service | &check; | &check; | &cross; | &cross; |
| **Operator** | | | | | |
| Overview | View Overview | &check; | &cross; | &cross; | &cross; |
| GPU Management | View GPU Management | &check; | &cross; | &cross; | &cross; |
| Queue Management | View Queue Management | &check; | &cross; | &cross; | &cross; |
| | View Queue Details | &check; | &cross; | &cross; | &cross; |
| | Create Queue | &check; | &cross; | &cross; | &cross; |
| | Update Queue | &check; | &cross; | &cross; | &cross; |
| | Delete Queue | &check; | &cross; | &cross; | &cross; |
