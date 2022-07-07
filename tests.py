from tkinter import *


class MainWindow(Frame):
    def __init__(self):
        FG_COLOR_ACTIVE = "#2e2e2e"
        FG_COLOR = "#55776f"
        BG_COLOR = "#f7f3f3"

        Frame.__init__(self)
        self.master.title("input")
        self.master.minsize(250, 150)
        self.master.configure(bg = BG_COLOR)
        self.grid(sticky=E+W+N+S)

        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        for i in range(2):self.rowconfigure(i, weight=1)
        self.columnconfigure(1, weight=1)

        self.button0 = Button(self, text="Start", command=self.save, fg = FG_COLOR, 
            activeforeground = FG_COLOR_ACTIVE, disabledforeground = FG_COLOR_ACTIVE,
            bg = BG_COLOR, activebackground = BG_COLOR, borderwidth=0)
        self.button0.grid(row=0, column=0, columnspan=2, pady=2, padx=2, sticky=E+W+N+S)

        self.button1 = Button(self, text="Stop", command=self.stop, fg = FG_COLOR,
            activeforeground = FG_COLOR_ACTIVE, disabledforeground = FG_COLOR_ACTIVE,
            bg = BG_COLOR, activebackground = BG_COLOR, borderwidth=0)
        self.button1.grid(row=1, column=0, columnspan=2, pady=2, padx=2, sticky=E+W+N+S)

    def save(self):
        self.button0.config(relief=SUNKEN, state=DISABLED)
        self.button1.config(relief=RAISED, state=ACTIVE)

    def stop(self):
        self.button1.config(relief=SUNKEN, state=DISABLED)
        self.button0.config(relief=RAISED, state=ACTIVE)


if __name__=="__main__":
   d=MainWindow()
   d.mainloop()