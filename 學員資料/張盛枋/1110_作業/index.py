import datasource
from threading import Timer
import time
import threading

def countdown(n:int)->None:
    while n > 0:
        print(f'倒數計時:{n}')
        n -= 1
        time.sleep(600) # 暫停執行 600 秒

def main():
    datasource.update_render_data()
    max_cnt = 24    # 下載次數
    count = 1
    while count != max_cnt:
        # 建立執行緒
        t = threading.Thread(target=countdown,args=(10,)) # 倒數n次
        t.start()   # 開始執行

        while t.is_alive():
            time.sleep(1)
            print('小猴子還在做事')            
            print('------------')
        else:
            datasource.update_render_data()
            count += 1
            print(f"第{count}次下載資料")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Program interrupted by user.")
        