# request log

The microservice gateway supports viewing request logs and instance logs. This page describes how to view instance logs and related operations when viewing logs.

## view mode

Click the name of the target gateway to enter the gateway overview page, and then click `Log View`->`Request Log` in the left navigation bar.

![View request log path](imgs/reqlog-path.png)

## Related operations

- Filtering logs: Support filtering logs by Request ID, request path, domain name, request method, HTTP, GRPC and other conditions, and support sorting logs according to request start time, request time consumption, and request service time consumption.

    ![Filter log](imgs/log-filter1.png)

- Limited time range: You can choose the logs of the last 5 minutes, 10 minutes, 15 minutes, or customize the time range.

    ![Limited Time](imgs/logtime1.png)

- Export log: support exporting log files to local.

    ![Export Log](imgs/log-export1.png)