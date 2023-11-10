SELECT DISTINCT 站點名稱,max(更新時間)as 更新時間,行政區,地址,總車輛數,可借,可還 FROM 台北市youbike
GROUP by 站點名稱
ORDER BY 更新時間 DESC