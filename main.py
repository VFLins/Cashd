import prompter as ppt
import handler as hdl
import db_manager as dbm
import gui
import tkinter as tk


if __name__ == "__main__":
    class App:
        def __init__(self, master: tk) -> None:
            self.defaultFont = font.nametofont("TkDefaultFont")
            self.defaultFont.configure(
                family="Segoe UI",
                size=12)
            #for a, b in zip(*hdl.SHORTCUTS):
            #    print(a.ljust(6), b)
            #ppt.prompt_entry()
            gui
