import sys
sys.path.append("..")
from src  import mysql
sql='SELECT * FROM blog;'
dbHelper= mysql.MysqlDBHelper()
print dbHelper.ExecDataSql(sql)[0][6]