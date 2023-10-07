# Nacos 版本降级

如果你使用的是高于 Nacos 2.1.x 的版本，想要将版本降级到低于 2.1.x，并且使用了外置数据库，
可以参照以下步骤来降级版本：

1. 找到需要降级的 Nacos CR 资源

    ```bash
    kubecl get nacos -A
    ```

2. 修改 `image` 字段，替换成需要降级的版本

3. 修改数据库

   ```sql
   alter table config_info drop column encrypted_data_key;
   alter table config_info_beta drop column encrypted_data_key;
   alter table his_config_info drop column encrypted_data_key;
   ```

4. 重启此 Nacos 的 StatefulSet。
