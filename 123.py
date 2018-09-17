import pymysql
import pandas as pd
import matplotlib.pyplot as plt

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='954672813', db='Hoba')
cur = conn.cursor()
sql = 'SELECT * FROM Hobana'
df = pd.read_sql_query(sql, conn)
df_date = set(df.Date)
print(*df_date)
df_by_date = df[df.Date == df_date]
df1 = df[df.Podhod == '1']
plt.plot(df.Date[0], df1.How)

