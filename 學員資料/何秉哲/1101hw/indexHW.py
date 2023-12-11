import tkinter as tk
from tkinter import *
import tkintermapview as tkmap


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # 建立地圖
        map_widget = tkmap.TkinterMapView(self, width=800, height=600, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        myplace = map_widget.set_position(
            24.13748000027454, 121.27594971934855, marker=True
        )  # 台北市位置
        map_widget.set_zoom(8)  # 設定顯示大小
        myplace.set_text("Home")
        myplace.set_position(24.13748000027454, 121.27594971934855)


if __name__ == "__main__":
    window = Window()
    window.geometry("800x600")
    window.title("地圖")
    window.mainloop()
