---
MTPE: FanLin
Date: 2024-01-15
---

# Integrate Toolchain

DevOps toolchain is a set of tools that enables DevOps teams to collaborate and address key DevOps fundamentals throughout the product lifecycle.

Workbench supports tool chain integration from two perspectives: workspace integration and administrator integration. Instances integrated by administrators can be assigned to workspaces for use in workspaces.

## Support for integrated toolchains

| Toolchain Name | Description | Authentication | Remarks |
| --------------- | ----------- | -------------- | -------- |
| GitLab | After integrating the GitLab repository, it can be used in the pipeline | Personal Access Token, path to obtain: Top right avatar -> **Settings** -> **Access Tokens** -> **Create personal access token** | When creating a personal access token, you must select `api`, and it must be the user's personal token. |
| Jira | By integrating Jira in the application workbench, it supports tracking of Jira -> Issue | Username/Password | - |
| Jenkins | After integrating Jenkins, all workspaces will have the pipeline capability for building | Username/Password | Only administrators can integrate, and the entire platform can only integrate Jenkins once. |
| SonarQube | After integrating SonarQube, code quality scans can be defined in the pipeline | User-Token, path to obtain: **My Account** -> **Profile** -> **Security** -> **Generate Token** (Note: Select User-Token type) | - |
| Nexus | Nexus is a software repository management tool | Username/Password | - |
| TestLink | TestLink is a test case management tool that provides a collaborative platform for creating, managing, and executing test cases, and supports defect management integration | Token | - |

## Steps

1. Enter the __Toolchain Integration__ page and click the __Toolchain Integration__ button.

    ![Toolchain Integration](../../images/tool01.png)

2. Refer to the following instructions to configure related parameters:

    - Tools: Select a toolchain type to integrate.
    - Integration Name: the name of the integration tool, which cannot be repeated.
    - Jira URL: The address where the toolchain can be accessed, the domain name or IP address starting with http://, https://.
    - Username and password: the user and password that can log in to the toolchain,

    ![Configure Parameters](../../images/tool02.png)

3. Click __OK__ , the integration is successful and return to the toolchain list page.

    ![Successfully Created](../../images/tool03.png)
