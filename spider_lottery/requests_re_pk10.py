
import requests
from requests.exceptions import RequestException
import re
import time
import csv
import pymysql.cursors
from pymysql.err import IntegrityError


def get_one_page(url):
    #  使用requests获取数据
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # 判断这个页面是否返回成功
            return response.text
        return response.status_code
    except RequestException:
        return None

def parse_one_page(html):
    # 使用正则进行数据提取。
    pattern = re.compile('class="qihao">(.*?)期.*?class="time">(.*?)</td>.*?class="kjhm t_center">.*?img/\d{15}(\d{2}).*?img/\d{15}(\d{2}).*?img/\d{15}(\d{2}).*?img/\d{15}(\d{2}).*?img/\d{15}(\d{2}).*?img/\d{15}(\d{2}).*?img/\d{15}(\d{2}).*?img/\d{15}(\d{2}).*?img/\d{15}(\d{2}).*?img/\d{15}(\d{2}).*?' , re.S)
    items = re.findall(pattern, html)
    return items

def save_to_csv(items):
<<<<<<< HEAD
    file_path = '/Users/pizi/Documents/git_flie/code_file/pk10_7.csv'
=======
<<<<<<< HEAD
    file_path = '/Users/pizi/Documents/git_flie/code_file/pk10_7_26.csv'
=======
    file_path = '/Users/pizi/Documents/git_flie/code_file/pk10_8.csv'
>>>>>>> 5a54066077d5ec6e852495dd82d55f7ca658cb5c
>>>>>>> 8871d73cabebc908c60da16940c8457a34860a4d
    with open(file_path,'a') as files:
    # reader =csv.reader(files)    

        writer = csv.writer(files)
        # writer.writerow(['data', 'time', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'])
        for item in items:
            writer.writerow([item[0], str(item[1]), int(item[2]), int(item[3]), int(item[4]), int(item[5]), int(item[6]), 
            int(item[7]), int(item[8]), int(item[9]), int(item[10]), int(item[11])])
        # files.close()

def save_data(items):
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        password='li123456',
        db='lotterydb',
        charset='utf8'
        )
    cursor = conn.cursor()
    for item in items:
        try:
            insert_data = "INSERT INTO pk10db  VALUES ({},'{}',{},{},{},{},{},{},{},{},{},{})".format(*item)
            cursor.execute(insert_data)
            conn.commit()
        except pymysql.err.IntegrityError:
            pass
    cursor.close()
    conn.close()



def main():
<<<<<<< HEAD
    file_path = '/Users/pizi/Documents/git_flie/code_file/pk10_7.csv'
=======
<<<<<<< HEAD
    file_path = '/Users/pizi/Documents/git_flie/code_file/pk10_7_26.csv'
    with open(file_path,'a') as files:
            
        writer = csv.writer(files)
        writer.writerow(['data', 'time', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'])
        # for i in range(0,7):
        url = 'https://kj.cjcp.com.cn/gaopin/bjpk10/index.php?topage=1' 
        html = get_one_page(url)    
        items= parse_one_page(html)
        # print(items)
        save_to_csv(items)
=======
    file_path = '/Users/pizi/Documents/git_flie/code_file/pk10_8.csv'
>>>>>>> 8871d73cabebc908c60da16940c8457a34860a4d
    with open(file_path,'a') as files:
            
        # writer = csv.writer(files)
        # writer.writerow(['data', 'time', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'])
<<<<<<< HEAD
        for i in range(0,9742):
            try:                
                url = 'https://kj.cjcp.com.cn/gaopin/bjpk10/index.php?topage='+ str(i)
                html = get_one_page(url)    
                items= parse_one_page(html)
                print(i)
                # save_to_csv(items)
                save_data(items)
                print(i)
            except TypeError:
                pass
=======
        for i in range(0,9726):
            url = 'https://kj.cjcp.com.cn/gaopin/bjpk10/index.php?topage='+str(i) 
            html = get_one_page(url)    
            items= parse_one_page(html)
            # print(items)
            save_to_csv(items)
>>>>>>> 5a54066077d5ec6e852495dd82d55f7ca658cb5c
>>>>>>> 8871d73cabebc908c60da16940c8457a34860a4d
    # print(html)
    files.close()

if __name__=='__main__':
    main()