'''
作業 ttk.Treeview  個股資訊
'''
import tkinter as tk
from tkinter import ttk
import csv

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('個股收盤')

class Window22(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('22個股收盤')


'''
建立 tkinter 視窗物件後，透過 LabelFrame 方法，就能在視窗物件中建立 LabelFrame 框架，
必要的參數有兩個，表示要加入的視窗物件，以及要顯示的標題文字，建立 Frame 框架後再使用 pack() 方法將其加入'''

class Myframe(tk.LabelFrame):
    def __init__(self, master, title, **kwargs):
        super().__init__(master, text=title, **kwargs)
        self.pack(expand=1,fill='both', padx=10,pady=10)

        self.tree=ttk.Treeview(self, columns=['#1', '#2','#3','#4', '#5', '#6', '#7'], show='headings')

        self.tree.heading('#1',text='日期')
        self.tree.heading('#2',text='開盤')
        self.tree.heading('#3',text='最高價')
        self.tree.heading('#4',text='最低價')
        self.tree.heading('#5',text='收盤價')
        self.tree.heading('#6',text='還原股價')
        self.tree.heading('#7',text='成交股數')

        with open('../lesson18/台積電.csv', 'r', encoding='utf-8', newline='') as csvf:
            csvfile = csv.reader(csvf)
            csvc=[]
            for row in csvfile:
                csvc.append(row)

                for va in list(csvc) :
                    self.tree.insert('', 0, values=va)
                csvc=[]
        #print(csvc)
        
        self.tree.pack()



def main():
    window22 = Window22()
    window = Window()
    myframe = Myframe(window,"視窗")
    window22.mainloop()



if __name__ == "__main__":
    main()
