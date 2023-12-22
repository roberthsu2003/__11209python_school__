import psycopg2
from . import password as pw

class InvolidEmailException(Exception):
    pass

def insert_data(values:list[any] | None = None) -> None:
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER, 
                            password=pw.PASSWORD,
                            host=pw.HOST, 
                            port="5432")
    
    cursor = conn.cursor()
    insertSql = '''
    INSERT INTO 使用者("姓名", "性別", "聯絡電話", "電子郵件", "isGetEmail","出生年月日", "自我介紹", "密碼", "連線密碼") 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    try:
        cursor.execute(insertSql,values)
    except psycopg2.errors.UniqueViolation:
        raise InvolidEmailException
    except:
        raise RuntimeError
    conn.commit()
    cursor.close()
    conn.close()
