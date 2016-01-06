import sys
sys.path.append("..")
from src  import mysql
sql='insert blog(blogContent, blogTitle, blogAuthor, blogSiteUrl, blogCreateDate ) values("test1","testTitle1","fuwei1","www.baid1u.com",now());'
dbHelper= mysql.MysqlDBHelper()
print dbHelper.ExecSql(sql)