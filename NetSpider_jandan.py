# env       ：Python v 3.7.3
# -*- coding：utf-8 -*-
# @Time     ：2019/10/29 17:06
# @Author   ：Jason Phillip
# @File     ：.py

import requests
import re
from bs4 import BeautifulSoup


class JanDan():

    def __init__(self,url):
        self.headers =  {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/'
                    '537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        self.url = url

    def get_html(self):
        response = requests.get(self.url,self.headers)
        self.html = response.content
        return self.html

    def get_text(self):
        html = self.get_html()
        soup = BeautifulSoup(html,"html.parser")
        # 数组对象定义（用于存放对象）
        content_list = []
        # 按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,使用 class 做参数会导致语法错误.从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag
        # 查找dl标签class为dataItem02的所有dl标签
        for tag in soup.find_all("div", class_="indexs"):
            # 对tag的子节点进行循环输出
            for child in tag.children:
                text = self.parser_text(str(child))
                content_list.append(text)
        print(list(content_list))

    def parser_text(self,str):
        """找到并返回符合规则的字符串"""
        str.split('<h2>')
        parserrole = re.compile(r'^<h2>')
        #parserrole = re.compile(r'[\u4e00-\u9fa5]+')
        text = re.findall(parserrole,str)
        self.content = text
        return self.content

    def savetofile(self,path):
        html = self.get_html()
        with open(path, 'wb') as file:
            file.write(html)

if __name__ == '__main__':
    jd = JanDan('http://jandan.net/2019/10/29')
    # jd.savetofile(r'e:\ttt\jd.txt')
    jd.get_text()