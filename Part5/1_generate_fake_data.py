from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
import uuid
from random import randint, choice
import pandas as pd
from itertools import chain

OBJECT_IDS = [x for x in range(20)]
OBJECT_OPTIONS = [x for x in ["open", "close", "push", "pull"]]

# A login event
@dataclass
class Login:
    user_id: str
    session_id: str
    timestamp: datetime


# An object use event
@dataclass
class ObjectUse:
    session_id: str
    timestamp: datetime
    object_id: str
    object_option: str


class RouteCreator:
    def __init__(self, user_id):
        self.user_id = user_id
        self.login_timestamp = datetime.now()
        self.session_id = str(uuid.uuid4())
        self.route = []

    def _append_login(self):
        self.route.append(
            Login(
                user_id=self.user_id,
                session_id=self.session_id,
                timestamp=self.login_timestamp,
            )
        )

    @staticmethod
    def _random_increase_timestamp(timestamp):
        return timestamp + timedelta(seconds=randint(1, 10))

    def _create_increasing_timestamps(self, num_times):
        times = 0
        timestamps = [self._random_increase_timestamp(self.login_timestamp)]
        while times < num_times:
            timestamps.append(self._random_increase_timestamp(timestamps[times]))
            times += 1
        return timestamps

    def _append_object_uses(self):
        for timestamp in self._create_increasing_timestamps(randint(1, 10)):
            self.route.append(
                ObjectUse(
                    session_id=self.session_id,
                    timestamp=timestamp,
                    object_id=choice(OBJECT_IDS),
                    object_option=choice(OBJECT_OPTIONS),
                )
            )

    def get_route(self):
        self._append_login()
        self._append_object_uses()
        return self.route


routes = [RouteCreator(str(uuid.uuid4())).get_route() for _ in range(100)]

logins = []
object_uses = []

for route in routes:
    logins.append(route[0])
    object_uses = object_uses + route[1:]

logins_df = pd.DataFrame(asdict(z) for z in logins)
logins_df.to_parquet("logins.parquet", engine="fastparquet", times="int96")

object_uses_df = pd.DataFrame(asdict(a) for a in object_uses)
object_uses_df.to_parquet("object_uses.parquet", engine="fastparquet", times="int96")
