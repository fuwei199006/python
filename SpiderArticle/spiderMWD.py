#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wells
# @Date:   2016-01-02 12:27:42
# @Last Modified by:   wells
# @Last Modified time: 2016-01-02 18:24:31
import urllib
import urllib2
import re
import os

class Spider:
	def __init__(self,url):
		self.siteUrl=url
	def getContent(self,url):
		request=urllib2.Request(url)
		respone=urllib2.urlopen(request)
		content= respone.read()
		return content
	def getDetail(self,items):
		href='http://blog.sina.com.cn/s/blog_{0}'
		pattern = re.compile(r'<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_(.+)</a>')
		spattern=re.compile(r'<!-- 正文开始 -->(.*)<!-- 正文结束 -->',re.S)
		articlPattern=re.compile(r'<[^<>]+>',re.S)
		#个人信息页面所有代码
		content = pattern.findall(items)
		for x in content:
			info=x.split('>')
			sUrl=href.format(info[0].replace('\"',''))
			print sUrl
			print info[1]
			sData= self.getContent(sUrl)
			sContent=spattern.findall(sData)
			for s in sContent:
				# print '提取后的文本：',s
				# print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
				s=articlPattern.sub('',s)
				s=s.replace('&nbsp;',' ')
				s="标题："+info[1]+"\n"+"原文链接："+sUrl+"\n\n"+s
				self.writeData(s,info[1].decode("utf-8"))
			# print sData
			print '-------------------------------------------------------------------'
	def writeData(self,data,fileName):
		fileName=self.clearCode(fileName)
		print '正在写入:',fileName
		_fileName="data/"+fileName+".txt"

		if(os.path.exists(_fileName)):
			print "文件已经存在，采用追加模式！"
			f=open(_fileName,"a")
			data="\n---------------------------------------------------------------------\n\n"+data
		else:
			f=open(_fileName,"w")
		f.write(data)
		f.close()
		print fileName,".txt  --写入完成！"
	def clearCode(self,fileName):
		return fileName.replace('?',"")
spider=Spider("http://blog.sina.com.cn/s/articlelist_1347712670_0_1.html")
for x in range(1,59):
	url="http://blog.sina.com.cn/s/articlelist_1191211465_0_"+str(x)+".html"
	# print url
	content=spider.getContent(url);
	spider.getDetail(content)