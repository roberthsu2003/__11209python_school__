import dataSource
import tkinter as tk
from tkinter import ttk

def main():
    window = tk.Tk()
    window.title("鄉鎮人口統計")
    label = ttk.Label(window,text="鄉鎮人口統計",font=('Helvetica', '30'))
    label.pack(padx=100,pady=50)
    window.mainloop()
    

if __name__ == "__main__":
    main()