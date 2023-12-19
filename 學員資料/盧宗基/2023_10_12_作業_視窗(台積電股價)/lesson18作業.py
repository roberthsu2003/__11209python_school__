import yfinance as yf
import csv
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import Dialog


class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("台積電股價")
        #self.geometry("300x250")
        #self.configure(background='#E79460')

# 建List視窗 & Data
class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',padx=10,pady=10)

        self.tree = ttk.Treeview(self,columns=['#1', '#2', '#3','#4', '#5', '#6', '#7'],show="headings")
        self.tree.heading('#1', text="Date")
        self.tree.heading('#2', text="Open")
        self.tree.heading('#3', text="High")
        self.tree.heading('#4', text="Low")
        self.tree.heading('#5', text="Close")
        self.tree.heading('#6', text="Adj Close")
        self.tree.heading('#7', text="Volume")

        with open('台積電.csv') as file:
           csv_reader=csv.reader(file)
           csv_list=list(csv_reader)
        contacts = []
        for n in csv_list:
            contacts.append([f'{n[0]}',f'{n[1]}',f'{n[2]}',f'{n[3]}',f'{n[4]}',f'{n[5]}',f'{n[6]}'])

        for contact in contacts:
            self.tree.insert('',tk.END,value=contact)
        
        self.tree.pack()

        self.tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        
#bind------------------------------------------------------
        self.tree.bind('<<TreeviewSelect>>',self.item_selected)
     
    def item_selected(self,event):
        
        item_id = self.tree.selection()[0]
        item_dict = self.tree.item(item_id)
        value = item_dict['values']
        print(value[0],value[1],value[2],value[3],value[4],value[5],value[6])
        dialog = GetdataInfo(self,values=value)
        #self.dialog

#Dialog-----------------------------------------------------
class GetdataInfo(Dialog):
    def __init__(self, master, values,**kwargs): 
        self.values = values
        super().__init__(master,**kwargs)

    def body(self, master):
        self.title("查看")
        #values = csv_list
        tk.Label(master, text='Date:').grid(row=0, sticky=tk.W)
        tk.Label(master, text='Open:').grid(row=1, sticky=tk.W)
        tk.Label(master, text='High:').grid(row=2, sticky=tk.W)
        tk.Label(master, text='Low:').grid(row=3, sticky=tk.W)
        tk.Label(master, text='Close:').grid(row=4, sticky=tk.W)
        tk.Label(master, text='AdjClose:').grid(row=5, sticky=tk.W)
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


#執行起點-----------------------------------------------------

def main():    
    window = Window()
    myFrame = MyFrame(window,"台積電股價")    
    window.mainloop()

if __name__ == "__main__":
    main()