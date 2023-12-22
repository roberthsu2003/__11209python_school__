import requests, sqlite3, datetime, json,threading, time


def getjson(aurl):  
               # 依據 URL 下載.並JSON()轉換為字典 dict格式  
        
      req = requests.get(aurl)
      reqj = req.json()
      return reqj
      
   

def jsondata(data):           # 將下載的檔案 (格式已轉為dict),get出 鍵 為"fields" 與 "records" 這2項的 值 ...
        fields=data.get("fields")
        records=data.get("records")
        #print(records)
        return records
      
def pushValue(rec):           # 將 "records" 這項的值 逐列讀取時, 依鍵取值, 存放入 values 變數 , 再將values 變數當參數引入sqlIsrtTb(conn, values)...
      for row in rec:
            values=(row["siteid"], row["sitename"],row["county"],row["itemid"],row["itemname"],row["itemengname"],row["itemunit"],row["monitordate"],row["concentration"],)

            sqlIsrtTb(conn, values)


def sqlCrtTb(conn):      # 創建 DB Table (已有同名Table 則不建立...[ IF NOT EXISTS ])
      conn = sqlite3.connect('./aqi.db')
      cursor = conn.cursor()
      a1sql='''CREATE TABLE IF NOT EXISTS 台北市aqi(
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
            UNIQUE(測站代碼,測項代碼,監測日期) ON CONFLICT REPLACE
            );
            '''
      cursor.execute(a1sql)
      conn.commit()



def sqlIsrtTb(conn, value):   # insert 資料進Table
      conn = sqlite3.connect('./aqi.db')     
      cursor=conn.cursor()
      csql='''
      INSERT INTO 台北市aqi(測站代碼, 測站名稱, 縣市, 測項代碼, 測項名稱, 測項英文名稱, 測項單位, 監測日期, 數值) VALUES(?,?,?,?,?,?,?,?,?);
      '''
      cursor.execute(csql, value)
      conn.commit()
      conn.close()


aqurl = '''https://data.moenv.gov.tw/api/v2/aqx_p_136?api_key=1f7402cf-f22f-4253-95d7-02821ce4bf65'''

conn = sqlite3.connect('./aqi.db')
sqlCrtTb(conn)
reqjson=getjson(aqurl)
jdata=jsondata(reqjson)
pushValue(jdata)