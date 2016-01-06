#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wells
# @Date:   2016-01-02 12:27:42
# @Last Modified by:   wells
# @Last Modified time: 2016-01-05 15:06:58
import urllib
import urllib2
import re
import os
import mysql

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
		for x in content:
			info=x.split('>')
			sUrl=href.format(info[0].replace('\"',''))
			#print sUrl
			#print info[1]
			sData= self.getContent(sUrl)
			sContent=spattern.findall(sData)
			print sContent
			for s in sContent:
			
				# print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
				html=s
				s=articlPattern.sub('',s)
				s=s.replace('&nbsp;',' ')
				s="标题："+info[1]+"\n"+"原文链接："+sUrl+"\n\n"+s
				print s
				self.writeDateToMysql(s,html,sUrl,"马未都",info[1])
				#self.writeData(s,info[1].decode("utf-8"))
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
		print fileName,".txt  ----写入完成！"
	def writeDateToMysql(self,cotent,html,url,author,title):
		sql='insert blog(blogContent,blogContentHtml,blogTitle, blogAuthor, blogSiteUrl, blogCreateDate ) values('
		sql+='"'+content+'","'+html+'","'+title+'","'+author+'","'+url+'","'+getNowDate()+");"
		print sql
		count=self.dbhelper.ExecSql(sql)
		if(count>0):
			print url,"添加成功!"
		else:
			print url,"添加失败!"
	def clearCode(self,fileName):
		return fileName.replace('?',"")
	def getNowDate():
		return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
dbhelper=mysql.MysqlDBHelper()
spider=Spider("http://blog.sina.com.cn/s/articlelist_1347712670_0_1.html",dbhelper)
for x in range(1,2):
	url="http://blog.sina.com.cn/s/articlelist_1347712670_0_"+str(x)+".html"
	# print url
	content=spider.getContent(url);
	spider.getDetail(content)