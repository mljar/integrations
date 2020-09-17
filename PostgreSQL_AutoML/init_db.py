import numpy as np
import pandas as pd
import psycopg2
from io import StringIO

from sklearn.model_selection import train_test_split
from db import db_engine 

create_table_sql = """
CREATE TABLE IF NOT EXISTS marketing (
    id serial PRIMARY KEY,
    age integer,
    job varchar(128),
    marital varchar(128),
    education varchar(128),
    default_payment varchar(128),
    balance integer,
    housing varchar(128),
    loan varchar(128),
    day integer,
    month varchar(128),
    duration real,
    campaign integer, 
    pdays integer,
    previous integer,
    poutcome varchar(128),
    response varchar(128),
    predicted_response varchar(128)
)
"""

get_data_sql = """select * from marketing"""

df = pd.read_csv("data/bank_cleaned.csv", index_col="id")
df.drop("response_binary", axis=1, inplace=True)
df["predicted_response"] = ""
test_size= 0.20 # 20% for testing
df_train, df_test = train_test_split(df, test_size=test_size, random_state=1234)
df_train.to_csv("data/train.csv")
df_test.to_csv("data/test.csv")
df_test = df_test.copy()
df_test["response"] = ""

df = pd.concat([df_train, df_test])

try:
    conn = psycopg2.connect(db_engine())
    cur = conn.cursor()
    print("Create marketing table")
    cur.execute(create_table_sql)
    conn.commit()
    print("Insert train and test data into table ...")
    buffer = StringIO()
    df.to_csv(buffer, index_label="id", header=False)
    buffer.seek(0)
    cur.copy_from(buffer, "marketing", sep=",")
    conn.commit()
    print("Insert finished.")

    cur.close()
except Exception as e:
    print("Problems:", str(e))
