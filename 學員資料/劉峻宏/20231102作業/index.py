import tkinter as tk
import tkintermapview as tkmap

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        map_widget = tkmap.TkinterMapView(self, width=800, height=600, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        marker = map_widget.set_position(25.03017973701443, 121.5362208630154, marker=True)
        map_widget.set_zoom(15)
        marker.set_text("")
        
if __name__ == '__main__':
    window = Window()
    window.geometry("800x600")
    window.title("地圖")
    window.mainloop()