from tkinter import ttk

class YoubikeTreeView(ttk.Treeview):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        #-----設定欄位名稱-----#
        self.heading('sna',text='站點名稱')
        self.heading('mday',text='更新時間')
        self.heading('sarea',text='行政區')
        self.heading('ar',text='地址')
        self.heading('tot',text='總車輛數')
        self.heading('sbi',text='可借數量')
        self.heading('bemp',text='可還車')

        #-----設定欄位寬度-----#
        #語法：self.column('欄位名',width=整數數字)
        self.column('sna',width=200)
        self.column('mday',width=150)
        self.column('sarea',width=50)
        self.column('ar',width=300)
        self.column('tot',width=80)
        self.column('sbi',width=80)
        self.column('bemp',width=80)

    def update_content(self,site_datas):
        '''
        更新站點資料狀況
        '''
        #-----清除所有內容-----#
        for item in self.get_children():
            self.delete(item)

        for site in site_datas:
            self.insert('','end',values=site)