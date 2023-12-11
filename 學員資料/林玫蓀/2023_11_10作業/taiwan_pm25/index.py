import tkinter as tk
from tkinter import messagebox
import datasource          
from threading import Timer
import datasource
import psycopg2

class Window(tk.Tk):      
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        try:
            datasource.updata_pm25_data()
        except Exception:
            messagebox.showerror("錯誤",'網路不正常\n將關閉應用程式\n請稍後再試')       
            self.destroy() 
    
t = None  
def main():
    #def on_closing():         
    #    print('window關閉')
    #    t.cancel()
    #    window.destroy()      

    
    def update_data(w:Window)->None:
        datasource.updata_pm25_data()
        window.after(60*60*1000,update_data,w)
        #t = Timer(5*60, update_data, args=(window,))
        #t.start()
        


    window = Window()
    window.title('台灣PM2.5')
    window.geometry('300x300')                  
    window.resizable(width=False,height=False)  
    update_data(window)
    #window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()


if __name__ =='__main__':
    main()