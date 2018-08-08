import time
import re
import requests

from PIL import Image
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


class JeeCaptcha(object):
    def __init__(self):
        options = Options()
        options.add_argument('--window-size=1366,768')
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_register(self):
        try:
            self.driver.get('https://www.huxiu.com')
            register_button = self.wait.until(EC.presence_of_element_located((
                By.XPATH, '//*[@id="top"]/div/ul[2]/li[4]/a'
            )))
            register_button.click()

            number_input = self.wait.until(EC.visibility_of_element_located((
                By.XPATH, '//*[@id="sms_username"]'
            )))
            number_input.clear()
            number_input.send_keys('16602856392')
        except Exception as e:
            print('注册函数有误：%s' % e)
            self.driver.quit()

    def get_image(self):
        try:
            gap_image_list = self.wait.until(EC.presence_of_all_elements_located((
                By.XPATH, '//div[@class="gt_cut_bg gt_show"]/div'
            )))
            gap_image_url = gap_image_list[0].get_attribute('style')
            gap_image_url = re.search(r'url\("(.*?)"\);', gap_image_url).group(1)
            print(gap_image_url)
            gap_image = requests.get(gap_image_url).content
            gap_image = self.get_complete_image(gap_image_list, gap_image)

            nogap_image_list = self.wait.until(EC.presence_of_all_elements_located((
                By.XPATH, '//div[@class="gt_cut_fullbg gt_show"]/div'
            )))
            nogap_image_url = nogap_image_list[0].get_attribute('style')
            nogap_image_url = re.search(r'url\("(.*?)"\);', nogap_image_url).group(1)
            nogap_image = requests.get(nogap_image_url).content
            nogap_image = self.get_complete_image(nogap_image_list, nogap_image)

            position = self.compare_image(gap_image, nogap_image)
            self.slide_button(position)

        except Exception as e:
            print('获取图片函数有误：%s' % e)
            self.driver.quit()

    def get_complete_image(self, image_list, image):
        image_list = [i.get_attribute('style') for i in image_list]
        image_list = [re.search(r'tion: -(.*?)px -?(.*?)px;', i).groups() for i in image_list]
        im = Image.open(BytesIO(image))
        new_im = Image.new('RGB', (260, 116))
        up_count = 0
        low_count = 0
        for i in image_list[:26]:
            croped = im.crop((int(i[0]), 58, int(i[0]) + 10, 116))
            new_im.paste(croped, (up_count, 0))
            up_count += 10
        for i in image_list[26:]:
            croped = im.crop((int(i[0]), 0, int(i[0]) + 10, 58))
            new_im.paste(croped, (low_count, 58))
            low_count += 10

        return new_im

    def compare_image(self, gap_image, nogap_image):
        def compare_pixel(pixel1, pixel2):
            for i in range(3):
                if abs(pixel1[i] - pixel2[i]) > 50:
                    return False

        for i in range(260):
            for j in range(116):
                pixel1 = gap_image.getpixel((i, j))
                pixel2 = nogap_image.getpixel((i, j))
                if compare_pixel(pixel1, pixel2) is False:
                    return i

    def slide_button(self, position):
        try:
            slide_button = self.wait.until(EC.visibility_of_element_located((
                By.XPATH, '//div[@class="gt_slider_knob gt_show"]'
            )))
            ActionChains(self.driver).click_and_hold(slide_button).perform()
            for i in self.slide_position(position-3):
                print(i)
                ActionChains(self.driver).move_by_offset(i, 0).perform()
            ActionChains(self.driver).release().perform()
        except Exception as e:
            print('滑动滑块有误：%s' % e)

    def slide_position(self, position):
        t = 0.2
        current = 0
        mid = position * 4 / 5
        speed = 0
        move_distance_list = []
        while current < position:
            if current < mid:
                a = 2
            else:
                a = -3
            move_distance = speed * t + 0.5 * a * t * t
            move_distance_list.append(round(move_distance))
            speed += (a * t)
            current += move_distance
        move_distance_list.extend([-3,-2])
        print(move_distance_list)
        return move_distance_list

    def __call__(self, *args, **kwargs):
        try:
            self.go_to_register()
            self.get_image()
        finally:
            time.sleep(3)
            self.driver.quit()


if __name__ == '__main__':
    jee = JeeCaptcha()
    jee()
