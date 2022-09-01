# 什么是 elasticsearch

Elasticsearch（下文简称 Elastic）是目前全文搜索引擎的首选。它可以快速地存储、搜索和分析海量数据。Elastic 的底层是开源库 Lucene，但是 Lucene 无法直接用，必须自己写代码去调用它的接口。Elastic 是 Lucene 的封装，提供了 REST API 的操作接口，开箱即用。

DCE 5.0 内置的搜索服务基于 Elasticsearch，能够提供分布式搜索服务，为用户提供结构化、非结构化文本以及基于 AI 向量的多条件检索、统计、报表。完全兼容 Elasticsearch 原生接口。它可以帮助网站和 APP 搭建搜索框，提升用户的搜索体验；也可以用于搭建日志分析平台，助力企业实现数据驱动运维，数据驱动运营；它的向量检索能力可以帮助客户快速构建基于 AI 的图搜、推荐、语义搜索、人脸识别等丰富的应用。

![欢迎界面](images/es01.png)