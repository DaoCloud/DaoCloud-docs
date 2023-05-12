---
hide:
  - toc
---

# Function Description

Elasticsearch stores data in the form of JSON documents.
Each document establishes a relationship between a set of keys (names of fields or properties) and their corresponding values ​​(strings, numbers, Booleans, dates, groups of numbers, geographic locations, or other types of data).

Elasticsearch uses a data structure called an inverted index, which is designed to allow very fast full-text searches.
An inverted index lists every unique term that occurs in all documents, and finds all documents that contain each term.

During the indexing process, Elasticsearch stores the documents and builds an inverted index so that users can search the document data in near real time.
The indexing process is initiated in the Indexing API, which allows you to both add and change JSON documents in a particular index.

The general features supported by Elasticsearch are as follows:

| Category | Features | Description |
| ---------- | -------------------------------------- ---------------------- | --------------------------- ------------------------- |
| Distributed Clusters | Cluster Deployment Cluster Monitoring | Provide an operation and maintenance platform page to monitor the health status of clusters, nodes, and indexes |
| Search management | Index configuration management structure definition, index reconstruction | Search management platform provides configuration functions |
| Full-text search | Search function, sorting function, statistical analysis function | Provided through RESTful API |
| Data collection | ElasticSearch data import APIMaxcompute data import tool full and incremental collection methods | Abundant native data collection interfaces, integrated with Maxcompute data import tool |
| Service Authentication | User Authentication Mechanism at Service Level | Unified User Authentication Settings |

After Elasticsearch is deployed in DCE 5.0, the following features will also be supported:

- Support Elasticsearch dedicated node, hot data node, cold data node, data node role deployment
-Integrate Kibana
- Exposure metrics based on elasticsearch-exporter
- Integrate Elasticsearch Dashboard based on Grafana Operator to display monitoring data
- Use ServiceMonitor to interface with Prometheus to capture metrics
- Multi-tenancy management based on [Workspace Workspace](../../../ghippo/user-guide/workspace/Workspaces.md)