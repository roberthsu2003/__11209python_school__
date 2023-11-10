import tkinter as tk
from tkinter import ttk
from youbikeTreeview import YoubikeTreeview
from tkinter import messagebox
from threading import Timer
import dataSource

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #---------更新資料庫資料-----------------#
        try:
            dataSource.update_sqlite_data()
        except Exception:
            messagebox.showerror("錯誤",'網路不正常\n將關閉應用程式\n請稍後再試')
            self.destroy()
        #---------建立介面------------------------
        # print(dataSource.lastest_datetime_data())
        topFrame = tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame,text="台北市youbike即時資料",font=("arial", 20), bg="#333333", fg='#ffffff',padx=10,pady=10).pack(padx=20,pady=20)
        topFrame.pack(pady=30)
        #----------------------------------------


        #---------建立搜尋------------------------
        middleFrame = ttk.LabelFrame(self, text='')
        tk.Label(middleFrame,text='站點名稱搜尋：').pack(side='left')
        # self.search_entry = tk.Entry(middleFrame)
        # self.search_entry.pack(side='left')
        search_entry = tk.Entry(middleFrame)
        search_entry.bind("<KeyRelease>", self.OnEntryClick)
        search_entry.pack(side='left')
        middleFrame.pack(fill='x', padx=20)
        #----------------------------------------


        
        #---------建立 Treeview------------------------
        bottomFrame = tk.Frame(self)

        self.youbikeTreeview = YoubikeTreeview(bottomFrame, show="headings", columns=('sna','mday','sarea','ar','tot','sbi','bemp'), height=20)
        self.youbikeTreeview.pack(side='left')

        # Create a Scrollbar
        vsb = ttk.Scrollbar(bottomFrame, orient="vertical", command=self.youbikeTreeview.yview)
        # Configure the Treeview to use the scrollbar
        self.youbikeTreeview.configure(yscrollcommand=vsb.set)
        # Place the scrollbar on the right side of the Treeview, and make it fill the entire height of the Treeview
        vsb.pack(side='right', fill='y')

        bottomFrame.pack(pady=(0,30), padx=20)
        # print(dataSource.search_sitename('大安'))
        #----------------------------------------

        #---------更新 Treeview 資料------------------------
        # latest_data = dataSource.lastest_datetime_data()
        # self.youbikeTreeview.update_content(latest_data)

    def OnEntryClick(self,event):
        searchEntry = event.widget
        #使用者輸入的文字
        input_text = searchEntry.get()
        if input_text == "":
            # print("空的")
            lastest_data = dataSource.lastest_datetime_data()
            self.youbikeTreeview.update_content(lastest_data)
        else:
            search_data = dataSource.search_sitename(text=input_text)
            self.youbikeTreeview.update_content(search_data)

# t = None
def main():
    # def on_closing(): 
    #     print("window關閉")
    #     t.cancel()
    #     window.destroy()
    def update_data(w:Window)->None:
        dataSource.update_sqlite_data()
        # global t
        # t = Timer(20,update_data)
        # t.start()
        #---------更新 Treeview 資料------------------------
        latest_data = dataSource.lastest_datetime_data()
        w.youbikeTreeview.update_content(latest_data)
        window.after(3*60*1000, update_data, w) # 每隔3分鐘

    window = Window()
    window.title('台北市youbike2.0')
    # window.geometry('600x300')
    window.resizable(width=False,height=False)
    update_data(window)
    # window.protocol("WM_DELETE_WINDOW",on_closing)      
    window.mainloop()

if __name__ == '__main__':
    main()