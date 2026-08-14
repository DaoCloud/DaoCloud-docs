# Historical Data Recalculation

After a GPU metric formula is changed, you can recalculate historical data so that existing reports and cost data use the updated calculation logic.

The recalculation covers:

- Resource alert data
- Resource audit data
- Cost allocation data

## Procedure

!!! warning

    The current version does not provide a console entry. To recalculate data, contact an administrator to trigger the task through the API.

### 1. Trigger a recalculation task

The administrator submits an API request and specifies the **start date** and **end date** of the recalculation period.

**Example request:**

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"start_date": "2025-01-01", "end_date": "2025-01-15"}' \
  "http://<api-address>/apis/gmagpie.io/v1alpha1/report/recalculate"
```

### 2. Task processing logic

After receiving the request, the system processes it in the background in the following order:

- **Queued execution**: Requests enter a queue and are processed on a first-in, first-out basis.
- **Daily recalculation**: Data is recalculated one day at a time in chronological order to ensure accuracy.
- **Status synchronization**: The task status is updated automatically after processing is complete.

### 3. Notes

- **Duration**: Recalculation is computationally intensive. Recalculating one month of data usually takes tens of minutes, depending on the cluster size.
- **Performance impact**: Run the task during off-peak hours whenever possible.
- **Data overwrite**: The operation overwrites existing report data. Confirm that the formulas are correct before starting the task.

## FAQ

**Q: Are reports available during recalculation?**

Yes. Reports remain accessible, but they may display old data or an intermediate state until the task is complete.

**Q: Does the system support parallel recalculation?**

No. To ensure data consistency, such as dependencies on previous cost allocation states, the system recalculates data serially, one day at a time.

**Q: What is the recalculation data range?**

The actual supported range depends on the retention period of the collected observability metrics. Recalculation retrieves the observability metrics and calculates the data again.
