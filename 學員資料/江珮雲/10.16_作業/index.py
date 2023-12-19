import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
import csv

class Window(tk.Tk):
    def __init__(self,**kwargs): 
        super().__init__(**kwargs)
        self.title("股票資料")
        
class Getstock(Dialog):
    
    def __init__(self,master,values):
        self.values = values
        super().__init__(master)
        self.title("個股資料")
         
        tk.Label(master,text='日期').grid(row=0,column=1,sticky=tk.W)
        tk.Label(master,text='開盤價').grid(row=1,column=1, sticky=tk.W)
        tk.Label(master,text='最高價').grid(row=2,column=1, sticky=tk.W)
        tk.Label(master,text='最低價').grid(row=3,column=1, sticky=tk.W)
        tk.Label(master,text='收市價').grid(row=4,column=1, sticky=tk.W)
        tk.Label(master,text='收盤價').grid(row=5,column=1, sticky=tk.W)
        tk.Label(master,text='成交量').grid(row=6,column=1, sticky=tk.W)
     
        self.date= tk.Label(master, width=16, show='*', sticky=tk.E)
        self.opan = tk.Label(master, width=16, show='*', sticky=tk.E)
        self.high = tk.Label(master, width=16, show='*',sticky=tk.E)
        self.low= tk.Label(master, width=16, show='*',sticky=tk.E)
        self.colse = tk.Label(master, width=16, show='*',sticky=tk.E)
        self.adjcolse = tk.Label(master, width=16, show='*',sticky=tk.E)
        self.volume = tk.Label(master, width=16, show='*',sticky=tk.E)
        return self.date
        
    
        
class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack()
        #卷軸
        scrollbar = ttk.Scrollbar(self, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        
        self.field =ttk.Treeview(self,columns=['#1','#2','#3','#4','#5','#6','#7'],show="headings", yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.tree.yview)
        
        self.field.heading('#1',text="Date")
        self.field.heading('#2',text="Open")
        self.field.heading('#3',text="High")
        self.field.heading('#4',text="Low")
        self.field.heading('#5',text="Close")
        self.field.heading('#6',text="Adj Close")
        self.field.heading('#7',text="Volume")
        self.field.pack()
        
        file = open('台積電.csv','r', encoding='utf-8')
        csv_reader = csv.reader(file)
        TSMC = list(csv_reader) 
        for contact in TSMC:
            self.field.insert('',tk.END,value=contact)
            
        self.field.pack()
        self.field.bind('<<TreeviewSelect>>',self.item_selected)

       
        
    def item_selected(self,event):
        item_id = self.field.selection()[0]
        item_dict = self.field.item(item_id)
        print(item_dict['values'])
        getstock = Getstock(self,values)
              
        
       
            
                
        
def main():
    wimdow = Window()
    myFrame = MyFrame(wimdow,"股票資料")
    wimdow.mainloop()
    
if __name__ == "__main__":
        main()
    