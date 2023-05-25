import logging
from tkinter import *
from Program import *
import MainScreen
import NewOrderScreen
import ProductsScreen
import TrackingOrders
import TrackingExpenseScreen
import Function


class MainMenu:
    def __init__(self, window):
        frame_menu = Frame(window, width=200, height=800, bg=Function.colors("color_nenu_screen"))
        frame_menu.place(x=1300, y=0)
        b_main = Button(frame_menu, text="ראשי", command=self.open_main_screen, width=12, height=3, font=("Narkisim", 15, 'bold'), bg=Function.colors("color_btn_menu"), fg='#ffffff')
        b_main.place(relx=.5, rely=.1, anchor=CENTER)
        b_new_order = Button(frame_menu, text="הזמנה חדשה", command=self.open_new_order_screen, width=12, height=3, font=("Narkisim", 15, 'bold'), bg=Function.colors("color_btn_menu"), fg='#ffffff')
        b_new_order.place(relx=.5, rely=.25, anchor=CENTER)
        b_tracking_order = Button(frame_menu, text="מעקב הזמנות", command=self.open_tracking_orders_screen, width=12, height=3, font=("Narkisim", 15, 'bold'), bg=Function.colors("color_btn_menu"), fg='#ffffff')
        b_tracking_order.place(relx=.5, rely=.4, anchor=CENTER)
        b_products = Button(frame_menu, text="מוצרים", command=self.open_products_screen, width=12, height=3, font=("Narkisim", 15, 'bold'), bg=Function.colors("color_btn_menu"), fg='#ffffff')
        b_products.place(relx=.5, rely=.55, anchor=CENTER)
        b_tracking_expense = Button(frame_menu, text="מעקב הוצאות", command=self.open_tracking_expense_screen, width=12, height=3, font=("Narkisim", 15, 'bold'), bg=Function.colors("color_btn_menu"), fg='#ffffff')
        b_tracking_expense.place(relx=.5, rely=.7, anchor=CENTER)
        b_backup = Button(frame_menu, text="גיבוי כללי", command=Function.backup_all, width=16, height=2, font=("Narkisim", 11), bg="gray", fg='#ffffff')
        b_backup.place(relx=.5, rely=.95, anchor=CENTER)



        self.main_screen = MainScreen.MainScreen(window)
        self.new_order_screen = NewOrderScreen.NewOrderScreen(window)
        self.tracking_orders_screen = TrackingOrders.TrackingOrders(window, self.new_order_screen)
        self.products_screen = ProductsScreen.ProductsScreen(window)
        self.tracking_expense_screen = TrackingExpenseScreen.TrackingExpenseScreen(window)


    def open_main_screen(self):
        logging.debug("Click main screen")
        self.main_screen.start()
        self.new_order_screen.close()
        self.tracking_orders_screen.close()
        self.products_screen.close()
        self.tracking_expense_screen.close()

    def open_new_order_screen(self):
        logging.debug("Click new order screen")
        self.main_screen.close()
        self.new_order_screen.start()
        self.tracking_orders_screen.close()
        self.products_screen.close()
        self.tracking_expense_screen.close()

    def open_tracking_orders_screen(self):
        logging.debug("Click tracking orders screen")
        self.main_screen.close()
        self.new_order_screen.close()
        self.tracking_orders_screen.start()
        self.products_screen.close()
        self.tracking_expense_screen.close()

    def open_products_screen(self):
        logging.debug("Click products screen")
        self.main_screen.close()
        self.new_order_screen.close()
        self.tracking_orders_screen.close()
        self.products_screen.start()
        self.tracking_expense_screen.close()

    def open_tracking_expense_screen(self):
        logging.debug("Click tracking expense screen")
        self.main_screen.close()
        self.new_order_screen.close()
        self.tracking_orders_screen.close()
        self.products_screen.close()
        self.tracking_expense_screen.start()



