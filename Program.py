from tkinter import *
import MainScreen
import ProductsScreen
import MainScreen
import MainMenu
import Function
import SearchOrderTop
import logging

logging.basicConfig(filename=f"{Function.main_path}/TrackingOrdersLog.log", level=logging.DEBUG, format="%(asctime)s\t%(filename)s\t%(funcName)s\t%(lineno)d\t%(message)s")


class Program:
    def __init__(self, window):
        self.window = window
        self.window.title(f'Ludiz.Foodiz - Tracking Orders - V{Function.version_number}')
        # icon = PhotoImage(file = "logo.png")
        # self.window.iconphoto(False, icon)
        width_win = 1500
        height_win = 800
        x_cor = (self.window.winfo_screenwidth() / 2) - (width_win / 2)
        y_cor = (self.window.winfo_screenheight() / 2) - (height_win / 2)
        self.window.geometry(f"{width_win}x{height_win}+{int(x_cor)}+{int(y_cor/2)}")
        self.window.resizable(False, False)

        MainMenu.MainMenu(self.window)

        self.window.mainloop()


if __name__ == '__main__':
    logging.debug("Start program")
    window = Tk()
    main_program = Program(window)
