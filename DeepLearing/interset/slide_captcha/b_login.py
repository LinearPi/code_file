# 使用selenium来做自动化登录，主要的点在于登录之后的验证，

from selenium import webdriver
import time
import re
from io import BytesIO
import requests
from PIL import Image
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from track import SlidingTrack

'''
driver = webdriver.Chrome(executable_path='D:\code_file\DeepLearing\interset\chromedriver.exe') 
driver.get('https://www.bilibili.com/')

driver.maximize_window()
login_button = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div[3]/ul/li[1]/a')
login_button.click()

myname = '18780236045'
mypassword = 'li15280221'

# 找到元素和填入密码
username = driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(myname)
password = driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys(mypassword)
'''

# 现在对验证码进行验证，

class ImgaeIdentify(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='D:\code_file\DeepLearing\interset\chromedriver.exe') 
        self.wait = WebDriverWait(self.driver, 10)

    def get_and_login(self, name, password):
        # 打开网页，找到元素和填入密码
        self.name = name
        self.passwd = password
        self.driver.get(r'https://www.bilibili.com/')
        self.driver.maximize_window()
        login_button = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div[3]/ul/li[1]/a')
        login_button.click()
        username = self.driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(name)
        password = self.driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys(password)

    def get_image(self):
        # 获取没有缺口的图片
        nogap_image = self.wait.until(EC.presence_of_all_elements_located((
            By.XPATH, '//div[@class="gt_widget gt_clean gt_show"]/div')))            
        nogap_image = self.get_complete_image(nogap_image)
        Image.SAVE()

        # 获取有缺口的图片
        gap_image = self.wait.until(EC.presence_of_all_elements_located((
                    By.XPATH, '//div[@class="gt_cut_bg gt_show"]/div')))
        gap_image = self.get_complete_image(gap_image)


    def get_complete_image(self, image):
        # 将获取的图片重新裁剪拼接为一张完整的图片
        # 用正则获取元素中的图片url链接
        image_url = re.search(r'url\("(.*?)"\);',
                              image[0].get_attribute('style')).group(1)
        # 获取列表中每张小图的位置偏移信息
        image_position_list = [i.get_attribute('style') for i in image]
        image_position_list = [
            re.search(r'position: -(.*?)px -?(.*?)px;',
                      i).groups() for i in image_position_list]                     
        
        # 访问图片链接，获取图片的二进制数据
        im = requests.get(image_url).content
        # PIL要从二进制数据读取一个图片的话，需要把其转化为BytesIO
        im = BytesIO(im)
        im = Image.open(im)
        # 生成一个新的相同大小的空白图片
        new_im = Image.new('RGB', (260, 116))

        # 设置一个粘贴坐标，坐标每次循环加10，则从左到右依次粘贴
        count_up = 0
        count_low = 0
        # 图片主要分为上下两个部分，所以分成两个循环分别粘贴
        # image_list前26个为上半部分，后26个为下半部分
        # 每个小图片大小为10，58
        for i in image_position_list[:26]:
            croped = im.crop((int(i[0]), 58, int(i[0])+10, 116))
            new_im.paste(croped, (count_up, 0))
            count_up += 10
        for i in image_position_list[26:]:
            croped = im.crop((int(i[0]), 0, int(i[0])+10, 58))
            new_im.paste(croped, (count_low, 58))
            count_low += 10

        return new_im
    
    def get_image_diff(self, nogap_image, gap_image):
        # 比较两个图片之间的不同
        # 图片是RGB格式， 有3层需要处理
        def compare_pixel(pixel1, pixel2):
            for i in range(3):
                if abs(pixel1[i] - pixel2[i])>50:
                    return False

        # 验证码大小应该是260*120
        for i in range(1, 259):
            for i in range(1, 115):
                nogap_pixel = nogap_image.getpixel(i. j)
                gap_pixel = gap_image.getpixel(i. j)
                if compare_pixel(nogap_pixel, gap_pixel) is False:
                    return i
                    
    def slide_butten(self, position):
        # 找到滑动的滑块
        slide_butten = self.wait.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="gc-box"]/div/div[3]/div[2]'
        )))
        # 开始滑动
        ActionChains(self.driver).click_and_hold(slide_butten).perform()
        # 利用生产的轨迹，逐步移动鼠标
        for i in SlidingTrack(position-5).get_move_list():
            ActionChains(self.driver).move_by_offset(
                xoffset=i, yoffset=0).perform()
        # 松开鼠标
        ActionChains(self.driver).release().perform()


if __name__ == '__main__':
    login_b =  ImgaeIdentify()
    myname = '18780236045'
    mypassword = 'li15280221'
    login_b.get_and_login(myname, mypassword)
    position = login_b.get_image()
    login_b.slide_butten(position)
    time.sleep(10)
    
    




# driver.quit()