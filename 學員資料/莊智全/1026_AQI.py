import requests, sqlite3, datetime, json, threading, time

'''
參考網址 URL=https://data.moenv.gov.tw/swagger/#/%E5%A4%A7%E6%B0%A3/get_aqx_p_07

url= https://data.moenv.gov.tw/api/v2/aqx_p_136?api_key=1f7402cf-f22f-4253-95d7-02821ce4bf65
'''

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
      
def pushvalue(jata):           # 將 "records" 這項的值 逐列讀取時, 依鍵取值, 存放入 values 變數 , 再將values 變數當參數引入sqlIsrtTb(conn, values)...
      conn = sqlite3.connect('./aqi.db')
      ccursor = conn.cursor()

      for row in jata:
            values=[row["siteid"], row["sitename"],row["county"],row["itemid"],row["itemname"],row["itemengname"],row["itemunit"],row["monitordate"],row["concentration"]]
            #sqlIsrtTb(conn, jvalues)
            #print('pushvalue')
            csql=f'''
            REPLACE INTO {city}aqi(測站代碼, 測站名稱, 縣市, 測項代碼, 測項名稱, 測項英文名稱, 測項單位, 監測日期, 數值) VALUES(?,?,?,?,?,?,?,?,?);
            '''
            ccursor.execute(csql, values)
            conn.commit()
            


def sqlCrtTb(conn, aq):      # 創建 DB Table (已有同名Table 則不建立...[ IF NOT EXISTS ])
      global city
      if aq==136:
            city='台北市'
      elif aq==137:
            city='新北市'
      elif aq==138:
            city='桃園市'
      elif aq==139:
            city='新竹市'
      elif aq==140:
            city='新竹縣'
      elif aq==141:
            city='苗栗縣'
      elif aq==142:
            city='臺中市'
      elif aq==143:
            city='彰化縣'
      elif aq==144:
            city='南投縣'
      elif aq==145:
            city='雲林縣'
      elif aq==146:
            city='嘉義市'
      elif aq==147:
            city='嘉義縣'
      elif aq==148:
            city='澎湖縣'
      elif aq==149:
            city='臺南市'
      elif aq==150:
            city='高雄市'
      elif aq==151:
            city='屏東縣'
      elif aq==152:
            city='臺東縣'
      elif aq==153:
            city='花蓮縣'
      elif aq==154:
            city='宜蘭縣'
      elif aq==155:
            city='金門縣'
      elif aq==156:
            city='連江縣'
      
      
      conn = sqlite3.connect('./aqi.db')
      cursor = conn.cursor()
      a1sql=f'''CREATE TABLE IF NOT EXISTS {city}aqi(
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
      print(f'CREATE {city}')


     

###

def main():

    conn = sqlite3.connect('./aqi.db')
    aq=int
    city=str
    


    for aq in range(136,157):
        aqurl = f'https://data.moenv.gov.tw/api/v2/aqx_p_{aq}?api_key=1f7402cf-f22f-4253-95d7-02821ce4bf65'
        sqlCrtTb(conn, aq)
        reqjson=getjson(aqurl)
        jdata=jsondata(reqjson)
        time.sleep(2)
        pushvalue(jdata)
        #pushValue(jdata)

    conn.close()
    time.sleep(3600)
    main()


if __name__=="__main__":
      main()
