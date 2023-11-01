import tkinter as tk
from tkinter import ttk
from youbikeTreeView import YoubikeTreeView

from tkinter import messagebox
from threading import Timer
import datasource

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #---------更新資料庫資料-----------------#
        try:
            datasource.updata_sqlite_data()
        except Exception:
            messagebox.showerror("錯誤",'網路不正常\n將關閉應用程式\n請稍後再試')
            self.destroy()
        

        #---------建立介面------------------------
        #print(datasource.lastest_datetime_data())
        topFrame = tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame,text="台北市youbike及時資料",font=("arial", 20), bg="#333333", fg='#ffffff',padx=10,pady=10).pack(padx=20,pady=20)
        topFrame.pack(pady=30)

        bottomFrame = tk.Frame(self)
        #---------------建立treeView---------------
        self.youbikeTreeView = YoubikeTreeView(bottomFrame,show="headings",columns=('sna','mday','sarea','ar','tot','sbi','bemp'))
        self.youbikeTreeView.pack()
        bottomFrame.pack(pady=30)

        


def main():    
    def update_data(w:Window)->None:
        datasource.updata_sqlite_data()
        window.after(3*60*1000,update_data,w) #每隔3分鐘
          

    window = Window()
    window.title('台北市youbike2.0')
    #window.geometry('600x300')
    window.resizable(width=False,height=False)
    update_data(window)          
    window.mainloop()

if __name__ == '__main__':
    main()