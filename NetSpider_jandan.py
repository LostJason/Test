# env       ：Python v 3.7.3
# -*- coding：utf-8 -*-
# @Time     ：2019/10/29 17:06
# @Author   ：Jason Phillip
# @File     ：.py

from bs4 import BeautifulSoup
import requests
import re
import os


def save_file(str):
    with open(r'e:\ttt\log.txt', 'wb') as file:
        file.write(str)


def parser_addr(str):
    """通过正则表达式解析http地址"""
    parser = re.compile(r'https?:\/\/[a-zA-Z0-9|.|/|-]+\.html')
    t = re.findall(parser, str)
    return t


def parser_content(str):
    """通过正则表达式解析标签文本"""
    parser = re.compile(
        r'[\u4e00-\u9fa5|0-9|\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]+')
    t = re.findall(parser, str)
    return t


if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/'
                                  '537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    responses = requests.get(r'http://jandan.net/2019/10/29',headers)
    html = responses.content
    soup = BeautifulSoup(html, "html.parser")

    content_list = []

    for tag in soup.find_all("h2"):
        addr = tag.a.attrs['href']
        txt = parser_content(tag.text)
        content_list.append([txt[0], addr])

    save_file(str(content_list).encode())