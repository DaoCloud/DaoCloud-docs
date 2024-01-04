# trigger trigger pipeline

Configure a trigger for the pipeline to automatically trigger the execution of the pipeline periodically. Click __Edit Configuration__ when editing the pipeline to configure the build trigger.

<!--![]()screenshots-->

## Trigger type

| Trigger Type | Description |
| ------------ | ------------------------------------ ------------------------ |
| Code Source Trigger | Check the code repository for changes at the specified time. For example, filling in __H/15 * * * *__ means that every 15 minutes the system will automatically check whether there are newly submitted changes in the code warehouse, and if there are newly submitted changes, the pipeline will be executed. |
| Timing trigger | Trigger the pipeline at a specified time. After the timing trigger is turned on, you can directly select the preset rules, or you can choose a custom CRON expression and enter a custom trigger rule. |

## trigger rules

Trigger rule syntax follows that of CRON (with a slight difference). Specifically, each line consists of 5 tab- or space-separated fields: __MINUTE HOUR DOM MONTH DOW__

| field | description | value range |
| ------ | ---- | -------------------------------------- |
| MINUTE | minute | 0 ~ 59 |
| HOUR | hour | 0 ~ 23 |
| DOM | days | 1 ~ 31 |
| MONTH | month | 1 ~ 12 |
| DOW | Week | 1 ~ 6 represent Monday to Saturday, 0, 7 represent Sunday |

To specify multiple values ​​for a field, the following operators can be used, in order of precedence:

| operator | description |
| ------------ | ------------------------------------ --------- |
| * | means to match all values ​​within the value range |
| M-N | means all values ​​in the specified range |
| M-N/X or */X | means to fire every X within the specified range or the entire effective range |
| A,B,...,Z | means match multiple values ​​|

In order for regularly scheduled tasks to create an even load on the system, the symbol H (for "hash") should be used whenever possible.
For example, using __0 0 * * *__ for a dozen daily jobs will result in a large spike at midnight, possibly straining resources.
In contrast, using __H H * * *__ will still run each job once a day, but not all at once, which makes better use of limited resources.

H can be used with ranges. For example, __H H(0-7) * * *__ means some time between 00:00 and 7:59.

Due to the different number of days in different months, when a short period such as __/3__ or __H/3__ appears in __DOM__ , it will not be triggered at the end of most months.
For example, __*/3__ will trigger the task on the 1st, 4th, ..., 31st of each month. If there are 30 days in the next month, the last time the task is triggered is the 28th day.

Also, @yearly, @annually, @monthly, @weekly, @daily, @midnight, and @hourly are convenient aliases.
These use hashes for automatic matching. For example, @hourly is the same as __H * * * *__ and can represent any time within an hour.
@midnight represents a period of time between 0:00 and 2:59 every day.

**Rule Example**

| Rules | Instructions |
| ------------------- | ----------------------------- ---------------------------------- |
| H/15 * * * * | means fire every 15 minutes, such as 07 minutes, 22 minutes, 37 minutes, and 52 minutes of every hour |
| H(0-29)/10 * * * * | means to trigger every 10 minutes in the first half hour of each hour, such as 04 minutes, 14 minutes and 24 minutes of every hour |
| 45 9-16/2 * * 1-5 | Indicates that each weekday starts at 9:45 and ends at 15:45 pm, every 2 hours, triggering at the 45th minute |
| H H(8-15)/2 * * 1-5 | Indicates that every working day from 8:00 to 16:00, trigger once every 2 hours, for example, at 9:38, 11 :38, 13:38, 15:38 |
| H H 1,15 1-11 | means once every day on the 1st and 15th of every month except December |