
import numpy as np
import pandas as pd
import psycopg2
from io import StringIO

host = "0.0.0.0"
port = 5555
user = "postgres"
password = "1234"
db = "db"

pg_engine = "user='{}' password='{}' host='{}' port='{}' dbname='{}'".format(user, password, host, port, db)

drop_table_sql = """drop table income"""


try:
    conn = psycopg2.connect(pg_engine)
    cur = conn.cursor()
    cur.execute(drop_table_sql)
    conn.commit()
    cur.close()
    print("Table dropped.")
    with open("config.json", "w") as fout:
        fout.write("{}")
except Exception as e:
    print("Problems:", str(e))
