# Kafka Cross-Data-Center Disaster Recovery Solution

## Background

When going live in production, to ensure continuous business operation, a dual data center deployment is usually adopted so that when one data center fails, applications in the other data center can still provide services. For Kafka, under a dual data center deployment, it is desirable that the replicas of a partition are located in different data centers as much as possible. Here, Kafka is still deployed in the same cluster, and the nodes in the cluster are located in different data centers.

## Introduction to Rack Awareness

The `Rack awareness` feature distributes the replicas of the same partition across different racks. This feature extends the guarantees Kafka provides for broker-failure to cover rack-failure, reducing the risk of data loss caused by the simultaneous failure of all brokers on the same rack. This feature can also be applied to other broker groupings, for example, EC2 availability zones on AWS. You can use `broker.rack` to specify that a broker belongs to a specific rack.

When creating or modifying a topic or redistributing replicas, Kafka takes the `broker.rack` configuration into account to ensure replicas are distributed across as many racks as possible. Note that replicas are divided as evenly as possible across racks rather than across brokers. A partition spans `min(racks, replication-factor)` different racks.

- When `broker.rack` is not configured, the algorithm for assigning replicas to brokers ensures that the number of leaders on each broker (the number of partition leaders) is the same, regardless of how the brokers are distributed across racks. This ensures balanced throughput, meaning the throughput of each broker is the same.

- When `broker.rack` is configured, all replicas must be divided evenly across racks, that is, "no matter how many brokers are allocated to a rack, replicas are blindly divided evenly by rack." Because of this, if different racks are allocated different numbers of brokers, the rack with fewer brokers (whose replicas are not fewer) will use more storage and devote more resources to replication, so those brokers will bear a heavier burden, and the load will be unbalanced. Therefore, the wise approach is to configure the same number of brokers for each rack.

For example, assume 2 racks, 6 brokers, and 100 replicas (including primary and standby). The replicas will be blindly divided evenly across racks. Therefore, rack1 and rack2 are each allocated 50 replicas:

1. If both rack1 and rack2 are allocated 3 brokers, then each broker on rack1 is allocated 50/3 replicas, and each broker on rack2 is allocated 50/3 replicas.

2. If rack1 is allocated 5 brokers and rack2 is allocated 1 broker, then each broker on rack1 is allocated 50/5 replicas, and each broker on rack2 is allocated 50/1 replicas. That is, rack2 with fewer brokers does not have fewer replicas at all, so those brokers will bear a heavier burden, and the load will be unbalanced. Therefore, the wise approach is to configure the same number of brokers for each rack.

## Dual Data Center Deployment Architecture

![kafka](../../kafka/images/kafka2-01.png)

## Steps

1. Log in to the console of the target cluster and perform the following operations to add labels to the nodes located in different data centers.

    ```shell
    kubectl label node master01 topology.kubernetes.io/zone=east # here, "east" can be replaced with a custom data center name

    kubectl label node worker01 topology.kubernetes.io/zone=west # here, "east" can be replaced with a custom data center name
    ```

2. Modify the Kafka CR and configure the rack feature on the CR resource.

    ```yaml
    apiVersion: kafka.strimzi.io/v1beta2
    kind: Kafka
    metadata:
      name: test-rack
    spec:
      kafka:
        rack:
          topologyKey: topology.kubernetes.io/zone  # The value here should be the key of the label added in step 1
        version: 3.1.0
        replicas: 4
        listeners:
          - name: plain
            port: 9092
            type: internal
            tls: false
          - name: tls
            port: 9093
            type: internal
            tls: true
        config:
          offsets.topic.replication.factor: 3
          transaction.state.log.replication.factor: 3
          transaction.state.log.min.isr: 2
          default.replication.factor: 3
          min.insync.replicas: 2
          inter.broker.protocol.version: "3.1"
        storage:
          class: local-path
          size: 1Gi
          type: persistent-claim
      zookeeper:
        replicas: 1
        storage:
          class: local-path
          size: 1Gi
          type: persistent-claim
      entityOperator:
        topicOperator: {}
        userOperator: {}
    ```

- After the deployment is complete, the scheduling distribution of the Kafka Pods is as follows:

    ```shell
    test-rack-kafka-0                            1/1     Running   0             89m    10.244.2.117   worker01   <none>           <none>
    test-rack-kafka-1                            1/1     Running   0             89m    10.244.0.109   master01   <none>           <none>
    test-rack-kafka-2                            1/1     Running   0             89m    10.244.2.118   worker01   <none>           <none>
    test-rack-kafka-3                            1/1     Running   0             12m    10.244.0.111   master01   <none>           <none>
    ```

