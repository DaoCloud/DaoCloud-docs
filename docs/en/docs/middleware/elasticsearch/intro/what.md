---
hide:
  - toc
---

# Elasticsearch

Elasticsearch (shortened as Elastic) is the preferred full-text search engine. It can quickly store, search, and analyze massive amounts of data. The underlying technology of Elastic is the open-source library Lucene. However, Lucene cannot be used directly, and you must write codes to call its interfaces. Elastic is a encapsulation for Lucene, providing REST APIs that are ready to use.

The search service built into DCE 5.0 is based on Elasticsearch and can provide distributed search services of structured or unstructured text, and multi-condition retrieval, statistics, and reporting based on AI vectors. It is fully compatible with the Elasticsearch native interface. It can help build search boxes in websites and apps to enhance user's search experience. It can also be used to build log analysis platforms to help enterprises achieve data-driven operations and management. Its vector retrieval capability can help customers quickly build rich applications, such as AI-based image search, recommendation systems, semantic search, face recognition, etc.

![welcome page](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/elasticsearch/images/what01.png)

## ElasticSearch Job Management

Raw data flows into Elasticsearch from multiple sources, including logs, system metrics, and network applications. Data collection aims to parse, standardize, and enrich this raw data in Elasticsearch before indexing it. After these data are indexed in Elasticsearch, users can run complex queries on their data and use aggregation to retrieve complex summaries of their data. In Kibana, users can create powerful visualizations based on their own data.

## What is Kibana?

Kibana is a data visualization and management tool designed for Elasticsearch. It can provide real-time histograms, line charts, pie charts, and maps. Kibana also includes advanced applications such as Canvas and Elastic Maps, among others. Canvas allows users to create customized dynamic infographics based on their own data, while Elastic Maps can be used to visualize geospatial data.

[Create Elasticsearch Instance](../user-guide/create.md){ .md-button .md-button--primary }
