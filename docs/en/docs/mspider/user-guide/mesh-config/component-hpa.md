# Component resource elastic scaling

Users can control the [Control Plane Components](../../intro/comp-archi-ui/cp-component.md) realizes the elastic scaling strategy. Currently, it provides three elastic scaling methods: metric shrinking (HPA), timing shrinking (CronHPA), and vertical scaling (VPA). Users can choose the appropriate elastic scaling strategy according to their needs. The following uses index scaling (HPA) as an example to introduce the method of creating an auto scaling policy.

## Prerequisites

Make sure the helm application __Metrics Server__ is installed on the cluster, please refer to [Install metrics-server plugin](../../../kpanda/user-guide/scale/install-metrics-server.md)

      

## create policy

Take the __istiod__ of the dedicated cluster as an example, the specific operation is as follows:


1. Select the corresponding cluster in [Container Management], and click to enter __Workload__ -> __Stateless Load__ page to find __istiod__ ;

     

2. Click the workload name to enter the __Auto Scaling__ tab page;

     

3. Click the __Edit__ button to configure the auto scaling policy parameters;

      - Policy name: Enter the name of the auto scaling policy. Please note that the name can contain up to 63 characters, and can only contain lowercase letters, numbers, and separators ("-"), and must start and end with lowercase letters or numbers, such as __hpa -my-dep__ .
      - Namespace: The namespace where the payload resides.
      - Workload: The workload object that performs auto scaling.
      - Target CPU Utilization: The CPU usage of the Pod under the workload resource. The calculation method is: the request (`request`) value of all Pod resources/workloads under the workload. When the actual CPU usage is greater/lower than the target value, the system automatically reduces/increases the number of Pod replicas.
      - Target Memory Usage: The memory usage of the Pod under the workload resource. When the actual memory usage is greater/lower than the target value, the system automatically reduces/increases the number of Pod replicas.
      - Replica range: the elastic scaling range of the number of Pod replicas. The default interval is 1 - 10.
     
      

4. Click __OK__ to finish editing, and the new policy has taken effect.

## More elastic scaling configurations

Please refer to:

- [Create HPA scaling policy](../../../kpanda/user-guide/scale/create-hpa.md)

- [Create VPA scaling policy](../../../kpanda/user-guide/scale/create-vpa.md)
