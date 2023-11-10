import datasource
import psycopg2
import password as pw
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    pass

def main():
    def update_data(w:Window)->None:
        datasource.updata_render_data()
        #-----------更新treeView資料---------------
        #lastest_data = datasource.lastest_datetime_data()
        #w.youbikeTreeView.update_content(lastest_data)

        w.after(5*60*1000,update_data,w) #每隔5分鐘

    window = Window()
    window.title('台北市youbike2.0')
    #window.geometry('600x300')
    window.resizable(width=False,height=False)
    window.after(1000,update_data,window)          
    window.mainloop()
    

    

if __name__ == "__main__":
    main()