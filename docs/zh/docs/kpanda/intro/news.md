# 容器管理功能发布动态

本文介绍 DCE 5.0 容器管理相关内容的最新动态。

## 2023 年 4 月

<table>
<thead>
<tr>
<th>新功能</th>
<th>描述</th>
<th>适用版本</th>
<th>操作文档</th>
</tr>
</thead>
<tbody>
<tr>
<td>新增界面查询 PVC 事件</td>
<td>支持在图形界面上直观地查阅集群中所有 PVC 事件的级别、相关 K8s 组件、操作对象、事件名称、发生的时间等信息</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/storage/pvc/">数据卷声明 (PVC)</a></td>
</tr>
<tr>
<td>Job 新增 backofflimit、completions、parallelism、activeDeadlineSeconds 等参数</td>
<td>
<ul>
  <li>backoffLimit：指定标记此 Job 失败之前的重试次数。默认值为 6。</li>
  <li>completions：指定 Job 应该运行并预期成功完成的 Pod 个数。设置为 nil 意味着任何 Pod 的成功都标识着所有 Pod 的成功， 并允许 parallelism 设置为任何正值。设置为 1 意味着并行性被限制为 1，并且该 Pod 的成功标志着任务的成功。</li>
  <li>Parallelism：指定 Job 应在任何给定时刻预期运行的 Pod 个数上限。当 (.spec.completions - .status.successful) &lt; .spec.parallelism 时， 即当剩余的工作小于最大并行度时，在稳定状态下运行的 Pod 的实际数量将小于此数量。</li>
  <li>activeDeadlineSeconds：系统尝试终止 Job 之前 Job 可以持续活跃的秒数，这个时间长度是相对于 startTime 的； 字段值必须为正整数。如果 Job 被挂起， 则当 Job 再次恢复时，此计时器会被停止并重置。</li>
</ul>
</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/workloads/create-job/">创建 Job</a></td>
</tr>
<tr>
<td>集成自主开源的存储组件 HwameiStor</td>
<td>支持在<code>容器存储</code>中查看本地存储资源概览等信息</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/storage/sc/">存储池</a></td>
</tr>
<tr>
<td>新增集群巡检功能</td>
<td>支持对集群进行秒级巡检，目前这是 Alpha 特性</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/clusterops/latest-operations/">集群最近操作</a></td>
</tr>
<tr>
<td>新增应用备份功能</td>
<td>支持在图形界面上快速备份和恢复应用，目前这是 Alpha 特性</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/backup/deployment/">备份工作负载</a></td>
</tr>
<tr>
<td>新增平台备份功能</td>
<td>支持对 etcd 数据进行备份和恢复，目前这是 Alpha 特性</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/best-practice/etcd-backup/">ETCD 备份还原</a></td>
</tr>
<tr>
<td>新增全局管理的自定义角色管理集群</td>
<td>支持通过全局管理创建自定义角色来管理集群</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/ghippo/user-guide/access-control/role/">角色和权限管理</a></td>
</tr>
</tbody>
</table>

有关容器管理完整的功能列表，请查阅[容器管理功能总览](./features.md)。
