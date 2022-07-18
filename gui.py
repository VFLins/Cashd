import csv
import tkinter as tk
import tkcalendar
from os import getcwd
from tkinter import ttk
from ttkwidgets import autocomplete as tkac
from tkinter.font import Font
import db_manager as dbm

FG_COLOR_ACTIVE = "#2e2e2e"
FG_COLOR = "#2e5077"
BG_COLOR = "white"


with open(f"{getcwd()}\\data\\random_names.csv", newline='') as f:
    reader = csv.reader(f)
    ACCOUNTS = [str(row) for row in reader]

# FrontPage Settings
fpage = tk.Tk()
fpage.configure(bg = BG_COLOR)
fpage.option_add("*font", "Segoe-UI 14")
fpage.title("não está mais tão feio")
fpage.geometry("640x480")
fpage.minsize(640, 480)

### Header Section
###################
label_logo = tk.Label(
    fpage,
    text = "Cashd",
    font = Font(weight = "bold", size = 32),
    fg = "#2e2e2e",
    bg = BG_COLOR)
label_logo.place(x = 15)

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
    frame_insert.place(y = 56, relwidth = 1, relheight = 1)

def button_click_acc():
    button_toggle_accounts.configure(state = tk.DISABLED, bg = FG_COLOR)
    button_toggle_insert.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_consult.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_setting.configure(state = tk.NORMAL, bg = BG_COLOR)

    frame_insert.place_forget()
    frame_consult.place_forget()
    frame_configure.place_forget()
    frame_accounts.place(y = 56, relwidth = 1, relheight = 1)
    
def button_click_con():
    button_toggle_consult.configure(state = tk.DISABLED, bg = FG_COLOR)
    button_toggle_accounts.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_insert.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_setting.configure(state = tk.NORMAL, bg = BG_COLOR)

    frame_insert.place_forget()
    frame_accounts.place_forget()
    frame_configure.place_forget()
    frame_consult.place(y = 56, relwidth = 1, relheight = 1)

def button_click_set():
    button_toggle_setting.configure(state = tk.DISABLED, bg = FG_COLOR)
    button_toggle_insert.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_accounts.configure(state = tk.NORMAL, bg = BG_COLOR)
    button_toggle_consult.configure(state = tk.NORMAL, bg = BG_COLOR)
        
    frame_insert.place_forget()
    frame_accounts.place_forget()
    frame_consult.place_forget()
    frame_configure.place(y = 56, relwidth = 1, relheight = 1)

# Button Widgets
button_toggle_insert = tk.Button(
    fpage, command = button_click_ins,
    text = "Insert",
    borderwidth = 0, font = Font(weight = "bold", size = 16),
    fg = FG_COLOR, activeforeground = BG_COLOR, disabledforeground = BG_COLOR,
    bg = BG_COLOR, activebackground = FG_COLOR)
button_toggle_insert.place(
    in_ = label_logo, bordermode = "outside",
    anchor = "nw", relx = 1, x = 20, y = 8)

button_toggle_accounts = tk.Button(
    fpage, command = button_click_acc,
    text = "Accounts",
    borderwidth = 0, font = Font(weight = "bold", size = 16),
    fg = FG_COLOR, activeforeground = BG_COLOR, disabledforeground = BG_COLOR,
    bg = BG_COLOR, activebackground = FG_COLOR)
button_toggle_accounts.place(
    in_ = button_toggle_insert, bordermode = "outside",
    anchor = "nw", relx = 1, x = 10)

button_toggle_consult = tk.Button(
    fpage, command = button_click_con,
    text = "Consult",
    borderwidth = 0, font = Font(weight = "bold", size = 16),
    fg = FG_COLOR, activeforeground = BG_COLOR, disabledforeground = BG_COLOR,
    bg = BG_COLOR, activebackground = FG_COLOR)
button_toggle_consult.place(
    in_ = button_toggle_accounts, bordermode = "outside",
    anchor = "nw", relx = 1, x = 10)

button_toggle_setting = tk.Button(
    fpage, command = button_click_set,
    text = "Settings",
    borderwidth = 0, font = Font(weight = "bold", size = 16),
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
separator_header.place(
    in_ = label_logo, bordermode = "outside", height = 30,
    anchor = "nw", relx = 1, x = 6, y = 12)

separator_sections = ttk.Separator(fpage, orient='horizontal')
separator_sections.place(y = 54, relwidth = 1)

### Frames
###################

## "Insert" frame
frame_insert = tk.Frame(fpage)

ins_label_account = tk.Label(
    frame_insert, text = "Account name:",
    width = 30, justify = "left")
ins_label_account.pack(pady = (10, 0))

ins_option_account = tkac.AutocompleteCombobox(
    frame_insert, completevalues = ACCOUNTS, width = 30)
ins_option_account.pack()

ins_label_date = tk.Label(
    frame_insert, text = "Transaction's date:",
    width = 30, justify = "left")
ins_label_date.pack(pady = (10, 0))

ins_option_date = tkcalendar.DateEntry(
    frame_insert, width = 30, relief = "solid",
    background = FG_COLOR, selectbackground = FG_COLOR)
ins_option_date.pack()

ins_label_value = tk.Label(
    frame_insert, text = "Value (positive for income):",
    width = 30, justify = "left")
ins_label_value.pack(pady = (10, 0))
ins_label_value.pack(pady = (10, 0))

ins_option_value = tk.Entry(
    frame_insert, text = "0000,00",
    width = 32, relief = "solid")
ins_option_value.insert(0, "0,00")
ins_option_value.pack()

ins_ok_button = tk.Button(frame_insert, text = "Confirm")
ins_ok_button.place(
    in_ = ins_option_value, bordermode = "outside",
    anchor = "se", relx = 1, rely = 1, y = 50)

ins_clear_button = tk.Button(frame_insert, text = "Clear")
ins_clear_button.place(
    in_ = ins_ok_button, bordermode = "outside",
    anchor = "e", relx = 0, x = -5, rely = 0.5)

frame_accounts = tk.Frame(fpage)

acc_label_account = tk.Label(
    frame_accounts, text = "Accounts:",
    width = 30, justify = "left")
acc_label_account.pack(pady = (10, 0))


frame_consult = tk.Frame(fpage)

frame_configure = tk.Frame(fpage)

fpage.after_idle(button_click_ins)
fpage.mainloop()
