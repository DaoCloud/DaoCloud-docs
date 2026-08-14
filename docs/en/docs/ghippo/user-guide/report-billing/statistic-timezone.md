# Configure the Time Zone for Statistics

Operations Management supports configuring the time zone used for report and billing statistics through a Helm parameter. This setting has no console entry and must be configured with `--set` when installing or upgrading the Operations Management module.

!!! info

    This page explains how to configure the statistic time zone when installing or upgrading the Operations Management module. The `gmagpie` name used in the commands below is the internal codename for the Operations Management module.

## Configuration parameter

| Parameter | Description | Default |
| --- | --- | --- |
| `global.statisticTimezone` | The time zone used for report and billing statistics and scheduled statistic jobs. Use an IANA time zone identifier. | `UTC` |

For available time zone values, see [IANA Time Zones](https://timeapi.io/documentation/iana-timezones), such as:

- `UTC`
- `Asia/Shanghai`
- `America/New_York`

!!! note

    If `global.statisticTimezone` is not set, the system uses the unified default time zone `UTC` in DCE 5.0. The parameter must be a valid IANA time zone identifier.

## Configure during installation

Add `--set global.statisticTimezone` to the Helm installation command:

```shell
helm install gmagpie gmagpie-release/gmagpie \
  -n gmagpie-system \
  --version <version> \
  --set global.statisticTimezone=Asia/Shanghai
```

Replace the Helm repository, namespace, version, and other parameters according to your environment.

## Configure during upgrade

For an existing Operations Management installation, use `helm upgrade` to change the setting. Back up the current Helm parameters before upgrading:

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

## Effect of the setting

After the setting takes effect, the start and end times of statistical data and the schedules of statistical jobs are calculated using the configured time zone. After the time zone setting is changed, subsequent scheduled jobs recalculate the data for today and yesterday. The scheduled job for the current day uses the new statistical criteria, and the scheduled job running at midnight the next day recalculates the previous day's data using the new criteria. Historical data is not recalculated.

To recalculate historical data for a specified period, see [Recalculate Historical Data](./report-recalculation.md).

!!! warning

    After changing the time zone, check report and billing data during a low-traffic period to verify that date boundaries meet expectations. An invalid time zone identifier may prevent Operations Management from starting.
