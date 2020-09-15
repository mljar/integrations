import time
import json
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
get_data_sql = """select * from income"""

config = json.load(open("config.json", "r"))
last_inserted = config.get("last_inserted", 0)
n_records = 1000
try:
    conn = psycopg2.connect(pg_engine)
    cur = conn.cursor()

    print(f"Insert {n_records} into db ...")
    df = pd.read_csv("data/Adult_test.csv")
    df.index += 30001 # need to shift index
    
    df = df[last_inserted:last_inserted+n_records]
    df["income"] = None
    df["predicted_income"] = None
    buffer = StringIO()
    df.to_csv(buffer, index_label='id', header=False)
    buffer.seek(0)
    cur.copy_from(buffer, "income", sep=",")
    conn.commit()
    

    print("Samples inserted.")        

    cur.close()
except Exception as e:
    print("Problems:", str(e))


config["last_inserted"] = last_inserted + n_records
print(config)
with open("config.json", "w") as fout:
    fout.write(json.dumps(config, indent=4))