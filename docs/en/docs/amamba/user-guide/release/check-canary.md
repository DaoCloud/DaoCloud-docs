# View canary release tasks

After creating the grayscale publishing task and associating the workload, modify the image of the workload, resource configuration, startup parameters, etc. so that when the pod restarts, the grayscale publishing task update version will be automatically triggered, and traffic scheduling will be performed according to the defined publishing rules.

This article mainly introduces related operations involved in viewing canary release tasks, such as viewing task details, updating version, updating release task, rolling back version, etc.

## View task details

1. Enter the __Workbench__ module, click __Grayscale Release__ in the left navigation bar, and click the name of the target task.

    <!--![]()screenshots-->

2. View the grayscale publishing task details page.

    - __Basic Information__ area: view the name, status, release type, release object and other information of the task.

    - __Grayscale progress__ area: Display the execution progress of the grayscale publishing task in a visual form, so that you can intuitively understand which step the task is currently executing and the status of the execution.

    - __Version Info__ area:

        - Major Version: Shows the current version and canary version information.
        - Historical version: display historical version records.

          <!--![]()screenshots-->

## updated version

After the updated version of the object is published, the grayscale publishing task will be automatically triggered.

1. Click the name of the target task, then click __Update Version__ in the upper right corner.

    <!--![]()screenshots-->

2. Set up the image released by the canary.

    <!--![]()screenshots-->

3. After the application is successfully updated, a new grayscale publishing process will be triggered.

    <!--![]()screenshots-->

## Update release task

By updating the release task, you can modify the traffic scheduling strategy of the grayscale release process.

1. On the __Grayscale Publishing Task__ details page, click __ⵗ__ in the upper right corner of the page and select __Update Publishing Task__ .

    <!--![]()screenshots-->

2. Adjust the publishing rules and click __OK__ .

    <!--![]()screenshots-->

## rollback

It supports viewing historical versions released in the past, and you can roll back to a previous version with one click.

1. On the details page of the __Grayscale Publishing Task__ , click the __Historical Version__ tab.

    <!--![]()screenshots-->

2. Select the target version and click __Rollback__ .

    <!--![]()screenshots-->

3. After the rollback is successful, a new grayscale publishing process will be triggered.

    <!--![]()screenshots-->

## Other operating instructions

| Operation | |
| --- | --- |
| Continue Release | For ongoing or paused canary release tasks, continue release can push the canary release process to the next stage of release. |
| Release | For the ongoing or suspended canary release task, release can push the canary release process to complete the release directly, and update the canary version to a stable version. |
| Terminate the release | For the ongoing or suspended canary release task, terminate the release to suspend all current steps and roll back to the stable version. |