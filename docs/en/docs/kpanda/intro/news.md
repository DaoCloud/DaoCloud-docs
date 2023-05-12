# Container management function release dynamics

This page provides an update on DCE 5.0 container management.

## April 2023

<table>
<thead bgcolor="#ECEAE9" align="center">
<tr>
<th>feature</th>
<th>Description</th>
<th>version</th>
<th>documentation</th>
</tr>
</thead>
<tbody>
<tr>
<td>Add interface to query PVC events</td>
<td>Support visually check the level of all PVC events in the cluster, related K8s components, operation objects, event names, time of occurrence and other information on the graphical interface</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/storage/pvc/">Data Volume Declaration (PVC)</a></td>
</tr>
<tr>
<td>Job adds backofflimit, completions, parallelism, activeDeadlineSeconds and other parameters</td>
<td>
<ul>
  <li><code>backoffLimit</code>: Specifies the number of retries before marking this Job as failed. The default value is 6. </li>
  <li><code>completions</code>: Specifies the number of Pods that the Job should run and expect to complete successfully. Setting to nil means that the success of any Pod marks the success of all Pods, and allows parallelism to be set to any positive value. A setting of 1 means that parallelism is limited to 1, and the success of this Pod marks the success of the task. </li>
  <li><code>parallelism</code>: Specifies an upper bound on the number of Pods that the Job should expect to run at any given moment. When (.spec.completions - .status.successful) < .spec.parallelism, i.e. when the remaining work is less than the maximum degree of parallelism, the actual number of Pods running in steady state will be less than this number. </li>
  <li><code>activeDeadlineSeconds</code>: The number of seconds that the job can be active before the system tries to terminate the job. This length of time is relative to startTime; the field value must be a positive integer. If the Job is suspended, this timer is stopped and reset when the Job resumes again. </li>
</ul>
</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/workloads/create-job/">Create Job</a></td>
</tr>
<tr>
<td>Integrate the independent open source storage component HwameiStor</td>
<td>Support to view local storage resource overview and other information in <code>container storage</code></td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/storage/sc/">Storage Pool</a></td>
</tr>
<tr>
<td>New cluster inspection function</td>
<td>Support second-level inspection of the cluster, currently this is an Alpha feature</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/clusterops/latest-operations/">Cluster recent operations</a></td>
</tr>
<tr>
<td>Add application backup function</td>
<td>Support quick backup and restore of applications on the GUI, currently this is an Alpha feature</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/backup/deployment/">Backing up workloads</a></td>
</tr>
<tr>
<td>New platform backup function</td>
<td>Support backup and recovery of etcd data, currently this is an Alpha feature</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/best-practice/etcd-backup/">ETCD backup restore</a></td>
</tr>
<tr>
<td>Add <code>global management</code> custom role management cluster</td>
<td>Support to create custom roles through global management to manage the cluster</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/ghippo/user-guide/access-control/custom-role/">Create a custom role</a></td>
</tr>
</tbody>
</table>

For a complete list of container management features, see [Container Management Features Overview](./features.md).