# keycloak failed to start

## Failure performance

MySQL is ready without errors. keycloak fails to start after installing global management (>10 times).



## Check items

- If the database is MySQL, check if the keycloak database encoding is UTF8.

- Check the network from keycloak to the database, and check whether the database resources are sufficient, including but not limited to resource constraints, storage space, and physical machine resources.

## Resolution steps



1. Check whether the MySQL resource usage reaches the limit limit
2. Check whether the number of database keycloak table in MySQL is 92
3. Delete the keycloak database and create it, prompt `CREATE DATABASE IF NOT EXISTS keycloak CHARACTER SET utf8`
4. Restart the keycloak Pod to solve the problem