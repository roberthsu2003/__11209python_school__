import tkinter as tk
import tkintermapview as tkmap


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # 建立地圖
        map_widget = tkmap.TkinterMapView(
            self,
            width=800,
            height=600,
            corner_radius=0,
        )
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        marker_1 = map_widget.set_position(23.465682, 120.757903, marker=True)  # 台北市位置
        map_widget.set_zoom(15)  # 設定顯示大小
        marker_1.set_text("🐱‍👤山上的孩子💖")


if __name__ == "__main__":
    window = Window()
    window.geometry("800x600")
    window.title("地圖")
    window.mainloop()
