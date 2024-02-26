---
hide:
  - toc
---

# Create Job

Job management refers to the functionality of creating and managing task lifecycles through job scheduling and control components.

DCE 5.0 Smart Computing Capability adopts Kubernetes' Job mechanism to schedule various AI inference and training tasks.

1. Click **Task Center** -> **Job List** in the left navigation bar to enter the job list. Click the **Create** button on the right.

    <!-- add image later -->

2. The system will pre-fill basic configuration data, including the cluster to deploy to, namespace, task type, queue, priority, etc. Adjust these parameters and click **Next**.

    <!-- add image later -->

3. Configure the image address, runtime parameters, and associated datasets, then click **Next**.

    <!-- add image later -->

4. Optionally add tags, annotations, environment variables, and other task parameters. Select a scheduling strategy and click **Confirm**.

    <!-- add image later -->

5. After the job is successfully created, it will have several running statuses:

    - Running
    - Queued
    - Submission successful, submission failed
    - Task successful, task failed

## Next Steps

- [View Job Load](./view.md)
- [Delete Job](./delete.md)
