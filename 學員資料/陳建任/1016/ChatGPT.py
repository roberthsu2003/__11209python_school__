import tkinter as tk
from tkinter import ttk, filedialog, simpledialog
import csv

class CSVViewer:
    def __init__(self, root):
        self.root = root
        self.root.title('CSV Viewer')
        self.tree = self.create_treeview()
        self.load_csv()

    def create_treeview(self):
        tree = ttk.Treeview(self.root, columns=[1, 2, 3, 4, 5, 6, 7], show='headings')
        tree.heading(1, text='日期')
        tree.heading(2, text='開盤價')
        tree.heading(3, text='盤中最高價')
        tree.heading(4, text='盤中最低價')
        tree.heading(5, text='收盤價')
        tree.heading(6, text='調整後收盤價')
        tree.heading(7, text='成交量')
        tree.pack(fill=tk.BOTH, expand=True)
        return tree

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip header row
                for row in csv_reader:
                    self.tree.insert('', tk.END, values=row)
        else:
            # Handle file not selected
            self.root.destroy()

    def show_popup(self, values):
        result = simpledialog.askstring("Selected Row", "\n".join(values))
        print("User entered:", result)

def main():
    root = tk.Tk()
    viewer = CSVViewer(root)
    root.mainloop()

if __name__ == '__main__':
    main()
