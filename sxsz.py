import re
from mylib import toUrl
from urllib import request
import urllib
import os

def reportProcess(hasDl,block,size):
    print(f'\rdownload:{1.0 if hasDl*block/size>1 else hasDl*block/size:5.1f}')



kw=input('请输入关键词')
req = request.Request(f'https://www.doutula.com/search?keyword={toUrl(kw)}')
req.add_header('User-Agent','MQQBrowser/7.3')
with request.urlopen(req,timeout=3) as respond:
    if respond and respond.code/100==2:
        result=respond.read().decode('utf-8')
        #控制正则表达式待匹配字符串的长度，避免高CPU占用
        start=result.find('<!--0-->')
        k=re.findall(r'inal="(.*?)"(?:.|\s)*?ne">(.*?)</p',
                     result[start+7:result.rfind('<div class="pic-content text-center">')])\
                    if start!=-1 else []
        #下载斗图
        if not os.path.exists(f'./{kw}/'):
                os.makedirs(f'./{kw}/')
        for i,(address,name) in enumerate(k):
            print(f'图片名字:{name}\n网址：{address}\n',end=f'{"="*80}\n')
            try:
                request.urlretrieve(address if address.find('http')!=-1 else f'https:{address}',
                                    os.path.join(f'./{kw}/', f'{i}.jpg'),
                                    reporthook=reportProcess)
            except:
                print(f'发生错误，链接是{address}')
        print(len(k))
        
    else:
        print(f'发生错误,状态码为{respond.code}')
