from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random
import pytesseract
from PIL import Image

import requests
from hashlib import md5




def phone_num():
    num = ''
    num = random.choice(['182','187','155']) + str(random.randint(1000,9999)) + str(random.randint(1000,9999))
    num = int(num)
    return(num) 


def password(randomlength=8):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

def image():
    # image=Image.open('img_code.png')
    # vcode=pytesseract.image_to_string(image, lang="eng", config="-psm 7")
    # print(vcode)
    # return vcode
    # driver.maximize_window()  #将浏览器最大化

    driver.save_screenshot('D:\code_file\DeepLearing\interset\\aa.png')  #截取当前网页，该网页有我们需要的验证码
    imgelement = driver.find_element_by_xpath('//*[@id="back"]/div[2]/div[5]/div[3]/img')  #定位验证码
    location = imgelement.location  #获取验证码x,y轴坐标
    size=imgelement.size  #获取验证码的长宽
    rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
    i=Image.open("D:\code_file\DeepLearing\interset\\aa.png") #打开截图
    frame4=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save('D:\code_file\DeepLearing\interset\\frame4.jpg')
    qq=Image.open('D:\code_file\DeepLearing\interset\\frame4.jpg')
    text=pytesseract.image_to_string(qq).strip() #使用image_to_string识别验证码
    # 图片的正确率直接使用pytesseract不高， 可以使用超级鹰
    print(text)
    return text

# browser = webdriver.Chrome(executable_path='chromedriver.exe')
# driver = webdriver.Chrome()

driver = webdriver.Chrome('D:\code_file\DeepLearing\interset\chromedriver.exe') 
driver.get('http://t.cn/R1FawHe')

# 找到输入框位置
# input = WebDriverWait(browser, 10).until(
#                 EC.presence_of_element_located((By.XPATH, '//*[@id="phone"]')))

phone_num = phone_num()
input = driver.find_element_by_id('phone').send_keys(phone_num)

str_pw = password(8)
input1 = driver.find_element_by_id('password').send_keys(str_pw)
input2 = driver.find_element_by_id('n_password').send_keys(str_pw)

# image = driver.find_element_by_class_name('weui-vcode-img')
# image.screenshot_as_png()

image_num = image()
input_img = driver.find_element_by_id('code').send_keys(image_num)

# 在输入框中输入Python
driver.find_element_by_xpath('//*[@id="reg"]').click()

# 现在做滑动验证 有极验的验证方式， 可以用来参考， 这个滑动验证没有补全的图吗，需要用pil的灰度处理(时间7/12))
driver.save_screenshot('D:\code_file\DeepLearing\interset\slide.png')
s_image = driver.find_element_by_xpath('//*[@id="slideBkg"]')
s_loca = s_image.location
s_size = s_image.size
print(s_loca)
print(s_size)

driver.quit()

