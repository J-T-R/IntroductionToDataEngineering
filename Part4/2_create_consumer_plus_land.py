from confluent_kafka import Consumer

consumer = Consumer({"bootstrap.servers": "localhost:9092", "group.id": "test"})
consumer.subscribe(["batch"])

while True:
    # set maximum number of messages to be 5 and a wait timeout of 10s
    messages = consumer.consume(num_messages=5, timeout=10)
    print(f"Total number of messages: {len(messages)}")
    for message in messages:
        print(message.value().decode("utf-8"))
