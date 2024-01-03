# Unable to start Keycloak

## Symptom

MySQL is ready without any errors. After installing Global Management, Keycloak fails to start (more than 10 times).

![img](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/restart01.png)

## Checklist

- If the database is MySQL, check if the Keycloak database encoding is UTF8.

- Check the network from Keycloak to the database and ensure that the database resources are sufficient, including but not limited to resource limits, storage space, and physical machine resources.

## Solution

![img](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/restart02.png)

1. Check if MySQL resource usage has reached the limit.
2. Check if the number of tables in the Keycloak database in MySQL is 92.
3. Delete and recreate the Keycloak database, using __CREATE DATABASE IF NOT EXISTS keycloak CHARACTER SET utf8__ .
4. Restart the Keycloak Pod to resolve the issue.
