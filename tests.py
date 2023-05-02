import csv
import json
from tkinter import *
from tkinter.ttk import Treeview, Style
import Function
###################read
# all_products = []
# with open("AllProducts.csv", "r", encoding='utf8') as r_ap:
#     csvreader = csv.reader(r_ap)
#     for i in csvreader:
#         all_products.append(i)
# print(all_products)


##################write
# all_products = [['מוצר כלשהו', ' 45'], ['מוצר אחר', ' 12'], ['והשלישי הוא כזה', ' 50']]
# all_products.append(["בדיקה של מוצר בעברית", 34])
#
# with open("AllProducts.csv", "w", newline="", encoding='utf8') as w_ap:
#     csvwriter = csv.writer(w_ap)
#     csvwriter.writerows(all_products)


################################################################################
from tkcalendar import DateEntry
from datetime import *
from tkinter import ttk
# from tkinter import *
# with open("AllProducts.json", encoding="utf8") as r_nf:
#     all_products = json.loads(r_nf.read())
#
# window = Tk()
# window.title('Ludiz.Foodiz')
# width_win = 500
# height_win = 500
# # מיקום במרכז המסך לפי הקורדינטות ונעילת אפשרות לשנות גודל
# x_cor = (window.winfo_screenwidth() / 2) - (width_win / 2)
# y_cor = (window.winfo_screenheight() / 2) - (height_win / 2)
# window.geometry(f"{width_win}x{height_win}+{int(x_cor)}+{int(y_cor) - 20}")
#
# # date_delivery_entry = DateEntry(window, width=16, borderwidth=2, date_pattern='dd-MM-yyyy',
# #                                      justify="center", font=(None, 12), showweeknumbers=False,
# #                                      year=datetime.today().year, month=datetime.today().month,
# #                                      day=datetime.today().day, firstweekday='sunday',
# #                                      locale='he_IL',
# #                                      weekenddays=[7, 7])
# # date_delivery_entry.place(relx=0.4, rely=0.4)
# # date_delivery_entry.delete(0, "")
#
# style = ttk.Style(window)
# style.configure('Treeview', rowheight=20)
# tree_products_in_new_order = Treeview(window, show='headings', height=20, columns=(1),
#                                            style="Custom3.Treeview")
# tree_products_in_new_order.column("1", anchor=CENTER, width=300)
# tree_products_in_new_order.heading("1", text="שם המוצר")
# tree_products_in_new_order.place(relx=.4, rely=.51, anchor=CENTER)
#
# tree_products_in_new_order.insert("", END, values=("aaaaaaa aaaaaaaaaaaa aaaaaaaaaa aaaaaaa bbbbbbbbbb ccccccccccccc"))
#
# window.mainloop()


###############################################################################

# d1 = {"product1": {"cost": "12","price": "20"},"product2": {"cost": "40","price": "90"},"product3":{"cost": "6","price": "12"},"product4": {"cost": "20","price": "34"}}
# name = "product5"

# with open("AllProducts.json", encoding="utf8") as r_nf:
#     all_products = json.loads(r_nf.read())
#
#
# print(all_products)
# print(all_products["product1"])
# print(type(all_products["product1"]))
# print(all_products["product1"]["cost"])
# print(type(all_products["product1"]["cost"]))

# print(sorted(Function.read_all_products_from_json()))

###################################


