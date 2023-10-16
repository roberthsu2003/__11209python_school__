'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("Image")
        self.geometry("300x250")
        #self.configure(background='#E79460')

class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',padx=10,pady=10)

        #標題
        heading = ttk.Label(self,text="會員登入",font=('Helvetica',20),foreground='red')
        heading.grid(column=0, row=0, columnspan=2)

        username_label = ttk.Label(self,text="使用者名稱:",font=('Helvetica',12))
        username_label.grid(column=0,row=1,pady=10)

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1,row=1)

        password_label = ttk.Label(self,text="密碼:",font=('Helvetica',12))
        password_label.grid(column=0,row=2,sticky=tk.E,pady=10)

        password_entry = ttk.Entry(self)
        password_entry.grid(column=1,row=2)

        login_button = ttk.Button(self,text="登入")
        login_button.grid(column=1,row=3,sticky=tk.E)

       
        

    def choised(self):
        print(self.aligement.get())


def main():    
    window = Window()
    myFrame = MyFrame(window,"對齊方式")    
    window.mainloop()

if __name__ == "__main__":
    main()