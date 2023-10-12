import dataSource
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("鄉鎮人口統計")
        self.configure(background='#CB1B45')

        topFrame = tk.Frame(self,background='#B19693')
        label = ttk.Label(topFrame,text="鄉鎮人口統計",font=('Helvetica', '30'))
        label.pack(padx=100,pady=50)
        topFrame.pack()

        bottomFrame = tk.Frame(self,background='#B9887D')
        choices = ["apple", "orange", "banana"]
        choicesvar = tk.StringVar(value=choices)
        listbox = tk.Listbox(bottomFrame,listvariable=choicesvar)
        listbox.pack()
        bottomFrame.pack(expand=True,fill='x')


def main():
    window = Window()    
    window.mainloop()
    

if __name__ == "__main__":
    main()