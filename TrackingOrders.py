from tkinter import Frame, Label, Entry, Button, CENTER, Scrollbar, END, messagebox, LabelFrame
from tkinter.ttk import Treeview, Style
import NewOrderScreen
import Function
import SearchOrderTop
from datetime import datetime


class TrackingOrders:
    def __init__(self, window, new_order_screen):
        self.window = window
        self.tracking_order_screen = Frame(window, width=1300, height=800, bg=Function.colors("color_screen"))
        self.edit_order_screen = new_order_screen

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

        self.tree_products_in_order = Treeview(self.tracking_order_screen, columns=(2, 1), show='headings', height=20, style="Custom1.Treeview", selectmode="none")
        self.tree_products_in_order.column("1", anchor=CENTER, width=300)
        self.tree_products_in_order.heading("1", text="שם המוצר")
        self.tree_products_in_order.column("2", anchor=CENTER, width=70)
        self.tree_products_in_order.heading("2", text="כמות")
        self.tree_products_in_order.place(relx=.16, rely=.375, anchor=CENTER)
        # self.vsb = Scrollbar(self.tracking_order_screen, orient="vertical", command=self.tree_products_in_order.yview)
        # self.vsb.place(relx=.53, rely=.64, anchor=CENTER, height=500)
        # self.tree_products_in_order.configure(yscrollcommand=self.vsb.set)

        # הזמנות עתידיות
        # כל ההזמנות
        # עריכת הזמנה
        # מחיקת הזמנה
        # יצוא דוח
        # חיפוש

        self.b_fudure_orders = Button(self.tracking_order_screen, text="הזמנות\nעתידיות", width=7, height=2, bg=Function.colors("color_btn_menu"), fg='white', font=(None, 16, "bold"), command=self.show_future_orders)
        self.b_fudure_orders.place(relx=.21, rely=.75)

        self.b_all_orders = Button(self.tracking_order_screen, text="כל\nההזמנות", width=7, height=2, bg=Function.colors("color_btn_menu"), fg='white', font=(None, 16, "bold"), command=self.add_all_orders_to_tree)
        self.b_all_orders.place(relx=.21, rely=.875)

        self.b_edit_order = Button(self.tracking_order_screen, text="עריכת\nהזמנה", width=7, height=2, bg=Function.colors("color_btn_menu"), fg='white', font=(None, 16, "bold"), command=self.click_edit_order)
        self.b_edit_order.place(relx=.115, rely=.75)

        self.b_delete_order = Button(self.tracking_order_screen, text="מחיקת\nהזמנה", width=7, height=2, bg=Function.colors("color_btn_menu"), fg='white', font=(None, 16, "bold"), command=self.delete_order)
        self.b_delete_order.place(relx=.115, rely=.875)

        self.b_report = Button(self.tracking_order_screen, text='ייצוא\nדו"ח', width=7, height=2, bg=Function.colors("color_btn_menu"), fg='white', font=(None, 16, "bold"), command=self.to_report)
        self.b_report.place(relx=.02, rely=.75)

        self.b_search_order = Button(self.tracking_order_screen, text="חיפוש\nהזמנה", width=7, height=2, bg=Function.colors("color_btn_menu"), fg='white', font=(None, 16, "bold"), command=self.search_by_parameters)
        self.b_search_order.place(relx=.02, rely=.875)







    def start(self):
        self.tracking_order_screen.place(x=0, y=0)
        self.add_all_orders_to_tree()

    def close(self):
        self.tracking_order_screen.place_forget()

    def add_all_orders_to_tree(self):
        all_order = Function.read_new_orders_from_json()
        for item in self.tree_order.get_children():
            self.tree_order.delete(item)
        for item in self.tree_products_in_order.get_children():
            self.tree_products_in_order.delete(item)
        for id in all_order:
            self.tree_order.insert("", END, values=(Function.status_order_option[all_order[id]["status"]].split()[0], all_order[id]["price"], all_order[id]["date_delivery"], all_order[id]["phone"], all_order[id]["name"], all_order[id]["date_order"], id))

    def click_on_order(self, event):
        try: selected_order = self.tree_order.selection()[0]
        except: return
        all_order = Function.read_new_orders_from_json()
        for item in self.tree_products_in_order.get_children():
            self.tree_products_in_order.delete(item)
        for product in all_order[str(self.tree_order.item(selected_order)["values"][6])]["products"]:
            self.tree_products_in_order.insert("", END, values=(product["amount"], product["name"]))

    def delete_order(self):
        try: selected_order = self.tree_order.selection()[0]
        except: return
        if not messagebox.askokcancel("מחיקת הזמנה", "האם למחוק לצמיתות את ההזמנה?\nלאחר המחיקה לא יהיה ניתן לשחזר את ההזמנה!"): return
        all_order = Function.read_new_orders_from_json()
        Function.delete_order_from_json_by_id(str(self.tree_order.item(selected_order)["values"][6]))
        self.add_all_orders_to_tree()

    def click_edit_order(self):
        try: selected_order = self.tree_order.selection()[0]
        except: return
        self.close()
        self.edit_order_screen.edit_order(str(self.tree_order.item(selected_order)["values"][6]), self.tracking_order_screen)

    def show_after_edit_order(self):
        self.tracking_order_screen.place(x=0, y=0)

    def show_future_orders(self):
        all_orders = Function.read_new_orders_from_json(reverse=False)
        for item in self.tree_order.get_children():
            self.tree_order.delete(item)
        for item in self.tree_products_in_order.get_children():
            self.tree_products_in_order.delete(item)

        for i in all_orders:
            if datetime.today() <= datetime.strptime(all_orders[i]["date_delivery"],"%d-%m-%Y"):
                self.tree_order.insert("", END, values=(Function.status_order_option[all_orders[i]["status"]].split()[0], all_orders[i]["price"], all_orders[i]["date_delivery"], all_orders[i]["phone"], all_orders[i]["name"], all_orders[i]["date_order"], i))

    def search_by_parameters(self):
        id, date_order, date_order_2, name, date_delivery, date_delivery_2, status, method = SearchOrderTop.SearchOrderTop(self.window).start()
        if id==date_order==date_order_2==name==date_delivery==date_delivery_2==status==method==None:
            self.add_all_orders_to_tree()
            return

        all_orders = Function.read_new_orders_from_json()
        for item in self.tree_order.get_children():
            self.tree_order.delete(item)
        for item in self.tree_products_in_order.get_children():
            self.tree_products_in_order.delete(item)

        res_ids = []
        for i in all_orders:
            if (id is None or id == i) and\
                (date_order is None or datetime.strptime(date_order, "%d-%m-%Y") <= datetime.strptime(all_orders[i]["date_order"],"%d-%m-%Y")) and\
                (date_order_2 is None or datetime.strptime(date_order_2, "%d-%m-%Y") >= datetime.strptime(all_orders[i]["date_order"],"%d-%m-%Y")) and\
                (name is None or all_orders[i]["name"].find(name) != -1) and\
                (date_delivery is None or datetime.strptime(date_delivery, "%d-%m-%Y") <= datetime.strptime(all_orders[i]["date_delivery"],"%d-%m-%Y")) and\
                (date_delivery_2 is None or datetime.strptime(date_delivery_2, "%d-%m-%Y") >= datetime.strptime(all_orders[i]["date_delivery"],"%d-%m-%Y")) and\
                (status is None or all_orders[i]["status"] == status) and \
                (method is None or all_orders[i]["method"] == method):
                res_ids.append(i)

        for i in res_ids:
            self.tree_order.insert("", END, values=(Function.status_order_option[all_orders[i]["status"]].split()[0], all_orders[i]["price"], all_orders[i]["date_delivery"], all_orders[i]["phone"], all_orders[i]["name"], all_orders[i]["date_order"],i))

    def to_report(self):
        ids = []
        for i in self.tree_order.get_children():
            ids.append(str(self.tree_order.item(i)["values"][6]))
        Function.export_report(ids)
