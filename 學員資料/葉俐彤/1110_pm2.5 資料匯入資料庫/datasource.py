import requests
import psycopg2
import password as pw

#--------------下載資料---------------
def __download_pm25_data()->list[dict]:
    #下載環境部pm2.5資料：
    air_url = f'https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key={pw.API_KEY}'
    response = requests.get(air_url)
    response.raise_for_status()
    data = response.json()
    print("下載成功")
    return data

#--------------建立table---------------
def __create_table(conn)->None:    
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS taiwan_pm25(
            "id"	SERIAL,
            "測站名稱"	TEXT NOT NULL,
            "縣市名稱"	TEXT NOT NULL,
            "pm25"	TEXT NOT NULL,
            "資料建置時間"	TEXT,
            PRIMARY KEY("id"),
            UNIQUE(測站名稱,資料建置時間) 
        );
        '''
    )
    conn.commit()
    cursor.close()
    print("create_table成功")

#--------------寫入資料---------------
def __insert_data(conn,values:list[any])->None:
    cursor = conn.cursor()
    sql = '''
    INSERT INTO taiwan_pm25 (測站名稱, 縣市名稱, pm25, 資料建置時間) 
    VALUES (%s,%s,%s,%s)
    ON CONFLICT (測站名稱,資料建置時間) DO NOTHING
    '''
    cursor.execute(sql,values)    
    conn.commit()
    cursor.close()

#--------------更新資料庫：下載並寫入資料---------------
def updata_render_data()->None:
    data = __download_pm25_data()
    
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER, 
                            password=pw.PASSWORD,
                            host=pw.HOST, 
                            port="5432")

    __create_table(conn)
    for item in data['records']:
        __insert_data(conn,values=[item['site'],item['county'],item['pm25'],item['datacreationdate']])
    print('資料建置成功')
    conn.close()

#--------------找出每個站點的最新資料---------------
def lastest_datetime_data()->list[tuple]:
    
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER, 
                            password=pw.PASSWORD,
                            host=pw.HOST, 
                            port="5432")
    cursor = conn.cursor()
    sql = '''
    select a.* from taiwan_pm25 as a
    join (select distinct 測站名稱,max(資料建置時間) 資料建置時間 from taiwan_pm25 group by 測站名稱) as b
    on a.資料建置時間=b.資料建置時間 and a.測站名稱=b.測站名稱
 
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
