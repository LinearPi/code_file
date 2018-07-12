# import tensorflow as tf
from PIL import Image
import numpy as np 
from captcha.image import ImageCaptcha
import random 
import matplotlib.pyplot as plt


# 1.使用imageCaptcha 来创建数据；
# 2.建立cnn来对生成的数据进行
# 3.保存现在的模型
# 4.调用现在的模型对图片进行预测


# 1 使用imageCaptcha 来创建数据；
def create_captcha(num):
    intchar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    c_captcha = ""
    for i in range(num):
        c_char =  random.choice(intchar)
        c_captcha += c_char
    print(c_captcha)
    return c_captcha

def gen_captcha_text_and_image(num):
    g_image = ImageCaptcha()

    captcha_text = create_captcha(num)
    captcha_image = g_image.generate(captcha_text)
    # g_image.write(captcha_image, 'captcha_text'+'.jpg')

    captcha_image = Image.open(captcha_image)
    captcha_image = np.array(captcha_image)
    print(captcha_text)
    return captcha_text, captcha_image


# 1.5 对产生的数据进行处理
def convert2gray(img):
    if len(img.shape) > 2:
        gray=np.mean(img, -1)
        return gray
    else:
        return img 
# 1.


# 2.建立cnn来对生成的数据进行
def my_cnn():
    pass




if __name__ == "__main__":
    num = 5
    # text, image = gen_captcha_text_and_image(num)
    # f = plt.figure()
    # ax = f.add_subplot(11)
    # ax.text(0.1, 0.9, text, ha='center', va ='center', transform=ax.transAxes)
    # plt.imshow(image)
    # plt.show() 





