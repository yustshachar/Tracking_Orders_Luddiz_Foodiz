from tkinter import Frame, Label, Entry, Button, CENTER, Scrollbar, END, messagebox, LabelFrame
from tkinter.ttk import Treeview, Style
from Program import *
import Function


class TrackingOrders:
    def __init__(self, window):
        self.tracking_order_screen = Frame(window, width=1300, height=800, bg=Function.colors("color_screen"))

        self.style = Style()
        self.style.theme_use("clam")
        self.style.configure("Custom1.Treeview", rowheight=25, font=(None, 12))
        # self.style.map('Custom1.Treeview')
        self.style.configure('Custom1.Treeview.Heading', background=Function.colors("color_nenu_screen"), font=(None, 12, 'bold'))

        self.tree_order = Treeview(self.tracking_order_screen, columns=(7, 6, 5, 4, 3, 2, 1), show='headings', height=28, style="Custom1.Treeview", selectmode="browse")
        self.tree_order.column("1", anchor=CENTER, width=80)
        self.tree_order.heading("1", text="מספר")
        self.tree_order.column("2", anchor=CENTER, width=150)
        self.tree_order.heading("2", text="תאריך הזמנה")
        self.tree_order.column("3", anchor=CENTER, width=150)
        self.tree_order.heading("3", text="שם לקוח")
        self.tree_order.column("4", anchor=CENTER, width=150)
        self.tree_order.heading("4", text="טלפון")
        self.tree_order.column("5", anchor=CENTER, width=150)
        self.tree_order.heading("5", text="תאריך אספקה")
        self.tree_order.column("6", anchor=CENTER, width=80)
        self.tree_order.heading("6", text="מחיר")
        self.tree_order.column("7", anchor=CENTER, width=80)
        self.tree_order.heading("7", text="סטטוס")
        self.tree_order.place(relx=.644, rely=.5, anchor=CENTER)
        self.vsb = Scrollbar(self.tracking_order_screen, orient="vertical", command=self.tree_order.yview)
        self.vsb.place(relx=.975, rely=.52, anchor=CENTER, height=700)
        self.tree_order.configure(yscrollcommand=self.vsb.set)

        self.tree_order.bind("<<TreeviewSelect>>", self.click_on_order)

        self.tree_products_in_order = Treeview(self.tracking_order_screen, columns=(2, 1), show='headings', height=22, style="Custom1.Treeview", selectmode="none")
        self.tree_products_in_order.column("1", anchor=CENTER, width=300)
        self.tree_products_in_order.heading("1", text="שם המוצר")
        self.tree_products_in_order.column("2", anchor=CENTER, width=70)
        self.tree_products_in_order.heading("2", text="כמות")
        self.tree_products_in_order.place(relx=.16, rely=.406, anchor=CENTER)
        # self.vsb = Scrollbar(self.tracking_order_screen, orient="vertical", command=self.tree_products_in_order.yview)
        # self.vsb.place(relx=.53, rely=.64, anchor=CENTER, height=500)
        # self.tree_products_in_order.configure(yscrollcommand=self.vsb.set)

        self.b_edit_order = Button(self.tracking_order_screen, text="עריכה", width=10, height=2, bg=Function.colors("color_btn_menu"), fg='white', font=(None, 16, "bold"))
        self.b_edit_order.place(relx=.03, rely=.85)

        self.b_delete_order = Button(self.tracking_order_screen, text="מחיקה", width=10, height=2, bg=Function.colors("color_btn_menu"), fg='white', font=(None, 16, "bold"))
        self.b_delete_order.place(relx=.17, rely=.85)





    def start(self):
        self.tracking_order_screen.place(x=0, y=0)
        self.add_all_orders_to_tree()
        for item in self.tree_products_in_order.get_children():
            self.tree_products_in_order.delete(item)

    def close(self):
        self.tracking_order_screen.place_forget()

    def add_all_orders_to_tree(self):
        all_order = Function.read_new_orders_from_json()
        for item in self.tree_order.get_children():
            self.tree_order.delete(item)
        for id in all_order:
            self.tree_order.insert("", END, values=(all_order[id]["status"], all_order[id]["price"], all_order[id]["date_delivery"], all_order[id]["phone"], all_order[id]["name"], all_order[id]["date_order"], id))

    def click_on_order(self, event):
        try: selected_order = self.tree_order.selection()[0]
        except: return
        all_order = Function.read_new_orders_from_json()
        for item in self.tree_products_in_order.get_children():
            self.tree_products_in_order.delete(item)
        for product in all_order[str(self.tree_order.item(selected_order)["values"][6])]["products"]:
            self.tree_products_in_order.insert("", END, values=(product["amount"], product["name"]))
