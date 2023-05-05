from tkinter import Tk
import MainScreen
import ProductsScreen
import MainScreen
import MainMenu
from Function import *
import SearchOrderTop


class Program:
    def __init__(self, window):
        self.window = window
        window.title('Ludiz.Foodiz - Tracking Orders - V1.2')
        width_win = 1500
        height_win = 800
        x_cor = (window.winfo_screenwidth() / 2) - (width_win / 2)
        y_cor = (window.winfo_screenheight() / 2) - (height_win / 2)
        window.geometry(f"{width_win}x{height_win}+{int(x_cor)}+{int(y_cor) - 20}")
        window.resizable(False, False)

        MainMenu.MainMenu(self.window)
        # SearchOrderTop.SearchOrderTop(self.window)

        self.window.mainloop()



if __name__ == '__main__':
    window = Tk()
    main_program = Program(window)
