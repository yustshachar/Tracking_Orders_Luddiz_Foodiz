from tkinter import *
from Program import *
import Function


class MainScreen:
    def __init__(self, window):
        self.main_screen = Frame(window, width=1300, height=800, bg=Function.colors("color_screen"))
        self.main_screen.place(x=0, y=0)
        self.logo = PhotoImage(file="logo.png")
        self.label_logo = Label(self.main_screen, image=self.logo)
        self.label_logo.place(relx=.5, rely=.5, anchor=CENTER)


    def start(self):
        self.main_screen.place(x=0, y=0)

    def close(self):
        self.main_screen.place_forget()

