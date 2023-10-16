'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("400x250+300+300")
        self.title("Lines")

class MyFrame(tk.Frame):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


def main():    
    window = Window()
    window.mainloop()
    
if __name__ == "__main__":
    main()