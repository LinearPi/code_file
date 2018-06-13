from PIL import Image
import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

def binarizing(img, threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
    return img


out = Image.open(r'13.jpg')
img = out.convert('L')

img1 = binarizing(img, 100)

text = pytesseract.image_to_string(img1, lang='chi_sim')

n = re.findall(r"[\d]+", text)

print(text)
print('*'*20)
print(n)
