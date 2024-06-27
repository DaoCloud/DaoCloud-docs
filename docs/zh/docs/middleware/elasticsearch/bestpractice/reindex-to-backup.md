# 使用 reindex 迁移 Elasticsearch 数据

## 背景

使用 Elasticsearch 的 `reindex` 功能实现跨集群之间的数据迁移，同时保证 source 集群业务不中断。为了完全同步 source 集群的数据，在某个时刻还是需要停止 source 集群的写入操作。

![move-data-to-new-es](../images/move-data-to-new-es.png)

## 注意事项

- 重新索引要求源中的所有文档启用 `_source`。
- 在调用 `_reindex` 之前，应该将目标配置为所需的状态。重新索引不会复制源或其关联模板的设置。映射、分片数量、副本等必须提前配置好。
- 因为 reindex 有个 snapshot 的动作，在 reindex 过程中发生的数据变更是不会体现在 dest 集群的。参见 "source 集群的数据发生变化" 这一节。

## 测试环境说明

### 虚拟机部署 Elasticsearch

- 版本：7.15.2
- 访问地址：172.30.120.85:9200
- 用户名/密码：elastic/root123!

### DCE5.0 部署 Elasticsearch 实例

- 版本：7.16.3
- es 访问地址：https://10.6.178.179:30486
- 用户名/密码：elastic/m5!586LM33Hz0qf

## 操作步骤

1. 修改 DCE5.0 es 的 CR 内容，将虚拟机 es 的访问地址添加到白名单，如下图所示。

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
          reindex.remote.whitelist: 172.30.120.85:9200, localhost:*  /添加虚拟机 es 访问地址
    ```

2. 查看虚拟机 es 中的索引数据。

    ```shell
    GET cat/indices/test_data*

    yellow open test_data3 WA6qaRp5QC21nvuJMF33kA 1 1 10000 0 954.1kb 954.1kb
    yellow open test_data4 _H8LWZ28RdmdVkCae-3Piw 1 1 10000 0 953.8kb 953.8kb
    yellow open test_data1 xoFHZRvxT1uRMZ0tWxFfNQ 1 1  9000 0 869.3kb 869.3kb
    yellow open test_data2 dtM5J7poS6Wo7BhymKaxcQ 1 1 10000 0 953.1kb 953.1kb
    ```

### 使用 reindex 迁移单个索引

    - 在 DCE5.0 es 执行以下命令：

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

    - 迁移完成后，在 DCE5.0 es 中查询迁移的索引数据。

    ```shell
    GET _cat/indices/test_data1

    yellow open test_data1 46SIN0ddTDyKUeX_fzLwAw 1 1 9000 0 862.5kb 862.5kb
    ```

### 使用 reindex 迁移多个索引

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

### 使用异步 reindex 迁移数据

1. 请求的 url 加上 wait_for_completion=false 会立即返回，通过查看 task 来知道任务的进度。

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

2. 执行完成后，命令行中会返回以下数据：
  
    ```shell
    {
      "task" : "GxbeiC6NT3apWh6potbpkA:38152"
    }
    ```

3. 查看任务详情：

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

## 方案建议

建议分多次进行 reindex，并且在 reindex 的时候加上筛选条件，比如指定的 index 有个 `last_updated`  字段，第一次 reindex 的时候，可以限制 `last_updated` 在某时间点之前：

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

第二次的时候可以将 `range.last_updated` 设置为 `{"gt": 1718265586034}`  。

!!! note

    完成 reindex 后，需要验证数据的完整性。

---

#### 参考文档

- [Migrating data | Elasticsearch Service Documentation | Elastic](https://www.elastic.co/guide/en/cloud/current/ec-migrating-data.html)
- [Reindex from a remote cluster | Elasticsearch Guide [7.15] | Elastic](https://www.elastic.co/guide/en/cloud/current/ec-migrating-data.html)
- [Migrating an Elasticsearch cluster with 0 downtime | by Flavien Berwick | Medium](https://medium.com/@flavienb/migrating-an-elasticsearch-cluster-with-0-downtime-ecd7dffbe674)
- [Elasticsearch 跨集群数据迁移方案总结 - 腾讯云开发者社区 - 腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1825511)