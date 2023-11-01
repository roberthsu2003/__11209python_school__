import password #匯入並執行password.py檔
import requests #匯入並執行requests
import json #匯入json模組
import sqlite3
import time

def get_air_data():
    url=f'https://data.moenv.gov.tw/api/v2/aqx_p_319?api_key={password.apikey}'
    #print(url) #驗證url是否正確
    res=requests.get(url)
    data=res.json()['records']
    return data

def create_table_air(conn:sqlite3.Connection):
#conn=sqlite3.Connection(database='air.db') #測試建立db
    cursor=conn.cursor()
    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS AIR(
    "ID"    INTEGER,
    "監測日期"  TEXT NOT NULL,
    "監測站編號"    TEXT NOT NULL,
    "監測站名"  TEXT NOT NULL,
    "縣市行政區"    TEXT NOT NULL,
    "監測項目名稱"  TEXT NOT NULL,
    "監測數值"  TEXT NOT NULL,
    "監測單位"  TEXT NOT NULL,
    PRIMARY KEY("ID" AUTOINCREMENT)
    );
    '''
)
    conn.commit()

def insert_data_air(conn:sqlite3.Connection,values:list[any])->None:
    cursor=conn.cursor()
    sql='''
    REPLACE INTO AIR(監測日期,監測站編號,監測站名,縣市行政區,監測項目名稱,監測數值,監測單位)
    values(?,?,?,?,?,?,?)
    '''
    cursor.execute(sql,values)
    conn.commit()

def update_data_air() ->None :
    data=get_air_data()
    conn=sqlite3.Connection('air.db')
    create_table_air(conn)
    for item in data:
        #print(type(item))
        insert_data_air(conn,[item['monitordate'],item['siteid'],item['sitename'],item['county'],item['itemname'],item['concentration'],item['itemunit']])
    conn.close()

n=1
while n>0:
    print('working')
    update_data_air()
    time.sleep(3600)



