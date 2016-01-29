#coding:utf-8
import urllib2
import mysql
import time
import re
def getLotteryByYear(year):
        url = " http://baidu.lecai.com/lottery/draw/phase_result_download.php?file_format=txt&lottery_type=50&year="+str(year)
        request = urllib2.Request(url)
        request.add_header("Host","baidu.lecai.com")
        request.add_header("Referer","http://baidu.lecai.com/user/baidu/callback/?referer=%2Flottery%2Fdraw%2Fphase_result_download.php%3Ffile_format%3Dxls&code=8114f35297008375dc7190482d89c143")
        request.add_header( "User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2587.3 Safari/537.36")
        request.add_header( "Cookie","LSID=2mk6v3tlcp40b4l2ct5a8iukd4; _lhc_uuid=sp_56a0d1b27626c4.42574684; _adwb=110406678; _adwc=110406678; _adwp=110406678.7411827446.1453380046.1453380046.1453380046.1; _adwr=110406678%230; Hm_lvt_6c5523f20c6865769d31a32a219a6766=1453380047; Hm_lpvt_6c5523f20c6865769d31a32a219a6766=1453380047; Hm_lvt_9b75c2b57524b5988823a3dd66ccc8ca=1453380047; Hm_lpvt_9b75c2b57524b5988823a3dd66ccc8ca=1453380047; lehecai_request_control_stats=2; paypassword=sig%3Da547721dd7e7c76fc7055ea7b4a80bdb%2Cuid%3D828509350%2Cts%3D1453380022%2Cexpire%3D1200%2Cstatus%3D0%2Crc%3D112fdb12175df306b0c322e94f6dc4d7; bds_yRlmiCbrv56CcjfMwS21DkqP=expires_in%3D2592000%26refresh_token%3D22.d55dd17092b11925eea41a45cd1a1d39.315360000.1768740021.3288587357-106251%26access_token%3D21.1bd60eda0048dfdd8e0f5986676b8829.2592000.1455972021.3288587357-106251%26session_secret%3D2eb36510c6f5693e323cebfada5b2704%26session_key%3D9mnRdfskWO%252BEEWLtK5xDSrH88ypv2OIwH4Ik%252FKLkhRBDntcWWfH2VdsKl07x8mO8ioEBadGpMxE2xa06DiPZcNhQbxGOTF%252Fv%26scope%3Dbasic%2Bsuper_msg%26uid%3D3288587357%26uname%3D756091180%26portrait%3D92c43735363039313138308207; lehecai_request_control_userinfo=1")
        response = urllib2.urlopen(request)
        content=response.read()
        while(content.find("  ")!=-1):
                content=content.replace("  "," ")
        line=content.split("\r\n")
        list=[]
        for l in line:
                if(l!=""):
                        arrInfo=l.split(" ")
                        period=arrInfo[0]
                        lottery=arrInfo[1]
                        releaseDate=arrInfo[2]
                        balls=lottery.split("|")
                        redBalls=balls[0].split(",")
                        blueBall=balls[1]
                        tup=(period,redBalls[0],redBalls[1],redBalls[2],redBalls[3],redBalls[4],redBalls[5],blueBall,getNowDate(),releaseDate)
                        list.append(tup)
        count=insertData(list)
        if (count > 0):
            print year, ":success"
        else:
            print year, ":fail"


def insertData(list):
    sql = 'insert lottery(periodId,redBall1,redBall2, redBall3, redBall4, redBall5,redBall6,blueBall1,createDate,releaseDate ) values(%s, %s, %s,%s, %s, %s, %s,%s, %s, %s)'
    dbhelper = mysql.MysqlDBHelper()
    count = dbhelper.ExecManySql(sql, list)
    return  count


def getNowDate():
        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
def getAll():
    minYear=2003
    nowYear=int(time.strftime("%Y",time.localtime(time.time())))
    for x in range(minYear,nowYear+1):
            getLotteryByYear(x)
def getNearLottery():
       url = "http://baidu.lecai.com/lottery/draw/list/50"
       request = urllib2.Request(url)
       response = urllib2.urlopen(request)
       content=response.read()
       pattern=re.compile(r'<td>[^<>|^&nbsp]+</td>|<em>[^<>|^&nbsp]+</em>|>\d+</a>')
       item = pattern.findall(content)
       sql="SELECT * from lottery   ORDER BY releaseDate desc LIMIT 1"
       dbhelper=mysql.MysqlDBHelper()
       db=dbhelper.ExecDataSql(sql)
       lastDate= db[0][1]
       list=[]
       arrlen=len(item)
       if(lastDate==item[0]):
           pass
       else:
           for x in range(0,arrlen,9):
               item[x]=item[x].replace("</a>","").replace(">","")
               if(item[x]!=lastDate):
                   arr=[]
                   for i in range(x,x+9):
                         if(i<arrlen and (x+9)<arrlen):
                             item[i]= item[i].replace("<em>","").replace("</em>","")
                             item[i]= item[i].replace("<td>","").replace("</td>","").split((r'（'))[0]
                             item[i]=item[i].replace("</a>","").replace(">","")
                             arr.append(item[i])
                   if(len(arr)>0):
                         list.append(arr)
               else:
                    break
       if(len(list)>0):
           tupList=[]
           for l in list:
               tup=(l[0],l[2],l[3],l[4],l[5],l[6],l[7],l[8],getNowDate(),l[1])
               tupList.append(tup)
           count=insertData(tupList)
           if(count>0):
               print "获得最新的数据成功!共更新"+str(len(list))+"条数据！"
               print list
       else:
           print "当前的数据为最新数据，结果为",db[0]
def getMaxShowNum(count):
    count=6*count;
    sql="SELECT res.redBall,COUNT(0) as count  from (SELECT redBall from v_redball ORDER BY periodId DESC LIMIT "+str(count)+") as res GROUP BY redBall ORDER BY  count desc";
    dbhelper = mysql.MysqlDBHelper()
    db=dbhelper.ExecDataSql(sql)
    print db;
getMaxShowNum(100);
