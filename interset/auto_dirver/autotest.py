from selenium import webdriver
import time

def login_xigua():
    driver = webdriver.Chrome('/Users/gouweiqi/Documents/code_py/code_file/interset/auto_dirver/chromedriver') 
    driver.get('https://www.xiguacity.cn/admin')
    print('1')
    # time.sleep(10)
    
    # print('2')
    # driver.close()




if __name__=='__main__':
    login_xigua()