# Compatibility Rules for HPA and CronHPA

HPA stands for HorizontalPodAutoscaler, which refers to horizontal pod auto-scaling.

CronHPA stands for Cron HorizontalPodAutoscaler, which refers to scheduled horizontal pod auto-scaling.

## Conflict Between CronHPA and HPA

Scheduled scaling with CronHPA triggers horizontal pod scaling at specified times.
To prevent sudden traffic surges, you may have configured HPA to ensure the normal operation
of your application. If both HPA and CronHPA are detected simultaneously, conflicts arise
because CronHPA and HPA operate independently without awareness of each other.
Consequently, the actions performed last will override those executed first.

By comparing the definition templates of CronHPA and HPA, the following points can be observed:

- Both CronHPA and HPA use the `scaleTargetRef` field to identify the scaling target.
- CronHPA schedules the number of replicas to scale based on crontab rules in jobs.
- HPA determines scaling based on resource utilization.

!!! note

    If both CronHPA and HPA are set, there will be scenarios where CronHPA and HPA
    simultaneously operate on a single `scaleTargetRef`.

## Compatibility Solution for CronHPA and HPA

As noted above, the fundamental reason that simultaneous use of CronHPA and HPA results in
the later action overriding the earlier one is that the two controllers cannot sense each other.
Therefore, the conflict can be resolved by enabling CronHPA to be aware of HPA's current state.

The system will treat HPA as the scaling object for CronHPA, thus achieving scheduled scaling
for the Deployment object defined by the HPA.

HPA's definition configures the Deployment in the `scaleTargetRef` field, and then the Deployment
uses its definition to locate the ReplicaSet, which ultimately adjusts the actual number of replicas.

In DCE 5.0, the `scaleTargetRef` in CronHPA is set to the HPA object, and it uses the HPA object
to find the actual `scaleTargetRef`, allowing CronHPA to be aware of HPA's current state.

<!-- add images later -->

CronHPA senses HPA by adjusting HPA. CronHPA determines whether scaling is needed and modifies
the HPA upper limit by comparing the target number of replicas with the current number of replicas,
choosing the larger value. Similarly, CronHPA determines whether to modify the HPA lower limit by
comparing the target number of replicas from CronHPA with the configuration in HPA,
choosing the smaller value.
