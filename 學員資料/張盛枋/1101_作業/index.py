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
        tk.Label(topFrame,text="台北市youbike即時資料",font=("arial", 20), bg="#333333", fg='#ffffff',padx=10,pady=10).pack(padx=20,pady=20)
        topFrame.pack(pady=30)
        
        #--------- middle frame ------
        middleFrame = tk.Frame(self)
        
        name_label = tk.Label(middleFrame,text="搜尋站點名稱:",font=('Helvetica',12))
        name_label.grid(column=0,row=0)
       
        self.e = tk.StringVar()          
        tk.Entry(middleFrame, width=40, textvariable=self.e).grid(column=1, row=0)
              
        ok_button = tk.Button(middleFrame,text="OK", state='active',command=self.search)
        ok_button.grid(column=2,row=0)
        middleFrame.pack(pady=10)

        #--------- bottom frame ------
        bottomFrame = tk.Frame(self)
        #---------------建立treeView---------------
        self.youbikeTreeView = YoubikeTreeView(bottomFrame,show="headings",columns=('sna','mday','sarea','ar','tot','sbi','bemp'))
        self.youbikeTreeView.pack(side='left')
        vsb = ttk.Scrollbar(bottomFrame, orient="vertical", command=self.youbikeTreeView.yview)
        vsb.pack(side='left',fill='y')
        self.youbikeTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=30)
        print(datasource.search_sitename('三'))
        
    def search(self):
            search_name = self.e.get()
            result = datasource.search_sitename(search_name)
            if result:
                for i in self.youbikeTreeView.get_children():
                    self.youbikeTreeView.delete(i)

                for results in result:
                    self.youbikeTreeView.insert('','end',values=results)
        

def main():    
    def update_data(w:Window)->None:
        datasource.updata_sqlite_data()
        #-----------更新treeView資料---------------
        lastest_data = datasource.lastest_datetime_data()
        w.youbikeTreeView.update_content(lastest_data)

        window.after(1*60*1000,update_data,w) #每隔1分鐘
          

    window = Window()
    window.title('台北市youbike2.0')
    #window.geometry('600x300')
    window.resizable(width=False,height=False)
    update_data(window)          
    window.mainloop()

if __name__ == '__main__':
    main()