'''
1. 下載台灣股市資訊
2. 存成csv檔案
3. 視窗樹狀表格
4. 當點選特定資料時，可以顯示點選欄位的詳細資訊
'''

import datasource
import csv
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import Dialog

#建立window視窗
class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("台積電2023年股票查詢")
        #self.MyFrame = MyFrame(self,"台積電2023-01-01-2023-10-17")

#建立容器Frame，裡面放樹狀選單＋匯入CSV資料＋滾動軸
class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',padx=10,pady=10)

        #建立treeView欄位
        self.tree = ttk.Treeview(self,columns=['#1', '#2', '#3', '#4', '#5', '#6', '#7'],show="headings")
        self.tree.heading('#1', text="Date")
        self.tree.heading('#2', text="Open")
        self.tree.heading('#3', text="High")
        self.tree.heading('#4', text="Low")
        self.tree.heading('#5', text="Close")
        self.tree.heading('#6', text="Adj Close")
        self.tree.heading('#7', text="Volume")

        #建立滾動軸
        self.scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side='right',fill='y')
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        #匯入csv檔案，寫入treeView
        with open('yf_2330.csv') as data:
            data = csv.DictReader(data)
            for row in data: 
                Date = row['Date']
                Open = row['Open']
                High = row['High']
                Low = row['Low']
                Close = row['Close']
                Adj_Close = row['Adj Close']
                Volume = row['Volume']
                self.tree.insert('',tk.END,value=(Date, Open, High, Low, Close, Adj_Close, Volume))

        #layout
        self.tree.pack()

        #註冊選單被使用者點擊後觸發的方法 
        self.tree.bind('<<TreeviewSelect>>',self.item_selected)

    def item_selected(self, event):
        item_id = self.tree.selection()[0] 
        #self.tree.item(item_id)
        item_dict = self.tree.item(item_id)
        value = item_dict['values']
        print(value[0],value[1],value[2],value[3],value[4],value[5],value[6])
        dialog = GetPassword(self,values=value)

class GetPassword(Dialog):
    def __init__(self, master, values, **kwargs):
        self.values = values
        super().__init__(master, **kwargs)
        
    def body(self, master): 
        self.title("詳細資訊")

        tk.Label(master, text='Date:').grid(row=0, sticky=tk.W)
        tk.Label(master, text='Open:').grid(row=1, sticky=tk.W)
        tk.Label(master, text='High:').grid(row=2, sticky=tk.W)
        tk.Label(master, text='Low:').grid(row=3, sticky=tk.W)
        tk.Label(master, text='Close:').grid(row=4, sticky=tk.W)
        tk.Label(master, text='Adj Close:').grid(row=5, sticky=tk.W)
        tk.Label(master, text='Volume:').grid(row=6, sticky=tk.W)
        tk.Label(master, text=self.values[0]).grid(row=0,column=1, sticky=tk.E)
        tk.Label(master, text=self.values[1]).grid(row=1,column=1, sticky=tk.E)
        tk.Label(master, text=self.values[2]).grid(row=2,column=1, sticky=tk.E)
        tk.Label(master, text=self.values[3]).grid(row=3,column=1, sticky=tk.E)
        tk.Label(master, text=self.values[4]).grid(row=4,column=1, sticky=tk.E)
        tk.Label(master, text=self.values[5]).grid(row=5,column=1, sticky=tk.E)
        tk.Label(master, text=self.values[6]).grid(row=6,column=1, sticky=tk.E)
    
    def buttonbox(self):
        box = tk.Frame(self) 
        w = tk.Button(box, text="確認", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="取消", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok) 
        self.bind("<Escape>", self.cancel) 
        box.pack()

def main():    
    window = Window()
    myFrame = MyFrame(window,"台積電2023年股票查詢")  
    window.mainloop()

if __name__ == "__main__":
    main()