import password as pw
import psycopg2 #匯入portgre sql模組
import requests
import time

    

#-----建立資料表-----#
def get_air_data():
    url=f'https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key={pw.api}'
    #print(url) #驗證url是否正確
    res=requests.get(url)
    data=res.json()['records']
    return data
    print('下載成功')

def create_table_air(conn):
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS 台灣空氣數值(
            "id"	SERIAL,
            "站點名稱"	TEXT NOT NULL,
            "縣市名稱"	TEXT NOT NULL,
            "更新時間"	TEXT NOT NULL,
            "空氣數值"  TEXT,
            PRIMARY KEY("id"),
            UNIQUE(站點名稱,更新時間) 
        );
        '''
    )
    conn.commit()
    cursor.close()

#-----在資料表內插入資料-----#
def insert_data(conn,values:list[any])->None:
    cursor = conn.cursor()
    sql = '''
    INSERT INTO 台灣空氣數值 (站點名稱, 縣市名稱, 更新時間, 空氣數值) 
    VALUES (%s,%s,%s,%s)
    ON CONFLICT (站點名稱,更新時間) DO NOTHING
    '''
    cursor.execute(sql,values)    
    conn.commit()
    cursor.close()

#-----更新資料-----#
def update_render_data()->None:
    '''
    下載,並更新資料庫
    '''
    data = get_air_data()
    conn = psycopg2.connect(
        database=pw.DATABASE,
        user=pw.USER, 
        password=pw.PASSWORD, 
        host=pw.HOST, 
        port="5432")
    create_table_air(conn)
    for item in data:
        insert_data(conn,[item['site'],item['county'],item['datacreationdate'],item['pm25']])
    conn.close()
    print('資料已完成匯入動作')

n=1
while n>0:
    print('下載資料中')
    update_render_data()
    time.sleep(3600)
