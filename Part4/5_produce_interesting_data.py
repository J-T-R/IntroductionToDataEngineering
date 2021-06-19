# This is an extension of 3_produce_data.py and will therefore not run on its own

"""
dataclasses are fairly new to python, they give us lots of nice things for free but I won't be
exploring them here
"""
from dataclasses import dataclass, asdict
import json
from datetime import datetime
import uuid


@dataclass
class ChangeBalance:
    user_id: str
    area_id: str
    event_timestamp: str
    balance: int


producer.produce(
    "batch",
    json.dumps(
        asdict(
            ChangeBalance(
                user_id=str(uuid.uuid4()),
                area_id=str(uuid.uuid4()),
                # timezones are important, let's keep everything utc
                event_timestamp=datetime.utcnow().isoformat(),
                balance=-10,
            )
        )
    ),
)
