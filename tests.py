import csv
from tkinter import *
from tkinter import ttk

with open('C:\\Users\\Dercio\\Documents\\GitHub\\Cashd\\data\\fake_dataset.csv', newline='', encoding="ISO 8859-1") as f:
    reader = csv.reader(f, delimiter = ";")
    ACCOUNTS = [tuple(row) for row in reader]


fpage = Tk()
fpage.geometry("640x480")
fpage.minsize(640, 480)

acc_table_view = ttk.Treeview(fpage)
acc_table_view["columns"] = [
    "Code", "Name", "Id", "Phone", "Email", "Street", "Number", "Zip Code", "City"]
#labels for the table view
acc_table_view.column("#0", width = 100, minwidth = 20)
for col in acc_table_view["columns"]:
    acc_table_view.column(col, width = 80, minwidth = 20, anchor = W)
#headings for the table view
acc_table_view.heading("#0", text = "", anchor = W)
for col in acc_table_view["columns"]:
    acc_table_view.heading(col, text = col, anchor = W)
#adding data on the table
for idx, val in enumerate(ACCOUNTS):
    acc_table_view.insert(
        parent = "", 
        index = "end", 
        iid = idx, 
        text = "eae guei", 
        values = val)
acc_table_view.pack(pady=50)

fpage.mainloop()