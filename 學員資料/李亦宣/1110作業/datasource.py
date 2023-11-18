import requests
import psycopg2
import pw
import key

__all__=['update_sqlite_data']

#-----------------download data-----------------#
def __download_pm25_data()->list[dict]:
    aqi_url = f'https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key={key.key}'
    response = requests.get(aqi_url)
    response.raise_for_status()
    print('下載成功')
    data = response.json()
    return data

#---------------create sql table----------------#
def __create_table(conn)->None:
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS taiwan_pm25(
            "id"	SERIAL,
            "城市名稱"	TEXT NOT NULL,
            "縣市名稱"	TEXT NOT NULL,
            "pm25"	TEXT NOT NULL,
            "時間"	TEXT NOT NULL,
            PRIMARY KEY("id"),
            UNIQUE(城市名稱,時間)
        );
        '''
    )
    conn.commit()
    cursor.close()  

#-----------------insert data-------------------#
def __insert_data(conn,values:list[any])->None:
    cursor = conn.cursor()
    sql = '''
        INSERT INTO taiwan_pm25(城市名稱, 縣市名稱, pm25, 時間)
        VALUES(%s,%s,%s,%s)
        ON CONFLICT (城市名稱,時間) DO NOTHING   
    '''
    cursor.execute(sql,values)
    conn.commit()
    cursor.close()

def update_render_data()->None:
    data = __download_pm25_data()

    #---------------連線到postgresql----------------#
    conn = psycopg2.connect(database=pw.DATABASE,
                                user=pw.USER, 
                                password=pw.PASSWORD,
                                host=pw.HOST, 
                                port="5432")
   
    __create_table(conn)
    for item in data['records']: 
        __insert_data(conn,values=[item['site'],item['county'],item['pm25'],item['datacreationdate']])
    conn.close()
