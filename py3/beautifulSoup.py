#!/usr/bin/python 
# -*- coding:utf-8 -*-
from urllib.request import  urlopen
from bs4 import BeautifulSoup
from pip._vendor.requests.exceptions import HTTPError
try:
    html=urlopen("http://www.pythonscraping.com/pages/page1.html")
    #这行代码可能会发生两种异常
    #1.网页在服务器上不存在（或者获取页面的时候出现错误）
    #2.服务器不存在
    #可以用下面的方式处理异常
except HTTPError as e:
    #如果返回HTTP错误代码，程序就会显示错误内容，不再执行else语句后面的代码
    print(e)    
else:
    if html is None:
        print("URL is not found")
    else:
        bsObj=BeautifulSoup(html.read(),"html.parser")
        #增加一个检查条件保证标签确实存在
        try:
            badContent=bsObj.nonExistingTag.anotherTag
        except AttributeError as e:
            print("Tag was not found")
        else:
            if badContent == None:
                print("Tag was not found")
            else:
                print(badContent)