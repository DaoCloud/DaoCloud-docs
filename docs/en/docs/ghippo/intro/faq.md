---
hide:
  - toc
---

# Global Management FAQs

This page collects troubleshooting ideas and solutions for common issues encountered while using Global Management (Ghippo).

??? "istio-ingressgateway cannot start after restarting the cluster (virtual machine)"

    The error message is as shown in the following image:

    ![istio-ingressgateway startup error](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/bug01.png)

    **Possible cause:**

    The `jwtsUri` address of the RequestAuthentication CR cannot be accessed, causing istiod to be unable to push the configuration to istio-ingressgateway (This bug can be avoided in Istio 1.15: [istio/istio#39341](https://github.com/istio/istio/pull/39341/files)).

    **Solution:**

    1. Back up the RequestAuthentication ghippo CR.

        ```shell
        kubectl get RequestAuthentication ghippo -n istio-system -o yaml > ghippo-ra.yaml
        ```

    2. Delete the RequestAuthentication ghippo CR.

        ```shell
        kubectl delete RequestAuthentication ghippo -n istio-system
        ```

    3. Restart Istio.

        ```shell
        kubectl rollout restart deploy/istiod -n istio-system
        kubectl rollout restart deploy/istio-ingressgateway -n istio-system
        ```

    4. Reapply the RequestAuthentication ghippo CR.

        ```shell
        kubectl apply -f ghippo-ra.yaml
        ```

        !!! warning

            Before applying the RequestAuthentication ghippo CR, make sure that ghippo-apiserver
            and ghippo-keycloak are started correctly.

??? "Infinite login loop with a 401 or 403 error"

    **Possible cause:**

    The MySQL database connected to ghippo-keycloak has failed, causing __OIDC Public keys__ to be reset.

    In Global Management v0.11.1 and later versions, follow the steps below to restore normal operation using __helm__ to update the Global Management configuration file.

    ```shell
    # Update the Helm repository
    helm repo update ghippo

    # Back up the ghippo parameters
    helm get values ghippo -n ghippo-system -o yaml > ghippo-values-bak.yaml

    # Get the version of the currently deployed ghippo
    version=$(helm get notes ghippo -n ghippo-system | grep "Chart Version" | awk -F ': ' '{ print $2 }')

    # Run the update so that the configuration file takes effect
    helm upgrade ghippo ghippo/ghippo \
      -n ghippo-system \
      -f ./ghippo-values-bak.yaml \
      --version ${version}
    ```

??? "Keycloak cannot start"

    MySQL is ready with no errors reported. After Global Management is installed, Keycloak cannot start (restarted more than 10 times).

    ![Keycloak restart error](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/restart01.png)

    **Checks:**

    - If the database is MySQL, check whether the keycloak database character encoding is UTF8.
    - Check the network from Keycloak to the database, and check whether database resources are sufficient, including but not limited to resource limits, storage space, and physical machine resources.

    **Solution:**

    ![Keycloak solution steps](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/restart02.png)

    1. Check whether MySQL resource usage has reached the limit.
    2. Check whether the number of tables in the keycloak database in MySQL is 95. (The number of Keycloak database tables may vary across versions. You can compare it with the number of Keycloak database tables in a development or test environment of the same version.) If the number is smaller, the database table initialization has failed (command to query the number of tables: `show tables;`).
    3. Delete the keycloak database and recreate it:

        ```sql
        CREATE DATABASE IF NOT EXISTS keycloak CHARACTER SET utf8;
        ```

    4. Restart the Keycloak Pod to resolve the issue.

??? "Keycloak cannot start and reports that the CPU does not support x86-64-v2"

    Keycloak cannot start normally, the keycloak pod status is `CrashLoopBackOff`,
    and the keycloak log shows the following message:

    ![Keycloak CPU does not support x86-64-v2](../images/14.png)

    **Checks:**

    Run the following check script to query the feature level of the x86-64 architecture of the current node CPU:

    ```bash
    cat <<"EOF" > detect-cpu.sh
    #!/bin/sh -eu

    flags=$(cat /proc/cpuinfo | grep flags | head -n 1 | cut -d: -f2)

    supports_v2='awk "/cx16/&&/lahf/&&/popcnt/&&/sse4_1/&&/sse4_2/&&/ssse3/ {found=1} END {exit !found}"'
    supports_v3='awk "/avx/&&/avx2/&&/bmi1/&&/bmi2/&&/f16c/&&/fma/&&/abm/&&/movbe/&&/xsave/ {found=1} END {exit !found}"'
    supports_v4='awk "/avx512f/&&/avx512bw/&&/avx512cd/&&/avx512dq/&&/avx512vl/ {found=1} END {exit !found}"'

    echo "$flags" | eval $supports_v2 || exit 2 && echo "CPU supports x86-64-v2"
    echo "$flags" | eval $supports_v3 || exit 3 && echo "CPU supports x86-64-v3"
    echo "$flags" | eval $supports_v4 || exit 4 && echo "CPU supports x86-64-v4"
    EOF

    chmod +x detect-cpu.sh
    sh detect-cpu.sh
    ```

    Run the following command to view the features of the current CPU. If the output contains `sse4_2`,
    your processor supports SSE 4.2.

    ```bash
    lscpu | grep sse4_2
    ```

    **Solution:**

    You need to upgrade the CPU of your virtual machine or physical machine to support x86-64-v2 or later,
    and make sure the x86 CPU instruction set supports SSE 4.2. For how to upgrade, consult your virtual machine platform provider or physical machine provider.

    See also: [keycloak/keycloak#17290](https://github.com/keycloak/keycloak/issues/17290)

??? "A CRD not updated error appears when upgrading Global Management separately"

    If the upgrade failure includes the following message, refer to the "Update ghippo CRD" steps in
    [Offline Upgrade](../install/offline-install.md#__tabbed_3_2) to complete the CRD installation.

    ```console
    ensure CRDs are installed first
    ```

??? "A database migration error appears when upgrading Global Management separately"

    Pod fails to start, and the following log message appears:

    ```console
    init database failed    {"error": "migrate failed: Dirty database version 0. Fix and force version."}
    ```

    **Cause:**

    The SQL migration fails due to issues such as abnormal environment conditions, inconsistent database state,
    or SQL syntax errors. The real database error message is only output the first time the Pod reports the failure;
    subsequent restarts will show the error above.

    **Solution:**

    1. Log in to MySQL and select the database corresponding to the failed service (possible databases include `audit` and `ghippo`).
    2. Update the `dirty` field in the `schema_migrations` table:

        ```sql
        UPDATE schema_migrations SET dirty = 0;
        ```

    3. Restart the failed service.

    4. If the SQL migration still fails after the restart, it may be due to an actual issue in the SQL statements.
       In this case, report a bug and contact the development team for resolution.
