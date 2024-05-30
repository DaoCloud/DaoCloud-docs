---
hide:
  - toc
---

# Container Management Permission Description

The container management module uses the following roles:

- Admin / Kpanda Owner
- [Cluster Admin](../../kpanda/user-guide/permissions/permission-brief.md#cluster-admin)
- [NS Admin](../../kpanda/user-guide/permissions/permission-brief.md#ns-admin)
- [NS Editor](../../kpanda/user-guide/permissions/permission-brief.md#ns-edit)
- [NS Viewer](../../kpanda/user-guide/permissions/permission-brief.md#ns-view)

!!! note

    - For more information about permissions, please refer to the [Container Management Permission System Description](../../kpanda/user-guide/permissions/permission-brief.md).
    - For creating, managing, and deleting roles, please refer to [Role and Permission Management](../user-guide/access-control/role.md).
    - The permissions of __Cluster Admin__ , __NS Admin__ , __NS Editor__ , __NS Viewer__ only take effect within the current cluster or namespace.

The permissions granted to each role are as follows:

<!--
Use `&check;`for permissions granted and `&cross;`for permissions not granted.
-->

| Primary Function       | Secondary Function | Permission     | Cluster Admin | Ns Admin      | Ns Editor | NS Viewer |
| ------------ | -------------------- | -------------- | ------------- | --------------- | ------------------------ | ----------------- |
| Cluster       | Cluster List  | View Cluster List     | &#x2714;      | &#x2714;       | &#x2714;     | &#x2714;       |
|  |  | Access Cluster        | &#x2718;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | Create Cluster        | &#x2718;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  | Cluster Operations            | Enter Console         | &#x2714;      | &#x2714; (only in the list)   | &#x2714;     | &#x2718;  |
|  |  | View Monitoring       | &#x2714;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | Edit Basic Configuration     | &#x2714;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | Download kubeconfig   | &#x2714;      | &#x2714; (with ns permission) | &#x2714; (with ns permission)        | &#x2714; (with ns permission) |
|  |  | Disconnect Cluster    | &#x2718;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | View Logs             | &#x2714;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | Retry    | &#x2718;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | Uninstall Cluster     | &#x2718;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  | Cluster Overview | View Cluster Overview | &#x2714;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  | Node Management  | Access Node           | &#x2718;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | View Node List        | &#x2714;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | View Node Details     | &#x2714;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | View YAML             | &#x2714;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | Pause Scheduling      | &#x2714;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | Modify Labels         | &#x2714;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | Modify Annotations    | &#x2714;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | Modify Taints         | &#x2714;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  |  | Remove Node           | &#x2718;      | &#x2718;  | &#x2718;   | &#x2718;  |
|  | Stateless Workload            | View List             | &#x2714;      | &#x2714;       | &#x2714;     | &#x2714;       |
|  |  | View/Manage Details   | &#x2714;      | &#x2714;       | &#x2714;     | &#x2714; (view only)   |
|  |  | Create by YAML        | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Create by image       | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
| Select an instance in ws bound to ns | Select image  | &#x2714;      | &#x2714;      | &#x2714;       | &#x2718;   |
|  |  | View IP Pool          | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Edit Network Interface       | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Enter Console         | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | View Monitoring       | &#x2714;      | &#x2714;       | &#x2714;     | &#x2714;       |
|  |  | View Logs             | &#x2714;      | &#x2714;       | &#x2714;     | &#x2714;       |
|  |  | Load Balancer Scaling | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Edit YAML             | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Update   | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Status - Pause Upgrade       | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Status - Stop         | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Status - Restart      | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Delete   | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  | Stateful Workload             | View List             | &#x2714;      | &#x2714;       | &#x2714;     | &#x2714;       |
|  |  | View/Manage Details   | &#x2714;      | &#x2714;       | &#x2714;     | &#x2714; (view only)   |
|  |  | Create by YAML        | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Create by image       | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  | Select an instance in ws bound to ns | Select image          | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Enter Console         | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | View Monitoring       | &#x2714;      | &#x2714;       | &#x2714;     | &#x2714;       |
|  |  | View Logs             | &#x2714;      | &#x2714;       | &#x2714;     | &#x2714;       |
|  |  | Load Balancer Scaling | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Edit YAML             | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Update   | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Status - Stop         | &#x2714;      | &#x2714;       | &#x2714;     | &#x2718;  |
|  |  | Status - Restart      | &check;       | &check;   | &check;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | 守护进程      | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Create by YAML        | &check;       | &check;   | &check;       | &cross;   |
|  |  | Create by image       | &check;       | &check;   | &check;       | &cross;   |
|  | Select an instance in ws bound to ns | Select image          | &check;       | &check;   | &check;       | &cross;   |
|  |  | Go to console         | &check;       | &check;   | &check;       | &cross;   |
|  |  | Check monitor         | &check;       | &check;   | &check;       | &check;   |
|  |  | View logs             | &check;       | &check;   | &check;       | &check;   |
|  |  | Edit YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Update   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Status - restart      | &check;       | &check;   | &check;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | Job   | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Create by YAML        | &check;       | &check;   | &check;       | &cross;   |
|  |  | Create by image       | &check;       | &check;   | &check;       | &cross;   |
|  |  | Instance list         | &check;       | &check;   | &check;       | &check;   |
|  | Select an instance in ws bound to ns | Select image          | &check;       | &check;   | &check;       | &cross;   |
|  |  | Go to console         | &check;       | &check;   | &check;       | &cross;   |
|  |  | View logs             | &check;       | &check;   | &check;       | &check;   |
|  |  | View YAML             | &check;       | &check;   | &check;       | &check;   |
|  |  | Restart  | &check;       | &check;   | &check;       | &cross;   |
|  |  | View event            | &check;       | &check;   | &check;       | &check;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | CronJob       | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Create by YAML        | &check;       | &check;   | &check;       | &cross;   |
|  |  | Create by image       | &check;       | &check;   | &check;       | &cross;   |
|  | Select an instance in ws bound to ns | Select image          | &check;       | &check;   | &check;       | &cross;   |
|  |  | Edit YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Stop  | &check;       | &check;   | &check;       | &cross;   |
|  |  | View jobs             | &check;       | &check;   | &check;       | &check;   |
|  |  | View event            | &check;       | &check;   | &check;       | &check;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | Pod    | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Go to console         | &check;       | &check;   | &check;       | &cross;   |
|  |  | Check monitor         | &check;       | &check;   | &check;       | &check;   |
|  |  | View logs             | &check;       | &check;   | &check;       | &check;   |
|  |  | View YAML             | &check;       | &check;   | &check;       | &check;   |
|  |  | Upload file           | &check;       | &check;   | &check;       | &cross;   |
|  |  | Download file         | &check;       | &check;   | &check;       | &cross;   |
|  |  | View containers       | &check;       | &check;   | &check;       | &check;   |
|  |  | View event            | &check;       | &check;   | &check;       | &check;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | ReplicaSet    | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Go to console         | &check;       | &check;   | &check;       | &cross;   |
|  |  | Check monitor         | &check;       | &check;   | &check;       | &check;   |
|  |  | View logs             | &check;       | &check;   | &check;       | &check;   |
|  |  | View YAML             | &check;       | &check;   | &check;       | &check;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | Helm app      | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Update   | &check;       | &check;   | &check;       | &cross;   |
|  |  | View YAML             | &check;       | &check;   | &check;       | &check;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | Helm chart    | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View details          | &check;       | &check;   | &check;       | &check;   |
|  |  | Install chart         | &check;       | &check; (Fine for ns level)   | &cross;       | &cross;   |
|  |  | Download chart        | &check;       | &check;   | &check; (Consistent with viewing interface) | &check;   |
|  | Helm repo     | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | Create repo           | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Update repo           | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Clone repo            | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Refresh repo          | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Modify label          | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Modify annotation     | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &cross;   | &cross;       | &cross;   |
|  | Service       | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Create by YAML        | &check;       | &check;   | &check;       | &cross;   |
|  |  | Create   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Update   | &check;       | &check;   | &check;       | &cross;   |
|  |  | View event            | &check;       | &check;   | &check;       | &check;   |
|  |  | Edit YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | Ingress       | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Create by YAML        | &check;       | &check;   | &check;       | &cross;   |
|  |  | Create   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Update   | &check;       | &check;   | &check;       | &cross;   |
|  |  | View event            | &check;       | &check;   | &check;       | &check;   |
|  |  | Edit YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | Network policy   | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Create by YAML        | &check;       | &check;   | &check;       | &cross;   |
|  |  | Create   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | Network config   | Config   | &check;       | &check;   | &check;       | &cross;   |
|  | CRD    | View list             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View/Manage details   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Create by YAML        | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Edit YAML             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &cross;   | &cross;       | &cross;   |
|  | PVC    | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Create   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Select sc             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Create by YAML        | &check;       | &check;   | &check;       | &cross;   |
|  |  | Edit YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Clone    | &check;       | &check;   | &check;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | PV     | View list             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View/Manage details   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Create by YAML        | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Create   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Edit YAML             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Update   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Clone    | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Modify label          | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Modify annotation     | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &cross;   | &cross;       | &cross;   |
|  | SC     | View list             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Create by YAML        | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Create   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View YAML             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Update   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Authorize NS          | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Deauthorize           | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &cross;   | &cross;       | &cross;   |
|  | ConfigMap     | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Create by YAML        | &check;       | &check;   | &check;       | &cross;   |
|  |  | Create   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Edit YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Update   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Export ConfigMap      | &check;       | &check;   | &check;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | Secret | View list             | &check;       | &check;   | &check;       | &cross;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Create by YAML        | &check;       | &check;   | &check;       | &cross;   |
|  |  | Create   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Edit YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Update   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Export secret         | &check;       | &check;   | &check;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | Namespace     | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Create by YAML        | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Create   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Modify label          | &check;       | &check;   | &cross;       | &cross;   |
|  |  | Unbind WS             | &cross;       | &cross;   | &cross;       | &cross;   |
|  |  | Bind WS  | &cross;       | &cross;   | &cross;       | &cross;   |
|  |  | Quotas   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &cross;   | &cross;       | &cross;   |
|  | Cluster operation             | View list             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View YAML             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View logs             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &cross;   | &cross;       | &cross;   |
|  | Helm operation   | Set preserved entries | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View YAML             | &check;       | &check;   | &cross;       | &cross;   |
|  |  | View logs             | &check;       | &check;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &cross;       | &cross;   |
|  | Cluster upgrade  | View details          | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Upgrade  | &cross;       | &cross;   | &cross;       | &cross;   |
|  | Cluster settings      | Addon config        | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Advanced config | &check;       | &cross;   | &cross;       | &cross;   |
| Namespace      |  | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | Create   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check;   |
|  |  | View YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Modify label          | &check;       | &check;   | &cross;       | &cross;   |
|  |  | Bind WS          | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Quotas | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &cross;   | &cross;       | &cross;   |
| Workload      | Deployment    | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Go to console         | &check;       | &check;   | &check;       | &cross;   |
|  |  | Check monitor         | &check;       | &check;   | &check;       | &check;   |
|  |  | View logs             | &check;       | &check;   | &check;       | &check;   |
|  |  | Workload scaling      | &check;       | &check;   | &check;       | &cross;   |
|  |  | Edit YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Update   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Status - Pause Upgrade       | &check;       | &check;   | &check;       | &cross;   |
|  |  | Status - Stop         | &check;       | &check;   | &check;       | &cross;   |
|  |  | Status - restart      | &check;       | &check;   | &check;       | &cross;   |
|  |  | Revert   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Modify label and annotation  | &check;       | &check;   | &check;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | StatefulSet   | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Go to console         | &check;       | &check;   | &check;       | &cross;   |
|  |  | Check monitor         | &check;       | &check;   | &check;       | &check;   |
|  |  | View logs             | &check;       | &check;   | &check;       | &check;   |
|  |  | Workload scaling      | &check;       | &check;   | &check;       | &cross;   |
|  |  | Edit YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Update   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Status - Stop         | &check;       | &check;   | &check;       | &cross;   |
|  |  | Status - restart      | &check;       | &check;   | &check;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | DaemonSet     | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Go to console         | &check;       | &check;   | &check;       | &cross;   |
|  |  | Check monitor         | &check;       | &check;   | &check;       | &check;   |
|  |  | View logs             | &check;       | &check;   | &check;       | &check;   |
|  |  | Edit YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Update   | &check;       | &check;   | &check;       | &cross;   |
|  |  | Status - restart      | &check;       | &check;   | &check;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | Job    | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Go to console         | &check;       | &check;   | &check;       | &cross;   |
|  |  | View logs             | &check;       | &check;   | &check;       | &check;   |
|  |  | View YAML             | &check;       | &check;   | &check;       | &cross;   |
|  |  | Restart  | &check;       | &check;   | &check;       | &cross;   |
|  |  | View event            | &check;       | &check;   | &check;       | &check;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | CronJob       | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | View event            | &check;       | &check;   | &check;       | &check;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
|  | Pod    | View list             | &check;       | &check;   | &check;       | &check;   |
|  |  | View/Manage details   | &check;       | &check;   | &check;       | &check; (Only view)    |
|  |  | Go to console         | &check;       | &check;   | &check;       | &cross;   |
|  |  | Check monitor         | &check;       | &check;   | &check;       | &check;   |
|  |  | View logs             | &check;       | &check;   | &check;       | &check;   |
|  |  | View YAML             | &check;       | &check;   | &check;       | &check;   |
|  |  | Upload file           | &check;       | &check;   | &check;       | &cross;   |
|  |  | Download file         | &check;       | &check;   | &check;       | &cross;   |
|  |  | View containers       | &check;       | &check;   | &check;       | &check;   |
|  |  | View event            | &check;       | &check;   | &check;       | &check;   |
|  |  | Delete   | &check;       | &check;   | &check;       | &cross;   |
| Backup and Restore            | App backup    | View list             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View/Manage details   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Create backup schedule       | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View YAML             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Update Schedule           | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Pause    | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Run now  | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &cross;   | &cross;       | &cross;   |
|  | Resume backup    | View list             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View/Manage details   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Resume backup         | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &cross;   | &cross;       | &cross;   |
|  | Backup point  | View list             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &cross;   | &cross;       | &cross;   |
|  | Object storage   | View list             | &check;       | &cross;   | &cross;       | &cross;   |
|  | etcd backup   | View backup policies  | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Create backup policies       | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View logs             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View YAML             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Update backup policy  | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Stop/Start            | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Run now  | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View/Manage details   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete backup records | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View backup points    | &check;       | &cross;   | &cross;       | &cross;   |
| Cluster inspection            | Cluster inspection            | View list             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View/Manage details   | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Cluster inspection    | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Settings | &check;       | &cross;   | &cross;       | &cross;   |
| Permissions   | Permissions   | View list             | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Grant to cluster admin       | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &cross;   | &cross;       | &cross;   |
|  | NS permissions   | View list             | &check;       | &check;   | &cross;       | &cross;   |
|  |  | Grant to ns admin     | &check;       | &check;   | &cross;       | &cross;   |
|  |  | Grant to ns editor      | &check;       | &check;   | &cross;       | &cross;   |
|  |  | Grant to ns viewer      | &check;       | &check;   | &cross;       | &cross;   |
|  |  | Edit permissions      | &check;       | &check;   | &cross;       | &cross;   |
|  |  | Delete   | &check;       | &check;   | &cross;       | &cross;   |
| Security      | Compliance scanning           | View scanning report  | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View scanning report details | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Download scanning report     | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete scanning report       | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View scanning policies       | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Create scanning policy       | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete scanning policy       | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View scanning config list    | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View scanning config details | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete scanning config       | &check;       | &cross;   | &cross;       | &cross;   |
|  | Scan permission  | View scanning reports | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View scanning report details | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete scanning report       | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View scanning policies    | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Create scanning policy       | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete scanning policy       | &check;       | &cross;   | &cross;       | &cross;   |
|  | Scan vulnerability            | View scanning reports | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View scanning report detail  | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete scanning report       | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | View scanning policies       | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Create scanning policy       | &check;       | &cross;   | &cross;       | &cross;   |
|  |  | Delete scanning policy       | &check;       | &cross;   | &cross;       | &cross;   |
