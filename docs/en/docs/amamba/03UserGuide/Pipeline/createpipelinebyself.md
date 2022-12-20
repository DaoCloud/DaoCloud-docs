---
hide:
  - toc
---

# Create a custom pipeline

The application workbench pipeline supports custom creation, and you can visually arrange the pipeline through the pipeline created in this way.

You need to create a workspace and a user who must be invited to the workspace and given the `workspace edit` role.
Refer to [Create Workspace](../../../ghippo/04UserGuide/02Workspace/Workspaces.md), [Users and Roles](../../../ghippo/04UserGuide/01UserandAccess/User .md).

The specific operation steps are as follows:

1. Click `Create Pipeline` on the pipeline list page.

    ![createpipelinbutton](../../images/createpipelinbutton.png)

2. In the pop-up dialog box, select Custom Create Pipeline and click OK.

    ![selecttype](../../images/selecttype.png)

3. Go to the `custom creation page` and configure related parameters.

    ![customizepage](../../images/customizepage.png)

4. Fill in the basic information. The name of the pipeline, which must be unique in the same workspace.

    ![pipeline01](../../images/pipeline01.png)

5. Fill in the build settings.

    ![pipeline02](../../images/pipeline02.png)

    - Delete expired build records: Determines when build records under a branch are deleted to save disk space used by Jenkins.

    - Do not allow concurrent builds: If enabled, multiple builds cannot run concurrently.

6. Fill in the build parameters.
   
    A parameterized build process allows you to pass in one or more parameters when starting to run your pipeline. Five parameter types are provided by default, including `string`, `multiline string`, `boolean`, `option` and `password`.
    When parameterizing a project, the build is replaced with a parameterized build, where the user is prompted to enter a value for each defined parameter.

    ![pipeline03](../../images/pipeline03.png)

7. Fill in the build triggers.

    ![pipeline04](../../images/pipeline04.png)

    - Code source triggering: Allows periodic execution of build pipelines.

    - Timing trigger: Allows regular execution to scan the remote code repository, and execute the build pipeline if there is a change in the code repository.

8. Complete the creation. After confirming that all parameters have been entered, click the `OK` button to complete the creation of the custom pipeline and automatically return to the pipeline list. Click `︙` to the right of the list to perform various actions.

    ![pipeline05](../../images/pipeline05.png)

## Edit pipeline

1. After the custom pipeline is created, you can click on the pipeline on the 'Pipeline List' page to enter the 'Pipeline Details' page. Then click on `Edit Pipeline`.

    ![pipelinedetail](../../images/pipelinedetail.png)

2. On the editing pipeline page, you can visually arrange the pipeline. For detailed operations, please refer to the document [Using Graphical Editing Pipeline](graphicaleditingpipeline.md)

    ![editpipeline](../../images/editpipeline.png)