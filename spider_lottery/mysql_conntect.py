import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='shan123456',
    db='spiderdb',
    charset='utf8'
    )

# 获取游标

cursor = connect.cursor()

# 插入数据
sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
data1 = ('王磊', '13544445678', 10001)
data2 = ('张红雷', '13555545678', 10002)
cursor.execute(sql % data2)
connect.commit()
