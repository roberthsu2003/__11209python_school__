select *
from 台北市youbike

drop table 台北市youbike

delete from 台北市youbike

INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_捷運科技大樓站','大安區','2023-11-10 09:55:09','復興南路二段235號前',100,100,100)
ON CONFLICT (站點名稱,更新時間) DO UPDATE 
  SET 總車輛數 = 100, 
      可借 = 100,
	  可還 = 100;

select * 
from 台北市youbike
where 站點名稱='YouBike2.0_捷運科技大樓站'