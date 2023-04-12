from tkinter import Frame, Label, CENTER, Scrollbar
from tkinter.ttk import Treeview, Style
# from Program import *
import Function


class NewOrderScreen:
    def __init__(self, window):
        self.new_order_screen = Frame(window, width=900, height=800, bg=Function.colors("color_screen"))
        self.all_products_frame = Frame(window, width=400, height=800, bg=Function.colors("color_menu_tracking_orders"))

        # רשימת מוצרים בהזמנה
        self.lable_title_in = Label(self.new_order_screen, text=":המוצרים בהזמנה", bg=Function.colors("color_screen"), font=(None, 14, 'bold'))
        self.lable_title_in.place(relx=0.3, rely=0.032)
        self.tree_all_products_in_new = Treeview(self.new_order_screen, columns=(2, 1), show='headings', height=32, style="Treeview.Heading")
        self.style_tap = Style()
        self.style_tap.theme_use("clam")
        self.style_tap.configure('Treeview.Heading', background=Function.colors("color_nenu_screen"), font=(None, 14, 'bold'))
        self.style_tap.configure('Treeview', rowheight=25, font=(None, 12))
        self.tree_all_products_in_new.column("1", anchor=CENTER, width=280)
        self.tree_all_products_in_new.heading("1", text="שם המוצר")
        self.tree_all_products_in_new.column("2", anchor=CENTER, width=60)
        self.tree_all_products_in_new.heading("2", text="מחיר")
        self.tree_all_products_in_new.place(relx=.48, rely=.52, anchor=CENTER)
        self.vsb = Scrollbar(self.new_order_screen, orient="vertical", command=self.tree_all_products_in_new.yview)
        self.vsb.place(relx=.947, rely=.535, anchor=CENTER, height=665)
        self.tree_all_products_in_new.configure(yscrollcommand=self.vsb.set)




        # רשימת כל המוצרים
        self.lable_title_all = Label(self.all_products_frame, text="רשימת כל המוצרים", bg=Function.colors("color_menu_tracking_orders"), font=(None, 14, 'bold'))
        self.lable_title_all.place(relx=0.3, rely=0.032)
        self.tree_all_products_in_new = Treeview(self.all_products_frame, columns=(2, 1), show='headings', height=32, style="Treeview2.Heading")
        self.style_tapin = Style()
        self.style_tapin.theme_use("clam")
        self.style_tapin.configure('Treeview2.Heading', background="white", font=(None, 10, 'bold'))
        self.style_tapin.configure('Treeview2', rowheight=25, font=(None, 12))
        self.tree_all_products_in_new.column("1", anchor=CENTER, width=280)
        self.tree_all_products_in_new.heading("1", text="שם המוצר")
        self.tree_all_products_in_new.column("2", anchor=CENTER, width=60)
        self.tree_all_products_in_new.heading("2", text="מחיר")
        self.tree_all_products_in_new.place(relx=.48, rely=.52, anchor=CENTER)
        self.vsb = Scrollbar(self.all_products_frame, orient="vertical", command=self.tree_all_products_in_new.yview)
        self.vsb.place(relx=.947, rely=.535, anchor=CENTER, height=665)
        self.tree_all_products_in_new.configure(yscrollcommand=self.vsb.set)






    def start(self):
        self.new_order_screen.place(x=400, y=0)
        self.all_products_frame.place(x=0, y=0)

    def close(self):
        self.new_order_screen.place_forget()
        self.all_products_frame.place_forget()
