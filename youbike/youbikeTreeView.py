from tkinter import ttk

class YoubikeTreeView(ttk.Treeview):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        #------設定欄位名稱---------------
        self.heading('sna',text='站點名稱')
        self.heading('mday',text='更新時間')
        self.heading('sarea',text='行政區')
        self.heading('ar',text='地址')
        self.heading('tot',text='總車輛數')
        self.heading('sbi',text='可借')
        self.heading('bemp',text='可還')

        #----------設定欄位寬度------------
        self.column('sna',width=120)
        self.column('mday',width=150)
        self.column('sarea',width=50)
        self.column('ar',width=250)
        self.column('tot',width=50)
        self.column('sbi',width=50)
        self.column('bemp',width=50)

    def update_content(self,site_datas):
        print(site_datas)



        