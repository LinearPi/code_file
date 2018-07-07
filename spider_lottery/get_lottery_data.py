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
        password='shan123456',
        db='datadb',
        charset='utf8'
        )
    # 获取游标
    cursor = conn.cursor()
    # 创建表单
    sql_table = "CREATE TABLE qxct (date int(5), data int(7)zerofill)"
    cursor.execute(sql_table)
    conn.commit()

def income_data(data):
    # 数据库的链接
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        password='shan123456',
        db='datadb',
        charset='utf8'
        )
    # 获取游标
    cursor = conn.cursor()
  
    # 加入数据 加入循环, 把所有的数据都传进去 写一个循环
    for i in range(0,119):
        sql_add_data = "INSERT INTO qxct (date, data) VALUES ( '%s', '%s' )"
        dataes = (str(data[i][0]), str(data[i][1]))
        cursor.execute(sql_add_data % dataes)
        conn.commit()

    cursor.close()
    conn.close()

if __name__ =='__main__':
    get_data_and_date(url)
    income_data(dd)
    # create_tabel()
    # for i in range(1, len(dd)+1):
    #     print(dd[i][0], dd[i][1])
    # income_data(dd)