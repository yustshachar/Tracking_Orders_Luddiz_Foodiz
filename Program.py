from tkinter import *
import MainScreen
import ProductsScreen
import MainScreen
import MainMenu
import Function
import SearchOrderTop


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
        self.window.geometry(f"{width_win}x{height_win}+{int(x_cor)}+{int(y_cor) - 20}")
        self.window.resizable(False, False)

        MainMenu.MainMenu(self.window)

        self.window.mainloop()


if __name__ == '__main__':
    window = Tk()
    main_program = Program(window)
