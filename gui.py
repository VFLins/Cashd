import tkinter as tk
from tkinter.font import Font
import db_manager as dbm

def button1_click():
    with FrontPage() as fp:
        fp.label_entry1.text = fp.entry1.get()

class FrontPage:
    window = tk.Tk()
    window.geometry("640x480")
    label_temp = tk.Label(text = "mostrando essa janela só pra testar uma coisa kkkkkkkkkkk").pack()
    label_greet = tk.Label(
        text = f"Welcome to Cashd, your data is stored in:\n{dbm.WORK_DIR}",
        height = 4,
        justify = "left",
        font = Font(size=12, slant = "roman"))

    label_entry1 = tk.Label(
        text = "Type Something there:",
        justify = "left").pack()

    entry1 = tk.Entry().pack()

    button1 = tk.Button(
        text = "Do magic", command = button1_click).pack()

    window.mainloop()
