from tkinter import ttk



class YoubikeTreeView(ttk.Treeview):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # ------設定欄位名稱---------------
        self.heading('sna', text='站點名稱')
        self.heading('mday', text='更新時間')
        self.heading('sarea', text='行政區')
        self.heading('ar', text='地址')
        self.heading('tot', text='總車輛數')
        self.heading('sbi', text='可借')
        self.heading('bemp', text='可還')

        # ----------設定欄位寬度------------
        self.column('sna', minwidth=0)
        self.column('mday', minwidth=0)
        self.column('sarea', minwidth=0)
        self.column('ar', minwidth=0)
        self.column('tot', minwidth=0)
        self.column('sbi', minwidth=0)
        self.column('bemp', minwidth=0)

    def update_content(self, site_datas):
        '''
        更新內容
        '''
        for i in self.get_children():
            self.delete(i)

        for site in site_datas:
            self.insert('', 'end', values=site)

