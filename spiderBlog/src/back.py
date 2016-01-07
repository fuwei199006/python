#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wells
# @Date:   2016-01-02 12:27:42
# @Last Modified by:   wells
# @Last Modified time: 2016-01-05 16:40:07
import urllib
import urllib2
import re
import os
import mysql
import time

class Spider:
	def __init__(self,url,dbhelper):
		self.siteUrl=url
		self.dbhelper=dbhelper
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
		content = pattern.findall(items)
		sql='insert blog(blogContent,blogContentHtml,blogTitle, blogAuthor, blogSiteUrl, blogCreateDate ) values(%s, %s, %s,%s, %s, %s)'
		list=[]
		for x in content:
			info=x.split('>')
			sUrl=href.format(info[0].replace('\"',''))
			#print sUrl
			#print info[1]
			sData= self.getContent(sUrl)
			sContent=spattern.findall(sData)
			for s in sContent:
				# print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
				html=s.replace("&nbsp;<wbr>","").replace("  "," ").replace("  \n","").strip()
				s=articlPattern.sub('',s)
				s=s.replace('&nbsp;',' ')
				s="标题："+info[1]+"\n"+"原文链接："+sUrl+"\n\n"+s
				s=s.replace("&nbsp;<wbr>","").replace("  "," ").replace("  \n","").strip()
				h=html.replace("'","\\'").replace('"','\\"')
				tup=(s,h,info[1],'马未都',url,self.getNowDate())
				list.append(tup)
				# print s
				# self.writeData(html,info[1].decode("utf-8"))
			    # print sData
		self.writeDateToMysql(sql,list)
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
		print fileName,".txt  ----写入完成！"
	def writeDateToMysql(self,sql,list):
		count=self.dbhelper.ExecManySql(sql,list)
		if(count>0):
			print  "success!"
		else:
			print  "fail!"



	def clearCode(self,fileName):
		return fileName.replace('?',"")
	def getNowDate(self):
		return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
dbhelper=mysql.MysqlDBHelper()
spider=Spider("http://blog.sina.com.cn/s/articlelist_1347712670_0_1.html",dbhelper)
# url="http://blog.sina.com.cn/s/articlelist_1347712670_0_2.html"
# print url
# content=spider.getContent(url);
# spider.getDetail(content)
for x in range(1,28):
	url="http://blog.sina.com.cn/s/articlelist_1347712670_0_"+str(x)+".html"
	print url
	content=spider.getContent(url);
	spider.getDetail(content)