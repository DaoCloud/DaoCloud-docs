---
hide:
  - toc
---

# Technical Features and Basic Concepts

The containerized PostgreSQL database provided in DCE 5.0 Enterprise Edition offers the following features:

- **Multiversion Concurrency Control (MVCC)**

	PostgreSQL's MVCC mechanism greatly improves concurrency control, allowing transactions to execute in a non-blocking manner and avoiding deadlock situations.

- **Replication and High Availability**

	Supports various replication and high availability solutions, including master-slave replication, streaming replication, and logical replication. These solutions provide data redundancy and automatic failover capabilities, thereby improving system availability.

- **Security**

	Provides strict security measures, including Access Control Lists (ACL), encrypted communication, password authentication, and audit logging. These measures ensure the security and integrity of the database.

- **Scalability**

	Allows users to enhance its functionality through extensions. For example, users can define custom types, functions, operators, and indexes. These extensions enhance the capabilities and adaptability of PostgreSQL.

- **Performance Optimization**

	Provides mechanisms for performance optimization, including index optimization, query optimization, and configuration optimization. PostgreSQL also offers powerful statistical information and real-time monitoring tools to help users troubleshoot and optimize performance issues.

- **Support for JSON and JSONB Data Types**

	Supports direct storage and processing of data in JSON format, making PostgreSQL a useful NoSQL database.

- **Full-Text Search Support**

	Built-in full-text search functionality enables efficient searching and matching of large amounts of text data.

- **Support for Geospatial Data Types**

	Supports storage and querying of geospatial data, making PostgreSQL a valuable GIS database.

- **Support for Partitioned Tables**

	Supports partitioning a large table into multiple smaller tables for storage and querying, which improves query efficiency and ease of management.

- **Concurrency Control Support**

	Improves concurrency control capabilities through the MVCC mechanism. PostgreSQL also supports multiple isolation levels, including Read Committed, Repeatable Read, and Serializable.

- **Support for Stored Procedure Languages such as PL/SQL and PL/Python**

	Supports various stored procedure languages, including PL/SQL, PL/Python, and PL/Perl, allowing PostgreSQL to be integrated with other programming languages for development and extension purposes.
