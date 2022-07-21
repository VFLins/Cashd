import csv
from tkinter import *
from tkinter import ttk

with open('C:\\Users\\Dercio\\Documents\\GitHub\\Cashd\\data\\fake_dataset.csv', newline='', encoding="ISO 8859-1") as f:
    reader = csv.reader(f, delimiter = ";")
    ACCOUNTS = [tuple(row) for row in reader]
ACCOUNTS_NAMES = [x[1] for x in ACCOUNTS]
print(ACCOUNTS_NAMES)

