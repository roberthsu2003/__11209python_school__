'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
import csv

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("台積電股價")
        self.frame = MyFrame(self) 
 
class MyFrame(ttk.LabelFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.pack()
        
        # new 1017-16:10
        scrollbar = ttk.Scrollbar(self, orient='vertical')
        scrollbar.pack(side='right', fill='y')

        self.tree = ttk.Treeview(self,columns=['#1', '#2', '#3', '#4', '#5', '#6', '#7'],show='headings',yscrollcommand=scrollbar.set )

        scrollbar.configure(command=self.tree.yview)  
        self.tree.heading('#1', text="日期")
        self.tree.heading('#2', text="開盤")
        self.tree.heading('#3', text="最高")
        self.tree.heading('#4', text="最低")
        self.tree.heading('#5', text="收盤")
        self.tree.heading('#6', text="調整後收盤")
        self.tree.heading('#7', text="成交量")
        self.tree.pack()
        
        self.price = self.getPrice()
        
        for contact in self.price:
            self.tree.insert('',tk.END,value=contact)

        self.tree.bind('<<TreeviewSelect>>',self.show_popup)
    
    def getPrice(self):
        with open('台積電.csv','r',encoding='UTF-8') as file:
            csvReader = csv.reader(file)
            next(csvReader)
            list_csvReader = list(csvReader)
        return list_csvReader
                                     
    def show_popup(self, event):
        index = self.tree.selection()[0]
        tree_dict = self.tree.item(index)
        values = tree_dict['values']
        popup = Popup(self, values)
           
class Popup(Dialog):
    def __init__(self, master, values):
        self.values = values
        super().__init__(master)

    def body(self, master):
        tk.Label(master, text='日期:').grid(row=0, column=0, sticky='W')
        tk.Label(master, text='開盤:').grid(row=1, column=0, sticky='W')
        tk.Label(master, text='最高:').grid(row=2, column=0, sticky='W')
        tk.Label(master, text='最低:').grid(row=3, column=0, sticky='W')
        tk.Label(master, text='收盤:').grid(row=4, column=0, sticky='W')
        tk.Label(master, text='調整後收盤:').grid(row=5, column=0, sticky='W')
        tk.Label(master, text='成交量:').grid(row=6, column=0, sticky='W')
        tk.Label(master, text=self.values[0]).grid(row=0, column=1, sticky='E')
        tk.Label(master, text=self.values[1]).grid(row=1, column=1, sticky='E')
        tk.Label(master, text=self.values[2]).grid(row=2, column=1, sticky='E')
        tk.Label(master, text=self.values[3]).grid(row=3, column=1, sticky='E')
        tk.Label(master, text=self.values[4]).grid(row=4, column=1, sticky='E')
        tk.Label(master, text=self.values[5]).grid(row=5, column=1, sticky='E')
        tk.Label(master, text=self.values[6]).grid(row=6, column=1, sticky='E')
                
        
def main():    
    window = Window()
    window.mainloop()

if __name__ == '__main__':
    main()