import requests
import password as pw
import json, csv, psycopg2


# 下載資料 並將其.json() 轉換--------------
def getjson():  # ->jsonfile
    f = requests.get(f"https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key={pw.apikey}")
    file = f.json()
    return file
    # print(f"file = f.json()   file_type= {type(file)}")


# ((寫入)成一個 *.csv檔)------------------
# 取出JSON 格式下 鍵="records"的值, 將其csv.DictWriter 轉換(寫入)成一個 *.csv檔案
def jsontocsv(jsonfile):  # ->records
    r = jsonfile.get("records")
    # records = file["records"]

    fieldnames = ["site", "county", "pm25", "datacreationdate", "itemunit"]
    with open("records.csv", "w", encoding="utf-8") as rec:
        csvf = csv.DictWriter(rec, fieldnames=fieldnames)
        csvf.writerows(r)


# 連接 Render (PostgreSQL)資料庫--------------
def linkDb(conn):
    cursor = conn.cursor()
    sqltb = """
        CREATE TABLE IF NOT EXISTS taiwan_pm25(
            "id" SERIAL,
            "站名" TEXT NOT NULL,
            "縣市" TEXT NOT NULL,
            "pm25" INTEGER NOT NULL,
            "更新時間" TEXT NOT NULL,
            "測量單位" TEXT NOT NULL,
            PRIMARY KEY("id"),
            UNIQUE("站名","更新時間")
            );
        """
    cursor.execute(sqltb)
    conn.commit()  # <注意>  容易忘記 >> conn.commit()

    # print("建立 Table: taiwan_pm25  建立完成 ")
    cursor.close()
    conn.close()
    # print('連線 RENDER_DB 成功')


# Insert data into table ----------------
def insertDb():
    try:
        conn = psycopg2.connect(
            host=pw.HOST, database=pw.DATABASE, user=pw.USER, password=pw.PASSWORD
        )
    except psycopg2.Error as e:
        print("連接資料庫失敗")
        print(e)
    else:
        print("資料庫連接成功")

    sqlinsert = """
    INSERT INTO taiwan_pm25 (站名, 縣市, pm25, 更新時間, 測量單位) 
        VALUES (%s,%s,%s,%s,%s)
        ON CONFLICT (站名,更新時間) DO NOTHING 
    """
    cursor = conn.cursor()
    with open("records.csv", "r", encoding="utf-8") as csvf:
        csvfile = csv.reader(csvf)
        for row in csvfile:
            rowvolues = [
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
            ]
            cursor.execute(sqlinsert, rowvolues)
            conn.commit()

    
    cursor.close()
    conn.close()
