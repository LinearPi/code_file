import pymysql.cursors


def create_tabel():
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        password='li123456',
        db='lotterydb',
        charset='utf8'
        )
    # 获取游标
    cursor = conn.cursor()
    # 创建表单
    # sql_table = "CREATE TABLE pk10db (date int(6) primary key, times DATETIME NULL , number1 int, number2 int)"
    # cursor.execute(sql_table)
    insert_data = "INSERT INTO pk10db  VALUES (64347,'2018-07-23 23:07:07',05,06)"
    cursor.execute(insert_data)
    conn.commit()
    cursor.close()
    conn.close()


if __name__=="__main__":
    create_tabel()