import json
from datetime import datetime, date
import configparser
from tkinter import *
from tkinter.ttk import Treeview, Style

import MainScreen
from ProductsScreen import *
import MainScreen
import MainMenu
from Function import *


class Program:
    def __init__(self, window):
        self.window = window
        window.title('Ludiz.Foodiz')
        width_win = 1500
        height_win = 800
        x_cor = (window.winfo_screenwidth() / 2) - (width_win / 2)
        y_cor = (window.winfo_screenheight() / 2) - (height_win / 2)
        window.geometry(f"{width_win}x{height_win}+{int(x_cor)}+{int(y_cor) - 20}")
        window.resizable(False, False)

        MainMenu.MainMenu(self.window)
        MainScreen.MainScreen(window).start()

        self.window.mainloop()



if __name__ == '__main__':
    window = Tk()
    main_program = Program(window)
