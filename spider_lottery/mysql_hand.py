import pymysql.cursors


lista = [696425,'2018-08-03 21:28:52', 1, 4, 7, 2, 5, 9, 6, 3,10, 8] 
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
    # 创建表单 'data', 'time', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'
    # sql_table = "CREATE TABLE pk10db (date int(6) primary key, times DATETIME NULL , one int, two int, three int, four int, five int, six int,seven int, eight int, nine int, ten int)"
    # cursor.execute(sql_table)
    # print("{},{},{},{},{},{},{},{},{},{},{},{}".format(*lista))
    insert_data = "INSERT INTO pk10db  VALUES ({},'{}',{},{},{},{},{},{},{},{},{},{})".format(*lista)
    cursor.execute(insert_data)
    conn.commit()
    cursor.close()
    conn.close()


if __name__=="__main__":

    create_tabel()