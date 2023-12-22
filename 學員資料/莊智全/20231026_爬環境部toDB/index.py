import requests, sqlite3, datetime, json,threading, time
#from city import *
from datasource import *

class Aqi:         # 建一個 class 用attribution 儲存 資料 (url. SQL 指令)
    def __init__(self, xurl, xtable, xinsert):  
        self.xurl=xurl
        self.xtable=xtable
        self.xinsert=xinsert

# A1:台北市 /  A2:新北市 /  A3:桃園市 /  A4:新竹市 / 


aqurlA1 = '''https://data.moenv.gov.tw/api/v2/aqx_p_136?api_key=1f7402cf-f22f-4253-95d7-02821ce4bf65'''

aqurlA2 = '''
https://data.moenv.gov.tw/api/v2/aqx_p_137?api_key=1f7402cf-f22f-4253-95d7-02821ce4bf65'''

aqurlA3 = '''
https://data.moenv.gov.tw/api/v2/aqx_p_138?api_key=1f7402cf-f22f-4253-95d7-02821ce4bf65
'''

aqurlA4 = '''
https://data.moenv.gov.tw/api/v2/aqx_p_139?api_key=1f7402cf-f22f-4253-95d7-02821ce4bf65
'''


sqlB1='''CREATE TABLE IF NOT EXISTS 台北市aqi(
            "id" INTEGER,
            "測站代碼" TEXT NOT NULL,
            "測站名稱" TEXT NOT NULL,
            "縣市" TEXT NOT NULL,
            "測項代碼" TEXT NOT NULL,
            "測項名稱" TEXT NOT NULL,
            "測項英文名稱" TEXT NOT NULL,
            "測項單位" TEXT NOT NULL,
            "監測日期" TEXT NOT NULL,
            "數值" TEXT NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
            UNIQUE(測站代碼,監測日期) ON CONFLICT REPLACE
            );
            '''

sqlB2='''CREATE TABLE IF NOT EXISTS 新北市aqi(
            "id" INTEGER,
            "測站代碼" TEXT NOT NULL,
            "測站名稱" TEXT NOT NULL,
            "縣市" TEXT NOT NULL,
            "測項代碼" TEXT NOT NULL,
            "測項名稱" TEXT NOT NULL,
            "測項英文名稱" TEXT NOT NULL,
            "測項單位" TEXT NOT NULL,
            "監測日期" TEXT NOT NULL,
            "數值" TEXT NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
            UNIQUE(測站代碼,監測日期) ON CONFLICT REPLACE
            );
            '''

sqlB3='''CREATE TABLE IF NOT EXISTS 桃園市aqi(
            "id" INTEGER,
            "測站代碼" TEXT NOT NULL,
            "測站名稱" TEXT NOT NULL,
            "縣市" TEXT NOT NULL,
            "測項代碼" TEXT NOT NULL,
            "測項名稱" TEXT NOT NULL,
            "測項英文名稱" TEXT NOT NULL,
            "測項單位" TEXT NOT NULL,
            "監測日期" TEXT NOT NULL,
            "數值" TEXT NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
            UNIQUE(測站代碼,監測日期) ON CONFLICT REPLACE
            );
            '''

sqlB4='''CREATE TABLE IF NOT EXISTS 新竹市aqi(
            "id" INTEGER,
            "測站代碼" TEXT NOT NULL,
            "測站名稱" TEXT NOT NULL,
            "縣市" TEXT NOT NULL,
            "測項代碼" TEXT NOT NULL,
            "測項名稱" TEXT NOT NULL,
            "測項英文名稱" TEXT NOT NULL,
            "測項單位" TEXT NOT NULL,
            "監測日期" TEXT NOT NULL,
            "數值" TEXT NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
            UNIQUE(測站代碼,監測日期) ON CONFLICT REPLACE
            );
            '''


sqlC1='''
      INSERT INTO 台北市aqi(測站代碼, 測站名稱, 縣市, 測項代碼, 測項名稱, 測項英文名稱, 測項單位, 監測日期, 數值) VALUES(?,?,?,?,?,?,?,?,?);
      '''

sqlC2='''
      INSERT INTO 新北市aqi(測站代碼, 測站名稱, 縣市, 測項代碼, 測項名稱, 測項英文名稱, 測項單位, 監測日期, 數值) VALUES(?,?,?,?,?,?,?,?,?);
      '''

sqlC3='''
      INSERT INTO 桃園市aqi(測站代碼, 測站名稱, 縣市, 測項代碼, 測項名稱, 測項英文名稱, 測項單位, 監測日期, 數值) VALUES(?,?,?,?,?,?,?,?,?);
      '''

sqlC4='''
      INSERT INTO 新竹市aqi(測站代碼, 測站名稱, 縣市, 測項代碼, 測項名稱, 測項英文名稱, 測項單位, 監測日期, 數值) VALUES(?,?,?,?,?,?,?,?,?);
      '''




#

def main():
    台北市AQI = Aqi(aqurlA1, sqlB1, sqlC1)
    新北市AQI = Aqi(aqurlA2, sqlB2, sqlC2)
    桃園市AQI = Aqi(aqurlA3, sqlB3, sqlC3)
    新竹市AQI = Aqi(aqurlA4, sqlB4, sqlC4)
    
    cities = [台北市AQI, 新北市AQI, 桃園市AQI, 新竹市AQI]

    conn = sqlite3.connect('./aqi.db')

    for loadcity in cities:   
        a1sql=loadcity.xtable 
        aurl=loadcity.xurl
        csql=loadcity.xinsert
        T1 = threading.Thread(target=sqlCrtTb, args=(a1sql,))
        T2 = threading.Thread(target=getjson, args=(aurl,))
        T3 = threading.Thread(target=jsondata)
        T4 = threading.Thread(target=pushValue)
        T5 = threading.Thread(target=sqlIsrtTb, args=(csql,))
        
        
        T1.start()
        time.sleep(5)
        T2.start()
        T2.join()
        T3.start()
        T4.start()
        T4.join()

time.sleep(3600)
main()



if __name__=="__main__":
    main()