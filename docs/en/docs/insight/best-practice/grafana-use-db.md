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

1. **Initialize the Database**

    Create a new database for Grafana in your external database, and we recommend naming it `grafana`.

2. **Configure Grafana to Use the Database**

    Within the `insight-system` namespace, locate the Grafana Custom Resource (CR) named
    `insight-grafana-operator-grafana`. Update the configuration to include:

    ```yaml
    apiVersion: integreatly.org/v1alpha1
    kind: Grafana
    metadata:
      name: insight-grafana-operator-grafana
      namespace: insight-system
    spec:
      baseImage: 10.64.40.50/docker.m.daocloud.io/grafana/grafana:9.3.14
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

    After updating, your Grafana configuration file (`grafana-config`) should include the following:

    ```toml
    [database]
      host = 10.6.216.101:30782
      name = grafana
      password = grafana_password
      type = mysql
      user = grafana
    ```

    Additionally, update your `insight.yaml` file to include:

    ```yaml
    grafana-operator:
      grafana:
        config:
          database:
            type: mysql
            host: "10.6.216.101:30782"
            name: "grafana"
            user: "grafana"
            password: "grafana_password"
    ```

4. **Upgrade the Insight Server**

    It’s best to upgrade via Helm:

    ```shell
    helm upgrade insight insight/insight \
      -n insight-system \
      -f ./insight.yaml \
      --version ${version}
    ```

5. **Or Upgrade via Command Line**

    If you prefer using the command line, start by retrieving the original configuration from the Insight Helm:

    ```shell
    helm get values insight -n insight-system -o yaml > insight.yaml
    ```

    Then, specify the original configuration file while saving the Grafana database connection details:

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
