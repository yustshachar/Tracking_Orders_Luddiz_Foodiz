from tkinter import Frame, Label, CENTER, Scrollbar, Entry, Button, Text, scrolledtext, WORD, END, StringVar
from tkinter.ttk import Treeview, Style, OptionMenu
from tkcalendar import DateEntry
from datetime import *
# from Program import *
import Function


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
        self.tree_products_in_new = Treeview(self.new_order_screen, columns=(3, 2, 1), show='headings', height=30, style="Custom3.Treeview")
        self.tree_products_in_new.column("1", anchor=CENTER, width=290)
        self.tree_products_in_new.heading("1", text="שם המוצר")
        self.tree_products_in_new.column("2", anchor=CENTER, width=75)
        self.tree_products_in_new.heading("2", text="מחיר")
        self.tree_products_in_new.column("3", anchor=CENTER, width=75)
        self.tree_products_in_new.heading("3", text="כמות")
        self.tree_products_in_new.place(relx=.3, rely=.51, anchor=CENTER)
        self.vsb1 = Scrollbar(self.new_order_screen, orient="vertical", command=self.tree_products_in_new.yview)
        self.vsb1.place(relx=.556, rely=.53, anchor=CENTER, height=664)
        self.tree_products_in_new.configure(yscrollcommand=self.vsb1.set)


        # שדות
        self.id_order_lable = Label(self.new_order_screen, text="מספר הזמנה", bg=Function.colors("color_screen"), font=(None, 12))
        self.id_order_lable.place(relx=0.85, rely=0.1)
        self.id_order_entry = Entry(self.new_order_screen, width=18, justify="center", font=(None, 12))
        self.id_order_entry.insert(0, Function.last_id_order())
        self.id_order_entry.config(state="disabled")
        self.id_order_entry.place(relx=0.63, rely=0.1)

        self.date_order_lable = Label(self.new_order_screen, text="תאריך הזמנה", bg=Function.colors("color_screen"), font=(None, 12))
        self.date_order_lable.place(relx=0.85, rely=0.15)
        self.date_order_entry = DateEntry(self.new_order_screen, width=16, borderwidth=2, date_pattern='dd-MM-yyyy', justify="center", font=(None, 12), showweeknumbers=False, firstweekday='sunday', mindate=datetime.today(), locale='he_IL', weekenddays=[7,7])
        self.date_order_entry.place(relx=0.63, rely=0.15)

        self.name_lable = Label(self.new_order_screen, text="שם לקוח", bg=Function.colors("color_screen"), font=(None, 12))
        self.name_lable.place(relx=0.85, rely=0.25)
        self.name_entry = Entry(self.new_order_screen, width=18, justify="right", font=(None, 12))
        self.name_entry.place(relx=0.63, rely=0.25)

        self.phone_lable = Label(self.new_order_screen, text="מספר טלפון", bg=Function.colors("color_screen"), font=(None, 12))
        self.phone_lable.place(relx=0.85, rely=0.3)
        self.phone_entry = Entry(self.new_order_screen, width=18, justify="right", font=(None, 12))
        self.phone_entry.place(relx=0.63, rely=0.3)

        self.date_delivery_lable = Label(self.new_order_screen, text="תאריך אספקה", bg=Function.colors("color_screen"), font=(None, 12))
        self.date_delivery_lable.place(relx=0.85, rely=0.35)
        self.date_delivery_entry = DateEntry(self.new_order_screen, width=16, borderwidth=2, date_pattern='dd-MM-yyyy', justify="center", font=(None, 12), showweeknumbers=False, year=datetime.today().year, month=datetime.today().month, day=datetime.today().day+1, firstweekday='sunday', mindate=datetime.today(), locale='he_IL', weekenddays=[7,7])
        self.date_delivery_entry.place(relx=0.63, rely=0.35)

        self.remarks_lable = Label(self.new_order_screen, text="הערות", bg=Function.colors("color_screen"), font=(None, 12))
        self.remarks_lable.place(relx=0.85, rely=0.4)
        # self.remarks_entry = Entry(self.new_order_screen, width=15, justify="right", font=(None, 12))
        # self.remarks_entry.place(relx=0.65, rely=0.4)
        self.remarks_text = Text(self.new_order_screen, width=18, height=6, font=(None, 12), wrap=WORD)
        self.remarks_text.place(relx=0.63, rely=0.4)

        self.price_lable = Label(self.new_order_screen, text="מחיר סופי", bg=Function.colors("color_screen"), font=(None, 12))
        self.price_lable.place(relx=0.85, rely=0.6)
        self.price_entry = Entry(self.new_order_screen, width=18, justify="center", font=(None, 12))
        self.price_entry.place(relx=0.63, rely=0.6)

        self.status_lable = Label(self.new_order_screen, text="סטטוס", bg=Function.colors("color_screen"), font=(None, 12))
        self.status_lable.place(relx=0.85, rely=0.65)
        self.options_drop_list = ["לא שולם", "שולם"]
        self.status_selected = StringVar()
        self.status_drop = OptionMenu(self.new_order_screen, self.status_selected, self.options_drop_list[0], *self.options_drop_list)
        self.status_drop.config(width=22)
        self.status_drop.place(relx=0.63, rely=0.645)

        self.method_lable = Label(self.new_order_screen, text="אמצעי תשלום", bg=Function.colors("color_screen"), font=(None, 12))
        self.method_lable.place(relx=0.85, rely=0.7)
        self.method_entry = Entry(self.new_order_screen, width=18, justify="right", font=(None, 12))
        self.method_entry.place(relx=0.63, rely=0.7)

        self.b_save_order = Button(self.new_order_screen, text="שמור", bg=Function.colors("color_btn_menu"), fg='white', font=(None, 16, "bold"), width=7)
        self.b_save_order.place(relx=.64, rely=.8)

        self.b_clear_to_new = Button(self.new_order_screen, text="נקה", bg=Function.colors("color_btn_menu"), fg='white', font=(None, 16, "bold"), width=7)
        self.b_clear_to_new.place(relx=.83, rely=.8)

        self.b_delete_products = Button(self.new_order_screen, text="מחק פריט", bg=Function.colors("color_menu_tracking_orders"), fg='red', font=(None, 10, "bold"), command=self.delete_selected_product_from_order_in_new)
        self.b_delete_products.place(relx=.054, rely=.952)




        # רשימת כל המוצרים
        self.style = Style()
        self.style.theme_use("clam")
        self.style.configure("Custom2.Treeview", rowheight=21, font=(None, 11), background=Function.colors("color_screen"), fieldbackground=Function.colors("color_screen"))
        self.style.configure('Custom2.Treeview.Heading', font=(None, 12, 'bold'))

        self.lable_title_all = Label(self.all_products_frame, text=":רשימת כל המוצרים", bg=Function.colors("color_menu_tracking_orders"), font=(None, 14, 'bold'))
        self.lable_title_all.place(relx=0.25, rely=0.032)
        self.tree_all_products_in_new = Treeview(self.all_products_frame, columns=(2, 1), show='headings', height=32, style="Custom2.Treeview")
        self.tree_all_products_in_new.column("1", anchor=CENTER, width=282)
        self.tree_all_products_in_new.heading("1", text="שם המוצר")
        self.tree_all_products_in_new.column("2", anchor=CENTER, width=70)
        self.tree_all_products_in_new.heading("2", text="מחיר")
        self.tree_all_products_in_new.place(relx=.48, rely=.52, anchor=CENTER)
        self.vsb = Scrollbar(self.all_products_frame, orient="vertical", command=self.tree_all_products_in_new.yview)
        self.vsb.place(relx=.947, rely=.539, anchor=CENTER, height=671)
        self.tree_all_products_in_new.configure(yscrollcommand=self.vsb.set)

        # אירוע בעת לחיצה כפולה
        self.tree_all_products_in_new.bind("<Double-1>", self.add_product_to_order)







    def start(self):
        self.new_order_screen.place(x=400, y=0)
        self.all_products_frame.place(x=0, y=0)
        self.clear_all()
        self.add_all_products()

    def close(self):
        self.new_order_screen.place_forget()
        self.all_products_frame.place_forget()

    def delete_selected_product_from_order_in_new(self):
        try: selected_item = self.tree_products_in_new.selection()[0]
        except: return
        self.tree_products_in_new.delete(selected_item)


    def add_all_products(self):
        for item in self.tree_all_products_in_new.get_children():
            self.tree_all_products_in_new.delete(item)
        for name in Function.read_all_products_from_json().keys():
            self.tree_all_products_in_new.insert("", END, values=[Function.read_all_products_from_json()[name]["price"], name])

    def add_product_to_order(self, event):
        try: selected_item = self.tree_all_products_in_new.selection()[0]
        except: return
        self.tree_products_in_new.insert("", END, values=[1]+self.tree_all_products_in_new.item(selected_item)['values'])
        self.tree_all_products_in_new.delete(selected_item)

    def clear_all(self):
        for item in self.tree_products_in_new.get_children():
            self.tree_products_in_new.delete(item)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.remarks_text.delete('1.0', END)
        self.price_entry.delete(0, END)
        self.status_selected.set(self.options_drop_list[0])
        self.method_entry.delete(0, END)

