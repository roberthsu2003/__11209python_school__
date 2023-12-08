import psycopg2
import password as pw
import datasource as dts
import threading, time, datetime


def main():
    conn = psycopg2.connect(
        host=pw.HOST, database=pw.DATABASE, user=pw.USER, password=pw.PASSWORD
    )
    dts.linkDb(conn)  # 連接 Render (PostgreSQL)資料庫. 建立 Table

    def repeat():
        file = dts.getjson()  # 下載資料
        dts.jsontocsv(file)  # ((寫入)成一個 *.csv檔)
        
        dts.insertDb()
        print("資料寫入完成", datetime.datetime.now())
        
        time.sleep(3600)
        repeat()

    repeat()


if __name__ == "__main__":
    main()
