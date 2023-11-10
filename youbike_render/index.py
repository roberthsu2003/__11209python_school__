import datasource
import psycopg2
import password as pw

def main():
    jsonData = datasource.download_youbike_data()    
    try:
        conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER, 
                            password=pw.PASSWORD,
                            host=pw.HOST, 
                            port="5432")
    except psycopg2.Error as e:
        print("error")
        print(e)
    else:
        print("連線成功")
        datasource.create_table(conn)
        for item in jsonData:
            datasource.insert_data(conn,[item['sna'],item['sarea'],item['mday'],item['ar'],item['tot'],item['sbi'],item['bemp']])
        conn.close()

    

if __name__ == "__main__":
    main()