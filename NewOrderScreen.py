from tkinter import Frame, Label, CENTER, Scrollbar, Entry
from tkinter.ttk import Treeview, Style
# from Program import *
import Function


class NewOrderScreen:
    def __init__(self, window):
        self.new_order_screen = Frame(window, width=900, height=800, bg=Function.colors("color_screen"))
        self.all_products_frame = Frame(window, width=400, height=800, bg=Function.colors("color_menu_tracking_orders"))

        # רשימת מוצרים בהזמנה
        self.lable_title_in = Label(self.new_order_screen, text=":המוצרים בהזמנה", bg=Function.colors("color_screen"), font=(None, 14, 'bold'))
        self.lable_title_in.place(relx=0.2, rely=0.032)
        self.tree_products_in_new = Treeview(self.new_order_screen, columns=(3, 2, 1), show='headings', height=32, style="Treeview3.Heading")
        self.style_tap = Style()
        self.style_tap.theme_use("clam")
        self.style_tap.configure('Treeview3.Heading', background="#FFFFFF", font=(None, 14, 'bold'))
        self.style_tap.configure('Treeview', rowheight=25, font=(None, 12))
        self.tree_products_in_new.column("1", anchor=CENTER, width=280)
        self.tree_products_in_new.heading("1", text="שם המוצר")
        self.tree_products_in_new.column("2", anchor=CENTER, width=70)
        self.tree_products_in_new.heading("2", text="מחיר")
        self.tree_products_in_new.column("3", anchor=CENTER, width=70)
        self.tree_products_in_new.heading("3", text="כמות")
        self.tree_products_in_new.place(relx=.3, rely=.52, anchor=CENTER)
        self.vsb1 = Scrollbar(self.new_order_screen, orient="vertical", command=self.tree_products_in_new.yview)
        self.vsb1.place(relx=.556, rely=.535, anchor=CENTER, height=669)
        self.tree_products_in_new.configure(yscrollcommand=self.vsb1.set)


        # שדות
        self.id_order_lable = Label(self.new_order_screen, text="מספר הזמנה", bg=Function.colors("color_screen"), font=(None, 12))
        self.id_order_lable.place(relx=0.85, rely=0.1)
        self.id_order_entry = Entry(self.new_order_screen, width=15, justify="right", font=(None, 12))
        self.id_order_entry.place(relx=0.65, rely=0.1)

        self.date_order_lable = Label(self.new_order_screen, text="תאריך הזמנה", bg=Function.colors("color_screen"), font=(None, 12))
        self.date_order_lable.place(relx=0.85, rely=0.15)
        self.date_order_entry = Entry(self.new_order_screen, width=15, justify="right", font=(None, 12))
        self.date_order_entry.place(relx=0.65, rely=0.15)

        self.name_lable = Label(self.new_order_screen, text="שם לקוח", bg=Function.colors("color_screen"), font=(None, 12))
        self.name_lable.place(relx=0.85, rely=0.2)
        self.name_entry = Entry(self.new_order_screen, width=15, justify="right", font=(None, 12))
        self.name_entry.place(relx=0.65, rely=0.2)

        self.phone_lable = Label(self.new_order_screen, text="מספר טלפון", bg=Function.colors("color_screen"), font=(None, 12))
        self.phone_lable.place(relx=0.85, rely=0.25)
        self.phone_entry = Entry(self.new_order_screen, width=15, justify="right", font=(None, 12))
        self.phone_entry.place(relx=0.65, rely=0.25)

        self.date_delivery_lable = Label(self.new_order_screen, text="תאריך אספקה", bg=Function.colors("color_screen"), font=(None, 12))
        self.date_delivery_lable.place(relx=0.85, rely=0.3)
        self.date_delivery_entry = Entry(self.new_order_screen, width=15, justify="right", font=(None, 12))
        self.date_delivery_entry.place(relx=0.65, rely=0.3)

        self.remarks_lable = Label(self.new_order_screen, text="הערות", bg=Function.colors("color_screen"), font=(None, 12))
        self.remarks_lable.place(relx=0.85, rely=0.35)
        self.remarks_entry = Entry(self.new_order_screen, width=15, justify="right", font=(None, 12))
        self.remarks_entry.place(relx=0.65, rely=0.35)

        self.price_lable = Label(self.new_order_screen, text="מחיר סופי", bg=Function.colors("color_screen"), font=(None, 12))
        self.price_lable.place(relx=0.85, rely=0.4)
        self.price_entry = Entry(self.new_order_screen, width=15, justify="right", font=(None, 12))
        self.price_entry.place(relx=0.65, rely=0.4)

        self.status_lable = Label(self.new_order_screen, text="סטטוס", bg=Function.colors("color_screen"), font=(None, 12))
        self.status_lable.place(relx=0.85, rely=0.45)
        self.status_entry = Entry(self.new_order_screen, width=15, justify="right", font=(None, 12))
        self.status_entry.place(relx=0.65, rely=0.45)

        self.method_lable = Label(self.new_order_screen, text="אמצעי תשלום", bg=Function.colors("color_screen"), font=(None, 12))
        self.method_lable.place(relx=0.85, rely=0.5)
        self.method_entry = Entry(self.new_order_screen, width=15, justify="right", font=(None, 12))
        self.method_entry.place(relx=0.65, rely=0.5)





        # רשימת כל המוצרים
        self.lable_title_all = Label(self.all_products_frame, text=":רשימת כל המוצרים", bg=Function.colors("color_menu_tracking_orders"), font=(None, 14, 'bold'))
        self.lable_title_all.place(relx=0.3, rely=0.032)
        self.tree_all_products_in_new = Treeview(self.all_products_frame, columns=(2, 1), show='headings', height=32, style="Treeview2.Heading")
        self.style_tapin = Style()
        self.style_tapin.theme_use("clam")
        self.style_tapin.configure('Treeview2.Heading', background=Function.colors("color_screen"), font=(None, 10, 'bold'))
        self.style_tapin.configure('Treeview2', rowheight=25, font=(None, 12))
        self.tree_all_products_in_new.column("1", anchor=CENTER, width=270)
        self.tree_all_products_in_new.heading("1", text="שם המוצר")
        self.tree_all_products_in_new.column("2", anchor=CENTER, width=70)
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
