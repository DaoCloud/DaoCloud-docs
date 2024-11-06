# 开启 PGVector 插件

pgvector 是一个在 PostgreSQL 数据库中存储和操作向量数据的扩展，它提供了对高维向量数据的支持，使得用户可以在关系数据库中直接存储、检索和操作向量。它的主要特性包括：

1. 向量存储：支持将高维向量直接存储在 PostgreSQL 表中，方便与其他关系数据结合使用。
2. 相似性搜索：提供了高效的向量相似性搜索算法，如欧氏距离、余弦相似度和内积，使得在数据库中进行向量搜索变得高效和方便。
3. 索引支持：支持使用向量索引（如 L2、IP、Cosine）来加速向量相似性搜索，提高查询性能。

## 启用 pgvector 扩展

1. 登录到 PostgreSQL 实例，在预启用 pgvector 的数据库中执行以下 SQL 命令，创建 pgvector 扩展插件

    ```sql
    CREATE EXTENSION vector;
    ```

## 验证 pgvector  插件

1. 创建一个包含向量数据的测试表，并插入一些测试的向量数据。

    ```sql
    -- 创建测试表

    CREATE TABLE test_vectors (
      id serial PRIMARY KEY,
      embedding vector(3)
    );

    -- 插入测试数据
    INSERT INTO test_vectors (embedding) VALUES
      ('[1, 2, 3]'),
      ('[4, 5, 6]'),
      ('[7, 8, 9]');
    ```

2. 查询表中的向量数据。

    ```sql
    SELECT * FROM test_vectors;
    ```

返回结果如下：

    ```json
    id | embedding 
    ----+-----------
      1 | [1, 2, 3]
      2 | [4, 5, 6]
      3 | [7, 8, 9]
    ```

## 验证向量相似性搜索

1. 执行以下 SQL，验证相似性搜索功能

    ```sql
    -- 使用欧氏距离进行相似性搜索
    SELECT id, embedding
    FROM test_vectors
    ORDER BY embedding <-> '[1, 2, 3]'
    LIMIT 5;
    ```

返回结果如下：

    ```json
    id | embedding 
    ----+-----------
      1 | [1, 2, 3]
      2 | [4, 5, 6]
      3 | [7, 8, 9]
    ```
