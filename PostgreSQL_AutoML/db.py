""" Database API """
import json
import numpy as np
import pandas as pd
import psycopg2
from io import StringIO

def db_engine():
    config = json.load(open("config.json"))
    host = config["connection"]["host"]
    port = config["connection"]["port"]
    user = config["connection"]["user"]
    # password should be hidden in production setting
    # do not store it in config.json
    password = config["connection"]["password"]
    db = config["connection"]["db"]

    return "user='{}' password='{}' host='{}' port='{}' dbname='{}'".format(
        user, password, host, port, db
    )

def sql_to_df(sql_query):
    try:
        conn = psycopg2.connect(db_engine())
        cur = conn.cursor()
        cur.execute(sql_query)
        df = pd.DataFrame(cur.fetchall(), columns=[elt[0] for elt in cur.description])
        cur.close()
        return df
    except Exception as e:
        print("Problems:", str(e))
    
    return None


def get_train_data():
    config = json.load(open("config.json"))
    table = config["automl"]["table"]
    features = config["automl"]["features"]
    target = config["automl"]["target"]
    get_data_sql = f"select {','.join(features+[target])} from {table} where {target} != ''"
    df = sql_to_df(get_data_sql)
    if df is None:
        return None, None
    return df[features], df[target]
    
    
def get_live_data():
    config = json.load(open("config.json"))
    table = config["automl"]["table"]
    features = config["automl"]["features"]
    target = config["automl"]["target"]
    predicted = config["automl"]["predicted"]
    id_column = config["automl"]["id"]
    get_data_sql = f"select {','.join(features + [id_column])} from {table} where {target} = '' and {predicted} = ''"
    df = sql_to_df(get_data_sql)
    if df is None:
        return None, None
    return df[features], df[id_column]


def get_predictions():
    config = json.load(open("config.json"))
    table = config["automl"]["table"]
    target = config["automl"]["target"]
    predicted = config["automl"]["predicted"]
    id_column = config["automl"]["id"]
    get_data_sql = f"select {','.join([predicted] + [id_column])} from {table} where {target} = ''"
    df = sql_to_df(get_data_sql)
    if df is None:
        return None
    df.index = df[id_column]
    return df
    
def insert_predictions(predictions, ids):
    config = json.load(open("config.json"))
    table = config["automl"]["table"]
    predicted = config["automl"]["predicted"]
    id_column = config["automl"]["id"]

    try:
        conn = psycopg2.connect(db_engine())
        cur = conn.cursor()
        tuples = list(zip(predictions, ids))
        sql_query = f"update {table} set {predicted} = %s where {id_column} = %s"
        cur.executemany(sql_query, tuples)
        conn.commit()
    except Exception as e:
        print("Problems:", str(e))
    
