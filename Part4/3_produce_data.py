# This is an extension of 1_create_topic_setup_producer.py and will therefore not run on its own

# Send a single message
producer.produce("batch", "first".encode("utf-8"))

# More messages
for x in range(0, 5):
    producer.produce("batch", str(x).encode("utf-8"))

# More messages with some sleeping to make things interesting
import time
from random import randint

for x in range(0, 20):
    producer.produce("batch", str(x).encode("utf-8"))
    time.sleep(randint(1, 5))

# More messages that are allowed per consumer batch
for x in range(0, 100):
    producer.produce("batch", str(x).encode("utf-8"))
