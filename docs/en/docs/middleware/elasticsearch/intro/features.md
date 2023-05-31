---
hide:
  - toc
---

# Features

Elasticsearch stores data in the form of JSON documents. Each document establishes a relationship between a set of keys (names of fields or attributes) and values (strings, numbers, booleans, dates, arrays, geographic coordinates, or other types of data).

Elasticsearch uses a data structure called inverted index, which allows for extremely fast full-text searches. The inverted index lists every unique term that appears in all documents and can find all documents containing each of these terms.

During indexing, Elasticsearch stores documents and builds the inverted index so that users can search document data in near real-time. The indexing process is initiated through the indexing API, which allows you to add JSON documents to a specific index or modify JSON documents in a specific index.

The following are the general features supported by Elasticsearch:

| Category        | Features                                                      | Description                                            |
| --------------- | ------------------------------------------------------------- | ------------------------------------------------------ |
| Distributed cluster    | Cluster deployment and monitoring                        | Monitor data of clusters, nodes, and indexes |
| Search management | Index configuration management, structure definition, index rebuilding | Provides configuration functions |
| Full-text search | Search, sorting, statistical analysis | Provided through RESTful APIs                          |
| Data collection  | Elasticsearch data import API,MaxCompute data import tool, full/incremental acquisition method | Rich native interfaces for data collection, integrates Maxcompute data import tools |
| Service authentication | Service-level user authentication | Unified user authentication settings |

After deploying Elasticsearch in DCE 5.0, the following features will also be supported:

- Support to deploy Elasticsearch proprietary nodes, hot/cold data nodes, and data nodes
- Integrate with Kibana
- Expose metrics based on elasticsearch-exporter
- Integrate with Elasticsearch Dashboard based on Grafana Operator to display monitoring data
- Use ServiceMonitor to connect to Prometheus to capture metrics
- Manage multiple tenants based on [Workspace](../../../ghippo/user-guide/workspace/workspace.md).
