# Log Query

By default, Insight collects node logs, container logs, and Kubernetes audit logs. In the log query page, you can search for standard output (stdout) logs within the permissions of your login account. This includes node logs, product logs, and Kubernetes audit logs. You can quickly find the desired logs among a large volume of logs. Additionally, you can use the source information and contextual raw data of the logs to assist in troubleshooting and issue resolution.

## Steps

1. Click the primary navigation bar to enter __Insight__.
2. In the left navigation bar, select __Log Query__.

    - By default, the last 24 hours are queried;
    - When you enter for the first time, by default it queries the container logs of the clusters or namespaces that you have permission to access based on your login account permissions;

    ![Log Query](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/log01.png)

3. The top Tab defaults to __Normal Query__.

    1. Click __Filter__ to expand the filter panel, where you can switch log search conditions and types.
    2. Log types:

        - __Container Log__: Records the activities and events inside containers in the cluster, including application output, error messages, warnings, and debugging information, etc. Supports filtering logs by cluster, namespace, pod, and container.
        - __Node Log__: Records the system-level logs of each node in the cluster. These logs contain information about the node's operating system, kernel, services, and components. Supports filtering logs by cluster, node, and file path.

    3. Supports fuzzy search for a single keyword.

        ![Search](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/log02.png)

4. Switch the top Tab to select __Lucene Syntax Query__.

    When you enter for the first time, by default it selects the container logs of the clusters or namespaces that you have permission to query based on your login account permissions.

    ![Node](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/log03.png)

    **Lucene Syntax Explanation:**

    1. Use logical operators (AND, OR, NOT, "") to query multiple keywords. For example: keyword1 AND (keyword2 OR keyword3) NOT keyword4.
    2. Use a tilde (~) for fuzzy queries. You can optionally specify a parameter after the "~" to control the similarity of the fuzzy query. If not specified, it defaults to 0.5. For example: error~.
    3. Use wildcards (*, ?) as single-character placeholders to match any character.
    4. Use square brackets [ ] or curly braces { } for range queries. Square brackets [ ] represent a closed interval and include the boundary values. Curly braces { } represent an open interval and exclude the boundary values. Range queries are applicable only to fields that can be sorted, such as numeric fields and date fields. For example: `timestamp:[2022-01-01 TO 2022-01-31]`.
    5. For more information, please refer to the [Lucene Syntax Explanation](../../reference/lucene.md).

### Other Operations

#### View Log Context

Click the button after a log, and in the panel that slides out on the right, you can view the default 100 lines of context for that log.

- You can switch __Display Rows__ to view more context.
- You can click the icon after the search box to enable the display of time information in the context.

![view](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/log06.png)

#### Export Log Data

Click the download button in the upper right corner of the list.

- You can configure the exported log fields. The configurable fields vary depending on the log type, and the __Log Content__ field is mandatory.
- You can export the log query results in **.txt** or **.csv** format.

![export](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/log05.png)

!!! note

    If you need to specify that the logs of certain pods are not collected, please refer to: [Container Log Blacklist](../../faq/ignore-pod-log-collect.md).
