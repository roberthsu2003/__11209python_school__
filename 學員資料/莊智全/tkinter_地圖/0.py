import tkinter as tk
import tkintermapview as tkmap

class window(tk.Tk):
    def __init__(self):
        super().__init__()
        


class WinPos(tk.Tk):           # 經緯度定位展現圖之預覽
    def __init__(self):
        super().__init__()
        pmap_widget=tkmap.TkinterMapView(self, width=800, height=600, corner_radius=0)
        pmap_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        pmap_widget.set_position(25.057754658977288, 121.54325064288345)  #台北市
        pmap_widget.set_zoom(15)  #設定顯示大小
        

class WinMap(tk.Tk):           # 依輸入文字, 定位展現圖之預覽
    def __init__(self):
        super().__init__()
        amap_widget=tkmap.TkinterMapView(self, width=800, height=600, corner_radius=0)
        amap_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        amap_widget.set_address('Taipei City ,Taiwan')  #台北市位置
        amap_widget.set_zoom(15)



if __name__=="__main__":
    winPos=WinPos()
    winPos.geometry("800x600")
    winPos.title('MAP')
    winPos.mainloop()