# This is an extension of 4_consume_json.py and will therefore not run on its own

from datetime import datetime

while True:
    messages = consumer.consume(num_messages=5, timeout=10)
    print(f"Total number of messages: {len(messages)}")
    # Only write a file if there's data to write
    if len(messages) > 0:
        # Use "a" here for append, if we use "w" then we risk overriding a file
        with open(f"batch_{datetime.utcnow().isoformat()}.json", "a") as file:
            for message in messages:
                json.dump(json.loads(message.value()), file)
                # Remember to end with a newline!
                file.write("\n")
