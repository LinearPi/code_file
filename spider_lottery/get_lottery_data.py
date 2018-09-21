import requests 
import urllib.request
from lxml import etree

import pymysql.cursors


url = "http://trend.caipiao.163.com/qxc/?periodNumber=100"
dd = []

def get_data_and_date(url):
    # 只需要爬到两个数据就行, 
    data = urllib.request.urlopen(url).read()
    html = data.decode('UTF-8','ignore')
    page = etree.HTML(html.lower())

    for i in range(1,120):
        datas = page.xpath('string(//*[@id="cpdata"]/tr[' + str(i) + ']/td[1])')
        nums = page.xpath('string(//*[@id="cpdata"]/tr[' + str(i) + ']/td[3])')
        dd.append([datas, nums])


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
    sql_table = "CREATE TABLE qxc (date int(5), data int(7)zerofill)"
    cursor.execute(sql_table)
    conn.commit()
    cursor.close()
    conn.close()


def income_data(data):     
    # 数据库的链接
    conn = pymysql.Connect(
        # host='118.24.26.162',
        host='localhost',
        port=3306,
        user='linear',
        password='lin123456',
        db='pk10db',
        charset='utf8'
        )
    # 获取游标
    cursor = conn.cursor()
    # 加入数据 加入循环, 把所有的数据都传进去 写一个循环
    for i in range(0,119):
        sql_add_data = "INSERT INTO qxc (date, data) VALUES ( '%s', '%s' )"
        dataes = (str(data[i][0]), str(data[i][1]))
        cursor.execute(sql_add_data % dataes)
        conn.commit()
    cursor.close()
    conn.close()


def query_data():
     # 数据库的链接
    conn = pymysql.Connect(
        # host='118.24.26.162',
        host='localhost',
        port=3306,
        user='root',
        password='li123456',
        db='lotterydb',
        charset='utf8'
        )
    # 获取游标
    cursor = conn.cursor()
    # 添加查询的语句
    sql_query = "select * from qxc" 
    cursor.execute(sql_query)
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for row in results:
            # 打印时间
            date = row[0]
            # 打印数据
            data = row[1]
            # print(data)
            print("date : {},  data : {}".format(date,data))
    except:
        print("error")
    # conn.commit()

    cursor.close()
    conn.close()


if __name__ =='__main__':
    # create_tabel()

    # get_data_and_date(url)
    # income_data(dd)

    query_data()