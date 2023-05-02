from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from datetime import *
import Function


class SearchOrderTop:
    def __init__(self, window):
        self.top = Toplevel(window)
        self.top.title('Ludiz.Foodiz - Search Order')
        width_win = 800
        height_win = 400
        x_cor = (self.top.winfo_screenwidth() / 2) - (width_win / 2)
        y_cor = (self.top.winfo_screenheight() / 2) - (height_win / 2)
        self.top.geometry(f"{width_win}x{height_win}+{int(x_cor)}+{int(y_cor) - 20}")
        self.top.resizable(False, False)
        self.top.configure(bg=Function.colors("color_screen"))
        self.top.withdraw()

        self.var_id = IntVar()
        self.cb_id = Checkbutton(self.top, variable=self.var_id, onvalue=1, offvalue=0, bg=Function.colors("color_screen"), command=lambda: self.open_lock(self.var_id.get(), self.id_order_entry))
        self.cb_id.place(x=700, y=40, anchor=CENTER)
        self.id_order_lable = Label(self.top, text="מספר הזמנה", bg=Function.colors("color_screen"), font=(None, 12))
        self.id_order_lable.place(x=700, y=70, anchor=CENTER)
        self.id_order_entry = Entry(self.top, width=18, justify="center", font=(None, 12), state="disabled")
        self.id_order_entry.place(x=700, y=100, anchor=CENTER)

        self.var_date_order = IntVar()
        self.cb_date_order = Checkbutton(self.top, variable=self.var_date_order, onvalue=1, offvalue=0, bg=Function.colors("color_screen"), command=lambda: self.open_lock(self.var_date_order.get(), self.date_order_entry))
        self.cb_date_order.place(x=500, y=40, anchor=CENTER)
        self.date_order_lable = Label(self.top, text="תאריך הזמנה מ", bg=Function.colors("color_screen"), font=(None, 12))
        self.date_order_lable.place(x=500, y=70, anchor=CENTER)
        self.date_order_entry = DateEntry(self.top, state="disabled", width=16, borderwidth=2, date_pattern='dd-MM-yyyy', justify="center", font=(None, 12), showweeknumbers=False, firstweekday='sunday', locale='he_IL', weekenddays=[7,7])
        self.date_order_entry.place(x=500, y=100, anchor=CENTER)
        self.var_date_order_2 = IntVar()
        self.cb_date_order_2 = Checkbutton(self.top, variable=self.var_date_order_2, onvalue=1, offvalue=0, bg=Function.colors("color_screen"), command=lambda: self.open_lock(self.var_date_order_2.get(), self.date_order_entry_2))
        self.cb_date_order_2.place(x=500, y=140, anchor=CENTER)
        self.date_order_lable_2 = Label(self.top, text="תאריך הזמנה עד", bg=Function.colors("color_screen"), font=(None, 12))
        self.date_order_lable_2.place(x=500, y=170, anchor=CENTER)
        self.date_order_entry_2 = DateEntry(self.top, state="disabled", width=16, borderwidth=2, date_pattern='dd-MM-yyyy', justify="center", font=(None, 12), showweeknumbers=False, firstweekday='sunday', locale='he_IL', weekenddays=[7,7])
        self.date_order_entry_2.place(x=500, y=200, anchor=CENTER)
        # self.date_order_entry.bind("<<DateEntrySelected>>", self.update_entrydate_delivery)

        self.var_name = IntVar()
        self.cb_name = Checkbutton(self.top, variable=self.var_name, onvalue=1, offvalue=0, bg=Function.colors("color_screen"), command=lambda: self.open_lock(self.var_name.get(), self.name_entry))
        self.cb_name.place(x=700, y=140, anchor=CENTER)
        self.name_lable = Label(self.top, text="שם לקוח", bg=Function.colors("color_screen"), font=(None, 12))
        self.name_lable.place(x=700, y=170, anchor=CENTER)
        self.name_entry = Entry(self.top, state="disabled", width=18, justify="right", font=(None, 12))
        self.name_entry.place(x=700, y=200, anchor=CENTER)

        self.var_date_delivery = IntVar()
        self.cb_date_delivery = Checkbutton(self.top, variable=self.var_date_delivery, onvalue=1, offvalue=0, bg=Function.colors("color_screen"), command=lambda: self.open_lock(self.var_date_delivery.get(), self.date_delivery_entry))
        self.cb_date_delivery.place(x=300, y=40, anchor=CENTER)
        self.date_delivery_lable = Label(self.top, text="תאריך אספקה מ", bg=Function.colors("color_screen"), font=(None, 12))
        self.date_delivery_lable.place(x=300, y=70, anchor=CENTER)
        self.date_delivery_entry = DateEntry(self.top, state="disabled", width=16, borderwidth=2, date_pattern='dd-MM-yyyy', justify="center", font=(None, 12), showweeknumbers=False, year=datetime.today().year, month=datetime.today().month, day=datetime.today().day+1, firstweekday='sunday', locale='he_IL', weekenddays=[7,7])
        self.date_delivery_entry.place(x=300, y=100, anchor=CENTER)
        self.var_date_delivery_2 = IntVar()
        self.cb_date_delivery_2 = Checkbutton(self.top, variable=self.var_date_delivery_2, onvalue=1, offvalue=0, bg=Function.colors("color_screen"), command=lambda: self.open_lock(self.var_date_delivery_2.get(), self.date_delivery_entry_2))
        self.cb_date_delivery_2.place(x=300, y=140, anchor=CENTER)
        self.date_delivery_lable_2 = Label(self.top, text="תאריך אספקה עד", bg=Function.colors("color_screen"), font=(None, 12))
        self.date_delivery_lable_2.place(x=300, y=170, anchor=CENTER)
        self.date_delivery_entry_2 = DateEntry(self.top, state="disabled", width=16, borderwidth=2, date_pattern='dd-MM-yyyy', justify="center", font=(None, 12), showweeknumbers=False, year=datetime.today().year, month=datetime.today().month, day=datetime.today().day+1, firstweekday='sunday', locale='he_IL', weekenddays=[7,7])
        self.date_delivery_entry_2.place(x=300, y=200, anchor=CENTER)

        self.var_status = IntVar()
        self.cb_status = Checkbutton(self.top, variable=self.var_status, onvalue=1, offvalue=0, bg=Function.colors("color_screen"), command=lambda: self.open_lock(self.var_status.get(), self.status_drop))
        self.cb_status.place(x=100, y=40, anchor=CENTER)
        self.status_lable = Label(self.top, text="סטטוס", bg=Function.colors("color_screen"), font=(None, 12))
        self.status_lable.place(x=100, y=70, anchor=CENTER)
        self.status_selected = StringVar()
        self.status_drop = OptionMenu(self.top, self.status_selected, *Function.status_order_option)
        # self.status_drop = ttk.Combobox(self.top, self.status_selected, *Function.status_order_option)
        self.status_drop.config(width=22)
        self.status_drop.place(x=100, y=100, anchor=CENTER)
        self.status_drop.config(state="disabled")

        self.var_method = IntVar()
        self.cb_method = Checkbutton(self.top, variable=self.var_method, onvalue=1, offvalue=0, bg=Function.colors("color_screen"), command=lambda: self.open_lock(self.var_method.get(), self.method_entry))
        self.cb_method.place(x=100, y=140, anchor=CENTER)
        self.method_lable = Label(self.top, text="אמצעי תשלום", bg=Function.colors("color_screen"), font=(None, 12))
        self.method_lable.place(x=100, y=170, anchor=CENTER)
        self.method_entry = Entry(self.top, state="disabled", width=18, justify="right", font=(None, 12))
        self.method_entry.place(x=100, y=200, anchor=CENTER)

        self.b_search = Button(self.top, text="חיפוש", bg=Function.colors("color_menu_tracking_orders"), font=(None, 16, "bold"), width=12, height=4, command=self.search)
        self.b_search.place(x=100, y=300, anchor=CENTER)


        self.option_select_filter = ["כל ההזמנות", "הזמנות להיום ולמחר", "הזמנות פתוחות"]
        self.monthchoosen = ttk.Combobox(self.top, width=35, justify="right", state="readonly")
        self.monthchoosen['values'] = self.option_select_filter
        self.monthchoosen.place(x=600, y=300, anchor=CENTER)
        self.monthchoosen.set("ניתן לבחור חיפוש מוגדר מראש")

        self.b_search = Button(self.top, text="הצב פילטר", bg=Function.colors("color_menu_tracking_orders"), font=(None, 12), width=8, height=1, command=self.filters_from_saved)
        self.b_search.place(x=400, y=300, anchor=CENTER)



    def start(self):
        self.top.deiconify()
        self.top.grab_set()

    def search(self):
        self.top.destroy()

    def open_lock(self, var, entry):
        if var: entry.config(state="normal")
        else:
            try: entry.delete(0, END)
            except: self.status_selected.set("")
            entry.config(state="disabled")

    def filters_from_saved(self):
        try: print(self.option_select_filter.index(self.monthchoosen.get()))
        except: pass


if __name__ == '__main__':
    window = Tk()
    SearchOrderTop(window)
    window.mainloop()
