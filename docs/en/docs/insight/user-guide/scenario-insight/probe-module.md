# Custom Probe Methods

In this page, we will explain how to configure custom probe methods in an existing Blackbox ConfigMap.
We will use the HTTP probe method as an example to demonstrate how to modify the ConfigMap to achieve custom HTTP probing.

## Procedure

1. Go to the cluster list in `Container Management` and enter the details of the target cluster.
2. Click on the left navigation pane and select `Configurations & Secrets` > `ConfigMaps`.
3. Find the configuration item named `insight-agent-prometheus-blackbox-exporter` and click `Edit YAML` in the actions.
   
    - Add custom probe methods under `modules`. Here we use the HTTP probe method as an example:

    ```yaml
    module:
      http_2xx:
        prober: http
        timeout: 5s
        http:
          valid_http_versions: [HTTP/1.1, HTTP/2]
          valid_status_codes: []  # Defaults to 2xx
          method: GET
    ```

!!! Info

    For more probe methods, refer to [blackbox_exporter Configuration](https://github.com/prometheus/blackbox_exporter/blob/master/CONFIGURATION.md).
