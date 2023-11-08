import tkinter as tk#匯入tkinter視窗模組，簡寫為tk
import tkintermapview as tkmap #匯入tkinter map view，簡寫為tkmap


class Window(tk.Tk):
    def __init__(self):
        '''
        建立視窗
        '''
        super().__init__()
        #-----建立地圖視窗-----#
        map_widget=tkmap.TkinterMapView(self,width=800,height=600,corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        map_widget.set_zoom(8) #設定顯示大小，範圍為0到19，其中19為最精細顯示
        
        #使用經緯度座標顯示地圖-高手保齡球館位置
        #map_widget.set_position(25.022340588185052, 121.47942218061716) #高手保齡球館位置
        
        #使用城市名稱標示地圖-台南市
        #map_widget.set_address('Tainan city, Taiwan') #台南市
        
        #製作一個標示位置-關西服務站
        service_Guanxi=map_widget.set_position(24.80132251222446, 121.19250776891039,marker=True)
        service_Guanxi.set_text('國道3號-關西服務區')
        
        '''
        重新執行標示位置
        service_Guanxi.set_position(25.022340588185052, 121.47942218061716) #如果前面有已執行定位點標記，則後面set_position的新座標點會取代已執行的標記點
        '''

        #製作多個標示位置-國道三號休息站
        service_xihu=map_widget.set_marker(24.56529817891379, 120.76086913762678,text='國道3號-西湖服務區')
        service_Qingshui=map_widget.set_marker(24.281449112188884, 120.6014142106016,text='國道3號-清水服務區')

        #設定標示位置文字顏色-text_color='色號'
        service_Nantou=map_widget.set_marker(23.899673930067426, 120.71043408175095,text='國道3號-南投服務區',text_color='#24936E')

        #設定標示圖標
        # 內圈：marker_color_circle='色號/顏色'
        # 外圈：marker_color_outside='色號/顏色'
        service_Gukeng=map_widget.set_marker(23.609407146139468, 120.54458035649537,text='國道3號-古坑服務區',marker_color_circle='#FEDFE1',marker_color_outside='black')

        #設定點選後吐出值
        service_Dongshan=map_widget.set_marker(23.286768450223214, 120.39850203754699,text='國道3號-東山服務區',command=self.click1)
        service_Dongshan.data={1:'休息區',2:'東山有個張鍚銘'}

        #在標示上顯示圖片-這部份還沒讓我試出來
        service_Guanmiao=map_widget.set_marker(22.92935429985622, 120.35258712141908,text='國道3號-關廟服務區',marker_color_circle='green')
        

        
    #套用點選地圖吐出數值的方法
    def click1(self,marker):
        print("click1")
        print(marker.__class__)
        print(marker.data)


    
if __name__ == "__main__":
    window=Window() #呼叫“Window”class
    window.geometry('800x600') #設定視窗大小為800x600
    window.title('地圖視窗')
    window.mainloop()
