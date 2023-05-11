---
hide:
  - toc
---

# Create a custom pipeline

The App Workbench pipeline supports custom creation, and you can visually arrange the pipeline through the pipeline created in this way.

You need to create a workspace and a user who must be invited to the workspace and given the `workspace edit` role.
Refer to [Create Workspace](../../../ghippo/user-guide/workspace/Workspaces.md), [Users and Roles](../../../ghippo/user-guide/access-control/User.md).

The specific operation steps are as follows:

1. Click `Create Pipeline` on the pipeline list page.

    

2. In the pop-up dialog box, select Custom Create Pipeline and click OK.

    

3. Go to the `custom creation page` and configure related parameters.

    

4. Fill in the basic information. The name of the pipeline, which must be unique in the same workspace.

    

5. Fill in the build settings.

    

    - Delete expired build records: Determines when build records under a branch are deleted to save disk space used by Jenkins.

    - Do not allow concurrent builds: If enabled, multiple builds cannot run concurrently.

6. Fill in the build parameters.
   
    A parameterized build process allows you to pass in one or more parameters when starting to run your pipeline. Five parameter types are provided by default, including `string`, `multiline string`, `boolean`, `option` and `password`.
    When parameterizing a project, the build is replaced with a parameterized build, where the user is prompted to enter a value for each defined parameter.

    

7. Fill in the build triggers.

    

    - Code source triggering: Allows periodic execution of build pipelines.

    - Timing trigger: Allows regular execution to scan the remote code repository, and execute the build pipeline if there is a change in the code repository.

8. Complete the creation. After confirming that all parameters have been entered, click the `OK` button to complete the creation of the custom pipeline and automatically return to the pipeline list. Click `︙` to the right of the list to perform various actions.

    

## Edit pipeline

1. After the custom pipeline is created, you can click on the pipeline on the 'Pipeline List' page to enter the 'Pipeline Details' page. Then click on `Edit Pipeline`.

    

2. On the editing pipeline page, you can visually arrange the pipeline. For detailed operations, please refer to the document [Using Graphical Editing Pipeline](graphicaleditingpipeline.md)

    