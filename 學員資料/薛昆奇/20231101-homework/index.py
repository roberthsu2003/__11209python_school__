#在此感謝在得同學給予搜尋method的語法參考，我父繼承了全部XD

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
        #-----表頭標題-----#
        topFrame = tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame,text="台北市youbike及時資料",font=("arial", 20), bg="#333333", fg='#ffffff',padx=10,pady=10).pack(padx=20,pady=20)
        #設定變數 String 型別儲存目前內容
        var = tk.StringVar()
        topFrame.pack(pady=30)

        #-----中間搜尋entry及按鈕-----#
        middleFrame=tk.Frame(self)
        tk.Label(middleFrame,text='站點查詢',font=('arial',20),bg="#333333", fg='#ffffff').pack(padx=30,pady=30)
        middleFrame.pack(pady=30)
        self.e=tk.StringVar()
        tk.Entry(middleFrame,width=40,textvariable=self.e).pack(side='left')
        actionButton=tk.Button(middleFrame,text='查詢',state='normal',command=self.site_search)
        actionButton.pack(side='right')
        middleFrame.pack()

        #-----底層TreeView區塊-----#
        bottomFrame = tk.Frame(self)
        #---------------建立treeView---------------
        self.youbikeTreeView = YoubikeTreeView(bottomFrame,show="headings",columns=('sna','mday','sarea','ar','tot','sbi','bemp'))
        self.youbikeTreeView.pack(side='left')
        vsb = ttk.Scrollbar(bottomFrame, orient="vertical", command=self.youbikeTreeView.yview)
        vsb.pack(side='left')
        self.youbikeTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=30)
        #print(datasource.search_sitename('振興'))

    #-----設定搜尋的method-----#        
    def site_search(self):
        search_query=self.e.get()
        search_result=datasource.search_sitename(search_query)
        if search_result:
            for item in self.youbikeTreeView.get_children():
                self.youbikeTreeView.delete(item)
            for result in search_result:
                self.youbikeTreeView.insert("",'end',values=result)

        


def main():    
    def update_data(w:Window)->None:
        datasource.updata_sqlite_data()
        #-----------更新treeView資料---------------
        lastest_data = datasource.lastest_datetime_data()
        w.youbikeTreeView.update_content(lastest_data)

        window.after(3*60*1000,update_data,w) #每隔3分鐘
          

    window = Window()
    window.title('台北市youbike2.0')
    #window.geometry('600x300')
    window.resizable(width=False,height=False)
    update_data(window)          
    window.mainloop()

if __name__ == '__main__':
    main()