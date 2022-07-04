import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import db_manager as dbm

def button1_click(self):
        with FrontPage() as fp:
            entry1_input = fp.entry1.get()
            FrontPage.label_entry1(text = entry1_input)

class FrontPage:
    fpage = tk.Tk()
    fpage.option_add("*font", "Segoe-UI 11")
    fpage.geometry("640x480")
    fpage.minsize(640, 480)

    label_logo = tk.Label(
        fpage,
        text = "Cashd",
        font = Font(weight = "bold", size = 26))
    label_logo.place(relx = 0, rely = 0)

    separator_header = ttk.Separator(fpage, orient='vertical')
    
    label_greet = tk.Label(
        fpage,
        text = f"Welcome to Cashd, your data is stored in:\n{dbm.WORK_DIR}",
        height = 4, anchor = "nw")
    label_greet.place()

    label_entry1 = tk.Label(
        fpage,
        text = "Type Something there:",
        justify = "left")

    entry1 = tk.Entry(fpage)

    button1 = tk.Button(
        fpage,
        text = "Do magic", command = button1_click)
    
    fpage.mainloop()