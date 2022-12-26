# The data service is adapted to the Kubernetes version

At present, Data Service has officially released three data service middleware, MySQL, RabbitMQ, and Elasticsearch.

## Kubernetes version adaptation

| Middleware | Version | Features | 1.24 | 1.23 | 1.22 | 1.21 | 1.20 | Remarks |
| ------------- | ------ | -------- | -------- | -------- | - ------- | -------- | -------- | --------- |
| RabbitMq | 3.8.30 | operator | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Create instance | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Edit Example | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Query Example | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Instance connection | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Delete instance | ✅ | ✅ | ✅ | ✅ | ✅ | |
| ElasticSearch | 7.16.3 | operator | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Create instance | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Edit Example | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Query Example | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Instance connection | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Delete instance | ✅ | ✅ | ✅ | ✅ | ✅ | |
| MySQL | 5.7.31 | operator | ✅ | ✅ | ✅ | ✅ | ❌ | policy/v1 |
| | | Create instance | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Edit Example | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Query Example | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Instance connection | ✅ | ✅ | ✅ | ✅ | ✅ | |
| | | Delete instance | ✅ | ✅ | ✅ | ✅ | ✅ | |