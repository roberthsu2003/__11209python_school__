CREATE TABLE  IF NOT EXISTS taiwan_pm25(
            "id"	SERIAL,
            "城市名稱"	TEXT NOT NULL,
            "縣市名稱"	TEXT NOT NULL,                         
            "pm25"	TEXT ,             
            "時間"	TEXT NOT NULL,  
            PRIMARY KEY("id"),
            UNIQUE(城市名稱,時間)           
        );
		
		
INSERT INTO taiwan_pm25(城市名稱,縣市名稱,pm25,時間)
    VALUES('大城','彰化縣','pm25','10')
    ON CONFLICT (城市名稱,時間) DO NOTHING
	
select * from taiwan_pm25