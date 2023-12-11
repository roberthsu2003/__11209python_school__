import requests
import sqlite3
from datetime import datetime
from password import apikey           #要先導入password.py裡面名為apikey的變量

__all__ = ['ambient_air_sqlite_data']

'''下載資料'''
def download_air_data() -> dict:
    
    air_url = f"https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key={apikey}"   #如果上面只寫import password，這邊資料就跑不出來
    response = requests.get(air_url)
    response.raise_for_status()
    print('下載成功，你好棒喔！')
    return response.json()

'''創建資料表'''
def  create_table(conn:sqlite3.Connection) -> None: 
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "空氣品質監測站基本資料"(
        "ID" INTEGER,
        "測站名稱" TEXT NOT NULL,
        "測站英文名稱" TEXT NOT NULL,
        "空品區" TEXT NOT NULL,
        "城市" TEXT,
        "鄉鎮" TEXT,
        "測站地址" TEXT,
        "經度" TEXT,
        "緯度" TEXT,
        "測站類型" TEXT NOT NULL,
        "測站編號" TEXT NOT NULL,
        "更新時間" TEXT NOT NULL,    /*新增資料時有「更新時間」這項資料，創建資料表時也要有這個欄位*/
        PRIMARY KEY('ID' AUTOINCREMENT)    /*注意此處語法，不能寫成"PRIMARY KEY(ID AUTOINCREMENT)"*/
        )
        ''')
     
    conn.commit()
    
'''新增資料'''        
def insert_data(conn:sqlite3.Connection,values:list[any])->None:
    cursor = conn.cursor()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = '''
    REPLACE INTO 空氣品質監測站基本資料(測站名稱,測站英文名稱,空品區,城市,鄉鎮,測站地址,經度,緯度,測站類型,測站編號,更新時間)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)
    '''
    values.append(current_time)   #既然values有新增時間，上面sql語法也要加入「更新時間」，VALUES的問號也要多加1個
    cursor.execute(sql,values)
    conn.commit()
    
'''下載,並更新資料庫''' 
def update_sqlite_data()->None:
    data = download_air_data()
    conn = sqlite3.connect("air.db")
    create_table(conn)
    for item in data['records']:     #data本身是一個dictionary，後面要加對應的key值，才能抓到對應的value，而data['records']是一個list，裡面的item又是dictionary
        
        insert_data(conn,values=[item['siteid'],item['sitename'], item['siteengname'], item['areaname'], item['county'], item['township'], item['siteaddress'], item['twd97lon'], item['twd97lat'], item['sitetype']])
    conn.close()

update_sqlite_data()