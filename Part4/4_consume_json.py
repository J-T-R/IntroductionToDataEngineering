# This is an extension of 2_create_consumer_plus_land.py and will therefore not run on its own

import json

while True:
    messages = consumer.consume(num_messages=5, timeout=10)
    print(f"Total number of messages: {len(messages)}")
    for message in messages:
        print(json.loads(message.value()))
