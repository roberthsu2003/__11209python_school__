import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Timer
import datasource
import psycopg2
import password as pw


def main():
    def update_data()->None:
        #-----------更新treeView資料---------------   
        try:
            datasource.updata_render_data()

        except Exception as e:
            print(f"錯誤,網路不正常\n{e}")
            messagebox.showerror(f"錯誤,網路不正常\n{e}\n將關閉應用程式\n請稍後再試")

        lastest_data = datasource.lastest_datetime_data()
        #w.after(5*60*1000,update_data,w) #每隔5分鐘
        #t = Timer(5*60, update_data)
        #t.start()
    
    lastest_data = datasource.lastest_datetime_data()
    t = Timer(1, update_data)
    t.start()         
    

if __name__ == "__main__":
    main()