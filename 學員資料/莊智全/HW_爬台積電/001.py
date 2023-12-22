import tkinter as tk
from tkinter import ttk

#class Window(tk.Tk):
    #def __init__(self,**kwargs):
        #super().__init__(**kwargs)
        #self.geometry("400x300")
        #self.title("NEW")
        #self.configure(background='#F19483')

class Window(tk.Tk):                                                   #  自訂calss 繼承自 tk.TK 
    def __init__(self,**kwargs):                                        # **kwargs =>表示所有參數繼承
        super().__init__(**kwargs)                                       #   **kwargs =>表示  繼承的   所有參數 解密
        self.geometry("400x250+300+300")                                 #  繼承後   屬性 self.geometry
        self.title("Lines")                                               #  繼承後   屬性
        self.configure(background='#E79460')      


#class MyFrame(tk.Frame):
    #def __init__(self, master, **kwargs):
        #super().__init__(master, **kwargs)
        #self.configure(background='#854836')
        #canvas=tk.Canvas(self)
        #canvas.create_line(150,300,450,300)
        #canvas.create_line(20,20,100,20,60,50,20,20)
        #canvas.pack(expand=1,fill='both')
        #self.pack(expand=1,fill='both')

class MyFrame(tk.Frame):                                            # 自訂 框架 calss 繼承自 tk.Frame
    def __init__(self,master,**kwargs):                             #  
        super().__init__(master,**kwargs)                            #  繼承  所有屬性
        self.configure(background='#9E7A7A')  
        canvas = tk.Canvas(self)                                     # 引入 tk模組的 Canvas Class 給self用 [在 MyFrame 下自用]   canvas(畫布)實體化
        canvas.create_line(15, 30, 200, 30)                           # 
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        canvas.pack(expand=1,fill='both')                       #  繼承後   屬性
        self.pack(expand=1, fill='both')   



#def main():    
    #window = Window()                                              # class 實體化
    #myFrame = MyFrame(window)                                       # 將 MyFrame 放到 window 裡   
    #window.mainloop()



def main():
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()



if __name__ == "__main__":
    main()

