import time
import json
import numpy as np
import pandas as pd
import psycopg2
from io import StringIO
from supervised import AutoML

from db import db_engine 

get_data_sql = f"select * from census where income = ''"

try:
    conn = psycopg2.connect(db_engine())
    cur = conn.cursor()

    cur.execute(get_data_sql)
    df = pd.DataFrame(cur.fetchall(), columns=[elt[0] for elt in cur.description])
    print("New records:", df.shape[0])

    if df.shape[0] > 0:
        # compute accuracy
        test = pd.read_csv("data/Adult_test.csv")
        accuracy = np.sum(test["income"] == df["predicted_income"]) / test.shape[0] * 100.0
        print(f"Accuracy: {accuracy}%")


    cur.close()
except Exception as e:
    print("Problems:", str(e))
