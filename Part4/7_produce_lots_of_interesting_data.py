# This is an extension of 5_produce_interesting_data.py and will therefore not run on its own


def make_change_balance(
    user_id: str = str(uuid.uuid4()),
    area_id: str = str(uuid.uuid4()),
    timestamp: str = datetime.utcnow().isoformat(),
    balance: int = 10,
):
    return ChangeBalance(
        user_id=user_id,
        area_id=area_id,
        # timezones are important, let's keep everything utc
        event_timestamp=timestamp,
        balance=balance,
    )


# Send a single item, this should write 1 record to its own file
producer.produce("batch", json.dumps(asdict(make_change_balance(user_id="different"))))
# Sleep just to make sure that we are only going to write to a single file
# (remember that the timeout on the consumer is set to 10 seconds)
time.sleep(11)

# Send lots of data, this should write 20 files because we consume in batches of 5
for x in range(0, 100):
    producer.produce("batch", json.dumps(asdict(make_change_balance())))
