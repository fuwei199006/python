#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wells
# @Date:   2015-12-31 16:52:34
# @Last Modified by:   wells
# @Last Modified time: 2016-01-05 11:39:16
import MySQLdb
 
#try:
#    conn=MySQLdb.connect(host='localhost',user='root',passwd='111',db='spider',port=3306)
#    cur=conn.cursor()
#    cur.execute('select * from blog')
#    print cur.fetchmany(5)
#    cur.close()
#    conn.close()
#except MySQLdb.Error,e:
#     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

class MysqlDBHelper:
    def __init__(self):
        pass
    def ExecSql(self,sql):
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='111',db='spider',port=3306)
            cur=conn.cursor()
            count=cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
            return count
        except MySQLdb.Error,e:
            print  "Mysql Error %d: %s" % (e.args[0], e.args[1])
    def ExecManySql(self,sql,list):
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='111',db='spider',port=3306)
            cur=conn.cursor()
            count=cur.executemany(sql,list)
            conn.commit()
            cur.close()
            conn.close()
            return count
        except MySQLdb.Error,e:
            print  "Mysql Error %d: %s" % (e.args[0], e.args[1])
    def ExecDataSql(self,sql):
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='111',db='spider',port=3306)
            cur=conn.cursor()
            cur.execute(sql)
            data=cur.fetchmany(100)
            cur.close()
            conn.close()
            return data
        except MySQLdb.Error,e:
            print  "Mysql Error %d: %s" % (e.args[0], e.args[1])