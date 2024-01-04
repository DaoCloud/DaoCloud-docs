---
hide:
  - toc
---

# Create a multi-branch pipeline

Workbench pipeline supports the creation of multi-branch pipelines based on code repositories.

## prerequisites

- [Create workspace](../../../../ghippo/user-guide/workspace/workspace/), [Create user](../../../../ghippo/user-guide/access-control/user/).
- Add the user to the workspace with __workspace editor__ or higher privileges.
- Provide a code warehouse, and the source code of the code warehouse has multiple branches, and all have Jenkinsfile text files.
- If it is a private warehouse, you need to [create warehouse access credentials](../credential.md) in advance.

## Steps

1. Click __Create Pipeline__ on the pipeline list page.

2. Select __Create multi-branch pipeline__ and click __OK__ .

    <!--![]()screenshots-->

3. Fill in the basic information and code warehouse information by referring to the instructions below.

    - name: the name of the pipeline. The pipeline name must be unique under the same workspace.
    - Description information: The user describes the feature of the current pipeline.
    - Code warehouse address: fill in the address of the remote code warehouse.
    - Credentials: For private warehouses, you need to [create repo access credentials](../credential.md) in advance and select the credentials here.
    - Script path: the absolute path of the Jenkinsfile in the code repository.

    <!--![]()screenshots-->

4. Refer to the instructions below to fill in branch discovery policy, scan trigger, branch settings, and clone configuration information.

    - Open discovery branch: the default value is __ .*__ , and the branch is filtered by regular expression.
    - Turn on multi-branch scanning: After it is turned on, once there is a branch change in the code warehouse, it will be synchronized.
    - Scanning interval: Scan the code warehouse according to the preset interval to check whether it is updated again.
    - Delete old branches: After enabled, old branches and pipelines will be deleted according to the policy
    - Days to keep: the number of days to keep the old branch and the pipeline of the old branch, and delete it after expiration.
    - Number of reservations: the number of old branches and pipeline reservations of old branches.
    - Shallow clone: ​​When enabled, pull the latest version of the code repository. Supports setting the clone depth, generally the default is 1 to speed up the pull.
    - Clone timeout: The maximum waiting time when pulling code.

        <!--![]()screenshots-->

5. Complete the creation. After confirming that all parameters have been entered, click the __OK__ button to complete the creation of the multi-branch pipeline and automatically return to the pipeline list.

    <!--![]()screenshots-->

6. After the creation is complete, the corresponding pipeline that executes the branch that meets the conditions will be automatically triggered.

    <!--![]()screenshots-->

## Other operations

### Scan warehouse

The purpose of __scan repository__ is to manually trigger the discovery of new branches of the code repository.

<!--![]()screenshots-->

### View scan log

Displays the log of the branch found during the latest scan of the code repository.

<!--![]()screenshots-->

### View Branches

The branch information obtained according to the branch discovery policy, where the branch in the __disabled__ state represents that the latest scan results do not conform to the branch discovery strategy.

<!--![]()screenshots-->