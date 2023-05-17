# from Program import *
from tkinter import Frame, Label, Entry, Button, CENTER, Scrollbar, END, messagebox
from tkinter.ttk import Treeview, Style
import Function
from tkcalendar import DateEntry


class TrackingExpenseScreen:
    def __init__(self, window):
        self.tracking_expense_screen = Frame(window, width=1300, height=800, bg=Function.colors("color_screen"))

        self.lable_search = Label(self.tracking_expense_screen, text=":חיפוש מוצר", bg=Function.colors("color_screen"))
        self.lable_search.place(relx=0.62, rely=0.023)
        self.entry_search = Entry(self.tracking_expense_screen, width=35, justify='right')
        self.entry_search.place(relx=0.45, rely=0.025)
        self.b_search = Button(self.tracking_expense_screen, text="חיפוש", bg=Function.colors("color_btn_menu"), fg='#ffffff', command=self.search_product_or_shop_in_expense_screen)
        self.b_search.place(relx=.4, rely=.02)
        self.b_reset_search = Button(self.tracking_expense_screen, text="איפוס", bg=Function.colors("color_btn_menu"), fg='#ffffff', command=self.add_all_expense)
        self.b_reset_search.place(relx=.35, rely=.02)

        self.style = Style()
        self.style.theme_use("clam")
        self.style.configure("expense.Treeview", rowheight=25, font=(None, 12))
        self.style.configure('expense.Treeview.Heading', background=Function.colors("color_nenu_screen"), font=(None, 13, 'bold'))

        self.tree_all_expense = Treeview(self.tracking_expense_screen, columns=(7,6,5,4,3,2,1), show='headings', height=23, style="expense.Treeview")
        self.tree_all_expense.column("1", anchor=CENTER, width=100)
        self.tree_all_expense.heading("1", text="תאריך")
        self.tree_all_expense.column("2", anchor=CENTER, width=200)
        self.tree_all_expense.heading("2", text="חנות")
        self.tree_all_expense.column("3", anchor=CENTER, width=500)
        self.tree_all_expense.heading("3", text="מוצר")
        self.tree_all_expense.column("4", anchor=CENTER, width=100)
        self.tree_all_expense.heading("4", text="כמות")
        self.tree_all_expense.column("5", anchor=CENTER, width=100)
        self.tree_all_expense.heading("5", text="מידה")
        self.tree_all_expense.column("6", anchor=CENTER, width=100)
        self.tree_all_expense.heading("6", text="מחיר כולל")
        self.tree_all_expense.column("7", anchor=CENTER, width=100)
        self.tree_all_expense.heading("7", text="מחיר ליחידה")

        self.tree_all_expense.place(relx=.5, rely=.45, anchor=CENTER)
        self.vsb = Scrollbar(self.tracking_expense_screen, orient="vertical", command=self.tree_all_expense.yview)
        self.vsb.place(relx=.97, rely=.47, anchor=CENTER, height=580)
        self.tree_all_expense.configure(yscrollcommand=self.vsb.set)

        # # אירוע בעת לחיצה כפולה
        # self.tree_all_expense.bind("<Double-1>", self.double_click_on_cell)

        self.lable_date = Label(self.tracking_expense_screen, text=":תאריך", bg=Function.colors("color_screen"), font=(None, 13))
        self.lable_date.place(relx=0.92, rely=0.86, anchor=CENTER)
        self.entry_date = DateEntry(self.tracking_expense_screen, width=10, borderwidth=2, date_pattern='dd-MM-yyyy', justify="center", font=(None, 12), showweeknumbers=False, firstweekday='sunday', locale='he_IL', weekenddays=[7,7])
        self.entry_date.place(relx=0.92, rely=0.89, anchor=CENTER)
        # self.entry_date = Entry(self.tracking_expense_screen, width=12, justify="right", font=(None, 12))
        # self.entry_date.place(relx=0.92, rely=0.89, anchor=CENTER)
        self.lable_shop = Label(self.tracking_expense_screen, text=":חנות", bg=Function.colors("color_screen"), font=(None, 13))
        self.lable_shop.place(relx=0.8, rely=0.86, anchor=CENTER)
        self.entry_shop = Entry(self.tracking_expense_screen, width=21, justify='right', font=(None, 12))
        self.entry_shop.place(relx=0.8, rely=0.89, anchor=CENTER)
        self.lable_product = Label(self.tracking_expense_screen, text=":מוצר", bg=Function.colors("color_screen"), font=(None, 13))
        self.lable_product.place(relx=0.54, rely=0.86, anchor=CENTER)
        self.entry_product = Entry(self.tracking_expense_screen, width=52, justify='right', font=(None, 12))
        self.entry_product.place(relx=0.54, rely=0.89, anchor=CENTER)
        self.lable_amount = Label(self.tracking_expense_screen, text=":כמות", bg=Function.colors("color_screen"), font=(None, 13))
        self.lable_amount.place(relx=0.31, rely=0.86, anchor=CENTER)
        self.entry_amount = Entry(self.tracking_expense_screen, width=12, justify='right', font=(None, 12))
        self.entry_amount.place(relx=0.31, rely=0.89, anchor=CENTER)
        self.lable_type = Label(self.tracking_expense_screen, text=":מידה", bg=Function.colors("color_screen"), font=(None, 13))
        self.lable_type.place(relx=0.22, rely=0.86, anchor=CENTER)
        self.entry_type = Entry(self.tracking_expense_screen, width=12, justify='right', font=(None, 12))
        self.entry_type.place(relx=0.22, rely=0.89, anchor=CENTER)
        self.lable_price = Label(self.tracking_expense_screen, text=":מחיר כולל", bg=Function.colors("color_screen"), font=(None, 13))
        self.lable_price.place(relx=0.13, rely=0.86, anchor=CENTER)
        self.entry_price = Entry(self.tracking_expense_screen, width=12, justify='right', font=(None, 12))
        self.entry_price.place(relx=0.13, rely=0.89, anchor=CENTER)

        self.b_save = Button(self.tracking_expense_screen, text="שמור חדש", width=8, height=1, bg=Function.colors("color_btn_menu"), fg='#ffffff', font=(None, 14, 'bold'), command=self.save_new_record)
        self.b_save.place(relx=.57, rely=.92)
        self.b_reset_add = Button(self.tracking_expense_screen, text="ניקוי שדות", width=8, height=1, bg=Function.colors("color_btn_menu"), fg='#ffffff', font=(None, 14, 'bold'))
        self.b_reset_add.place(relx=.45, rely=.92)
        self.b_reset_del = Button(self.tracking_expense_screen, text="מחק מוצר", width=8, height=1, bg=Function.colors("color_btn_menu"), fg='#ffffff', font=(None, 14, 'bold'), command=self.delete_row)
        self.b_reset_del.place(relx=.33, rely=.92)


    def start(self):
        self.tracking_expense_screen.place(x=0, y=0)
        self.add_all_expense()
        self.clear_entrys()

    def close(self):
        self.tracking_expense_screen.place_forget()

    def add_all_expense(self):
        all_expense = Function.read_all_expense_from_json()
        for item in self.tree_all_expense.get_children():
            self.tree_all_expense.delete(item)
        for i in all_expense:
            self.tree_all_expense.insert("", 0, values=[float(i[5])/float(i[3])] + i[::-1])
        self.clear_entrys()

    def save_new_record(self):
        if self.entry_date.get() == "" or self.entry_shop.get() == "" or self.entry_product.get() == "" or self.entry_amount.get() == "" or self.entry_type.get() == "" or self.entry_price.get() == "":
            return
        list_record = [self.entry_date.get(), self.entry_shop.get(), self.entry_product.get(), self.entry_amount.get(), self.entry_type.get(), self.entry_price.get()]
        Function.add_one_expense_to_json(list_record)
        self.clear_entrys()
        self.add_all_expense()

    def clear_entrys(self):
        self.entry_date.delete(0, END)
        self.entry_shop.delete(0, END)
        self.entry_product.delete(0, END)
        self.entry_amount.delete(0, END)
        self.entry_type.delete(0, END)
        self.entry_price.delete(0, END)
        self.entry_search.delete(0, END)

    def search_product_or_shop_in_expense_screen(self):
        for item in self.tree_all_expense.get_children():
            self.tree_all_expense.delete(item)
        all_products = Function.read_all_expense_from_json()
        for name in all_products:
            for cell in name:
                if self.entry_search.get() in cell:
                    self.tree_all_expense.insert("", 0, values=[float(name[5])/float(name[3])] + name[::-1])
                    break

    def delete_row(self):
        try:
            selectedItem = self.tree_all_expense.selection()[0]
            if not messagebox.askokcancel("מחיקת הוצאה", "האם למחוק את ההוצאה?\nלא יהיה ניתן לשחזר לאחר מחיקה"): return
            all_rows = Function.read_all_expense_from_json()
            all_rows.remove([str(a) for a in self.tree_all_expense.item(selectedItem)['values'][:0:-1]])
            Function.write_expenses_to_json(all_rows)
            self.add_all_expense()
        except: return

