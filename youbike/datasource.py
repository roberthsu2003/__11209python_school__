import requests
import sqlite3

def __download_youbike_data()->list[dict]:
    '''
    下載台北市youbike資料2.0
    https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    '''
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    response.raise_for_status()
    print("下載成功")
    return response.json()

def __create_table(conn:sqlite3.Connection):    
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS 台北市youbike(
            "id"	INTEGER,
            "站點名稱"	TEXT NOT NULL,
            "行政區"	TEXT NOT NULL,
            "更新時間"	TEXT NOT NULL,
            "地址"	TEXT,
            "總車輛數"	INTEGER,
            "可借"	INTEGER,
            "可還"	INTEGER,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
        '''
    )
    conn.commit()

def updata_sqlite_data():
    '''
    下載,並更新資料庫
    '''
    data = __download_youbike_data()
    conn = sqlite3.connect("youbike.db")
    __create_table(conn)
    