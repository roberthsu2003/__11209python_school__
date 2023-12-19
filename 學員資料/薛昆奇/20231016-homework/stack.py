import csv
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('2330-台積電')
        self.frame=Frame(self) #套用class Frame的所有實體

class Frame(ttk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.pack()

        self.scroll = tk.Scrollbar(self)
        self.scroll.pack(side='right', fill='y')
        self.tree=ttk.Treeview(self,columns=['1','2','3','4','5','6','7'],show='headings')
        self.scroll.configure(command=self.tree.yview)
        self.tree.heading(1,text='交易日')
        self.tree.heading(2,text='開盤價')
        self.tree.heading(3,text='最高價')
        self.tree.heading(4,text='最低價')
        self.tree.heading(5,text='收盤價')
        self.tree.heading(6,text='調整後收盤價')
        self.tree.heading(7,text='成交量')
        self.tree.pack()

        stock=self.price_list()
        for row in stock:
            self.tree.insert('', tk.END, values=row)

        self.tree.bind('<<TreeviewSelect>>',self.item_select)
        
    def price_list(self):
        stacklist=list()
        with open('./台積電.csv','r',encoding='utf-8') as file:
            reader=csv.reader(file)
            next=(file)
            for row in reader:
                stacklist.append(row)
        return stacklist
    
    def item_select(self,event):
        item_id = self.tree.selection()[0]
        item_dict=self.tree.item(item_id)
        price=item_dict['values']
        print(price)
        dialog=Dialog_box(self,price)

class Dialog_box(Dialog):
    def __init__(self, master,price):
        self.price=price
        super().__init__(master)
        
    def body(self, master):
        tk.Label(master, text='日期:').grid(row=0, column=0, sticky='W')
        tk.Label(master, text='開盤價:').grid(row=1, column=0, sticky='W')
        tk.Label(master, text='盤中最高價:').grid(row=2, column=0, sticky='W')
        tk.Label(master, text='盤中最低價:').grid(row=3, column=0, sticky='W')
        tk.Label(master, text='收盤價:').grid(row=4, column=0, sticky='W')
        tk.Label(master, text='調整後收盤價:').grid(row=5, column=0, sticky='W')
        tk.Label(master, text='成交量:').grid(row=6, column=0, sticky='W')

        tk.Label(master, text=self.price[0]).grid(row=0, column=1, sticky='E')
        tk.Label(master, text=self.price[1]).grid(row=1, column=1, sticky='E')
        tk.Label(master, text=self.price[2]).grid(row=2, column=1, sticky='E')
        tk.Label(master, text=self.price[3]).grid(row=3, column=1, sticky='E')
        tk.Label(master, text=self.price[4]).grid(row=4, column=1, sticky='E')
        tk.Label(master, text=self.price[5]).grid(row=5, column=1, sticky='E')
        tk.Label(master, text=self.price[6]).grid(row=6, column=1, sticky='E')

def main():
    window=Window()
    s=ttk.Style() #套用ttk的style
    print(s.theme_use('classic')) #設定ttk的style為“classic”
    window.mainloop()

if __name__ == '__main__':
    main()