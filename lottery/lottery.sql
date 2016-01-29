/* 
* @Author: wells_fuwei
* @Date:   2016-01-23 17:09:20
* @Last Modified by:   wells_fuwei
* @Last Modified time: 2016-01-23 17:10:09
*/
create table lottery(
  id int primary key auto_increment,
  periodId varchar(50),
  redBall1 varchar(10),
  redBall2 varchar(10),
  redBall3 varchar(10),
  redBall4 varchar(10),
  redBall5 varchar(10),
  redBall6 varchar(10),
  blueBall1 varchar(10),
  createDate datetime,
  releaseDate varchar(50)
  
)
