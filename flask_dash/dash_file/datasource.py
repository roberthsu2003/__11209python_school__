import requests
import psycopg2
from . import password as pw


def lastest_datetime_data()->list[tuple]:
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER, 
                            password=pw.PASSWORD,
                            host=pw.HOST, 
                            port="5432")
    cursor = conn.cursor()
    sql = '''
    SELECT 站點名稱,更新時間,行政區,地址,總車輛數,可借,可還
    FROM 台北市youbike
    WHERE (更新時間,站點名稱) IN (
	        SELECT MAX(更新時間),站點名稱
	        FROM 台北市youbike
	        GROUP BY 站點名稱
            );
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return rows

def search_sitename(word:str) -> list[tuple]:
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER, 
                            password=pw.PASSWORD,
                            host=pw.HOST, 
                            port="5432")
    cursor = conn.cursor()
    sql = '''
        SELECT *
        FROM 台北市youbike
        WHERE (更新時間,站點名稱) IN (
	          SELECT MAX(更新時間),站點名稱
	          FROM 台北市youbike
	            GROUP BY 站點名稱
        )  AND 站點名稱 like %s
        '''
    cursor.execute(sql,[f'%{word}%'])
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows