import time
import json
import numpy as np
import pandas as pd
import psycopg2
from io import StringIO
from supervised import AutoML

host = "0.0.0.0"
port = 5555
user = "postgres"
password = "1234"
db = "db"

pg_engine = "user='{}' password='{}' host='{}' port='{}' dbname='{}'".format(user, password, host, port, db)


config = json.load(open("config.json", "r"))
predicted = 29999
get_data_sql = f"select * from income where id > {last_predicted}"

try:
    conn = psycopg2.connect(pg_engine)
    cur = conn.cursor()


    cur.execute(get_data_sql)
    df = pd.DataFrame(cur.fetchall(), columns=[elt[0] for elt in cur.description])
    print("New records:", df.shape[0])

    if df.shape[0] > 0:
        # compute predictions
        print("Train AutoML income classifier")
        
        automl = AutoML(results_path="Income_classifier")
        predictions = automl.predict(df)

        print(predictions)

        df["predicted_income"] = predictions["label"]


        tuples = [tuple(x) for x in df[["predicted_income", "id"]].to_numpy()]
        
        query  = "update income set predicted_income = %s where id = %s"
        
        cur.executemany(query, tuples)
        conn.commit()
        
        config["last_predicted"] = int(np.max(df["id"]))
        with open("config.json", "w") as fout:
            fout.write(json.dumps(config, indent=4))


    cur.close()
except Exception as e:
    print("Problems:", str(e))
