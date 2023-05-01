from tkinter import *
from tkcalendar import DateEntry
from tkinter.ttk import Treeview, Style, OptionMenu
from datetime import *
import Function


class SearchOrderTop:
    def __init__(self, window):
        self.top = Toplevel(window)
        self.top.title('Ludiz.Foodiz - Search Order')
        width_win = 300
        height_win = 200
        x_cor = (self.top.winfo_screenwidth() / 2) - (width_win / 2)
        y_cor = (self.top.winfo_screenheight() / 2) - (height_win / 2)
        self.top.geometry(f"{width_win}x{height_win}+{int(x_cor)}+{int(y_cor) - 20}")
        self.top.resizable(False, False)
        self.top.grab_set()


        self.id_order_lable = Label(self.top, text="מספר הזמנה", bg=Function.colors("color_screen"), font=(None, 12))
        self.id_order_lable.grid(row=0, column=1)
        self.id_order_entry = Entry(self.top, width=18, justify="center", font=(None, 12))
        self.id_order_entry.grid(row=0, column=0)

        self.date_order_lable = Label(self.top, text="תאריך הזמנה", bg=Function.colors("color_screen"), font=(None, 12))
        self.date_order_lable.grid(row=1, column=1)
        self.date_order_entry = DateEntry(self.top, width=16, borderwidth=2, date_pattern='dd-MM-yyyy', justify="center", font=(None, 12), showweeknumbers=False, firstweekday='sunday', locale='he_IL', weekenddays=[7,7])
        self.date_order_entry.grid(row=1, column=0)
        # self.date_order_entry.bind("<<DateEntrySelected>>", self.update_entrydate_delivery)

        self.name_lable = Label(self.top, text="שם לקוח", bg=Function.colors("color_screen"), font=(None, 12))
        self.name_lable.grid(row=2, column=1)
        self.name_entry = Entry(self.top, width=18, justify="right", font=(None, 12))
        self.name_entry.grid(row=2, column=0)

        self.phone_lable = Label(self.top, text="מספר טלפון", bg=Function.colors("color_screen"), font=(None, 12))
        self.phone_lable.grid(row=3, column=1)
        self.phone_entry = Entry(self.top, width=18, justify="right", font=(None, 12))
        self.phone_entry.grid(row=3, column=0)

        self.date_delivery_lable = Label(self.top, text="תאריך אספקה", bg=Function.colors("color_screen"), font=(None, 12))
        self.date_delivery_lable.grid(row=4, column=1)
        self.date_delivery_entry = DateEntry(self.top, width=16, borderwidth=2, date_pattern='dd-MM-yyyy', justify="center", font=(None, 12), showweeknumbers=False, year=datetime.today().year, month=datetime.today().month, day=datetime.today().day+1, firstweekday='sunday', mindate=datetime.strptime(self.date_order_entry.get(), "%d-%m-%Y"), locale='he_IL', weekenddays=[7,7])
        self.date_delivery_entry.grid(row=4, column=0)

        self.status_lable = Label(self.top, text="סטטוס", bg=Function.colors("color_screen"), font=(None, 12))
        self.status_lable.grid(row=5, column=1)
        self.options_status_drop_list = ["פתוח", "סגור - בוצע תשלום"]
        self.status_selected = StringVar()
        self.status_drop = OptionMenu(self.top, self.status_selected, self.options_status_drop_list[0], *self.options_status_drop_list)
        self.status_drop.config(width=22)
        self.status_drop.grid(row=5, column=0)

        self.method_lable = Label(self.top, text="אמצעי תשלום", bg=Function.colors("color_screen"), font=(None, 12))
        self.method_lable.grid(row=6, column=1)
        self.method_entry = Entry(self.top, width=18, justify="right", font=(None, 12))
        self.method_entry.grid(row=6, column=0)

    def start(self):
        # self.main_screen.place(x=0, y=0)
        pass


if __name__ == '__main__':
    window = Tk()
    SearchOrderTop(window)
    window.mainloop()
