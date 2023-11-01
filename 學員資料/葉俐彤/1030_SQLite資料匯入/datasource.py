'''
建立moudle，下載環境部資料的function
'''

import requests
import sqlite3
from datetime import datetime
import api

# module裡面可以放function、變數、class
# function內要寫說明用多行文字
# import建議放在最上面，不然放在def裡面每進到程式一次就會執行一次
# lambda 就是一個匿名(沒有名稱、參數)的function，只能用一行寫完

__all__=['update_sqlite_data']

def __download_data() ->list[dict]:
    '''
    下載環境部的資料，需事先至官網申請apikey並貼入連結中
    '''
    
    air_url = f'https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key={api.key}'

    response = requests.get(air_url)
    response.raise_for_status()
    print('下載成功')
    return response.json()

def __create_table(conn:sqlite3.Connection): 
    cursor = conn.cursor() 
    cursor.execute( 
        '''
        CREATE TABLE  IF NOT EXISTS '環境部空氣品質監測站'(        
            "id"	INTEGER,
            "測站編號"	INTEGER,
            "測站名稱"	TEXT NOT NULL,
            "測站英文名稱"	TEXT,
            "空品區"	TEXT NOT NULL,
            "城市"	TEXT NOT NULL,
            "鄉鎮"	TEXT,
            "測站地址"	TEXT,
            "經度"	INTEGER,
            "緯度"	INTEGER,
            "測站類型"	TEXT NOT NULL,
            "更新時間" TEXT NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(id, 測站名稱) ON CONFLICT REPLACE
        ); 
        '''
    ) 
    conn.commit() 

def __insert_data(conn:sqlite3.Connection,values:list[any])->None:
    cursor = conn.cursor()
    time = datetime.now()
    sql='''
    REPLACE INTO 環境部空氣品質監測站(測站編號,測站名稱,測站英文名稱,空品區,城市,鄉鎮,測站地址,經度,緯度,測站類型,更新時間)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)
    '''
    values.append(time)
    cursor.execute(sql,values)
    conn.commit()

def update_sqlite_data()->None:
    '''
    下載資料並更新資料庫
    '''
    data = __download_data()
    conn = sqlite3.connect('air_aql.db')
    __create_table(conn)
    for item in data['records']:
        __insert_data(conn, values=[item['sitename'], item['siteengname'], item['areaname'], item['county'], item['township'], item['siteaddress'], item['twd97lon'],item['twd97lat'],item['sitetype'],item['siteid']])
    conn.close() 
