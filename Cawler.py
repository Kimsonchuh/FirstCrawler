#!/usr/bin/python
# -*- coding: UTF-8 -*- #

import requests
import re
import time

# 获取当前网页的页面
url = 'http://www.dytt8.net/html/gndy/dyzz/index.html'
html = requests.get(url)

# 根据网页head中的charset确定编码格式
html.encoding = 'gb2312'

# 可以通过输入内容来验证是否成功get到网页代码
# print(html.text)

# 使用正则表达式匹配url
# <a href="/html/gndy/dyzz/20180315/56508.html" class="ulink">2018年郭富城赵丽颖奇幻《西游记女儿国》HD国语中英双字</a>
movie_pages = re.findall(r'<a href="(.*?)" class="ulink">', html.text)

# 检查一下是否正确匹配
# for movie_page in movie_pages:
#     print(movie_page+'\n')

# 匹配成功，之后开始我们的伪点击并使用正则表达式匹配下载地址
for movie_page in movie_pages:
    real_movie_page = 'http://www.dytt8.net' + movie_page
    movie_page_html = requests.get(real_movie_page)
    movie_page_html.encoding = 'gb2312'
    download_address = re.findall(r'<a href="(.*?)">.*?</a></td>', movie_page_html.text)
    print(download_address)
    try:
        # 创建一个文件来储存我们的链接。
        with open('xiaodianying.txt', 'a', encoding='utf-8') as file:
            file.write(download_address[0] + '\n')
    except:
        print('null')

