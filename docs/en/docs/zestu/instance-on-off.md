# Container Instance Power On/Off

After a container instance is created, you can perform **power on** and **power off** operations through the UI, the console, or the API, so as to flexibly manage the usage and cost of computing resources.

- **Power on**: After the container instance is started, computing resources (such as CPU, GPU, and memory) are allocated and put into operation, and the system begins billing according to the selected billing mode.
- **Power off**: Powering off releases computing resources and **stops billing**, but retains the instance's system disk data and configuration so that it can be quickly restored later.

For scenarios involving **intermittent tasks** or **on-demand use of computing power**, such as model training, batch computing, or test environment deployment,
arranging power on and power off times sensibly lets users reduce resource costs effectively while ensuring business continuity.

## Power Off

Prerequisites: A container instance has been created and is currently running.

The steps are as follows:

1. Log in to d.run, go to **Compute Cloud** -> **Container Instances** ,
   select a running instance, click the **┇** on the right side of the list,
   and choose **Power Off** from the dropdown list.

    <!-- ![Power Off 1](./images/poweroff1.png) -->

2. In the pop-up prompt, carefully read the power off notice, choose whether to save the system disk, and then click **OK**

    <!-- ![Power Off 2](./images/poweroff2.png) -->

!!! note

    - Instances that have not been powered on for 15 days will be automatically released.
    - GPU resources will not be reserved after power off. If there are insufficient
      available GPU resources of the required model when powering back on, you will need to wait.
    - If the image space quota is insufficient, saving the system disk may fail. Please make sure the image space quota is sufficient.

## Power On

Prerequisites: A container instance has been created and is currently powered off.

The steps are as follows:

1. Log in to d.run, go to **Compute Cloud** -> **Container Instances** ,
   select a powered-off instance, click the **┇** on the right side of the list,
   and choose **Start Instance** from the dropdown list.

    <!-- ![Power On 1](./images/poweron1.png) -->

2. If the required GPU resources are sufficient, click **OK** to start.
   If resources are insufficient, you may need to wait.

    <!-- ![Power On 2](./images/poweron2.png) -->

!!! note

    - Instances that are queued or starting do not incur charges; billing begins when in running status.
    - Container instances do not actively refresh their status;
      you need to manually refresh to check the real status of the container instance.
