# Enable the PGVector Plugin

pgvector is an extension for storing and manipulating vector data in the PostgreSQL database. It provides support for high-dimensional vector data, allowing users to directly store, retrieve, and manipulate vectors in a relational database. Its main features include:

1. Vector storage: Supports storing high-dimensional vectors directly in PostgreSQL tables, making it convenient to use together with other relational data.
2. Similarity search: Provides efficient vector similarity search algorithms, such as Euclidean distance, cosine similarity, and inner product, making vector search in the database efficient and convenient.
3. Index support: Supports using vector indexes (such as L2, IP, and Cosine) to accelerate vector similarity search and improve query performance.

## Enable the pgvector Extension

1. Log in to the PostgreSQL instance and execute the following SQL command in a database with pgvector pre-enabled to create the pgvector extension plugin.

    ```sql
    CREATE EXTENSION vector;
    ```

## Verify the pgvector Plugin

1. Create a test table containing vector data, and insert some test vector data.

    ```sql
    -- Create a test table

    CREATE TABLE test_vectors (
      id serial PRIMARY KEY,
      embedding vector(3)
    );

    -- Insert test data
    INSERT INTO test_vectors (embedding) VALUES
      ('[1, 2, 3]'),
      ('[4, 5, 6]'),
      ('[7, 8, 9]');
    ```

2. Query the vector data in the table.

    ```sql
    SELECT * FROM test_vectors;
    ```

The returned result is as follows:

    ```json
    id | embedding 
    ----+-----------
      1 | [1, 2, 3]
      2 | [4, 5, 6]
      3 | [7, 8, 9]
    ```

## Verify the Vector Similarity Search

1. Execute the following SQL to verify the similarity search feature.

    ```sql
    -- Perform a similarity search using Euclidean distance
    SELECT id, embedding
    FROM test_vectors
    ORDER BY embedding <-> '[1, 2, 3]'
    LIMIT 5;
    ```

The returned result is as follows:

    ```json
    id | embedding 
    ----+-----------
      1 | [1, 2, 3]
      2 | [4, 5, 6]
      3 | [7, 8, 9]
    ```
