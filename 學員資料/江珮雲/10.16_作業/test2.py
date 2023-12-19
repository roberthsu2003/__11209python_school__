import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
import csv

class StockApp(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("股票資料")

class GetStockDataDialog(Dialog):
    def body(self, master):
        super().__init__(master)
        self.title("個股資料")

        tk.Label(master, text='日期').grid(row=0, column=1, sticky=tk.W)
        tk.Label(master, text='開盤價').grid(row=1, column=1, sticky=tk.W)
        tk.Label(master, text='最高價').grid(row=2, column=1, sticky=tk.W)
        tk.Label(master, text='最低價').grid(row=3, column=1, sticky=tk.W)
        tk.Label(master, text='收市價').grid(row=4, column=1, sticky=tk.W)
        tk.Label(master, text='收盤價').grid(row=5, column=1, sticky=tk.W)
        tk.Label(master, text='成交量').grid(row=6, column=1, sticky=tk.W)

        self.date = tk.Label(master, width=16, show='*', sticky=tk.E)
        self.open = tk.Label(master, width=16, show='*', sticky=tk.E)
        self.high = tk.Label(master, width=16, show='*', sticky=tk.E)
        self.low = tk.Label(master, width=16, show='*', sticky=tk.E)
        self.close = tk.Label(master, width=16, show='*', sticky=tk.E)
        self.adj_close = tk.Label(master, width=16, show='*', sticky=tk.E)
        self.volume = tk.Label(master, width=16, show='*', sticky=tk.E)
        return self.date

class StockFrame(tk.LabelFrame):
    def __init__(self, master, title, csv_filename, **kwargs):
        super().__init__(master, text=title, **kwargs)
        self.pack(expand=1, fill='both', padx=10, pady=10)
        scrollbar = ttk.Scrollbar(self, orient='vertical')
        scrollbar.pack(side='right', fill='y')

        self.field = ttk.Treeview(self, columns=['#1', '#2', '#3', '#4', '#5', '#6', '#7'], show="headings")

        self.field.heading('#1', text="Date")
        self.field.heading('#2', text="Open")
        self.field.heading('#3', text="High")
        self.field.heading('#4', text="Low")
        self.field.heading('#5', text="Close")
        self.field.heading('#6', text="Adj Close")
        self.field.heading('#7', text="Volume")

        with open(csv_filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for contact in csv_reader:
                self.field.insert('', tk.END, values=list(contact.values()))

        self.field.pack()
        self.field.bind('<<TreeviewSelect>>', self.item_selected)

    def item_selected(self, event):
        item_id = self.field.selection()[0]
        item_dict = self.field.item(item_id)
        print(item_dict['values'])
        dialog = GetStockDataDialog(self, title="個股資料")

def main():
    window = StockApp()
    frame = StockFrame(window, "股票資料", csv_filename='台積電.csv')
    window.mainloop()

if __name__ == "__main__":
    main()
