import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import db_manager as dbm

def button_click_ins():
    FrontPage()

class FrontPage:
    #FPage Settings
    fpage = tk.Tk()
    fpage.option_add("*font", "Segoe-UI 11")
    fpage.title("ainda ta feio kkkkkkk")
    fpage.geometry("640x480")
    fpage.minsize(640, 480)

    label_logo = tk.Label(
        fpage,
        text = "Cashd",
        font = Font(weight = "bold", size = 26))
    label_logo.place(x = 15, rely = 0)

    separator_header = ttk.Separator(fpage, orient='vertical')
    separator_header.place(x = 130, y = 10, height = 30)

    label_greet = tk.Label(
        fpage,
        text = f"Welcome to Cashd, your data is stored in:\n{dbm.WORK_DIR}",
        height = 4, anchor = "ne")
    label_greet.place(x = 135, y = 3)

    separator_sections = ttk.Separator(fpage, orient='horizontal')
    separator_sections.place(y = 80, relwidth = 1)

    button_toggle_insert = tk.Button(
        fpage,
        text = "Insert",
        borderwidth = 0,
        font = Font(weight = "bold"))
    button_toggle_insert.place(x = 30, y = 50)

    button_toggle_consult = tk.Button(
        fpage,
        text = "Consult",
        borderwidth = 0,
        font = Font(weight = "bold"))
    button_toggle_consult.place(x = 110, y = 50)
    
    fpage.mainloop()
    