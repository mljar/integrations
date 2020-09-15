

import numpy as np
import pandas as pd
import psycopg2
from supervised import AutoML

host = "0.0.0.0"
port = 5555
user = "postgres"
password = "1234"
db = "db"

pg_engine = "user='{}' password='{}' host='{}' port='{}' dbname='{}'".format(user, password, host, port, db)

get_data_sql = """select * from income"""

try:
    conn = psycopg2.connect(pg_engine)
    cur = conn.cursor()

    cur.execute(get_data_sql)
    df = pd.DataFrame(cur.fetchall(), columns=[elt[0] for elt in cur.description])


    print(f"There is {df.shape[0]} records in the table.")
    cur.close()
except Exception as e:
    print("Problems:", str(e))

target = "income"
features = df.columns[:-2]

print("Train AutoML income classifier")
automl = AutoML(results_path="Income_classifier")
automl.fit(df[features], df[target])