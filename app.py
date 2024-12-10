import os
import logging
import duckdb
import streamlit as st


if "db" not in os.listdir():
    print("creating folder db")
    logging.error(os.listdir())
    logging.error("creating folder db")
    os.mkdir("db")

if "olympics.duckdb" in os.listdir("db"):
    logging.warning("deleting db")
    os.remove("db/olympics.duckdb")

if "olympics.duckdb" not in os.listdir("db"):
    logging.warning("creating db")
    exec(open("import_data/data.py").read())

con = duckdb.connect(database="db/olympics.duckdb", read_only=False)


# for tbl in ["athletes", "medals_total", "medals", "teams", "nocs"]:
for tbl in ["athletes"]:
    # breakpoint()
    df_table = con.execute(f"SELECT * FROM {tbl} LIMIT 5").df()
    st.dataframe(df_table)


con.close()
