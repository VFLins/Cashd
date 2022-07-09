import tkinter as tk
import tkcalendar
from tkinter import ttk
from ttkwidgets import autocomplete as tkac
from tkinter.font import Font
import db_manager as dbm

FG_COLOR_ACTIVE = "#2e2e2e"
FG_COLOR = "#55776f"
BG_COLOR = "#f7f3f3"

ACCOUNTS = [
    "Yacouba Warin", "Iskra Sho", "Ansgar Asiri", 
    "Eusebia Pawlu", "Rahul Andreas", "Rahul Andreas",
    "Debora Aline"]

# FrontPage Settings
fpage = tk.Tk()
fpage.configure(bg = BG_COLOR)
fpage.option_add("*font", "Segoe-UI 11")
fpage.title("ainda ta feio kkkkkkk")
fpage.geometry("640x480")
fpage.minsize(640, 480)

### Header Section
###################
label_logo = tk.Label(
    fpage,
    text = "Cashd",
    font = Font(weight = "bold", size = 26),
    fg = "#2e2e2e",
    bg = BG_COLOR)
label_logo.place(x = 15, rely = 0)

## Buttons
# Button Functions
def button_click_ins():
    button_toggle_insert.configure(state = tk.DISABLED, bg = FG_COLOR)
    button_toggle_accounts.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_consult.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_setting.configure(state = tk.NORMAL, bg = BG_COLOR)

    frame_accounts.place_forget()
    frame_consult.place_forget()
    frame_configure.place_forget()
    frame_insert.place(y = 50, relwidth = 1)

def button_click_acc():
    button_toggle_accounts.configure(state = tk.DISABLED, bg = FG_COLOR)
    button_toggle_insert.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_consult.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_setting.configure(state = tk.NORMAL, bg = BG_COLOR)

    frame_insert.place_forget()
    frame_consult.place_forget()
    frame_configure.place_forget()
    frame_accounts.place(y = 50, relwidth = 1)
    
def button_click_con():
    button_toggle_consult.configure(state = tk.DISABLED, bg = FG_COLOR)
    button_toggle_accounts.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_insert.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_setting.configure(state = tk.NORMAL, bg = BG_COLOR)

    frame_insert.place_forget()
    frame_accounts.place_forget()
    frame_configure.place_forget()
    frame_consult.place(y = 50, relwidth = 1)

def button_click_set():
    button_toggle_setting.configure(state = tk.DISABLED, bg = FG_COLOR)
    button_toggle_insert.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_accounts.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_consult.configure(state = tk.NORMAL, bg = BG_COLOR)
        
    frame_insert.place_forget()
    frame_accounts.place_forget()
    frame_consult.place_forget()
    frame_configure.place(y = 50, relwidth = 1)

# Button Widgets
button_toggle_insert = tk.Button(
    fpage, command = button_click_ins,
    text = "Insert",
    borderwidth = 0, font = Font(weight = "bold"),
    fg = FG_COLOR, activeforeground = BG_COLOR, disabledforeground = BG_COLOR,
    bg = BG_COLOR, activebackground = FG_COLOR)
button_toggle_insert.place(x = 150, y = 12)

button_toggle_accounts = tk.Button(
    fpage, command = button_click_acc,
    text = "Accounts",
    borderwidth = 0, font = Font(weight = "bold"),
    fg = FG_COLOR, activeforeground = BG_COLOR, disabledforeground = BG_COLOR,
    bg = BG_COLOR, activebackground = FG_COLOR)
button_toggle_accounts.place(
    in_ = button_toggle_insert, bordermode = "outside",
    anchor = "nw", relx = 1, x = 10)

button_toggle_consult = tk.Button(
    fpage, command = button_click_con,
    text = "Consult",
    borderwidth = 0, font = Font(weight = "bold"),
    fg = FG_COLOR, activeforeground = BG_COLOR, disabledforeground = BG_COLOR,
    bg = BG_COLOR, activebackground = FG_COLOR)
button_toggle_consult.place(
    in_ = button_toggle_accounts, bordermode = "outside",
    anchor = "nw", relx = 1, x = 10)

button_toggle_setting = tk.Button(
    fpage, command = button_click_set,
    text = "Settings",
    borderwidth = 0, font = Font(weight = "bold"),
    fg = FG_COLOR, activeforeground = BG_COLOR, disabledforeground = BG_COLOR,
    bg = BG_COLOR, activebackground = FG_COLOR)
button_toggle_setting.place(
    in_ = button_toggle_consult, bordermode = "outside",
    anchor = "nw", relx = 1, x = 10)

label_greet = tk.Label(
    fpage,
    text = f"Welcome to Cashd, your data is stored in:\n{dbm.WORK_DIR}",
    height = 4, anchor = "ne")
label_greet

# Separators
separator_header = ttk.Separator(fpage, orient='vertical')
separator_header.place(x = 135, y = 10, height = 30)

separator_sections = ttk.Separator(fpage, orient='horizontal')
separator_sections.place(y = 49, relwidth = 1)

### Frames
###################

## "Insert" frame
frame_insert = tk.Frame(fpage)

label_ins_account = tk.Label(
    frame_insert, text = "Account name:",
    width = 30, bg = BG_COLOR, justify = "left")
label_ins_account.pack(pady = (10, 0))

value_ins_account = tk.StringVar()
value_ins_account.set("Choose an account")

option_ins_account = tkac.AutocompleteCombobox(
    frame_insert, completevalues = ACCOUNTS, 
    background = BG_COLOR, width = 30)
option_ins_account.pack()

label_ins_date = tk.Label(
    frame_insert, text = "Transaction's date:",
    width = 30, bg = BG_COLOR, justify = "left")
label_ins_date.pack(pady = (10, 0))

date_ins = tkcalendar.DateEntry(frame_insert, width = 30)
date_ins.pack()

frame_accounts = tk.Frame(fpage)

frame_consult = tk.Frame(fpage)

frame_configure = tk.Frame(fpage)

fpage.after_idle(button_click_ins)
fpage.mainloop()
