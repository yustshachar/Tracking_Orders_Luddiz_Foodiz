import csv
import json
from tkinter import *
from tkinter.ttk import Treeview, Style
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

# with open("AllProducts.json", encoding="utf8") as r_nf:
#     all_products = json.loads(r_nf.read())
#
# window = Tk()
# window.title('Ludiz.Foodiz')
# width_win = 1500
# height_win = 800
# # מיקום במרכז המסך לפי הקורדינטות ונעילת אפשרות לשנות גודל
# x_cor = (window.winfo_screenwidth() / 2) - (width_win / 2)
# y_cor = (window.winfo_screenheight() / 2) - (height_win / 2)
# window.geometry(f"{width_win}x{height_win}+{int(x_cor)}+{int(y_cor) - 20}")
#
# tree_all_products = Treeview(window, columns=(2,1), show='headings', height=25)
# tree_all_products.column("1", anchor=CENTER, width=500)
# tree_all_products.heading("1", text="שם המוצר")
# tree_all_products.column("2", anchor=CENTER, width=120)
# tree_all_products.heading("2", text="מחיר")
# tree_all_products.place(relx=.7, rely=.52, anchor= CENTER)
#
#
# for name in all_products.keys():
#     tree_all_products.insert("", END, values=[all_products[name]["price"], name])
#
# window.mainloop()


###############################################################################

# d1 = {"product1": {"cost": "12","price": "20"},"product2": {"cost": "40","price": "90"},"product3":{"cost": "6","price": "12"},"product4": {"cost": "20","price": "34"}}
# name = "product5"

with open("AllProducts.json", encoding="utf8") as r_nf:
    all_products = json.loads(r_nf.read())


print(all_products)
print(all_products["product1"])
print(type(all_products["product1"]))
print(all_products["product1"]["cost"])
print(type(all_products["product1"]["cost"]))
