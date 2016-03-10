# coding=utf8
import sys  
import pymssql
try:
    conn = pymssql.connect(host=".",user="sa",password="111", database="LotteryTest")
except pymssql.OperationalError, msg:
    print "error: Could not Connection SQL Server!please check your dblink configure!"
    sys.exit()
else:
    cur = conn.cursor()
    query="SELECT * FROM dbo.forecast ORDER BY periodId DESC "
    cur.execute(query)
    conn.commit
    rows = cur.fetchall()
    print rows