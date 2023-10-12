import dataSource
import tkinter as tk
from tkinter import ttk

def main():
    window = tk.Tk()
    window.title("這是我的第一個視窗")
    label = tk.Label(window,text="Hello! Tkinter!",font=('Helvetica', '30'))
    label.pack(padx=100,pady=50)
    window.mainloop()
    

if __name__ == "__main__":
    main()