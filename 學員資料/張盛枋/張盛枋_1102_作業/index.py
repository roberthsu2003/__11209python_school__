# pip install tkintermapview
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
        marker_1 = map_widget.set_position(25.0412414862223, 121.56716571249191,marker=True, command=self.click0) #捷運市政府站-4號出口
        map_widget.set_zoom(13)     #設定顯示大小
        marker_1.set_text("捷運市政府站-4號出口")
        marker_1.data = {'捷運市政府站-4號出口'}

        marker_2 = map_widget.set_marker(25.0400789656165, 121.57210419914509,text ="松山工農",command=self.click1) #松山工農
        marker_2.data = {'松山工農'}
        marker_3 = map_widget.set_marker(25.03442299125834, 121.56400897897782,text ="台北101",command=self.click2) #台北101
        marker_3.data = {'台北101'}

    def click0(self,marker):
        print("click0")
        print(marker.__class__)
        print(marker.data)
    
    def click1(self,marker):
        print("click1")
        print(marker.__class__)
        print(marker.data)

    def click2(self,marker):
        print("click2")
        print(marker.__class__)
        print(marker.data)

if __name__ == "__main__":
    window = Window()
    window.geometry("800x600")
    window.title("地圖")
    window.mainloop()