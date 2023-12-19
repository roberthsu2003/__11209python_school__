import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.geometry("500x500+300+300")視窗大小
        self.title("1016上課內容")
        self.configure(background="red")

'''
class Frame(tk.Frame):
    def __init__(self,master,title, **kwargs):
        super().__init__(master=master,text=title,**kwargs)

        -畫多邊形-
        self.pack(expand=1,fill="x") 
        # expand填滿，fill：x(填滿左右)、y(填滿上下)、both(添滿整個頁面)
        canvas=tk.Canvas(self)
        canvas.create_polygon([100,50],[160,180],[13,6],[60,80]) # 填滿的多邊形
        canvas.pack()

        -畫圖片：要畫圖、線etc很多東西時-
        self.image=Image.open("bird.png")
        # 可以去google/icon找圖，記得設定Filters的Style：Material Icons，這樣才能改圖片大小
        self.bird=ImageTk.PhotoImage(self.image)
        canvas=tk.Canvas(self,width=48,height=48)
        canvas.create_image(24,24,image=self.bird,anchor=tk.CENTER)
        self.pack(expand=1,fill="both")

        -顯示圖片-
        self.image=Image.open("bird.png")
        self.bird=ImageTk.PhotoImage(self.image)
        bird_label=tk.Label(self,image=self.bird)
        bird_label.pack()
        self.pack(expand=1,fill="both")
'''
class Frame(ttk.LabelFrame):
    def __init__(self,master,title, **kwargs):
        super().__init__(master=master,text=title,**kwargs)
        '''
        -多選一表單-
        self.user=tk.StringVar(value="left") #預設選項在左邊
        ttk.Radiobutton(self,text="左邊",value="left",variable=self.user,command=self.choise).grid(column=0,row=0,padx=10) 
        #variable：預設值 command=value的值(left)會傳到choise裡面 grid=cloum欄row列
        ttk.Radiobutton(self,text="中間",value="center",variable=self.user,command=self.choise).grid(column=1,row=0,padx=10)
        ttk.Radiobutton(self,text="右邊",value="right",variable=self.user,command=self.choise).grid(column=2,row=0,padx=10)
        self.pack(padx=10,pady=10)
        
        # -簡單會員登入介面-
        # 標題
        heading=ttk.Label(self,text="會員登入",font=("Helvetica",20),foreground="black")
        heading.grid(column=0,row=0,columnspan=2,padx=10) 
        # columnspan合併儲存格

        # 輸入欄位：名稱
        username_label=ttk.Label(self,text="使用者名稱：")
        username_label.grid(column=0,row=1,sticky=tk.E,padx=10,pady=10)

        username_entry=ttk.Entry(self)
        username_entry.grid(column=1,row=1,padx=(0,10))
        
        # 輸入欄位：密碼
        password_label=ttk.Label(self,text="密碼：")
        password_label.grid(column=0,row=2,sticky=tk.E,padx=10,pady=10) 
        # sticky=tk.E 靠右(東方)對齊

        password_entry=ttk.Entry(self,show="*")
        password_entry.grid(column=1,row=2,padx=(0,10))

        # 登入按鈕
        login_buttpm=ttk.Button(self,text="登入")
        login_buttpm.grid(column=0,row=3,columnspan=2,sticky=tk.E,padx=10,pady=10)

        self.pack(expand=1,fill="both",padx=10,pady=20)
        '''

        self.tree=ttk.Treeview(self,columns=["#1","#2","#3"],show="headings")
        self.tree.heading("#1",text="表格1")
        self.tree.heading("#2",text="表格2")
        self.tree.heading("#3",text="表格3")

        text=[]
        for i in range(1,100):
            text.append([f"first{i}",f"last{i}",f"email{i}@gamil.com"])
        
        for t in text:
            self.tree.insert("",tk.END,values=t)
        
        self.tree.pack()

        self.tree.bind("<<TreeviewSelect>>",self.item)

        self.pack(expand=1,fill="both",padx=10,pady=20)
    
    def item(self,event):
        item_id=self.tree.selection()[0]
        item_dict=self.tree.item(item_id)
        item_values=item_dict["values"]

    def choise(self):
        print(self.user.get())

def main():
    window=Window()
    frame=Frame(window,"對齊方式")
    '''
    -畫多邊形&圖片用的-
    frame=Frame(window)  
    master=window。因為Frame第一個是master，所以可以直接(按順序)打想要輸入的值(window) 
    
    -更改表單樣式-
    s=ttk.Style()
    # print(s.theme_names()) # 關掉視窗後終端機會顯示哪些表單樣式可以用('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
    s.theme_use('default')# 關掉視窗後終端機會顯示vista
    '''


    window.mainloop()

if __name__ == "__main__":
    main()