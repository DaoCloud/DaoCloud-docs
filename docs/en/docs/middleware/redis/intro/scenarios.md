---
hide:
  - toc
---

# Applicable scene

Many large-scale e-commerce websites, live video and game platforms, etc., have **large-scale data access**, and require high **data query efficiency**, and **data structure is simple**, and **does not involve too many associations Inquire**.
Using Redis in this scenario has great advantages over traditional disk databases in terms of speed. It can effectively reduce database disk IO, improve data query efficiency, reduce management and maintenance workload, and reduce database storage costs.
Redis is an important supplement to traditional disk databases and has become one of the essential basic services for Internet applications, especially Internet applications that support high concurrent access.

Here are a few typical examples:

1. E-commerce website - flash sale

    Redis cache database is suitable for commodity categories, recommendation systems, and flash-buying activities of e-commerce websites.

    For example, flash sales activities, high concurrency, high access pressure for traditional relational databases, require high hardware configuration (such as disk IO) support.
    The QPS support of a single node of the Redis database can reach 100,000, which can easily handle spike concurrency. The commands to realize seckill and data locking are simple, just use SET, GET, DEL, RPUSH and other commands.

2. Live video - message barrage

    The online user list in the live broadcast room, gift rankings, barrage messages and other information are all suitable for storage using the SortedSet structure in Redis.

    For example, barrage messages can be sorted and returned using ZREVRANGEBYSCORE. In Redis 5.0, the new zpopmax and zpopmin commands are added to facilitate message processing.

3. Game App - Game Leaderboard

    Online games generally involve real-time display of leaderboards, such as listing the 10 users with the highest current score or combat power.
    It is very suitable to use Redis's ordered collection to store user leaderboards. The ordered collection is very easy to use and provides up to 20 commands for operating the collection.

4. Social App - Back to latest comments/replies

    In web applications, there are often queries such as "latest comments". If a relational database is used, it often involves reverse sorting by comment time. As more and more comments are made, the sorting efficiency is getting lower and lower, and the concurrency is frequent .

    Use Redis's List (linked list) to store the latest 1000 comments. When the number of requested comments is within this range, you don't need to access the disk database and return it directly from the cache, reducing the pressure on the database and improving the response speed of the App.