import numpy as np
import pandas as pd
import psycopg2
from io import StringIO

from db import db_engine 

drop_table_sql = """drop table marketing"""

try:
    conn = psycopg2.connect(db_engine())
    cur = conn.cursor()
    cur.execute(drop_table_sql)
    conn.commit()
    cur.close()
    print("Table dropped.")
    
except Exception as e:
    print("Problems:", str(e))
