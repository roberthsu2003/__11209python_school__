import requests
import sqlite3
import password
import json

__all__ = ['updata_sqlite_data']

def __download_airquality_data()->list[dict]:    
        airquality_url = f'https://data.moenv.gov.tw/api/v2/aqx_p_136?api_key={password.apikey}'
        response = requests.get(airquality_url)
        response.raise_for_status()     
        print("下載成功")
        return response.json()

    


def __create_table(conn:sqlite3.Connection):    
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS 台北市airquality(
            "id"	INTEGER,
            "測站名稱"	TEXT NOT NULL,
            "行政區"	TEXT NOT NULL,
            "測項編號"	INTEGER,             
            "測項名稱"	TEXT, 
            "測項英文名稱"	TEXT,
            "測項單位"	TEXT,
            "監測日期"	TEXT NOT NULL,
            "數值"	FLOAT,
            
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(測站名稱,測項編號,監測日期) ON CONFLICT REPLACE            
        );
        '''
    )
    conn.commit()

def __insert_data(conn:sqlite3.Connection,values:list[any])->None:
    cursor = conn.cursor()
    
    sql=   '''
    REPLACE INTO 台北市airquality(測站名稱,行政區,測項編號,測項名稱,測項英文名稱,測項單位,監測日期,數值)VALUES(?,?,?,?,?,?,?,?)

        '''
       
    cursor.execute(sql,values)
    conn.commit()
    


def updata_sqlite_data()->None:
    '''
    下載,並更新資料庫
    '''
    
    data = __download_airquality_data()    
    conn = sqlite3.connect("台北市airquality.db")
    __create_table(conn)    
    for item in data['records']:        
        __insert_data(conn,values=[item['sitename'],
                            item['county'],
                            item['itemid'],
                            item['itemname'],
                            item['itemengname'],
                            item['itemunit'],
                            item['monitordate'],
                            item['concentration']])
    conn.close()