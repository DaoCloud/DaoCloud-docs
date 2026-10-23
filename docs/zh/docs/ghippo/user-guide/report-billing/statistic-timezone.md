# 配置统计时区

运营管理支持通过 Helm 参数配置报表和计费数据的统计时区。该配置没有前端操作入口，需要在安装或升级运营管理模块时通过 `--set` 参数设置。

!!! info

    本页说明如何在安装或升级运营管理模块时配置统计时区。下述命令中的 `gmagpie` 是运营管理模块的内部开发代号。

## 配置参数

| 参数 | 说明 | 默认值 |
| --- | --- | --- |
| `global.statisticTimezone` | 报表和计费数据的统计时区，同时用于统计定时任务的调度。参数值使用 IANA 时区标识。 | `UTC` |

时区值可以参考 [IANA Time Zones](https://timeapi.io/documentation/iana-timezones)，例如：

- `UTC`
- `Asia/Shanghai`
- `America/New_York`

!!! note

    如果不设置 `global.statisticTimezone`，系统使用 DCE 统一的默认时区 `UTC`。该参数必须使用有效的 IANA 时区标识。

## 安装时配置

安装运营管理模块时，在 Helm 命令中添加 `--set global.statisticTimezone`：

```shell
helm install gmagpie gmagpie-release/gmagpie \
  -n gmagpie-system \
  --version <version> \
  --set global.statisticTimezone=Asia/Shanghai
```

请根据实际环境替换 Helm 仓库、命名空间和版本等参数。

## 升级时配置

已安装运营管理模块时，使用 `helm upgrade` 修改配置。升级前建议先备份当前 Helm 参数：

```shell
helm get values gmagpie -n gmagpie-system -o yaml > bak.yaml
```

```shell
helm upgrade gmagpie gmagpie-release/gmagpie \
  -n gmagpie-system \
  -f ./bak.yaml \
  --set global.statisticTimezone=Asia/Shanghai \
  --version <version>
```

## 生效范围

配置生效后，统计数据的起止时间和定时任务均按照配置的时区计算。修改完时区配置后，后续的定时任务会重新计算今天和昨天的数据：当日的定时任务会按照新的指标计算，第二天凌晨的定时任务会按照新的指标重算前一日的数据；历史数据不会重新计算。

如需重算指定时间范围的历史数据，请参考[历史数据重算](./report-recalculation.md)。

!!! warning

    修改时区后，建议在业务低峰期观察报表和计费数据，确认统计日期边界符合预期。无效的时区标识可能导致运营管理模块无法正常启动。
