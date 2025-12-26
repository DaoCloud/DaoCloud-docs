# Persisting Insight Grafana Data to a Database

Insight adopts a cloud-native approach using `GrafanaOperator` and `CRD` to leverage Grafana
effectively. We recommend using the `GrafanaDashboard` Custom Resource Definition (CRD) to
define the JSON data for dashboards. This allows for easy addition, deletion, and modification
of dashboards through `GrafanaDashboard`.

By default, Grafana utilizes SQLite3 as its local database to store configuration details
such as users, dashboards, alerts, and more. When an administrator creates or imports a
dashboard via the UI, the data is temporarily stored in SQLite3. Upon Grafana's restart,
all dashboard data will revert to what is defined by the GrafanaDashboard CR, meaning any
dashboards created, deleted, or modified through the UI will be completely reset.

Grafana also supports external databases like MySQL and PostgreSQL as alternatives to
the built-in SQLite3 storage. This document outlines how to configure an external
database for the Grafana instance provided by Insight.

## Using an External Database

Based on the official Grafana documentation (as of image version 9.3.14), follow
these steps to set up an external database, using MySQL as an example:

1. Create a new database in your external database (MySQL/PostgreSQL).
2. Configure Grafana to connect to this database (additional steps are needed for MySQL's MGR mode).

## Step-by-Step Instructions

### Method 1

1. **Initialize the Database**

    Create a new database for Grafana in your external database, and we recommend naming it `grafana`.

2. **Configure Grafana to Use the Database**

    Within the `insight-system` namespace, locate the Grafana Custom Resource (CR) named
    `insight-grafana-operator-grafana`. Update the configuration to include:

    ```diff
    apiVersion: grafana.integreatly.org/v1beta1
    kind: Grafana
    metadata:
      name: grafana
      namespace: insight-system
    spec:
      config:
        # Add the following fields
    +   database:
    +     type: mysql # Options include mysql, postgres
    +     host: "10.6.216.101:30782" # Database endpoint
    +     name: "grafana"  # Pre-created database
    +     user: "grafana"
    +     password: "grafana_password"
    ```

3. **Verify the Configuration**

    After updating, your Grafana configuration file (`grafana-ini`) should include the following:

    ```toml
    [database]
      host = 10.6.216.101:30782
      name = grafana
      password = grafana_password
      type = mysql
      user = grafana
    ```

### Method 2

1. **Initialize the Database**

    Create a new database for Grafana in your external database, and we recommend naming it `grafana`.

2. **Get the original value from the insight**

    ```shell
    helm get values insight -n insight-system -o yaml > insight.yaml
    ```

3. **Upgrade insight with database connection details**

    ```shell
    helm upgrade --install \
        --version ${version} \
        insight insight/insight -n insight-system \
        -f ./insight.yaml \
        --set grafana-operator.grafana.config.database.type=mysql \
        --set grafana-operator.grafana.config.database.host=10.6.216.101:30782 \
        --set grafana-operator.grafana.config.database.name=grafana \
        --set grafana-operator.grafana.config.database.user=grafana \
        --set grafana-operator.grafana.config.database.password=grafana_password 
    ```

## Important Notes

1. **Will user changes to built-in dashboards lead to upgrade failures?**

    Yes. If a user modifies Dashboard A (version 1.1) and Insight upgrades Dashboard A to
    v2.0, after the upgrade (which includes updating the image), the user will still see
    v1.1, and v2.0 will not be reflected in their environment.

2. **Potential issues when using MySQL in MGR mode could prevent grafana-deployment from starting properly.**

    This issue arises because the `alert_rule_tag_v1` and `annotation_tag_v2` tables lack primary keys,
    which are required in MySQL MGR mode.

    **Solution:** Temporarily add primary keys to the `alert_rule_tag_v1` and `annotation_tag_v2` tables:

    ```SQL
    ALTER TABLE alert_rule_tag_v1
        ADD CONSTRAINT alert_rule_tag_v1_pk
            PRIMARY KEY (tag_id, alert_id);
        
    ALTER TABLE annotation_tag_v2
        ADD CONSTRAINT annotation_tag_v2_pk
            PRIMARY KEY (tag_id, annotation_id);
    ```

3. **Enabling Grafana persistent database before upgrading Insight will cause permission issues such as inability to log 
   in with the upgraded grafana admin user and failure to create dashboards.**

    Root Cause: After Insight is upgraded, the admin password in the `grafana-admin-credentials` Secret is updated, 
    but the password of the admin user in the `grafana.user` table of the database is the one written during database initialization,
    resulting in a password conflict for the admin user and authentication failure.

    There are two solutions to this problem:

    **Solution 1: Fix the grafana admin password**

    Before upgrading Insight, add the following configuration to insight.yaml to fix the grafana password:

    ```diff
    grafana-operator:
      grafana:
        config:
          security:
            admin_user: admin
    +       admin_password: F4R1an5D2oPMRg==
    ```

    **Solution 2: Update the latest admin password to the database**

    Run the code according to the comments at https://go.dev/play, execute the generated SQL in the database, 
    and finally restart the grafana pod:

    ```go
    package main

    import (
      "fmt"

      "github.com/grafana/grafana/pkg/util"
    )

    func main() {
      sql := "UPDATE grafana.`user` SET password = '%s' WHERE login = 'admin';" // SQL update template
      salt := "JjTJT3vlVE"                                                      // Retrieve the salt via SQL query: SELECT salt FROM grafana.`user` WHERE login = 'admin';
      password := "yR1IQmNqHKjchw=="                                            // The value of GF_SECURITY_ADMIN_PASSWORD in the grafana-admin-credentials secret under the insight-system namespace
      encodeStr := util.EncodePassword(password, salt)
      fmt.Println(fmt.Sprintf(sql, encodeStr))                                  // Execute the output command in the database
      // Example output: UPDATE grafana.`user` SET password = '243c6eecaebe959d33f8f96563c6ada760efb6a2da8e46699550a8d33f28ab3a0317cb8abc3a392accea6229f6dd535173ff' WHERE login = 'admin';
    }
    ```