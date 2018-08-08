import re
import time
from io import BytesIO

import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random

from track import SlidingTrack


class CrackJee(object):
    def __init__(self):
        self.options = self._set_options()
        self.driver = webdriver.Chrome(executable_path='D:\code_file\DeepLearing\interset\chromedriver.exe',
                                       chrome_options=self.options)
        self.wait = WebDriverWait(self.driver, 10)

    # 设置启动选项
    def _set_options(self):
        options = Options()
        options.add_argument("--window-size=1366,768")
        # options.add_argument("--headless") # 启动无界面
        # options.add_argument("--disable-gpu")  # gpu
        return options

    # 跳转虎啸首页，点击注册按钮，并输入手机号码
    def go_to_register(self):
        try:
            self.driver.get(r'https://www.bilibili.com/')
            # 获取注册按钮并点击
            register_button = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div[1]/div[1]/div[3]/div[3]/ul/li[1]/a')
            register_button.click()
            # 获取手机号输入框
            phonenumber_input = self.wait.until(
                EC.visibility_of_element_located((
                    By.XPATH, '//*[@id="login-username"]'
                )))
            # 输入手机号
            phonenumber_input.clear()
            phonenumber_input.send_keys('18780236045')
            
            # 输入密码
            password_input = self.wait.until(
                EC.visibility_of_element_located((
                    By.XPATH, '//*[@id="login-passwd"]'
                )))
            # 输入手机号
            time.sleep(random.randrange(0,2))
            password_input.clear()
            password_input.send_keys('li15280221')                  
        except Exception as e:
            print('进入注册页面出错：%s' % e)
            self.driver.quit()

    # 获取滑动验证码图片，并获取52张图片的位置信息
    def get_image(self):
        try:
            # 获取无缺口图片
            nogap_image = self.wait.until(EC.presence_of_all_elements_located((
                By.XPATH, '//div[@class="gt_cut_fullbg gt_show"]/div'               
            )))
            nogap_image = self.get_complete_image(nogap_image)
            nogap_image.save('nogap_image.jpg')
            # 获取有缺口图片
            gap_image = self.wait.until(EC.presence_of_all_elements_located((
                By.XPATH, '//div[@class="gt_cut_bg gt_show"]/div'
            )))
            gap_image = self.get_complete_image(gap_image)
            gap_image.save('gap_image.jpg')
            # 获取图像不同点的坐标，以此为滑块移动的距离
            return self.get_image_diff(nogap_image, gap_image)
        except Exception as e:
            print('获取图片出错：%s' % e)
            self.driver.quit()

    # 将获取的图片重新裁剪拼接为一张完整的图片
    def get_complete_image(self, image):
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
        new_im.save('a.jpg')

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

    # 获取两张图片不同之处的位置，并返回
    def get_image_diff(self, nogap_image, gap_image):
        # 比较两个像素是否相同
        # 由于是RGB格式，所以需要分别判断每个像素点中的R，G，B值
        def compare_pixel(pixel1, pixel2):
            for i in range(3):
                if abs(pixel1[i] - pixel2[i]) > 50:
                    return False

        # 遍历整个图片
        for i in range(1, 259):
            for j in range(1, 115):
                # 获取两张图片相同坐标的像素进行比较
                # 如果为了确保找到不同的像素，可以再多比较一下周围像素
                nogap_pixel = nogap_image.getpixel((i, j))
                gap_pixel = gap_image.getpixel((i, j))
                # 如果像素不同，返回当前像素的x坐标
                if compare_pixel(nogap_pixel, gap_pixel) is False:
                    return i

    # 滑动滑块
    def slide_button(self, position):
        try:
            # 找到滑动的滑块
            slide_button = self.wait.until(EC.visibility_of_element_located((
                By.XPATH,
                '//*[@id="gc-box"]/div/div[3]/div[2]'
            )))
            # 点击并拿起滑块
            ActionChains(self.driver).click_and_hold(slide_button).perform()
            # 根据我们生成的移动轨迹，逐步移动鼠标
            for i in SlidingTrack(position-5).get_move_list():
                ActionChains(self.driver).move_by_offset(
                    xoffset=i, yoffset=0).perform()
            # 松开鼠标
            time.sleep(1)
            ActionChains(self.driver).release().perform()
        except Exception as e:
            print('滑动滑块出错：%s' % e)
            self.driver.quit()

    # 控制整体运行逻辑
    def __call__(self):
        try:
            self.go_to_register()     
            time.sleep(random.randrange(1,3))
            position = self.get_image()
            time.sleep(random.randrange(1,3))
            self.slide_button(position)
        finally:
            time.sleep(8)
            self.driver.quit()


if __name__ == '__main__':
    crack_jee = CrackJee()
    crack_jee()
