import datetime
from tkinter import Frame, Label, CENTER, Scrollbar, Entry, Button, Text, scrolledtext, WORD, END, StringVar, messagebox
from tkinter.ttk import Treeview, Style, OptionMenu
from tkcalendar import DateEntry
from datetime import *
# from Program import *
import Function
import TrackingOrders


class NewOrderScreen:
    def __init__(self, window):
        self.new_order_screen = Frame(window, width=900, height=800, bg=Function.colors("color_screen"))
        self.all_products_frame = Frame(window, width=400, height=800, bg=Function.colors("color_menu_tracking_orders"))

        # רשימת מוצרים בהזמנה
        self.style = Style()
        self.style.theme_use("clam")
        self.style.configure("Custom3.Treeview", rowheight=22, font=(None, 12))
        self.style.configure('Custom3.Treeview.Heading', font=(None, 14, 'bold'), background=Function.colors("color_nenu_screen"))

        self.lable_title_in = Label(self.new_order_screen, text=":המוצרים בהזמנה", bg=Function.colors("color_screen"), font=(None, 14, 'bold'))
        self.lable_title_in.place(relx=0.2, rely=0.032)
        self.tree_products_in_new_order = Treeview(self.new_order_screen, columns=(4, 3, 2, 1), show='headings', height=30, style="Custom3.Treeview")
        self.tree_products_in_new_order.column("1", anchor=CENTER, width=290)
        self.tree_products_in_new_order.heading("1", text="שם המוצר")
        self.tree_products_in_new_order.column("2", anchor=CENTER, width=70)
        self.tree_products_in_new_order.heading("2", text="עלות")
        self.tree_products_in_new_order.column("3", anchor=CENTER, width=70)
        self.tree_products_in_new_order.heading("3", text="מחיר")
        self.tree_products_in_new_order.column("4", anchor=CENTER, width=70)
        self.tree_products_in_new_order.heading("4", text="כמות")
        self.tree_products_in_new_order.place(relx=.3, rely=.51, anchor=CENTER)
        self.vsb1 = Scrollbar(self.new_order_screen, orient="vertical", command=self.tree_products_in_new_order.yview)
        self.vsb1.place(relx=.59, rely=.53, anchor=CENTER, height=664)
        self.tree_products_in_new_order.configure(yscrollcommand=self.vsb1.set)

        # אירוע בעת לחיצה כפולה
        self.tree_products_in_new_order.bind("<Double-1>", self.double_click_to_change_count)


        # שדות
        self.id_order_lable = Label(self.new_order_screen, text="מספר הזמנה", bg=Function.colors("color_screen"), font=(None, 12))
        self.id_order_lable.place(relx=0.85, rely=0.1)
        self.id_order_entry = Entry(self.new_order_screen, width=18, justify="center", font=(None, 12))
        self.id_order_entry.place(relx=0.63, rely=0.1)

        self.date_order_lable = Label(self.new_order_screen, text="תאריך הזמנה", bg=Function.colors("color_screen"), font=(None, 12))
        self.date_order_lable.place(relx=0.85, rely=0.15)
        self.date_order_entry = DateEntry(self.new_order_screen, width=16, borderwidth=2, date_pattern='dd-MM-yyyy', justify="center", font=(None, 12), showweeknumbers=False, firstweekday='sunday', locale='he_IL', weekenddays=[7,7])
        self.date_order_entry.place(relx=0.63, rely=0.15)
        self.date_order_entry.bind("<<DateEntrySelected>>", self.update_entrydate_delivery)

        self.name_lable = Label(self.new_order_screen, text="שם לקוח", bg=Function.colors("color_screen"), font=(None, 12))
        self.name_lable.place(relx=0.85, rely=0.2)
        self.name_entry = Entry(self.new_order_screen, width=18, justify="right", font=(None, 12))
        self.name_entry.place(relx=0.63, rely=0.2)

        self.phone_lable = Label(self.new_order_screen, text="מספר טלפון", bg=Function.colors("color_screen"), font=(None, 12))
        self.phone_lable.place(relx=0.85, rely=0.25)
        self.phone_entry = Entry(self.new_order_screen, width=18, justify="right", font=(None, 12))
        self.phone_entry.place(relx=0.63, rely=0.25)

        self.date_delivery_lable = Label(self.new_order_screen, text="תאריך אספקה", bg=Function.colors("color_screen"), font=(None, 12))
        self.date_delivery_lable.place(relx=0.85, rely=0.35)
        self.date_delivery_entry = DateEntry(self.new_order_screen, width=16, borderwidth=2, date_pattern='dd-MM-yyyy', justify="center", font=(None, 12), showweeknumbers=False, year=datetime.today().year, month=datetime.today().month, day=datetime.today().day+1, firstweekday='sunday', mindate=datetime.strptime(self.date_order_entry.get(), "%d-%m-%Y"), locale='he_IL', weekenddays=[7,7])
        self.date_delivery_entry.place(relx=0.63, rely=0.35)

        self.remarks_lable = Label(self.new_order_screen, text="הערות", bg=Function.colors("color_screen"), font=(None, 12))
        self.remarks_lable.place(relx=0.85, rely=0.4)
        # self.remarks_entry = Entry(self.new_order_screen, width=15, justify="right", font=(None, 12))
        # self.remarks_entry.place(relx=0.65, rely=0.4)
        self.remarks_text = Text(self.new_order_screen, width=18, height=6, font=(None, 12), wrap=WORD)
        self.remarks_text.place(relx=0.63, rely=0.4)

        # self.cost_lable = Label(self.new_order_screen, text="עלות", bg=Function.colors("color_screen"), font=(None, 12))
        # self.cost_lable.place(relx=0.85, rely=0.55)
        # self.def_in_cost = StringVar()
        # self.def_in_cost.set('0')
        # self.cost_entry = Entry(self.new_order_screen, width=18, justify="center", font=(None, 12), textvariable=self.def_in_cost)
        # self.cost_entry.place(relx=0.63, rely=0.55)
        # self.cost_entry.config(state="disabled")

        self.bid_lable = Label(self.new_order_screen, text="הצעת מחיר", bg=Function.colors("color_screen"), font=(None, 12))
        self.bid_lable.place(relx=0.85, rely=0.6)
        self.def_in_bid = StringVar()
        self.def_in_bid.set('0')
        self.bid_entry = Entry(self.new_order_screen, width=18, justify="center", font=(None, 12), textvariable=self.def_in_bid)
        self.bid_entry.place(relx=0.63, rely=0.6)
        self.bid_entry.config(state="disabled")

        self.price_lable = Label(self.new_order_screen, text="מחיר סופי", bg=Function.colors("color_screen"), font=(None, 12, "bold"))
        self.price_lable.place(relx=0.85, rely=0.65)
        self.price_entry = Entry(self.new_order_screen, width=18, justify="center", font=(None, 12))
        self.price_entry.place(relx=0.63, rely=0.65)

        self.status_lable = Label(self.new_order_screen, text="סטטוס", bg=Function.colors("color_screen"), font=(None, 12))
        self.status_lable.place(relx=0.85, rely=0.7)
        self.status_selected = StringVar()
        self.status_drop = OptionMenu(self.new_order_screen, self.status_selected, Function.status_order_option[0], *Function.status_order_option)
        self.status_drop.config(width=22)
        self.status_drop.place(relx=0.63, rely=0.695)

        self.method_lable = Label(self.new_order_screen, text="אמצעי תשלום", bg=Function.colors("color_screen"), font=(None, 12))
        self.method_lable.place(relx=0.85, rely=0.75)
        self.method_entry = Entry(self.new_order_screen, width=18, justify="right", font=(None, 12))
        self.method_entry.place(relx=0.63, rely=0.75)
        # self.options_method_drop_list = ["מזומן", "ביט", "פייבוקס", "העברה בנקאית", "אשראי", "אחר"]
        # self.method_selected = StringVar()
        # self.method_drop = OptionMenu(self.new_order_screen, self.method_selected, "נא לבחור אמצעי תשלום", *self.options_method_drop_list)
        # self.method_drop.config(width=22)
        # self.method_drop.place(relx=0.63, rely=0.745)


        self.b_save_order = Button(self.new_order_screen, text="שמור", bg=Function.colors("color_btn_menu"), fg='white', font=(None, 16, "bold"), width=7, command=self.save_order)
        self.b_save_order.place(relx=.64, rely=.85)

        self.b_clear_to_new = Button(self.new_order_screen, text="נקה", bg=Function.colors("color_btn_menu"), fg='white', font=(None, 16, "bold"), width=7, command=self.clear_all)
        self.b_clear_to_new.place(relx=.828, rely=.85)

        self.b_delete_products = Button(self.new_order_screen, text="מחק פריט", bg=Function.colors("color_menu_tracking_orders"), fg='red', font=(None, 10, "bold"), command=self.delete_selected_product_from_order_in_new)
        self.b_delete_products.place(relx=.02, rely=.952)

        self.b_back_to_tracking = Button(self.new_order_screen, text="חזרה למעקב ההזמנות", width=20, height=1, bg="gray", fg='white', font=(None, 12))






        # רשימת כל המוצרים
        self.style = Style()
        self.style.theme_use("clam")
        self.style.configure("Custom2.Treeview", rowheight=21, font=(None, 11), background=Function.colors("color_screen"), fieldbackground=Function.colors("color_screen"))
        self.style.configure('Custom2.Treeview.Heading', font=(None, 12, 'bold'))

        self.lable_title_all = Label(self.all_products_frame, text=":רשימת כל המוצרים", bg=Function.colors("color_menu_tracking_orders"), font=(None, 14, 'bold'))
        self.lable_title_all.place(relx=0.25, rely=0.032)
        self.tree_all_products_in_new = Treeview(self.all_products_frame, columns=(2, 1), show='headings', height=31, style="Custom2.Treeview")
        self.tree_all_products_in_new.column("1", anchor=CENTER, width=282)
        self.tree_all_products_in_new.heading("1", text="שם המוצר")
        self.tree_all_products_in_new.column("2", anchor=CENTER, width=70)
        self.tree_all_products_in_new.heading("2", text="מחיר")
        self.tree_all_products_in_new.place(relx=.48, rely=.505, anchor=CENTER)
        self.vsb = Scrollbar(self.all_products_frame, orient="vertical", command=self.tree_all_products_in_new.yview)
        self.vsb.place(relx=.947, rely=.525, anchor=CENTER, height=652)
        self.tree_all_products_in_new.configure(yscrollcommand=self.vsb.set)

        self.search_entry = Entry(self.all_products_frame, width=18, justify="center", font=(None, 12))
        self.search_entry.place(relx=.4, rely=0.953)
        self.search_btn = Button(self.all_products_frame, text="חיפוש", bg=Function.colors("color_menu_tracking_orders"), font=(None, 10, "bold"), command=self.search_product_from_all)
        self.search_btn.place(relx=.25, rely=.95)
        self.search_btn = Button(self.all_products_frame, text="איפוס", bg=Function.colors("color_menu_tracking_orders"), font=(None, 10, "bold"), command=self.add_all_products)
        self.search_btn.place(relx=.1, rely=.95)


        # אירוע בעת לחיצה כפולה
        self.tree_all_products_in_new.bind("<Double-1>", self.add_product_to_order)







    def start(self):
        self.new_order_screen.place(x=400, y=0)
        self.all_products_frame.place(x=0, y=0)
        self.clear_all()
        self.edit_id_order_entry()
        self.add_all_products()

    def close(self):
        self.new_order_screen.place_forget()
        self.all_products_frame.place_forget()

    def update_entrydate_delivery(self, event):
        self.date_delivery_entry.config(mindate=datetime.strptime(self.date_order_entry.get(), "%d-%m-%Y"))
        self.date_delivery_entry.set_date(datetime.strptime(self.date_order_entry.get(), "%d-%m-%Y") + timedelta(1))

    def delete_selected_product_from_order_in_new(self):
        try: selected_item = self.tree_products_in_new_order.selection()[0]
        except: return
        self.tree_products_in_new_order.delete(selected_item)
        self.calculate_bid()

    def add_all_products(self):
        self.search_entry.delete(0, END)
        for item in self.tree_all_products_in_new.get_children():
            self.tree_all_products_in_new.delete(item)
        for name in Function.read_all_products_from_json().keys():
            self.tree_all_products_in_new.insert("", END, values=[Function.read_all_products_from_json()[name]["price"], name])

    def add_product_to_order(self, event):
        try: selected_item = self.tree_all_products_in_new.selection()[0]
        except: return
        dict_all_products = Function.read_all_products_from_json()
        if len(self.tree_products_in_new_order.get_children()) == 0:
            self.tree_products_in_new_order.insert("", END, values=[1, dict_all_products[self.tree_all_products_in_new.item(selected_item)["values"][1]]["price"], dict_all_products[self.tree_all_products_in_new.item(selected_item)["values"][1]]["cost"], self.tree_all_products_in_new.item(selected_item)["values"][1]])
        else:
            for item in self.tree_products_in_new_order.get_children():
                if self.tree_all_products_in_new.item(selected_item)['values'][1] == self.tree_products_in_new_order.item(item)["values"][3]:
                    count_in_order = int(self.tree_products_in_new_order.item(item)["values"][0]) + 1
                    self.tree_products_in_new_order.item(item, values=[count_in_order, dict_all_products[self.tree_all_products_in_new.item(selected_item)["values"][1]]["price"], dict_all_products[self.tree_all_products_in_new.item(selected_item)["values"][1]]["cost"], self.tree_all_products_in_new.item(selected_item)["values"][1]])
                    self.calculate_bid()
                    return
            self.tree_products_in_new_order.insert("", END, values=[1, dict_all_products[self.tree_all_products_in_new.item(selected_item)["values"][1]]["price"], dict_all_products[self.tree_all_products_in_new.item(selected_item)["values"][1]]["cost"], self.tree_all_products_in_new.item(selected_item)["values"][1]])
        self.calculate_bid()

    def search_product_from_all(self):
        for item in self.tree_all_products_in_new.get_children():
            self.tree_all_products_in_new.delete(item)
        all_products = Function.read_all_products_from_json()
        for name in all_products.keys():
            if name.find(self.search_entry.get()) != -1:
                self.tree_all_products_in_new.insert("", END, values=[all_products[name]["price"], name])
        self.search_entry.delete(0, END)

    def clear_all(self):
        self.entrys_to_white()
        for item in self.tree_products_in_new_order.get_children():
            self.tree_products_in_new_order.delete(item)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.remarks_text.delete('1.0', END)
        self.price_entry.delete(0, END)
        self.status_selected.set(Function.status_order_option[0])
        self.method_entry.delete(0, END)
        self.def_in_bid.set('0')
        self.date_order_entry.config(state="normal")
        self.date_order_entry.set_date(date.today())
        self.date_delivery_entry.config(mindate=datetime.strptime(self.date_order_entry.get(), "%d-%m-%Y"))
        self.date_delivery_entry.set_date(date.today() + timedelta(days=1))
        self.b_back_to_tracking.place_forget()
        self.edit_id_order_entry()

    def double_click_to_change_count(self, event):
        """דורש תיקון"""
        clicked = self.tree_products_in_new_order.identify_region(event.x, event.y)
        column = self.tree_products_in_new_order.identify_column(event.x)
        column_indx = int(column[1:]) - 1
        if clicked != "cell" or column_indx != 0:
            return
        try:
            selectedItem = self.tree_products_in_new_order.selection()[0]
        except:
            return
        selected_all_value = self.tree_products_in_new_order.item(selectedItem)["values"]

        box_cell = self.tree_products_in_new_order.bbox(selectedItem, column)

        entry_edit = Entry(self.tree_products_in_new_order, width=box_cell[2], justify=CENTER)
        entry_edit.place(x=box_cell[0], y=box_cell[1], width=box_cell[2], height=box_cell[3])
        entry_edit.editing_column_index = column_indx
        entry_edit.editing_item_iid = selectedItem
        entry_edit.insert(0, selected_all_value[column_indx])
        entry_edit.select_range(0, END)
        entry_edit.focus()
        entry_edit.bind("<FocusOut>", self.focus_out_from_edit_entry)
        entry_edit.bind("<Return>", self.focus_out_from_edit_entry)
        self.calculate_bid()

    def focus_out_from_edit_entry(self, event):
        if not self.is_float(event.widget.get()):
            event.widget.destroy()
            return
        selectedItem = event.widget.editing_item_iid
        self.tree_products_in_new_order.item(selectedItem, values=[event.widget.get()] + self.tree_products_in_new_order.item(selectedItem)['values'][1:])
        event.widget.destroy()
        self.calculate_bid()

    def calculate_bid(self):
        bid = 0
        for item in self.tree_products_in_new_order.get_children():
            bid += float(self.tree_products_in_new_order.item(item)["values"][1]) * float(self.tree_products_in_new_order.item(item)["values"][0])
        self.def_in_bid.set(str(bid))

    def validate_entrys(self):
        red = []
        for ent in [self.name_entry, self.price_entry]:
            if ent.get() == "": red.append(ent)
        if not self.is_float(self.price_entry.get()): red.append(self.price_entry)
        if self.phone_entry.get() != "" and (self.phone_entry.get()[:2] != "05" or len(self.phone_entry.get()) != 10): red.append(self.phone_entry)
        if Function.status_order_option.index(self.status_selected.get()) and self.method_entry.get() == "": red.append(self.method_entry)
        if len(self.tree_products_in_new_order.get_children()) == 0: self.lable_title_in.config(fg="red")

        if len(red) > 0:
            for ent in red:
                ent.config(bg="#FFB6B6")
            return False
        elif len(self.tree_products_in_new_order.get_children()) == 0: return False
        elif float(self.price_entry.get()) < float(self.bid_entry.get()):
            if not messagebox.askyesno("מחיר סופי נמוך", "המחיר הסופי נמוך מהצעת המחיר\nהאם להמשיך בכל זאת?"): return False
        return True

    def entrys_to_white(self):
        for we in [self.name_entry, self.phone_entry, self.price_entry, self.method_entry]:
            we.config(bg="white")
        self.lable_title_in.config(fg="black")

    def edit_id_order_entry(self, id=None):
        if id == None:
            id = str(int(Function.last_id_order()) + 1)
        self.id_order_entry.config(state="normal")
        self.id_order_entry.delete(0, END)
        self.id_order_entry.insert(0, id)
        self.id_order_entry.config(state="disabled")

    def save_order(self):
        self.entrys_to_white()
        if not self.validate_entrys():
            return
        dict_new_order = {}
        dict_new_order[self.id_order_entry.get()] = {"date_order" : self.date_order_entry.get(),
                                                     "name" : self.name_entry.get(),
                                                     "phone" : self.phone_entry.get(),
                                                     "date_delivery" : self.date_delivery_entry.get(),
                                                     "remarks" : self.remarks_text.get("1.0",END),
                                                     "price" : self.price_entry.get(),
                                                     "status" : Function.status_order_option.index(self.status_selected.get()),
                                                     "method" : self.method_entry.get()}
        products_in_order = []
        for item in self.tree_products_in_new_order.get_children():
            products_in_order.append({"name" : self.tree_products_in_new_order.item(item)['values'][3],
                                      "cost" : self.tree_products_in_new_order.item(item)['values'][2],
                                      "price" : self.tree_products_in_new_order.item(item)['values'][1],
                                      "amount" : self.tree_products_in_new_order.item(item)['values'][0]})
        dict_new_order[self.id_order_entry.get()]["products"] = products_in_order
        Function.write_order_to_json(dict_new_order)
        if int(self.id_order_entry.get()) == int(Function.last_id_order()) + 1:
            Function.update_id_order()
        self.clear_all()
        # self.edit_id_order_entry()

    def edit_order(self, id, tracking_order_screen):
        self.start()
        all_orders = Function.read_new_orders_from_json()
        self.edit_id_order_entry(id)
        self.name_entry.insert(0, all_orders[id]["name"])
        self.phone_entry.insert(0, all_orders[id]["phone"])
        self.remarks_text.insert('1.0', all_orders[id]["remarks"])
        self.price_entry.insert(0, all_orders[id]["price"])
        self.status_selected.set(Function.status_order_option[all_orders[id]["status"]])
        self.method_entry.insert(0, all_orders[id]["method"])
        self.date_order_entry.set_date(datetime.strptime(all_orders[id]["date_order"], "%d-%m-%Y"))
        self.date_order_entry.config(state="disabled")
        self.date_delivery_entry.set_date(datetime.strptime(all_orders[id]["date_delivery"], "%d-%m-%Y"))
        self.date_delivery_entry.config(mindate=date.today())
        for product in all_orders[id]["products"]:
            self.tree_products_in_new_order.insert("", END, values=(product["amount"], product["price"], product["cost"], product["name"]))
        self.calculate_bid()

        self.b_back_to_tracking.place(relx=.69, rely=.92)
        self.b_back_to_tracking.config(command=lambda: self.back_to_tracking_orders_screen(tracking_order_screen))

    def back_to_tracking_orders_screen(self, tracking_order_screen):
        self.close()
        tracking_order_screen.place(x=0, y=0)

    def is_float(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

