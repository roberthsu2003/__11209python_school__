import tkinter as tk
from tkinter import ttk
import json
import csv
import yfinance as yf
import sqlite3
import pandas as pd

#-----下載個股價格-----#
def download_stock():
    stock_number=x.get()
    stock_data = yf.download(f'{stock_number}.tw', start='2022-1-1')
    stock_data.to_csv(f'{stock_number}.csv')
    stock = []
    with open(f'./{stock_number}.csv', 'r',  encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            stock.append(row)
            with open(f'{stock_number}.json', 'w', encoding='utf-8') as file2:
                json.dump(stock, file2, ensure_ascii=False)
      
#-----建立資料表-----#
def create_sql(conn):
    stock_number = x.get()
    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    CREATE TABLE stock{stock_number} (
        "id"	INTEGER,
	    "交易日"	INTEGER NOT NULL,
	    "開盤價"	INTEGER NOT NULL,
	    "當日最高價"	INTEGER NOT NULL,
	    "當日最低價"	INTEGER NOT NULL,
	    "收盤價"	INTEGER NOT NULL,
	    "調整後收盤價"	INTEGER NOT NULL,
	    "當日成交量"	INTEGER NOT NULL,
	    PRIMARY KEY("id" AUTOINCREMENT)
            
    );
    """)
    conn.commit()


# -----輸入資料表-----#
def insert_data(conn, values):
    stock_number = x.get()
    cursor = conn.cursor()
    sql = f"""
    INSERT INTO stock{stock_number}(交易日,開盤價,當日最高價,當日最低價,收盤價,調整後收盤價,當日成交量)
        VALUES(?,?,?,?,?,?,?)
    """
    cursor.execute(sql, values)
    conn.commit()


# -----寫入資料庫-----#
def update_data():
    stock_number = x.get()
    conn = sqlite3.connect('stock.db')
    download_stock()
    #treeview_stock()
    create_sql(conn)
    with open(f'{stock_number}.json', 'r', encoding='utf-8') as file:
        reader = json.load(file)
        for item in reader:
            insert_data(conn, [item['Date'], item['Open'], item['High'],
                        item['Low'], item['Close'], item['Adj Close'], item['Volume']])
    conn.commit()
    conn.close()

# -----顯示資料至treeview上-----#
def treeview_stock():
    stock_number=x.get()
    with open(f'{stock_number}.csv', 'r',  encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            tree.insert('','end',values=row)
# -----計算60日均值-----#
def count_60():
    stock_number=x.get()
    data = pd.read_csv(f'{stock_number}.csv')
    tail_60 = data.tail(60)
    save_60 = tail_60[["Date", "Close"]].to_csv('60day.csv')
    data_60 = pd.read_csv("60day.csv")
    close_60 = data_60["Close"]
    avg_60 = close_60.mean()
    return avg_60
    
        


#-----視窗設定-----#
Window=tk.Tk()
Window.title('個股資料查詢')
Window.geometry('1024x800')


#-----設定各個部位框架-----#
firstFrame=tk.Frame(Window) #第一部份的框架(下載股價)
firstFrame.pack()
secondFrame=tk.Frame(Window) #第二部份的框架(treeview顯示)
secondFrame.pack()
thirdFrame = tk.Frame(Window)  # 第三部份的框架(回傳均價值)
thirdFrame.pack()
fouthFrame=tk.Frame(Window) #第四部份的框架
fouthFrame.pack()
fifthFrame=tk.Frame(Window) #第五部份的框架
fifthFrame.pack()

#-----第一部份框架內容-----#
x=tk.StringVar()
topic_label=tk.Label(firstFrame,text='個股查詢',font=('細明體',40))
topic_label.pack()
#-----設定搜尋股票代號-----#
entry_number=tk.Entry(firstFrame,textvariable=x)
entry_number.pack()
download_buttom = tk.Button(firstFrame, text='下載資料', command=update_data)
download_buttom.pack()

#-----第二部份框架內容-----#
display=tk.Button(secondFrame,text='顯示個股',command=treeview_stock)
display.pack()
tree = ttk.Treeview(
    secondFrame, show="headings", columns=["日期", "開盤", "最低", "最高", "收盤", "還原", "成交量"]
)
#-----設定treeview欄位-----#
#tree.bind("<<TreeviewSelect>>", item_select)
tree.heading(0, text="日期")
tree.heading(1, text="開盤")
tree.heading(2, text="最低")
tree.heading(3, text="最高")
tree.heading(4, text="收盤")
tree.heading(5, text="還原")
tree.heading(6, text="成交量")
#-----設定treeview格式-----#
tree.column(0, anchor="center", width=130)
tree.column(1, anchor="center", width=130)
tree.column(2, anchor="center", width=130)
tree.column(3, anchor="center", width=130)
tree.column(4, anchor="center", width=130)
tree.column(5, anchor="center", width=130)
tree.column(6, anchor="center", width=130)
tree.pack()

#-----回傳均價值-----#
tk.Button(thirdFrame,text='計算60日均價',command=count_60).pack()
title = tk.Label(thirdFrame, text="60/20/5日均價")
title.pack()
sixty_60 = tk.Label(thirdFrame, text=count_60(), font=('細明體', 40)).pack()

#如何按下tk.BUTTOM執行def後才在tk.label顯示#







Window.mainloop()