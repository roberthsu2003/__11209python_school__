import tkinter as tk
import tkintermapview as tkmap

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立地圖
        map_widget = tkmap.TkinterMapView(self,
                                          width=800,
                                          height=600,
                                          corner_radius=0,
                                          )
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        marker_1 = map_widget.set_position(25.038128318756307, 121.56306490172479,marker=True) #台北市位置
        map_widget.set_zoom(13) #設定顯示大小
        marker_1.set_text("台北市中心")

        marker_2 = map_widget.set_marker(25.18390899975433, 121.41106653181126,text ="漁人碼頭",command=self.click1) #漁人碼頭
        marker_2.data = {'a':15,'b':'漁人碼頭'}

        marker_3 = map_widget.set_marker(25.255887809995677, 121.47436619812673,text ="三芝淺水灣",command=self.click2) #三芝淺水灣
        marker_3.data = {'a':18,'b':'三芝淺水灣'}

        marker_4 = map_widget.set_marker(25.295500500734974, 121.56803096187542,text ="石門港",command=self.click3) #石門港
        marker_4.data = {'a':20,'b':'石門港'}

    def click1(self,marker):
        print("click1")
        print(marker.__class__)
        print(marker.data)

    def click2(self,marker):
        print("click2")
        print(marker.__class__)
        print(marker.data)

    def click3(self,marker):
        print("click2")
        print(marker.__class__)
        print(marker.data)

if __name__ == "__main__":
    window = Window()
    window.geometry("800x600")
    window.title("地圖")
    window.mainloop()
