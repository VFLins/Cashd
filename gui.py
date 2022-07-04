import tkinter as tk
from tkinter.font import Font
import db_manager as dbm

class FrontPage:
    window = tk.Tk()
    window.geometry("640x480")

    label_temp = tk.Label(
        text = "mostrando essa janela só pra testar uma coisa kkkkkkkkkkk",
        font = Font(size = 11)).pack()
    
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

    def button1_click(self):
        with FrontPage() as fp:
            entry1_input = fp.entry1.get()
            FrontPage.label_entry1(text = entry1_input)

window.mainloop()