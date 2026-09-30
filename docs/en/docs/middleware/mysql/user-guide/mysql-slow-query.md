# MySQL Slow Log

The MySQL slow query log is a feature provided by the MySQL database engine for recording query statements whose execution time exceeds a specified threshold.
By recording long-running query statements, it helps database administrators identify and optimize performance issues in the database. The default threshold of the MySQL slow log is 1s.
The MySQL of the data service records SQL statements in the database whose execution time exceeds 1s (you can modify the `long_query_time` parameter in **Parameter Settings** to set the threshold), and deduplicates similar statements.

## Enable the Slow Log

1. Go to the MySQL database list and click the name of the target MySQL instance to enter the instance details.
2. Click **Slow Log** in the left navigation bar and switch to the **Slow Log Management** tab.
3. Click to enable the slow log feature.

    !!! info

        Enabling the slow log feature will restart the instance!

    ![alt text](../images/slow-query.png)

## View the Slow Log

1. Go to the MySQL database list and click the name of the target MySQL instance to enter the instance details.
2. Click **Slow Log** in the left navigation bar, and select the MySQL Pod and time range you want to view.
    
    The slow log feature is disabled by default. Go to the **Slow Log Management** tab to enable it.

    ![alt text](../images/slow-query-1.png)

## Delete the Slow Log

1. Click **Slow Log** in the left navigation bar and switch to the **Slow Log Management** tab.
2. In the clear slow log module, you can view the number of slow logs of the current instance.
3. Select the MySQL Pods you want to clean up and click Delete to clear the corresponding slow log data.

!!! info

    Currently there is no automatic slow log cleaning mechanism, and it must be done manually!
