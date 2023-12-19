import yfinance as yf
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
import csv

#抓股票
data = yf.download("0050.TW", start='2023-01-01')
data.to_csv("0050.csv")

#版面設定
class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("小小股票介面")

#樹狀
class Frame(ttk.LabelFrame):
    def __init__(self,master,title, **kwargs):
        super().__init__(master=master,text=title,**kwargs)
        self.tree=ttk.Treeview(self,columns=[1,2,3,4,5,6,7],show="headings")
        self.tree.heading(1,text="日期")
        self.tree.heading(2,text="開盤價")
        self.tree.heading(3,text="最高價")
        self.tree.heading(4,text="最低價")
        self.tree.heading(5,text="收盤價")
        self.tree.heading(6,text="調整後收盤價")
        self.tree.heading(7,text="成交量")

        with open('0050.csv', 'r', encoding='UTF-8') as file:
            data=csv.reader(file)
            next(data)
            self.text_data=[]
            for t in data:
                self.tree.insert("",tk.END,values=t)
            self.tree.pack()

        self.tree.bind("<<TreeviewSelect>>",self.item)

        self.pack(expand=1,fill="both",padx=10,pady=20)

            
    def item(self,event):
        item_id=self.tree.selection()[0]
        self.text_data= self.tree.item(item_id)['values']
        print(self.text_data)
        dialog = GetPassword(self,self.text_data)

# 點擊後小視窗
class GetPassword(Dialog):
    def __init__(self, parent,text_data):
        self.text_data=text_data
        super().__init__(parent)
    #股票
    def body(self, master):
        self.title(f"{self.text_data[0]}資料")

        for i, label in enumerate(["開盤價：", "最高價：", "最低價：", "收盤價：", "調整後收盤價：", "成交量："]):
            tk.Label(master, text=f"{label}{self.text_data[i+1]}").grid(row=i, sticky=tk.W)

    #確認/取消鍵
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
    window=Window()
    frame=Frame(window,"0050")
    window.mainloop()

if __name__ == "__main__":
    main()