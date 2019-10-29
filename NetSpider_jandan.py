# env       ：Python v 3.7.3
# -*- coding：utf-8 -*-
# @Time     ：2019/10/29 17:06
# @Author   ：Jason Phillip
# @File     ：.py


import requests

headers     = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
response    = requests.get('http://jandan.net/2019/10/29/haunted-house.html',headers)
content     =   response.content()

with open(r'e:\ttt\content.txt','wb') as file:
    file.write(content)

