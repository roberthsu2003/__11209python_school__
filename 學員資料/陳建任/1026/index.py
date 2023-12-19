import tkinter as tk
from threading import Timer
from tkinter import messagebox
import data

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            data.SQL()
        except Exception as e:
            messagebox.showerror("錯誤",e)
            self.destroy()

t=None
def main():
    def on_close():
        print("DB已建立成功")
        t.cancel()
        window.destroy()

    def update_data():
        data.SQL()
        global t
        t=Timer(10,update_data) 
        t.start()

    window=Window()
    window.title("空氣品質監測站")
    window.geometry("300x300")
    window.resizable(width=False,height=False) 
    update_data()
    window.protocol("WM_DELETE_WINDOW",on_close)
    window.mainloop()
    
if __name__=="__main__":
    main()