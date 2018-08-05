
import requests
from requests.exceptions import RequestException
import re
import time
import csv


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
    file_path = '/Users/pizi/Documents/git_flie/code_file/pk10_8.csv'
    with open(file_path,'a') as files:
    # reader =csv.reader(files)    

        writer = csv.writer(files)
        # writer.writerow(['data', 'time', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'])
        for item in items:
            writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5], item[6], 
            item[7], item[8], item[9], item[10], item[11]])
        # files.close()

def main():
    file_path = '/Users/pizi/Documents/git_flie/code_file/pk10_8.csv'
    with open(file_path,'a') as files:
            
        # writer = csv.writer(files)
        # writer.writerow(['data', 'time', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'])
        for i in range(0,9726):
            url = 'https://kj.cjcp.com.cn/gaopin/bjpk10/index.php?topage='+str(i) 
            html = get_one_page(url)    
            items= parse_one_page(html)
            # print(items)
            save_to_csv(items)
    # print(html)
    # files.close()

if __name__ == '__main__':
    
    main()



'''
time.strftime("%Y%m%d") + '(.*?).png.*?'+
time.strftime("%Y%m%d") + '(.*?).png.*?'+
time.strftime("%Y%m%d") + '(.*?).png.*?'+
time.strftime("%Y%m%d") + '(.*?).png.*?'+
time.strftime("%Y%m%d") + '(.*?).png.*?'+
time.strftime("%Y%m%d") + '(.*?).png.*?'+
time.strftime("%Y%m%d") + '(.*?).png.*?'+
time.strftime("%Y%m%d") + '(.*?).png.*?'+
time.strftime("%Y%m%d") + '(.*?).png.*?'
'''