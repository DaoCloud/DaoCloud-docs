---
hide:
  - toc
---

# Create a custom pipeline

Workbench pipeline supports custom creation, and you can visually arrange the pipeline through the pipeline created in this way.

## prerequisites

- [Create Workspace](../../../../ghippo/user-guide/workspace/workspace.md), [Create User](../../../../ghippo/user-guide/access-control/user.md).
- Add the user to the workspace with __workspace editor__ or higher privileges.

## Steps

The specific operation steps are as follows:

1. Click __Create Pipeline__ on the pipeline list page.

    <!--![]()screenshots-->

2. In the pop-up dialog box, select Custom Create Pipeline and click OK.

    <!--![]()screenshots-->

3. Fill in __Basic Information__ , __Build Settings__ , and __Build Parameters__ by referring to the following instructions.

    - name: the name of the pipeline. The pipeline name must be unique under the same workspace.
    - Delete expired pipeline records: Delete previous build records to save disk space used by Jenkins.

        - Build record retention period: Up to several days of build records are kept, the default value is 7 days, that is, build records older than seven days will be deleted.
        -Maximum number of build records: keep a maximum number of build records, the default value is 10, that is, keep a maximum of 10 records. When there are more than 10 records, the oldest records are deleted first.
        - The two rules __retention period__ and __maximum number__ are in effect at the same time, as long as one of them is met, the records will be deleted.

    - Do not allow concurrent builds: When enabled, only one pipeline build task can be executed at a time.
    - Build Parameters: Pass in one or more build parameters when starting to run the pipeline. Five parameter types are provided by default: __Boolean__ , __string__ , __multiline text__ , __options__ , __password__ , __upload file__ .
    - After adding build parameters, you need to enter the corresponding value for each build parameter when running the pipeline.

        <!--![]()screenshots-->

4. Fill in the trigger parameters by referring to the following instructions.

    - Code source trigger: After it is turned on, the system will periodically scan the specific branch in the warehouse code used to build the pipeline according to the __timed warehouse scan plan__ , and re-run the pipeline if there is an update.
    - Scheduled warehouse scan schedule: Enter a CRON expression to define the time period for scanning warehouses. **After entering the expression, the meaning of the current expression will be prompted at the bottom**. For detailed expression syntax rules, please refer to [Cron Schedule Syntax](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#cron-schedule-syntax).
    - Timing trigger: Timing triggers the construction pipeline, no matter whether the code warehouse is updated or not, the pipeline will be re-run at the specified time.

        <!--![]()screenshots-->

5. Complete the creation. After confirming that all parameters have been entered, click the __OK__ button to complete the creation of the custom pipeline and automatically return to the pipeline list. Click __︙__ to the right of the list to perform various actions.

    <!--![]()screenshots-->

!!! warning

    - After a custom pipeline is created, the stages of the pipeline need to be manually defined (i.e. edit the pipeline) before the pipeline can be run. If you define the process and run the pipeline directly, there will be a __build failed__ error.
    - If you [create a pipeline based on a template](template.md) or [create a pipeline based on a Jenkinsfile](jenkins.md), you can run it directly without manually editing the pipeline.

Next step: [edit pipeline](../edit.md){ .md-button .md-button--primary }