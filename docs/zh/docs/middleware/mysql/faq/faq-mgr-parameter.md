# MySQL MGR 参数配置

在配置 MySQL Group Replication（MGR）时，为了增加配置的灵活性和向后兼容性，部分参数需要使用 `loose_` 前缀。MySQL 中有些参数可能是实验性的或仅用于特定场景。在这些情况下，使用 loose_ 前缀可以确保这些参数在不支持的环境下被忽略。

## 具体示例

以下是一个使用 loose_ 前缀配置 MySQL Group Replication 的示例：

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

!!! Info

    使用 `loose_`前缀是配置 MGR 参数时的一种安全做法，尤其是在不同版本或插件状态下运行时。它可以确保配置文件的兼容性和灵活性，避免不必要的启动错误。