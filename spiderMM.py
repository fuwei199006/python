#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wells
# @Date:   2015-12-29 17:41:39
# @Last Modified by:   wells
# @Last Modified time: 2015-12-29 18:08:59
import urllib
import urllib2
import re
class Spider:
   
    def __init__(self, url):
        self.siteUrl=url

    def getPage(self,pageIndex):
        url=self.siteUrl+"?page="+str(pageIndex)
        print url
        request=urllib2.Request(url)
        response=urllib2.urlopen(request)
        return response.read().decode('gbk')
    def getContents(self,pageIndex):
        page=self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items=re.findall(pattern,page)
        contents = []
        for item in items:
            contents.append([item[0],item[1],item[2],item[3],item[4]])
        return contents
    def saveBrief(self,content,name):
        fileName=name+""+name+".txt"
        f=open(fileName,"w+")
        print u"正在保存。。",fileName
        f.write(content.ecode('utf-8'))
    def mkdir(self,path):
        path=path.strip()
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            return True
        else:
            return False
    def saveImgs(self,images,name):
        number = 1
        print u"发现",name,u"共有",len(images),u"张照片"
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            fileName = name + "/" + str(number) + "." + fTail
            self.saveImg(imageURL,fileName)
            number += 1
      #传入图片地址，文件名，保存单张图片
    def saveImg(self,imageURL,fileName):
         u = urllib.urlopen(imageURL)
         data = u.read()
         f = open(fileName, 'wb')
         f.write(data)
         print u"正在悄悄保存她的一张图片为",fileName
         f.close()
         
spider = Spider("http://mm.taobao.com/json/request_top_list.htm")
spider.getContents(1)