---
hide:
  - toc
---

# Failure to Upgrade Global Management Separately

If the upgrade fails and includes the following message, you can refer to the
[Offline Upgrade](../install/offline-install.md#__tabbed_3_2) section to complete
the installation of CRDs by following the steps for updating the ghippo crd.

```console
ensure CRDs are installed first
```

## Database Migration Error

### Symptoms

Pod fails to start, and the following log message appears:

```console
init database failed    {"error": "migrate failed: Dirty database version 0. Fix and force version."}
```

### Causes

This error usually occurs due to issues such as abnormal environment conditions, inconsistent database state,
or SQL syntax errors. The real database error message is only output the first time the Pod reports the failure;
subsequent restarts will show the generic “dirty database” error.

### Solution

1. Log in to MySQL and select the database corresponding to the failed service
   (possible databases include `audit` and `ghippo`).

2. Update the `dirty` field in the `schema_migrations` table:

    ```console
    update schema_migrations set dirty=0;
    ```

3. Restart the failed service.

4. If the SQL migration still fails after the restart, it may be due to an actual issue in the SQL statements.
   In this case, report a bug and contact the development team for resolution.
