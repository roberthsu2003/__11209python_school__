import requests
import sqlite3
import datetime

__all__=["SQL"] 

# 下載youbike data
def __download()->list[dict]:
    data_url="https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key=de3fce0a-b9c8-4740-98d8-a8cc97813e56"
    response=requests.get(data_url)
    response.raise_for_status()
    print("下載成功")

    return response.json()

#創建SQL的table
def __table(con:sqlite3.Connection):
    cur=con.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS 觀測站(
            "測站編號"	INTEGER,
            "城市"	TEXT NOT NULL,
            "測站名稱"	TEXT NOT NULL,
            "空品區"	TEXT NOT NULL,
            "測站類型"	TEXT NOT NULL,
            "測站地址"	TEXT NOT NULL,
            "資料更新時間" DATETIME NOT NULL,
            PRIMARY KEY(測站編號),
            UNIQUE(城市,測站名稱) ON CONFLICT REPLACE
        );
        '''
    )
    con.commit()

# 輸入資料到SQLlite裡
def __input_data(con: sqlite3.Connection, values: list[any]) -> None:
    cur = con.cursor()
    cur_time = datetime.datetime.now()
    sql = '''
    REPLACE INTO 觀測站(測站編號, 城市, 測站名稱, 空品區, 測站類型, 測站地址, 資料更新時間)
    values(?, ?, ?, ?, ?, ?, ?)
    '''
    cur.execute(sql, values + [cur_time])
    con.commit()

#更新並把資料存進SQLlite
def SQL():
    data=__download()
    con=sqlite3.connect("a.db")
    __table(con)
    for item in data["records"]:
        __input_data(con,[item["siteid"],item["county"],item["sitename"],item["areaname"],item["sitetype"],item["siteaddress"]])
    con.close()