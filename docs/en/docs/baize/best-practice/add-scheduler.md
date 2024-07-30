---
MTPE: windsonsea
Date: 2024-07-30
---

# Add Job Scheduler

DCE 5.0 Intelligent Engine provides a job scheduler to help you better manage jobs.
In addition to the basic scheduler, it also supports custom schedulers.

## Introduction to Job Scheduler

In Kubernetes, the job scheduler is responsible for deciding which node to assign a Pod to.
It considers various factors such as resource requirements, hardware/software constraints,
affinity/anti-affinity rules, and data locality.

The default scheduler is a core component in a Kubernetes cluster that decides
which node a Pod should run on. Let's delve into its working principles,
features, and configuration methods.

### Scheduler Workflow

The workflow of the default scheduler can be divided into two main phases: filtering and scoring.

#### Filtering Phase

The scheduler traverses all nodes and excludes those that do not meet the Pod's requirements,
considering factors such as:

- Resource requirements
- Node selectors
- Node affinity
- Taints and tolerations

These parameters can be set through advanced configurations when creating a job.

<!-- add screenshot later -->

#### Scoring Phase

The scheduler scores the nodes that passed the filtering phase and selects
the highest-scoring node to run the Pod. Factors considered include:

- Resource utilization
- Pod affinity/anti-affinity
- Node affinity, etc.

## Scheduler Plugins

In addition to basic job scheduling capabilities, we also support the use of
`Scheduler Plugins: Kubernetes SIG Scheduling`, which maintains a set of scheduler plugins
including `Coscheduling (Gang Scheduling)` and other features.

### Deploy Scheduler Plugins

To deploy a secondary scheduler plugin in a working cluster, refer to
[Deploying Secondary Scheduler Plugin](../../kpanda/user-guide/clusters/cluster-scheduler-plugin.md).

### Enable Scheduler Plugins in Intelligent Engine

!!! danger

    Improper operations when adding scheduler plugins may affect the stability of the entire cluster.
    It is recommended to test in a test environment or contact our technical support team.

Note that if you wish to use more scheduler plugins in training jobs, you need to manually install
them successfully in the working cluster first. Then, when deploying the `baize-agent` in the cluster,
add the proper scheduler plugin configuration.

Through the container management UI provided by **Helm Apps** ,
you can easily deploy scheduler plugins in the cluster.

<!-- add screenshot later -->

Then, click **Install** in the top right corner.
(If the `baize-agent` has already been deployed, you can update it in the Helm Application list.)
Add the scheduler.

<!-- add screenshot later -->

Note the parameter hierarchy of the scheduler. After adding, click **OK** .

> Note: Do not omit this configuration when updating the `baize-agent` in the future.

## Specify Scheduler When Creating a Job

Once you have successfully deployed the corresponding scheduler plugin in the cluster and
correctly added the corresponding scheduler configuration in the `baize-agent`,
you can specify the scheduler when creating a job.

If everything is set up correctly, you will see the scheduler plugin you deployed in the scheduler dropdown menu.

<!-- add screenshot later -->

This concludes the instructions for configuring and using the scheduler options in Intelligent Engine.
