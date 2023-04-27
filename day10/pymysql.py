from pymysql import Connect
conn = Connect(host= 'localhost',port=3306,user='root',password='123456')
cur = conn.cursor()
sql_str='show databases'
cur.execute(sql_str)

data= cur.fetchall()
print(data)

cur.close()
conn.close()


