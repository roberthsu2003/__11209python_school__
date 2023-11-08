import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource
from threading import Timer
from youbikeTreeView import YoubikeTreeView

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #----------------------update database------------------------#
        try:
            datasource.update_sqlite_data()
        except Exception:                     
            messagebox.showerror('錯誤','將關閉應用程式\n請稍後再試')
            self.destroy()

        #------------------------interface----------------------------#

        #topFrame
        topFrame = tk.Frame(self, relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame, text='台北市youbike即時資料', font=('arial', 20), bg='#333333', fg='#ffffff', padx=10, pady=10).pack(padx=20, pady=20)
        topFrame.pack(pady=30)

        #searchFrame
        searchFrame = tk.Frame(self)
        tk.Label(searchFrame, text='站點名稱:').grid(column=0, row=0)
        self.e = tk.StringVar()
        tk.Entry(searchFrame, width=40, textvariable=self.e).grid(column=1, row=0)
        tk.Button(searchFrame, text="搜尋", state='active',command=self.search).grid(column=2, row=0)
        searchFrame.pack(pady=10)

        
        bottomFrame = tk.Frame(self)
        #-------------------------treeview----------------------------#
        self.youbikeTreeView = YoubikeTreeView(bottomFrame,columns=('sna','mday','sarea','ar','tot','sbi','bemp'),show="headings")
        self.youbikeTreeView.pack(side='left')

        
        #-------------------------scrollbar---------------------------#
        self.scrollbar = ttk.Scrollbar(bottomFrame, orient="vertical", command=self.youbikeTreeView.yview)
        self.scrollbar.pack(side='left',fill='y')
        self.youbikeTreeView.configure(yscrollcommand=self.scrollbar.set)

        bottomFrame.pack(pady=30)
        print(datasource.search_sitename('振興'))
    

    def search(self):
        search_term = self.e.get()
        result = datasource.search_sitename(search_term)
        if result:
            for i in self.youbikeTreeView.get_children():
                self.youbikeTreeView.delete(i)

            for results in result:
                self.youbikeTreeView.insert('','end',values=results)


def main():
    def update_data(w:Window)->None:
        datasource.update_sqlite_data()

        #-------------------update treeview data----------------------#
        lastest_data = datasource.lastest_datetime_data()
        w.youbikeTreeView.update_content(lastest_data)

        window.after(3*60*1000,update_data,w) #每3分鐘執行一次


    window = Window()
    window.title('台北市youbike2.0')
    window.resizable(width=False,height=False)
    update_data(window)
    window.mainloop()




if __name__ == '__main__':
    main()

