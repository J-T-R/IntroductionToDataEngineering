import duckdb

# Run the query
ten_logins = duckdb.query("""select * from 'logins.parquet' limit 10""")

# Inspect what's available
dir(ten_logins)

# See that we can get a pandas dataframe
type(ten_logins.to_df())

# View the output
print(ten_logins)

# Join our data
joined_data = duckdb.query(
    """
    select a.user_id, a.session_id, b.timestamp, b.object_id, b.object_option
    from 'logins.parquet' a
    join 'object_uses.parquet' b
    on a.session_id = b.session_id
    """
)

# Create some views that are out parquet files, so we can run explains
conn = duckdb.connect(database=":memory:")
conn.execute("""create view logins as (select * from 'logins.parquet')""")
conn.execute("""create view object_uses as (select * from 'object_uses.parquet')""")

# Get single session_id
session_id = conn.execute("""select session_id from logins limit 1""").fetchall()[0][0]
print(session_id)

# Get the object_uses for that session
object_uses = conn.execute(
    f"""select timestamp, object_id, object_option from object_uses where session_id = '{session_id}'"""
).fetch_df()
print(object_uses)

# Explain yourself
object_uses_explained = conn.execute(
    f"""explain select timestamp, object_id, object_option from object_uses where session_id = '{session_id}'"""
).fetchall()
print(object_uses_explained[0][1])
