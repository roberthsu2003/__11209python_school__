import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource          
from threading import Timer


class Window(tk.Tk):      
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        try:
            datasource.updata_sqlite_data()        
        except Exception:
            messagebox.showerror("錯誤",'網路不正常\n將關閉應用程式\n請稍後再試')       
            self.destroy() 
    
t = None  
def main():
    def on_closing():         
        print('window關閉')
        t.cancel()
        window.destroy()      

    
    def update_data()->None:
        datasource.updata_sqlite_data()
        global t                 
        t = Timer(3600,update_data)  
        t.start()



    window = Window()
    window.title('台北市空氣品質')
    window.geometry('300x300')                  
    window.resizable(width=False,height=False)  
    update_data()
    window.protocol("WM_DELETE_WINDOW",on_closing)  
    window.mainloop()




if __name__ =='__main__':
    main()