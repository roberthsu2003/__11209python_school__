import tkinter as tk
from tkinter import ttk

def search_treeview():
    keyword = entry.get()
    if keyword:
        for item in tree.get_children():
            text = tree.item(item, "text")
            if keyword.lower() in text.lower():
                tree.selection_add(item)
            else:
                tree.selection_remove(item)
    else:
        for item in tree.get_children():
            tree.selection_remove(item)

root = tk.Tk()
root.title("Treeview with Search")

# 创建 Treeview
tree = ttk.Treeview(root, columns=("Name", "Age"))
tree.heading("#1", text="Name")
tree.heading("#2", text="Age")

# 添加一些示例数据
tree.insert("", "end", text="John", values=("30"))
tree.insert("", "end", text="Alice", values=("25"))
tree.insert("", "end", text="Bob", values=("35"))
tree.insert("", "end", text="Charlie", values=("28"))
tree.insert("", "end", text="David", values=("40"))

# 创建搜索框
entry = tk.Entry(root, width=30)
entry.pack()
entry.bind("<KeyRelease>", lambda event: search_treeview())

# 显示 Treeview
tree.pack()

root.mainloop()
