# Kafka Topic 使用介绍

本教程介绍如何使用 Kafka 服务。内容简单、通用、开箱即用，
适用于想要快速完成 Producer 和 Consumer 开发的用户。

## 前置条件

从平台界面获取以下信息：

- **Bootstrap Servers**
- **Topic 名称** （若无则创建一个）
- （可选）SASL / TLS 配置
- （可选）用户名、密码

如果你能正常访问 Kafka 的服务器地址，即可继续。

## 安装依赖（Python）

```bash
pip install confluent-kafka
```

## 生产者示例（Producer）

创建 `producer.py`：

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

运行：

```bash
python producer.py
```

## 消费者示例（Consumer）

创建 `consumer.py`：

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

运行：

```bash
python consumer.py
```

## 常见错误与解决方案

| 问题                 | 原因           | 解决方式                                 |
| -------------------- | -------------- | ---------------------------------------- |
| `Connection refused` | 网络不可达     | 检查安全组、防火墙、VPC                  |
| `Timed out`          | 服务地址错误   | 核对 Bootstrap Servers                   |
| 无消息消费           | offset 在末尾  | 将 `auto.offset.reset` 设置为 `earliest` |
| SASL 认证失败        | 账号配置不一致 | 检查用户名密码是否对应                   |
