import time
import json
import numpy as np
import pandas as pd
import psycopg2
from io import StringIO
from supervised import AutoML

from db import db_engine

get_data_sql = f"select * from census where income = '' and predicted_income = ''"

try:
    conn = psycopg2.connect(db_engine())
    cur = conn.cursor()

    cur.execute(get_data_sql)
    df = pd.DataFrame(cur.fetchall(), columns=[elt[0] for elt in cur.description])
    print("New records:", df.shape[0])

    if df.shape[0] > 0:
        # compute predictions
        print("Load AutoML income classifier")
        automl = AutoML(results_path="Income_classifier")
        print("Compute predictions")
        predictions = automl.predict(df)

        df["predicted_income"] = predictions
        tuples = [tuple(x) for x in df[["predicted_income", "id"]].to_numpy()]
        query = "update census set predicted_income = %s where id = %s"

        cur.executemany(query, tuples)
        conn.commit()

    cur.close()
except Exception as e:
    print("Problems:", str(e))
