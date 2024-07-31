---
hide:
  - toc
---

# MySQL MGR Parameter Configuration

When configuring MySQL Group Replication (MGR), the `loose_` prefix is required for some parameters to ensure 
flexibility and backward compatibility. Some parameters in MySQL may be experimental or used only in certain scenarios. 
In these cases, the `loose_` prefix ensures that these parameters can be ignored.

## Examples

The following is an example of configuring MySQL Group Replication with the `loose_` prefix:

```ini
[mysqld]
# Enable Group Replication
loose_group_replication_start_on_boot=off
loose_group_replication_bootstrap_group=off
loose_group_replication_group_name="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
loose_group_replication_local_address="192.168.0.1:33061"
loose_group_replication_group_seeds="192.168.0.1:33061,192.168.0.2:33061,192.168.0.3:33061"
loose_group_replication_single_primary_mode=on
loose_group_replication_enforce_update_everywhere_checks=off

# Group Replication SSL settings (optional)
loose_group_replication_ssl_mode=REQUIRED
loose_group_replication_ssl_ca=ca.pem
loose_group_replication_ssl_cert=server-cert.pem
loose_group_replication_ssl_key=server-key.pem

# Other necessary settings
binlog_checksum=NONE
binlog_format=ROW
log_slave_updates=ON
gtid_mode=ON
enforce_gtid_consistency=ON
master_info_repository=TABLE
relay_log_info_repository=TABLE
transaction_write_set_extraction=XXHASH64
```

!!! info

    Using the `loose_` prefix is a safe practice when configuring MGR parameters, especially when running in 
    different versions or plugin states. It ensures compatibility and flexibility of configuration files 
    and avoids unwanted startup errors.