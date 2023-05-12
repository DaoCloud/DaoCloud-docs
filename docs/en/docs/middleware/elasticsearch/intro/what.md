---
hide:
  - toc
---

# 什么是 Elasticsearch

Elasticsearch（下文简称 Elastic）是目前全文搜索引擎的首选。它可以快速地存储、搜索和分析海量数据。Elastic 的底层是开源库 Lucene，但是 Lucene 无法直接用，必须自己写代码去调用它的接口。Elastic 是 Lucene 的封装，提供了 REST API 的操作接口，开箱即用。

DCE 5.0 内置的搜索服务基于 Elasticsearch，能够提供分布式搜索服务，为用户提供结构化、非结构化文本以及基于 AI 向量的多条件检索、统计、报表。完全兼容 Elasticsearch 原生接口。它可以帮助网站和 APP 搭建搜索框，提升用户的搜索体验；也可以用于搭建日志分析平台，助力企业实现数据驱动运维，数据驱动运营；它的向量检索能力可以帮助客户快速构建基于 AI 的图搜、推荐、语义搜索、人脸识别等丰富的应用。

![欢迎界面](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/elasticsearch/images/es01.png)

## ElasticSearch 的工作管理

原始数据会从多个来源（包括日志、系统指标和网络应用程序）输入到 Elasticsearch 中。数据采集旨在 Elasticsearch 中进行索引之前解析、标准化并充实这些原始数据的过程。这些数据在 Elasticsearch 中完成索引之后，用户便可针对数据运行复杂的查询，并使用聚合来检索自身数据的复杂汇总。在 Kibana 中，用户可以基于自己的数据创建强大的可视化。

## Kibana 是什么？

Kibana 是一款适用于 Elasticsearch 的数据可视化和管理工具，可以提供实时的直方图、线形图、饼状图和地图。Kibana 同时还包括诸如 Canvas 和 Elastic Maps 等高级应用程序；其中 Canvas 允许用户基于自身数据创建定制的动态信息图表，而 Elastic Maps 则可用来对地理空间数据进行可视化。

[创建 Elasticsearch 实例](../user-guide/create.md){ .md-button .md-button--primary }
