import polars as pl
import duckdb

con = duckdb.connect(database="db/olympics.duckdb", read_only=False)

con.execute("CREATE TABLE athletes AS SELECT * FROM athletes")
tbl_to_read = ["athletes", "medals_total", "medals", "teams", "nocs"]
data_olympics = {tbl: pl.read_csv(f"raw_data/{tbl}.csv") for tbl in tbl_to_read}

for tbl in tbl_to_read:
    data = data_olympics[tbl]
    con.execute(f"CREATE TABLE IF NOT EXISTS {tbl} AS SELECT * FROM data")

con.close()
