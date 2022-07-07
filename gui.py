import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import db_manager as dbm


class FrontPage:
    FG_COLOR_ACTIVE = "#2e2e2e"
    FG_COLOR = "#55776f"
    BG_COLOR = "#f7f3f3"

    # FrontPage Settings
    fpage = tk.Tk()
    fpage.configure(bg = BG_COLOR)
    fpage.option_add("*font", "Segoe-UI 11")
    fpage.title("ainda ta feio kkkkkkk")
    fpage.geometry("640x480")
    fpage.minsize(640, 480)

    ### Header Section
    label_logo = tk.Label(
        fpage,
        text = "Cashd",
        font = Font(weight = "bold", size = 26),
        fg = "#2e2e2e",
        bg = BG_COLOR)
    label_logo.place(x = 15, rely = 0)

    ### Buttons
    # Button Functions
    def button_click_ins():
        button_toggle_insert

    # Button Widgets
    button_toggle_insert = tk.Button(
        fpage,
        text = "Insert",
        command = button_click_ins,
        borderwidth = 0,
        font = Font(weight = "bold"),
        fg = FG_COLOR, activeforeground = FG_COLOR_ACTIVE,
        bg = BG_COLOR, activebackground = BG_COLOR)
    button_toggle_insert.place(x = 150, y = 12)

    button_toggle_consult = tk.Button(
        fpage,
        text = "Consult",
        borderwidth = 0,
        font = Font(weight = "bold"),
        fg = FG_COLOR, activeforeground = FG_COLOR_ACTIVE,
        bg = BG_COLOR, activebackground = BG_COLOR)
    button_toggle_consult.place(x = 215, y = 12)

    button_toggle_setting = tk.Button(
        fpage,
        text = "Settings",
        borderwidth = 0,
        font = Font(weight = "bold"),
        fg = FG_COLOR, activeforeground = FG_COLOR_ACTIVE, disabledforeground = FG_COLOR_ACTIVE,
        bg = BG_COLOR, activebackground = BG_COLOR)
    button_toggle_setting.place(x = 300, y = 12)

    # Separators
    separator_header = ttk.Separator(fpage, orient='vertical')
    separator_header.place(x = 135, y = 10, height = 30)

    separator_sections = ttk.Separator(fpage, orient='horizontal')
    separator_sections.place(y = 50, relwidth = 1)

    ### Functions
    

    label_greet = tk.Label(
        fpage,
        text = f"Welcome to Cashd, your data is stored in:\n{dbm.WORK_DIR}",
        height = 4, anchor = "ne")
    label_greet


    fpage.mainloop()
    