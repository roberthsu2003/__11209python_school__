import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk         #查網站安裝pillow   
from tkinter.simpledialog import Dialog
import yfinance as yf
import csv



class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs) 
        self.geometry("1500x250")       
        self.title("股價查詢")  
        
class GetPrice(Dialog):
    def __init__(self, master, values):
        self.value = values
        super().__init__(master)

    def body(self, master):
        tk.Label(master, text='日期:').grid(row=0, sticky=tk.W)
        tk.Label(master, text='開盤價:').grid(row=1, sticky=tk.W)
        tk.Label(master, text='最高價:').grid(row=2, sticky=tk.W)
        tk.Label(master, text='最低價:').grid(row=3, sticky=tk.W)
        tk.Label(master, text='收盤價:').grid(row=4, sticky=tk.W)
        tk.Label(master, text='調整收盤價:').grid(row=5, sticky=tk.W)
        tk.Label(master, text='成交量:').grid(row=6, sticky=tk.W)

        tk.Label(master, text=self.value[0]).grid(row=0, column=1, sticky='E')
        tk.Label(master, text=self.value[1]).grid(row=1, column=1, sticky='E')
        tk.Label(master, text=self.value[2]).grid(row=2, column=1, sticky='E')
        tk.Label(master, text=self.value[3]).grid(row=3, column=1, sticky='E')
        tk.Label(master, text=self.value[4]).grid(row=4, column=1, sticky='E')        
        tk.Label(master, text=self.value[5]).grid(row=5, column=1, sticky='E')       
        tk.Label(master, text=self.value[6]).grid(row=6, column=1, sticky='E')
        
    def buttonbox(self):
          
        box = tk.Frame(self)        
        w = tk.Button(box, text="確認", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        #w = tk.Button(box, text="取消", width=10, command=self.cancel)
        #w.pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        #self.bind("<Escape>", self.cancel)           
        box.pack()
        
       

class MyFrame(ttk.LabelFrame):
    def __init__(self,master,title,**kwargs):               
        super().__init__(master,text=title,**kwargs)        
        self.pack(expand=1,fill="both",padx=10,pady=10)        
        

        self.tree = ttk.Treeview(self,columns=['#1','#2','#3','#4','#5','#6','#7'],show='headings')    
        self.tree.heading('#1',text='日期') 
        self.tree.heading('#2',text='開盤價')
        self.tree.heading('#3',text='最高價')
        self.tree.heading('#4',text='最低價') 
        self.tree.heading('#5',text='收盤價')
        self.tree.heading('#6',text='調整收盤價')
        self.tree.heading('#7',text='成交量')         


        self.scrollbar = ttk.Scrollbar(self,orient="vertical",command=self.tree.yview)        
        self.scrollbar.pack(side='right', fill='y')  
        self.tree.config(yscrollcommand=self.scrollbar.set)
         
        data = yf.download("2330.TW", start='2023-01-01')
        data.to_csv('台積電.csv')
        with open('台積電.csv', newline='') as csvfile:
            price_reader = csv.DictReader(csvfile)
            for row in price_reader:
                date = row['Date']
                open_v = row['Open']
                high = row['High']
                low = row['Low']
                close = row['Close']
                adj_close = row['Adj Close']
                value = row['Volume']       
                self.tree.insert('',tk.END,value=(date,open_v,high,low,close,adj_close,value))
            self.tree.pack()
        
        self.tree.bind('<<TreeviewSelect>>',self.item_selected)  

    def item_selected(self,event):
        item_id = self.tree.selection()[0]
        item_dict = self.tree.item(item_id)
        value =(item_dict['values'])
        get_price = GetPrice(self,value)        
       

    def choised(self):
        print(self.aligement.get())


def main():    
    window = Window()
    myFrame = MyFrame(window,"台積電股價查詢")    
    window.mainloop()


if __name__ == "__main__":
    main()