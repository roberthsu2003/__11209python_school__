import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        try:
            datasource.updata_sqlite_data()
        except Exception:
            messagebox.showerror("錯誤",'網路不正常\n將關閉應用程式\n請稍後再試')
            self.destroy()

        
        

def main():
    window = Window()
    window.title('台北市youbike2.0')
    window.geometry('600x300')
    window.resizable(width=False,height=False)    
    window.mainloop()

if __name__ == '__main__':
    main()