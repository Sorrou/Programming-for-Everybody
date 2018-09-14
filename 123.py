import pymysql
import pandas as pd

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='954672813', db='Hoba')
cur = conn.cursor()
sql = 'SELECT * FROM Hobana'
df = pd.read_sql_query(sql, conn)
for i in df:
