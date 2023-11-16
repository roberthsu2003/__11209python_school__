CREATE TABLE  IF NOT EXISTS taiwan_pm25(
            "id"	SERIAL,
            "城市名稱"	TEXT NOT NULL,
            "縣市名稱"	TEXT NOT NULL,                         
            "pm25"	INTEGER NOT NULL,             
            "時間"	TEXT NOT NULL,  
            PRIMARY KEY("id"),
            UNIQUE(城市名稱,時間)           
        );
		
drop table taiwan_pm25

INSERT INTO taiwan_pm25(城市名稱,縣市名稱,pm25,時間)
VALUES(%s,%s,%s,%s)ON CONFLICT (城市名稱,時間) DO NOTHING
