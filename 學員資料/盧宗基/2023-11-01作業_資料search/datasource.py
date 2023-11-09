import requests
import sqlite3

__all__=['update_sqlite_data']

#self = window實體

#download data-----------------------------------------------
def __download_youbike_data()->list:
    '''
    下載台北市youbike資料2.0
    https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    '''
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    response.raise_for_status()
    print('下載成功')
    return response.json()

#create sql table---------------------------------------------
def __create_table(conn:sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute(
        '''
		CREATE TABLE IF NOT EXISTS 台北市youbike(
			"id"	INTEGER,
			"站點名稱"	TEXT NOT NULL,
			"行政區"	TEXT NOT NULL,
			"更新時間"	TEXT NOT NULL,
			"地址"	TEXT,
			"總車輛數"	INTEGER,
			"可借"	INTEGER,
			"可還"	INTEGER,
			PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(站點名稱,更新時間) ON CONFLICT REPLACE
		);
		'''
    )
    conn.commit()
    cursor.close()


def __insert_data(conn:sqlite3.Connection,values:list)->None:
    cursor = conn.cursor()
    sql = '''
        REPLACE INTO 台北市youbike(站點名稱,行政區,更新時間,地址,總車輛數,可借,可還)
        VALUES(?,?,?,?,?,?,?)
    '''
    cursor.execute(sql,values)
    conn.commit()
    cursor.close()


def update_sqlite_data()->None:
    data = __download_youbike_data()
    conn = sqlite3.connect("youbike.db")
    __create_table(conn)
    for item in data:
        __insert_data(conn,values=[item['sna'],item['sarea'],item['mday'],item['ar'],item['tot'],item['sbi'],item['bemp']])
    conn.close()

def lastest_datetime_data()->list:
    conn = sqlite3.connect("youbike.db")
    cursor = conn.cursor()              
    sql = '''
        SELECT 站點名稱, MAX(更新時間) AS 更新時間, 行政區, 地址, 總車輛數, 可借, 可還
        FROM 台北市youbike
        GROUP BY 站點名稱
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows

def search_sitename(word:str) -> list:
    conn = sqlite3.connect("youbike.db")
    cursor = conn.cursor()
    sql = '''
        SELECT 站點名稱, MAX(更新時間) AS 更新時間,行政區,地址,總車輛數,可借,可還
        FROM 台北市youbike
        GROUP BY 站點名稱
        HAVING 站點名稱 like ?
        '''
    cursor.execute(sql,[f'%{word}%'])
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

