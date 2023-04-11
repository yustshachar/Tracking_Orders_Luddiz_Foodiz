from tkinter import *
from Program import *
import MainScreen
import NewOrderScreen
import ProductsScreen
import TrackingOrders
import ReportsScreen
import Function


class MainMenu:
    def __init__(self, window):
        frame_menu = Frame(window, width=200, height=800, bg=Function.colors("color_nenu_screen"))
        frame_menu.place(x=1300, y=0)
        b_main = Button(frame_menu, text="ראשי", command=lambda: self.open_main_screen(window), width=12, height=3, font=("Narkisim", 15, 'bold'), bg=Function.colors("color_btn_menu"), fg='#ffffff')
        b_main.place(relx=.5, rely=.1, anchor=CENTER)
        b_new_order = Button(frame_menu, text="הזמנה חדשה", command=lambda: self.open_new_order_screen(window), width=12, height=3, font=("Narkisim", 15, 'bold'), bg=Function.colors("color_btn_menu"), fg='#ffffff')
        b_new_order.place(relx=.5, rely=.25, anchor=CENTER)
        b_tracking_order = Button(frame_menu, text="מעקב הזמנות", command=lambda: self.open_tracking_orders_screen(window), width=12, height=3, font=("Narkisim", 15, 'bold'), bg=Function.colors("color_btn_menu"), fg='#ffffff')
        b_tracking_order.place(relx=.5, rely=.4, anchor=CENTER)
        b_products = Button(frame_menu, text="מוצרים", command=lambda: self.open_products_screen(window), width=12, height=3, font=("Narkisim", 15, 'bold'), bg=Function.colors("color_btn_menu"), fg='#ffffff')
        b_products.place(relx=.5, rely=.55, anchor=CENTER)
        b_reports = Button(frame_menu, text="דוחות", command=lambda: self.open_reports_screen(window), width=12, height=3, font=("Narkisim", 15, 'bold'), bg=Function.colors("color_btn_menu"), fg='#ffffff')
        b_reports.place(relx=.5, rely=.7, anchor=CENTER)

    def open_main_screen(self, window):
        MainScreen.MainScreen(window).start()

    def open_new_order_screen(self, window):
        NewOrderScreen.NewOrderScreen(window).start()

    def open_tracking_orders_screen(self, window):
        TrackingOrders.TrackingOrders(window).start()

    def open_products_screen(self, window):
        ProductsScreen.ProductsScreen(window).start()

    def open_reports_screen(self, window):
        ReportsScreen.ReportsScreen(window).start()



