# 任务和实例

在 Insight 里，可以从中抓取采样值的端点称为实例（Instance），为了性能扩展而复制出来的多个这样的实例形成了一个任务（Job）。

例如下面的 api-server 任务有四个相同的实例：

```css
job: api-server
instance 1: 1.2.3.4:5670
instance 2: 1.2.3.4:5671
instance 3: 5.6.7.8:5670
istance 4: 5.6.7.8:5671
  ```
  
Insight 抓取完采样值后，会自动给采样值添加下面的标签和值：

- job: 抓取所属任务

- instance: 抓取来源实例

另外每次抓取时，Insight 还会自动在以下时序里插入采样值：

- `up{job="[job-name]", instance="instance-id"}`：采样值为 1 表示实例健康，否则为不健康

- `scrape_duration_seconds{job="[job-name]", instance="[instance-id]"}`：采样值为本次抓取消耗时间

- `scrape_samples_post_metric_relabeling{job="<job-name>", instance="<instance-id>"}`：采样值为重新打标签后的采样值个数

- `scrape_samples_scraped{job="<job-name>", instance="<instance-id>"}`：采样值为本次抓取到的采样值个数