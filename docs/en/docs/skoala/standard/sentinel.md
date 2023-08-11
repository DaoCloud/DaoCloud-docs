---
hide:
  - toc
---

# Application access Sentinel specification

In order to normally use [Sentinel traffic management](../plugins/intro.md) and view [Sentinel data monitoring](../trad-ms/hosted/monitor/components.md) provided by the DCE 5.0 micro-service engine, the application needs to be connected to the Sentinel console and certain specifications need to be met when the application parameters are passed.

## project.name parameter

The format of the project.name parameter should be: `{{nacos_namespace_id}}@@{{nacos_group}}@@{{appName}}`.

**Note**：

- When this specification is met, the Sentinel governance rules will be pushed to the configuration center under the configuration group in the corresponding namespace.

- If this specification is not met, such as only `appName` or `{{nacos_group}}@@{{appName}}`, all governance rules are pushed to the `SENTINEL_GROUP` configuration center in the `public` namespace.

- The first part `{{nacos_namespace_id}}` refers to **ID** of the Nacos namespace, not the name of the namespace.

- Nacos `public` namespace has an ID corresponding to the null character "".

- If you want to add applications to the `public` namespace, you must use an empty string, for example, `@@A@@appA`.

??? note "How to Get the Sentinel Console"

    - Download the latest version of the console jar package from the [release](https://github.com/alibaba/Sentinel/releases) page, or

    - Build the Sentinel console yourself from the latest version of the source code

        1. Download [Console](https://github.com/alibaba/Sentinel/tree/master/sentinel-dashboard) project
        2. Package the code into a fat jar using the following command: `mvn clean package`

    Refer to the official document: [Launch Console](https://sentinelguard.io/docs/dashboard.html)
