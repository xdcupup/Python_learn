from pymysql import Connect
# 创建连接
conn = Connect(host='localhost',port=3306,user='root',password='123456')
# 生成游标 ：操作MySQL的一个对象
cur = conn.cursor()
# 编写sql语句
# sql_str = 'create database ming charset=utf8'
sql_str = 'show databases'
# 使用游标执行 sql语句
cur.execute(sql_str)

# 获取数据
data = cur.fetchall()
print(data)


# 关闭
cur.close()
conn.close()
