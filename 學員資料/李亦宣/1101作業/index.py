import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource
from threading import Timer
from youbikeTreeView import YoubikeTreeView

class Window(tk.Tk):                      
    def __init__(self, **kwargs):          
        super().__init__(**kwargs)         

        #-----------------------更新資料庫---------------------------#
        try:
            datasource.update_sqlite_data()
        except Exception:                     
            messagebox.showerror('錯誤','將關閉應用程式\n請稍後再試')
            self.destroy()                 #關閉視窗

        #------------------------視窗介面----------------------------#

        #------top Frame-----#
        topFrame = tk.Frame(self, relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame, text='台北市youbike即時資料', font=('arial', 20), bg='#333333', fg='#ffffff', padx=10, pady=10).pack(padx=20, pady=20)
        topFrame.pack(pady=30)

        #----search Frame----#
        searchFrame = tk.Frame(self)
        tk.Label(searchFrame, text='站點名稱:').grid(column=0, row=0)
        self.e = tk.StringVar()
        tk.Entry(searchFrame, width=40, textvariable=self.e).grid(column=1, row=0)
        tk.Button(searchFrame, text="搜尋", state='active',command=self.search_data).grid(column=2, row=0)
        searchFrame.pack()

        #----bottom Frame----#
        bottomFrame = tk.Frame(self)

        #-------------------------treeview----------------------------#
        self.youbikeTreeView = YoubikeTreeView(bottomFrame,columns=('sna','mday','sarea','ar','tot','sbi','bemp'),show="headings") #加'self.' => 在整個class中被公開使用
        self.youbikeTreeView.pack(side='left')
        
        #-------------------------scrollbar---------------------------#
        self.scrollbar = ttk.Scrollbar(bottomFrame, orient="vertical", command=self.youbikeTreeView.yview)
        self.scrollbar.pack(side='left',fill='y')
        self.youbikeTreeView.configure(yscrollcommand=self.scrollbar.set)

        bottomFrame.pack(pady=30)
    
    #----search data----#
    def search_data(self):
        search_term = self.e.get()
        result = datasource.search_sitename(search_term)
        self.youbikeTreeView.search(result = result)


def main():
    def update_data(w:Window)->None:
        datasource.update_sqlite_data()

        #-------------------update treeview data----------------------#
        lastest_data = datasource.lastest_datetime_data()
        w.youbikeTreeView.update_content(lastest_data)

        window.after(180*1000,update_data,w)

    window = Window()
    window.title('台北市youbike2.0')
    window.resizable(width=False,height=False)
    update_data(window)
    window.mainloop()


if __name__ == '__main__':
    main()