import polars as pl
import duckdb

con = duckdb.connect(database="db/olympics.duckdb", read_only=False)

tbl_to_read = ["athletes", "medals_total", "medals", "teams", "nocs"]
data_olympics = {tbl: pl.read_csv(f"raw_data/{tbl}.csv") for tbl in tbl_to_read}

for tbl in tbl_to_read:
    data = data_olympics[tbl]
    print(data)
    print(f"CREATE TABLE IF NOT EXISTS '{tbl}' AS SELECT * FROM data")
    con.execute(f"CREATE TABLE IF NOT EXISTS '{tbl}' AS SELECT * FROM data")

con.close()
