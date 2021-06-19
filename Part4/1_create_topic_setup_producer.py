from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Producer

# Create an admin client and use that to create a topic
admin_client = AdminClient({"bootstrap.servers": "localhost:9092"})
admin_client.create_topics([NewTopic("batch", 1, 1)])

# Check what topics are available
admin_client.list_topics().topics

# Setup a producer
producer = Producer({"bootstrap.servers": "localhost:9092"})
