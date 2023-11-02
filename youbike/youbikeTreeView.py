from tkinter import ttk
from tkinter.simpledialog import Dialog

class YoubikeTreeView(ttk.Treeview):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        self.parent = parent
        #------設定欄位名稱---------------
        self.heading('sna',text='站點名稱')
        self.heading('mday',text='更新時間')
        self.heading('sarea',text='行政區')
        self.heading('ar',text='地址')
        self.heading('tot',text='總車輛數')
        self.heading('sbi',text='可借')
        self.heading('bemp',text='可還')

        #----------設定欄位寬度------------
        self.column('sna',width=200)
        self.column('mday',width=150)
        self.column('sarea',width=50)
        self.column('ar',width=300)
        self.column('tot',width=50)
        self.column('sbi',width=50)
        self.column('bemp',width=50)

        #----------bind button1-------
        self.bind('<ButtonRelease-1>', self.selectedItem)

    def update_content(self,site_datas):
        '''
        更新內容
        '''
        #清除所有內容
        for i in self.get_children():
            self.delete(i)
        
        for index,site in enumerate(site_datas):
            self.insert('','end',text=f"abc{index}",values=site)


    def selectedItem(self,event):
        selectedItem = self.focus()
        print(selectedItem)
        data_dict = self.item(selectedItem)
        data_list = data_dict['values']
        title = data_list[0]
        detail = ShowDetail(self.parent,title=title)
        


class ShowDetail(Dialog):
    pass        