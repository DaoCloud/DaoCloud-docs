---
hide:
  - toc
---

# Latest News on Container Management Features

This page provides updates on DCE 5.0 container management.

## April 2023

<table>
<thead bgcolor="#ECEAE9" align="center">
<tr>
<th>Feature</th>
<th>Description</th>
<th>Version</th>
<th>Documentation</th>
</tr>
</thead>
<tbody>
<tr>
<td>Added interface to query PVC events</td>
<td>Users can now visually check all PVC events in the cluster, including related K8s components, operation objects, event names, and time of occurrence, on a graphical interface.</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/storage/pvc/">PersistentVolumeClaim (PVC)</a></td>
</tr>
<tr>
<td>Added parameters for Job, including backoffLimit, completions, parallelism, and activeDeadlineSeconds</td>
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
<td>Integrated the independent open-source storage component HwameiStor</td>
<td>Users can now view local storage resource overview and other information in the <code>container storage</code>.</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/storage/sc/">StorageClass</a></td>
</tr>
<tr>
<td>New cluster inspection function</td>
<td>A second-level inspection of the cluster is now available. Note that this is an Alpha feature.</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/clusterops/latest-operations/">Cluster recent operations</a></td>
</tr>
<tr>
<td>Added application backup function</td>
<td>Users can now quickly back up and restore applications on the GUI. Note that this is an Alpha feature.</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/user-guide/backup/deployment/">Backing up workloads</a></td>
</tr>
<tr>
<td>New platform backup function</td>
<td>A backup and recovery of etcd data is now available. Note that this is an Alpha feature.</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/kpanda/best-practice/etcd-backup/">ETCD backup restore</a></td>
</tr>
<tr>
<td>Added custom role management cluster for global management</td>
<td>Users can now create custom roles through global management to manage the cluster.</td>
<td>0.16.0</td>
<td><a href="https://docs.daocloud.io/ghippo/user-guide/access-control/custom-role/">Create a custom role</a></td>
</tr>
</tbody>
</table>

For a complete list of container management features, see [Container Management Features](features.md).
