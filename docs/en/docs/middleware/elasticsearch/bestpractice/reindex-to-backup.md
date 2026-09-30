# Migrate Elasticsearch Data Using reindex

## Background

Use the `reindex` feature of Elasticsearch to migrate data between clusters while ensuring that the business of the source cluster is not interrupted.
To fully synchronize the data of the source cluster, the write operations of the source cluster still need to be stopped at some point.

![move-data-to-new-es](../images/move-data-to-new-es.png)

## Notes

- Reindexing requires that `_source` is enabled for all documents in the source.
- Before calling `_reindex`, the destination should be configured to the desired state. Reindexing does not copy the settings of the source or its associated templates. Mappings, the number of shards, replicas, and so on must be configured in advance.
- Because reindex involves a snapshot action, data changes that occur during the reindex process will not be reflected in the destination cluster. See the section "Data changes in the source cluster".

## Test Environment Description

### Elasticsearch Deployed on a Virtual Machine

- Version: 7.15.2
- Access address: `172.30.120.85:9200`
- Username/password: elastic/root123!

### Elasticsearch Instance Deployed on DCE

- Version: 7.16.3
- ES access address: `https://10.6.178.179:30486`
- Username/password: elastic/m5!586LM33Hz0qf

## Steps

1. Modify the CR content of the DCE ES to add the access address of the virtual machine ES to the whitelist, as shown in the following figure.

    ```yaml
    nodeSets:
      - config:
          node.roles:
          - data
          - master
          - ingest
          - ml
          - data_cold
          - data_content
          - data_frozen
          - data_hot
          - data_warm
          - remote_cluster_client
          - transform
          reindex.remote.whitelist: 172.30.120.85:9200, localhost:*  /Add the virtual machine ES access address
    ```

2. View the index data in the virtual machine ES.

    ```shell
    GET cat/indices/test_data*

    yellow open test_data3 WA6qaRp5QC21nvuJMF33kA 1 1 10000 0 954.1kb 954.1kb
    yellow open test_data4 _H8LWZ28RdmdVkCae-3Piw 1 1 10000 0 953.8kb 953.8kb
    yellow open test_data1 xoFHZRvxT1uRMZ0tWxFfNQ 1 1  9000 0 869.3kb 869.3kb
    yellow open test_data2 dtM5J7poS6Wo7BhymKaxcQ 1 1 10000 0 953.1kb 953.1kb
    ```

### Migrate a Single Index Using reindex

- Execute the following command in the DCE ES:

    ```bash
    POST _reindex
    {
      "source": {
        "remote": {
          "host": "http://172.30.120.85:9200",
          "username": "elastic",
          "password": "root123!"
        },
        "index": "test_data1"
        
      },
      "dest": {
        "index": "test_data1"
      }
    }
    ```

- After the migration is complete, query the migrated index data in the DCE ES.

    ```shell
    GET _cat/indices/test_data1

    yellow open test_data1 46SIN0ddTDyKUeX_fzLwAw 1 1 9000 0 862.5kb 862.5kb
    ```

### Migrate Multiple Indexes Using reindex

```shell
#!/bin/bash
for index in 2 3 4; do
  curl -H "Content-Type: application/json" -k -u elastic:'m5!586LM33Hz0qf' -XPOST "https://10.6.178.179:30486/_reindex?pretty" -d '{
    "source": {
      "remote": {
        "host": "http://172.30.120.85:9200",
        "username": "elastic",
        "password": "root123!"
      },
      "index": "test_data'"$index"'"
    },
    "dest": {
      "index": "test_data'"$index"'"
    }
  }'
done
```

### Migrate Data Using Asynchronous reindex

1. Adding `wait_for_completion=false` to the request URL returns immediately. You can learn the progress of the task by viewing the task.

    ```shell
    Collapse source
    POST _reindex?wait_for_completion=false
    {
      "source": {
        "remote": {
          "host": "http://172.30.120.85:9200",
          "username": "elastic",
          "password": "root123!"
        },
        "index": "test_data1"
        
      },
      "dest": {
        "index": "test_data10"
      }
    }
    ```

2. After the execution is complete, the command line returns the following data:
  
    ```json
    {
      "task" : "GxbeiC6NT3apWh6potbpkA:38152"
    }
    ```

3. View the task details:

    ```shell
    GET /_tasks/GxbeiC6NT3apWh6potbpkA:38152
    {
      "completed" : true,
      "task" : {
        "node" : "GxbeiC6NT3apWh6potbpkA",
        "id" : 38152,
        "type" : "transport",
        "action" : "indices:data/write/reindex",
        "status" : {
          "total" : 9000,
          "updated" : 0,
          "created" : 9000,
          "deleted" : 0,
          "batches" : 9,
          "version_conflicts" : 0,
          "noops" : 0,
          "retries" : {
            "bulk" : 0,
            "search" : 0
          },
          "throttled_millis" : 0,
          "requests_per_second" : -1.0,
          "throttled_until_millis" : 0
        },
        "description" : """reindex from [host=172.30.120.85 port=9200 query={
      "match_all" : {
        "boost" : 1.0
      }
    } username=elastic password=<<>>][test_data1] to [test_data10][_doc]""",
        "start_time_in_millis" : 1718203864735,
        "running_time_in_nanos" : 6411335610,
        "cancellable" : true,
        "cancelled" : false,
        "headers" : { }
      },
      "response" : {
        "took" : 6399,
        "timed_out" : false,
        "total" : 9000,
        "updated" : 0,
        "created" : 9000,
        "deleted" : 0,
        "batches" : 9,
        "version_conflicts" : 0,
        "noops" : 0,
        "retries" : {
          "bulk" : 0,
          "search" : 0
        },
        "throttled" : "0s",
        "throttled_millis" : 0,
        "requests_per_second" : -1.0,
        "throttled_until" : "0s",
        "throttled_until_millis" : 0,
        "failures" : [ ]
      }
    }
    ```

## Recommendations

It is recommended to perform reindex in multiple batches and add filtering conditions during reindex. For example, if the specified index has a `last_updated` field, you can restrict `last_updated` to before a certain point in time during the first reindex:

```shell
POST _reindex
{
  "source": {
    "remote": {
      "host": "http://172.30.120.85:9200",
      "username": "elastic",
      "password": "root123!"
    },
    "index": "test_data100",
    "query": {
      "range": {
        "last_updated": {
          "lte": 1718265586034
        }
      }
    }
  },
  "dest": {
    "index": "test_data100"
  }
}
```

In the second batch, you can set `range.last_updated` to `{"gt": 1718265586034}`.

!!! note

    After reindex is complete, you need to verify the integrity of the data.

---

#### References

- [Migrating data | Elasticsearch Service Documentation | Elastic](https://www.elastic.co/guide/en/cloud/current/ec-migrating-data.html)
- [Reindex from a remote cluster | Elasticsearch Guide [7.15] | Elastic](https://www.elastic.co/guide/en/cloud/current/ec-migrating-data.html)
- [Migrating an Elasticsearch cluster with 0 downtime | by Flavien Berwick | Medium](https://medium.com/@flavienb/migrating-an-elasticsearch-cluster-with-0-downtime-ecd7dffbe674)
- [Elasticsearch cross-cluster data migration solutions - Tencent Cloud Developer Community - Tencent Cloud (tencent.com)](https://cloud.tencent.com/developer/article/1825511)
