import tkinter as tk
from tkinter import ttk
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
        self.treeview = ttk.Treeview(bottomFrame,columns=('sna','mday','sarea','ar','tot','sbi','bemp'))
        self.treeview.heading('sna',text='站點名稱')
        self.treeview.heading('mday',text='更新時間')
        self.treeview.heading('sarea',text='行政區')
        self.treeview.heading('ar',text='地址')
        self.treeview.heading('tot',text='總車輛數')
        self.treeview.heading('sbi',text='可借')
        self.treeview.heading('bemp',text='可還')
        self.treeview.pack()
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