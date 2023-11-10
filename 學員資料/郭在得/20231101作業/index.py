import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource
from youbikeTreeView import YoubikeTreeView
from threading import Timer

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        try:
            datasource.updata_sqlite_data()
        except Exception:
            messagebox.showerror("錯誤",'網路不正常\n將關閉應用程式\n請稍後再試')
            self.destroy()
        # 建立介面
        # print(datasource.lastest_datetime_data())
        topFrame=tk.Frame(self,relief=tk.GROOVE,borderwidth=2)
        tk.Label(topFrame,text="台北市youbike及時資料",font=("arial",20),bg="#333333",fg="#ffffff").pack(padx=20,pady=20)
        topFrame.pack(pady=30)

        # 搜尋
        searchFrame = tk.Frame(self)
        tk.Label(searchFrame, text="搜尋：").pack(side="left", padx=5, pady=10)
        self.e = tk.StringVar()
        tk.Entry(searchFrame, width=40, textvariable=self.e).pack(side="left")
        searchButton = tk.Button(searchFrame, text="執行", state="normal", command=self.perform_search)
        searchButton.pack(side="right")
        searchFrame.pack()

        # 建立treeview
        bottomFrame=tk.Frame(self)
        self.youbikeTreeView= YoubikeTreeView(bottomFrame,show="headings",columns=('sna','mday','sarea','ar','tot','sbi','bemp'))
        self.youbikeTreeView.pack(side="left")
        vsb=ttk.Scrollbar(bottomFrame,orient="vertical",command=self.youbikeTreeView.yview)
        vsb.pack(side="left",fill="y")
        self.youbikeTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=10)

    def perform_search(self):
        search_query = self.e.get()
        search_results = datasource.search_sitename(search_query)
        if search_results:
            for i in self.youbikeTreeView.get_children():
                self.youbikeTreeView.delete(i)
            for result in search_results:
                self.youbikeTreeView.insert("", "end", values=result)

        self.e.set("")

def main(): 
    def update_data(w:Window)->None:
        datasource.updata_sqlite_data()
        last_data=datasource.lastest_datetime_data()
        w.youbikeTreeView.update_content(last_data)
        window.after(3*60*1000,update_data,w)
          
    window = Window()
    window.title('台北市youbike2.0')
    # window.geometry('600x300')
    window.resizable(width=False,height=False)
    update_data(window)          
    window.mainloop()

if __name__ == '__main__':
    main()