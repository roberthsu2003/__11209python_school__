import tkinter as tk
import tkintermapview as tkmap

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立地圖
        map_widget = tkmap.TkinterMapView(self,
                                          width=800,
                                          height=600,
                                          corner_radius=0
                                          )
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        map_widget.set_position(25.04781739462304, 121.51733109484061) #台北車站位置
        map_widget.set_zoom(15) #設定顯示大小


if __name__ == "__main__":
    window = Window()
    window.geometry("800x600")
    window.title("地圖")
    window.mainloop()
