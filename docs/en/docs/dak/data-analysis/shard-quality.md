---
hide:
  - toc
---

# Shard Quality

A shard refers to dividing larger data into multiple segments, which facilitates model training by making it easier to locate and hit the data.
d.run supports viewing the quality of shards. The specific steps are as follows:

1. In the **Data Analysis** section, click **Shard Quality**, and use the **Search** function to find the shard you are interested in. Click the shard to enter the details page, where you can view detailed information about this shard.

    <!-- ![Select Details Menu Item](images/shard-quality.jpg) -->

2. You can view the following content:

    - Corpus: Which corpus the shard belongs to.
    - Update Time: The last update time of the shard file.
    - Shard ID: The unique identification code of the shard.
    - Shard Content: The specific content of the shard after slicing.
    - Additional Information: Additional content related to this shard.

    <!-- ![View Details](images/shard-quality-detail.jpg) -->

3. When new shard files are evaluated, you can click the **Refresh** button in the upper right corner to view the latest shard files.

    <!-- ![Refresh](images/refresh-shard-quality.png) -->
