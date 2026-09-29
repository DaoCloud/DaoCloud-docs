# Introduction to Using Kafka Topics

This tutorial introduces how to use the Kafka service. The content is simple, generic, and ready to use,
making it suitable for users who want to quickly complete Producer and Consumer development.

## Prerequisites

Obtain the following information from the platform UI:

- **Bootstrap Servers**
- **Topic name** (create one if you do not have one)
- (Optional) SASL / TLS configuration
- (Optional) Username and password

If you can access the Kafka server address normally, you can continue.

## Install Dependencies (Python)

```bash
pip install confluent-kafka
```

## Producer Example

Create `producer.py`:

```python
from confluent_kafka import Producer

conf = {
    "bootstrap.servers": "YOUR_BOOTSTRAP_SERVERS"
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print("Delivery failed:", err)
    else:
        print("Delivered to", msg.topic(), msg.partition())

producer.produce("YOUR_TOPIC", value="hello kafka", callback=delivery_report)
producer.flush()
```

Run:

```bash
python producer.py
```

## Consumer Example

Create `consumer.py`:

```python
from confluent_kafka import Consumer

conf = {
    "bootstrap.servers": "YOUR_BOOTSTRAP_SERVERS",
    "group.id": "demo-group",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(conf)
consumer.subscribe(["YOUR_TOPIC"])

print("Waiting for messages...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Error:", msg.error())
            continue
        print("value=", msg.value())
finally:
    consumer.close()
```

Run:

```bash
python consumer.py
```

## Common Errors and Solutions

| Issue                       | Cause                                | Solution                                        |
| --------------------------- | ------------------------------------ | ----------------------------------------------- |
| `Connection refused`        | Network unreachable                  | Check the security group, firewall, and VPC     |
| `Timed out`                 | Incorrect service address            | Verify the Bootstrap Servers                    |
| No messages consumed        | offset is at the end                 | Set `auto.offset.reset` to `earliest`           |
| SASL authentication failure | Inconsistent account configuration   | Check whether the username and password match   |
