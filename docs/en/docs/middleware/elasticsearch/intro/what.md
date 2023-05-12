---
hide:
  - toc
---

# What is Elasticsearch

Elasticsearch (hereinafter referred to as Elastic) is currently the first choice for full-text search engines. It can quickly store, search and analyze massive amounts of data. The bottom layer of Elastic is the open source library Lucene, but Lucene cannot be used directly, and you must write your own code to call its interface. Elastic is a package of Lucene, which provides the operation interface of REST API and is ready to use out of the box.

The built-in search service of DCE 5.0 is based on Elasticsearch, which can provide distributed search services and provide users with structured and unstructured text and AI vector-based multi-condition retrieval, statistics, and reports. Fully compatible with Elasticsearch native interface. It can help websites and APPs to build search boxes to improve users' search experience; it can also be used to build log analysis platforms to help enterprises achieve data-driven operation and maintenance, and data-driven operations; its vector retrieval capabilities can help customers quickly build AI-based Rich applications such as image search, recommendation, semantic search, and face recognition.

<!--screenshot-->

## ElasticSearch job management

Raw data is fed into Elasticsearch from multiple sources, including logs, system metrics, and web applications. Data ingestion is the process of parsing, normalizing, and enriching this raw data before indexing in Elasticsearch. Once this data is indexed in Elasticsearch, users can run complex queries against the data and use aggregations to retrieve complex summaries of their data. In Kibana, users can create powerful visualizations based on their own data.

## What is Kibana?

Kibana is a data visualization and management tool for Elasticsearch that provides real-time histograms, line graphs, pie charts, and maps. Kibana also includes advanced applications such as Canvas, which allows users to create custom dynamic infographics based on their own data, and Elastic Maps, which can be used to visualize geospatial data.

[Create an Elasticsearch instance](../user-guide/create.md){ .md-button .md-button--primary }