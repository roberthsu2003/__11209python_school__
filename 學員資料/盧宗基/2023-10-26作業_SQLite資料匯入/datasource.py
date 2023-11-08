import requests
import sqlite3
from datetime import datetime
import json
import key

#__all__=['update_sqlite_data']

#download data-----------------------------------------------------------------
def __download_aqi_data()-> list:
    aqi_url = f'https://data.moenv.gov.tw/api/v2/aqx_p_07?formate=json&api_key={key.key}'
    response = requests.get(aqi_url)
    response.raise_for_status()
    print('下載成功')
    data = response.json()
    with open('data.json','w', encoding='utf-8') as file:
        json.dump(data['records'],file,ensure_ascii=False)
    f = open('data.json','r', encoding='utf-8')
    list_json=list(f)
    print(list_json)
    return list_json


#create sql table--------------------------------------------------------------
def __create_table(conn:sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute(
        '''
		CREATE TABLE IF NOT EXISTS "空氣品質監測站"(
            "id" INTEGER,
            "測站編號" INTEGER,	
			"測站名稱" TEXT NOT NULL,
            "測站英文名稱" TEXT NOT NULL,
			"空品區" TEXT NOT NULL,
			"城市" TEXT NOT NULL,
            "鄉鎮" TEXT NOT NULL,
            "測站地址" TEXT NOT NULL,
			"經度" INTEGER,
			"緯度" INTEGER,
			"測站類型" TEXT NOT NULL,
            "更新時間" TEXT NOT NULL,
			PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(測站名稱,更新時間) ON CONFLICT REPLACE
		);
		'''
    )
    conn.commit()


def __insert_data(conn:sqlite3.Connection,values:list)->None:
    cursor = conn.cursor()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    sql = '''
		REPLACE INTO "空氣品質監測站"(測站編號,測站名稱,測站英文名稱,空品區,城市,鄉鎮,測站地址,經度,緯度,測站類型,更新時間)
		VALUES(?,?,?,?,?,?,?,?,?,?,?)
	'''
    values.append(current_time) 
    cursor.execute(sql,values)
    conn.commit()

def update_sqlite_data()->None:
    data = __download_aqi_data()
    conn = sqlite3.connect("空氣品質監測站.db")
    __create_table(conn)
    for item in data:
        # print(item)
        __insert_data(conn, values=[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9] ])
    conn.close()
