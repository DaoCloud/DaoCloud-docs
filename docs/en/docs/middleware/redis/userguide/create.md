# Create a Redis instance

After accessing the Redis cache service, follow the steps below to create a Redis instance.

1. In the instance list of the Redis cache service, click the `New Deployment` button.

    ![Basic Information](../images/create00.png)

2. On the `Create Redis Instance` page, after configuring `Basic Information`, click `Next`.

    ![Basic Information](../images/create01.png)

3. After selecting the deployment type, CPU, memory and storage, etc. `Specification Configuration`, click `Next`.

    ![Specification Configuration](../images/create02.png)

4. Set `service settings` such as user name and password, and use ClusterIP as the access method by default.

    ![Service Settings](../images/create03.png)

5. After confirming that the basic information, specification configuration, and service settings are correct, click `Confirm`.

    ![Confirm](../images/create04.png)

6. Return to the instance list, and the screen will prompt `Instance created successfully`. The status of the newly created instance is `Not Ready`, and it will become `Running` after a while.

    ![Created Successfully](../images/create05.png)