- kafka-operator will automatically add a `preferredDuringSchedulingIgnoredDuringExecution` affinity configuration to each Kafka Pod, as shown in the following code:

```yaml
podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 100
          podAffinityTerm:
            labelSelector:
              matchLabels:
                strimzi.io/cluster: test-rack
                strimzi.io/name: test-rack-kafka
            topologyKey: topology.kubernetes.io/zone
```

- Enter the Kafka Pod and check the internal configuration file. The `broker.rack` configuration is also added automatically, as shown in the following code:

    ```shell
    [kafka@test-rack-kafka-2 custom-config]$ cat server.config
    ##############################
    ##############################
    # This file is automatically generated by the Strimzi Cluster Operator
    # Any changes to this file will be ignored and overwritten!
    ##############################
    ##############################
    
    ##########
    # Broker ID
    ##########
    broker.id=2
    node.id=2
    
    ##########
    # Rack ID
    ##########
    broker.rack=${STRIMZI_RACK_ID}  // cat /opt/kafka/init/rack.id
    ```

## Test Cases

```shell
--- 1 partition under the topic, replication factor is 4, evenly distributed across each Kafka node
./bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 4 --partitions 1 --topic test-1
 
[kafka@test-rack-kafka-1 kafka]$ ./bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic test-1
1Topic: test-1  TopicId: -CNSnHsCT9eG7znhr5CYxA PartitionCount: 1       ReplicationFactor: 4    Configs: min.insync.replicas=2,message.format.version=3.0-IV1
        Topic: test-1   Partition: 0    Leader: 1       Replicas: 1,0,3,2       Isr: 1,0,3,2
 
--- 1 partition under the topic, replication factor is 2, distributed in west(0) and east(3) respectively, and the distribution across "data centers" is even
./bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 2 --partitions 1 --topic test-1
 
[kafka@test-rack-kafka-1 kafka]$ ./bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic test-2
Topic: test-2   TopicId: u_KNAaLjT3atQy_DTkmZfQ PartitionCount: 1       ReplicationFactor: 2    Configs: min.insync.replicas=2,message.format.version=3.0-IV1
        Topic: test-2   Partition: 0    Leader: 0       Replicas: 0,3   Isr: 0,3
 
--- 2 partitions under the topic, replication factor is 3, the distribution across "data centers" is not even, ensuring each "data center" has one
./bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 3 --partitions 2 --topic test-3
 
[kafka@test-rack-kafka-1 kafka]$ ./bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic test-3
Topic: test-3   TopicId: qBlTqRh6RCGS4vSukegMzg PartitionCount: 2       ReplicationFactor: 3    Configs: min.insync.replicas=2,message.format.version=3.0-IV1
        Topic: test-3   Partition: 0    Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
        Topic: test-3   Partition: 1    Leader: 1       Replicas: 1,2,0 Isr: 1,2,0
 
--- 10 partitions under the topic, replication factor is 4, the distribution across "data centers" is even
./bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 4 --partitions 10 --topic test-4
 
[kafka@test-rack-kafka-2 kafka]$  ./bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic test-4
Topic: test-4   TopicId: GDEe60DNST61gGCQX4OhLw PartitionCount: 10      ReplicationFactor: 4    Configs: min.insync.replicas=2,message.format.version=3.0-IV1
        Topic: test-4   Partition: 0    Leader: 1       Replicas: 1,2,0,3       Isr: 1,2,0,3
        Topic: test-4   Partition: 1    Leader: 0       Replicas: 0,1,3,2       Isr: 0,1,3,2
        Topic: test-4   Partition: 2    Leader: 3       Replicas: 3,0,2,1       Isr: 3,0,2,1
        Topic: test-4   Partition: 3    Leader: 2       Replicas: 2,3,1,0       Isr: 2,3,1,0
        Topic: test-4   Partition: 4    Leader: 1       Replicas: 1,0,3,2       Isr: 1,0,3,2
        Topic: test-4   Partition: 5    Leader: 0       Replicas: 0,3,2,1       Isr: 0,3,2,1
        Topic: test-4   Partition: 6    Leader: 3       Replicas: 3,2,1,0       Isr: 3,2,1,0
        Topic: test-4   Partition: 7    Leader: 2       Replicas: 2,1,0,3       Isr: 2,1,0,3
        Topic: test-4   Partition: 8    Leader: 1       Replicas: 1,2,0,3       Isr: 1,2,0,3
        Topic: test-4   Partition: 9    Leader: 0       Replicas: 0,1,3,2       Isr: 0,1,3,2
```
