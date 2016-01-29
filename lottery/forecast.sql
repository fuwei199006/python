create table forecast (
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
  forecastType varchar(100),
  isLottery varchar(10)
)