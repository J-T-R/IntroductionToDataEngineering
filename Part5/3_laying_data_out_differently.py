import pandas as pd

# Reread our data
object_uses = pd.read_parquet("object_uses.parquet")

# Rewrite with a partition
object_uses.to_parquet(
    "object_uses_session_partition.parquet",
    engine="fastparquet",
    times="int96",
    partition_cols=["session_id"],
)
