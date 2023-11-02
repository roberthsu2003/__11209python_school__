from tkinter import ttk

class YoubikeTreeView(ttk.Treeview):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        self.heading('sna',text='站點名稱')
        self.heading('mday',text='更新時間')
        self.heading('sarea',text='行政區')
        self.heading('ar',text='地址')
        self.heading('tot',text='總車輛數')
        self.heading('sbi',text='可借')
        self.heading('bemp',text='可還')


        self.column('sna',width=240)
        self.column('mday',width=160)
        self.column('sarea',width=60)
        self.column('ar',width=270)
        self.column('tot',width=80)
        self.column('sbi',width=60)
        self.column('bemp',width=60)


    def update_content(self,site_datas):
        '''
        更新內容
        '''

        for i in self.get_children():
            self.delete(i)
        
        for site in site_datas:
            self.insert('','end',values=site)