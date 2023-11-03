import password
import requests
import sqlite3
import time
import threading
import datetime

__all__ = ['update_sqlite_data']

def __download_AirQuality_data()->list[dict]:
    '''
    下載空氣品質監測站基本資料
    https://data.moenv.gov.tw/swagger/#/大氣/get_aqx_p_07
    '''
    AirQuality_url = f"https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key={password.apikey}"
    response = requests.get(AirQuality_url)
    response.raise_for_status()
    print("下載成功")
    data= response.json()['records']
    return data
   
def __create_table(conn:sqlite3.Connection):    
    cursor = conn.cursor()
    cursor.execute(
         '''
        CREATE TABLE IF NOT EXISTS 空氣品質(
            "id"	INTEGER,
            "測站編號"	TEXT NOT NULL,
            "城市"	    TEXT NOT NULL,
            "測站名稱"	TEXT NOT NULL,
            "空品區"	TEXT NOT NULL,
            "測站類型"	TEXT NOT NULL,
            "測站地址"	TEXT NOT NULL,
            "資料時間"  DATETIME NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
            );
        '''
    )
    conn.commit()

def __insert_data(conn:sqlite3.Connection, values:list[any])->None:
    cursor = conn.cursor()
    cur_time = datetime.datetime.now()
    sql = '''
    REPLACE INTO 空氣品質(測站編號, 城市, 測站名稱, 空品區, 測站類型, 測站地址, 資料時間)
    values(?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(sql, values + [cur_time] )
    conn.commit()

def update_sqlite_data()->None:
    '''
    下載,並更新資料庫
    '''
    data = __download_AirQuality_data()
    conn = sqlite3.connect("AirQuality.db")
    __create_table(conn)
    for item in data:
        __insert_data(conn,[item["siteid"],item["county"],item["sitename"],item["areaname"],item["sitetype"],item["siteaddress"]])
    conn.close()

def countdown(n:int)->None:
    while n > 0:
        print(f'倒數計時:{n}')
        n -= 1
        time.sleep(10)

def main():
    update_sqlite_data()
    max_cnt = 10    # 下載10次
    count = 1
    while count != max_cnt:
        t = threading.Thread(target=countdown,args=(6,))
        t.start()

        while t.is_alive():
            print('小猴子還在做事')
            time.sleep(1)
        else:
            update_sqlite_data()
            time.sleep(1) 
            count += 1
            print(f"第{count}次下載資料")
            
  
if __name__ == '__main__':
    main()