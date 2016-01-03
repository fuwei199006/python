#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wells
# @Date:   2015-12-24 17:24:17
# @Last Modified by:   wells
# @Last Modified time: 2015-12-29 17:40:18

 
#coding:utf-8 
import urllib
import urllib2
import re
 
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent,"Content-Type":'text/html; charset=UTF-8' }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    p_html=response.read().decode('utf-8')
    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+
                     '="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,p_html)
    for item in items:
        print item[0],item[1],item[2],item[3],item[4]
    
    # html=p_html.decode('utf-8','ignore').encode('utf-8')
    # f=open(r'log.txt','w')
    # f.writelines(html)
    # f.close()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason