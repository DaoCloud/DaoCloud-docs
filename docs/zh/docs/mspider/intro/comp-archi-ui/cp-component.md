---
hide:
  - toc
---

# 服务网格的控制面组件

<table>
<tr>
<th>组件名称</th>
<th>位置</th>
<th>描述</th>
<th>默认资源设置</th>
</tr>
<tr>
<td>mspider-ui</td>
<td>全局管理集群</td>
<td>服务网格界面</td>
<td>
<ul>
<li>requests: CPU: 未设置；内存: 未设置</li>
<li>limits: CPU: 未设置；内存: 未设置</li>
</ul>
</td>
</tr>
<tr>
<td>mspider-ckube</td>
<td>全局管理集群</td>
<td>Kubernetes API Server 的加速组件，用于调用全局集群相关的资源</td>
<td>
<ul>
<li>requests: CPU: 未设置；内存: 未设置</li>
<li>limits: CPU: 未设置；内存: 未设置</li>
</ul>
</td>
</tr>
<tr>
<td>mspider-ckube-remote</td>
<td>全局管理集群</td>
<td>用于调用远程集群的 Kubernetes， 聚合多集群资源，并且加速</td>
<td>
<ul>
<li>requests: CPU: 未设置；内存: 未设置</li>
<li>limits: CPU: 未设置；内存: 未设置</li>
</ul>
</td>
</tr>
<tr>
<td>mspider-gsc-controller</td>
<td>全局管理集群</td>
<td>服务网格管理组件，用于网格创建，网格配置等网格控制面生命周期管理，以及权限管理等 Mspider  控制面能力</td>
<td>
<ul>
<li>requests: CPU: 未设置；内存: 未设置</li>
<li>limits: CPU: 未设置；内存: 未设置</li>
</ul>
</td>
</tr>
<tr>
<td>mspider-api-service</td>
<td>全局管理集群</td>
<td>为 Mspider 后台 API 交互，等控制行为提供接口</td>
<td>
<ul>
<li>requests: CPU: 未设置；内存: 未设置</li>
<li>limits: CPU: 未设置；内存: 未设置</li>
</ul>
</td>
</tr>
<tr>
<td>托管网格</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>istiod-{meshID}-hosted</td>
<td>控制面集群</td>
<td>用于托管网格的策略管理</td>
<td>
<ul>
<li>requests: CPU: 100m；内存: 100m</li>
<li>limits: CPU: 未设置；内存: 未设置</li>
</ul>
</td>
</tr>
<tr>
<td>mspider-mcpc-ckube-remote</td>
<td>控制面集群</td>
<td>调用远程的网格工作集群，加速并且聚合多集群资源</td>
<td>
<ul>
<li>requests: CPU: 100m；内存: 50m</li>
<li>limits: CPU: 500m；内存: 500m</li>
</ul>
</td>
</tr>
<tr>
<td>mspider-mcpc-mcpc-controller</td>
<td>控制面集群</td>
<td>聚合网格多集群相关数据面信息</td>
<td>
<ul>
<li>requests: CPU: 100m；内存: 0</li>
<li>limits: CPU: 300m；内存: 1.56G</li>
</ul>
</td>
</tr>
<tr>
<td>{meshID}-hosted-apiserver</td>
<td>控制面集群</td>
<td>托管控制面虚拟集群 API Server</td>
<td>
<ul>
<li>requests: CPU: 未设置；内存: 未设置</li>
<li>limits: CPU: 未设置；内存: 未设置</li>
</ul>
</td>
</tr>
<tr>
<td>{meshID}-etcd</td>
<td>控制面集群</td>
<td>托管控制面虚拟集群 etcd，用于托管网格的策略存储</td>
<td>
<ul>
<li>requests: CPU: 未设置；内存: 未设置</li>
<li>limits: CPU: 未设置；内存: 未设置</li>
</ul>
</td>
</tr>
<tr>
<td>istiod</td>
<td>工作集群</td>
<td>主要用于所在集群的边车生命周期管理</td>
<td>
<ul>
<li>requests: CPU: 100；内存: 100</li>
<li>limits: CPU: 未设置；内存: 未设置</li>
</ul>
</td>
</tr>
<tr>
<td>专有网格</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>istiod</td>
<td></td>
<td>用于策略创建、下发、边车生命周期管理的工作</td>
<td>
<ul>
<li>requests: CPU: 100；内存: 100</li>
<li>limits: CPU: 未设置；内存: 未设置</li>
</ul>
</td>
</tr>
<tr>
<td>mspider-mcpc-ckube-remote</td>
<td>工作集群</td>
<td>调用远程的网格工作集群</td>
<td>
<ul>
<li>requests: CPU: 100m；内存: 50m</li>
<li>limits: CPU: 500m；内存: 500m</li>
</ul>
</td>
</tr>
<tr>
<td>mspider-mcpc-mcpc-controller</td>
<td>工作集群</td>
<td>收集集群数据面信息</td>
<td>
<ul>
<li>requests: CPU: 100m；内存: 0</li>
<li>limits: CPU: 300m；内存: 1.56G</li>
</ul>
</td>
</tr>
<tr>
<td>外接网格</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>mspider-mcpc-ckube-remote</td>
<td>工作集群</td>
<td>调用远程的网格工作集群</td>
<td>
<ul>
<li>requests: CPU: 100m；内存: 50m</li>
<li>limits: CPU: 500m；内存: 500m</li>
</ul>
</td>
</tr>
<tr>
<td>mspider-mcpc-mcpc-controller</td>
<td>工作集群</td>
<td>收集集群数据面信息</td>
<td>
<ul>
<li>requests: CPU: 100m；内存: 0</li>
<li>limits: CPU: 300m；内存: 1.56G</li>
</ul>
</td>
</tr>
</table>

服务网格的各控制面组件预设资源设置如上表所示，用户可以在[容器管理](../../../kpanda/user-guide/workloads/create-deployment.md)模块查找相应的工作负载，为工作负载自定义 CPU、内存资源。
