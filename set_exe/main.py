import json
import csv
from datetime import datetime, date
import configparser
from tkinter import *
from tkinter.ttk import Treeview, Style

######## colors
color_screen = "#DAEFF6"
color_nenu_screen = "#9AD0E2"
color_btn_menu = "#2483A4"
color_menu_tracking_orders = "#B8E1EF"


#############

def read_all_products_from_json():
    with open("AllProducts.json", encoding="utf8") as r_nf:
        return json.loads(r_nf.read())


def read_new_orders_from_json():
    with open("NewOrders.json", encoding="utf8") as r_nf:
        return json.loads(r_nf.read())


# קריאת ההזמנות מהקובץ
# with open("NewOrders.json", encoding="utf8") as r_nf:
#     new_orders = json.loads(r_nf.read())

# קריאת ההזמנות הקודמות מהקובץ
# with open("PreviousOrders.json", "r") as previous_orders_file:
#     previous_orders = json.load(previous_orders_file)

inif = configparser.ConfigParser()
inif.read('Tracking_Order.ini')


def write_product_to_csv():
    list_products = []
    for child in tree_all_products.get_children():
        list_products.append([tree_all_products.item(child)["values"][1], tree_all_products.item(child)["values"][0]])
    with open("AllProducts.csv", "w", newline="", encoding='utf8') as w_ap:
        csvwriter = csv.writer(w_ap)
        csvwriter.writerows(list_products)


def write_products_to_json(dict_products):
    with open("AllProducts.json", "wb") as w_no:
        w_no.write(json.dumps(dict_products, ensure_ascii=False).encode("utf-8"))


def write_to_order(ID_order, date_order, name, phone, date_delivery, remarks, price, method, procucts, status = 0):
    pass


def new_id_order():
    """מחזירה את הID של ההזמנה החדשה"""
    return int(inif["last_ID"]["order"])+1


# for i in new_orders:
#     if datetime.strptime(new_orders[i]["date_delivery"], "%d-%m-%Y").date() == date.today():
#         print(i)

# תאריך של היום והפורמט
# print(datetime.today().strftime("%d-%m-%Y"))

# print(new_orders["4"]["name"])
# new_orders["3"]["name"] = "אברהם"
# new_orders["4"]["products"].append({"name":"מארז", "price":22})

# with open("AllProducts.json", "w") as all_products_file:
#     json.dump(all_products, all_products_file)


# with open("NewOrders.json", "wb") as w_no:
#     w_no.write(json.dumps(new_orders, ensure_ascii=False).encode("utf-8"))

# with open("PreviousOrders.json", "w") as previous_orders_file:
#     json.dump(previous_orders, previous_orders_file)

# with open('Tracking_Order.ini', 'w') as configfile:
#     inif.write(configfile)



def show_mains_screens(screen):
    main_screen.place_forget()
    new_order_screen.place_forget()
    tracking_order_screen.place_forget()
    products_screen.place_forget()
    reports_screen.place_forget()
    menu_in_tracking_orders.place_forget()
    main_page_tracking_orders.place_forget()
    today_and_tomorow_screen.place_forget()
    future_orders_screen.place_forget()
    all_orders_screen.place_forget()
    not_pay_orders_screen.place_forget()
    search_orders_screen.place_forget()
    screen.place(x=0, y=0)
    if screen == tracking_order_screen:
        menu_in_tracking_orders.place(x=1100, y=0)
        main_page_tracking_orders.place(x=0, y=0)
    elif screen == products_screen:
        add_products_to_tree_products_screen()
        clear_entry_product()
    elif screen == new_order_screen:
        add_products_to_tree_new_order_screen()


###############################################
window = Tk()
window.title('Ludiz.Foodiz')
width_win = 1500
height_win = 800
# מיקום במרכז המסך לפי הקורדינטות ונעילת אפשרות לשנות גודל
x_cor = (window.winfo_screenwidth() / 2) - (width_win / 2)
y_cor = (window.winfo_screenheight() / 2) - (height_win / 2)
window.geometry(f"{width_win}x{height_win}+{int(x_cor)}+{int(y_cor) - 20}")
window.resizable(False, False)


frame_menu = Frame(window, width=200, height=800, bg=color_nenu_screen)
frame_menu.place(x=1300, y=0)

main_screen = Frame(window, width=1300, height=800, bg=color_screen)
main_screen.place(x=0, y=0)

new_order_screen = Frame(window, width=1300, height=800, bg=color_screen)
tracking_order_screen = Frame(window, width=1300, height=800, bg=color_screen)
products_screen = Frame(window, width=1300, height=800, bg=color_screen)
reports_screen = Frame(window, width=1300, height=800, bg=color_screen)

b_main = Button(frame_menu, text="ראשי", command=lambda: show_mains_screens(main_screen), width=12, height=3, font=("Narkisim", 15, 'bold'), bg=color_btn_menu, fg='#ffffff')
b_main.place(relx=.5, rely=.1,anchor= CENTER)
b_new_order = Button(frame_menu, text="הזמנה חדשה", command=lambda: show_mains_screens(new_order_screen), width=12, height=3, font=("Narkisim", 15, 'bold'), bg=color_btn_menu, fg='#ffffff')
b_new_order.place(relx=.5, rely=.25,anchor= CENTER)
b_tracking_order = Button(frame_menu, text="מעקב הזמנות", command=lambda: show_mains_screens(tracking_order_screen), width=12, height=3, font=("Narkisim", 15, 'bold'), bg=color_btn_menu, fg='#ffffff')
b_tracking_order.place(relx=.5, rely=.4,anchor= CENTER)
b_products = Button(frame_menu, text="מוצרים", command=lambda: show_mains_screens(products_screen), width=12, height=3, font=("Narkisim", 15, 'bold'), bg=color_btn_menu, fg='#ffffff')
b_products.place(relx=.5, rely=.55,anchor= CENTER)
b_reports = Button(frame_menu, text="דוחות", command=lambda: show_mains_screens(reports_screen), width=12, height=3, font=("Narkisim", 15, 'bold'), bg=color_btn_menu, fg='#ffffff')
b_reports.place(relx=.5, rely=.7,anchor= CENTER)


######### main screen: #########

logo = PhotoImage(file="logo.png")
label_logo = Label(main_screen, image=logo)
label_logo.place(relx=.5, rely=.5,anchor= CENTER)



######### new order screen: #########

def add_products_to_tree_new_order_screen():
    for item in tree_products_in_new_order.get_children():
        tree_products_in_new_order.delete(item)
    for name in read_all_products_from_json().keys():
        tree_products_in_new_order.insert("", END, values=[read_all_products_from_json()[name]["price"], name])

def click():
    multiselects = tree_products_in_new_order.selection()
    for i in multiselects:
        print(tree_products_in_new_order.item(i)['values'][1])

frame_all_products_in_new_order = Frame(new_order_screen, width=465, height=800, bg=color_menu_tracking_orders)
frame_all_products_in_new_order.place(x=0, y=0)

tree_products_in_new_order = Treeview(frame_all_products_in_new_order, columns=(2, 1), show='headings', height=27)
style = Style()
style.theme_use("clam")
style.configure('Treeview.Heading', background=color_nenu_screen, font=(None, 14, 'bold'))
style.configure('Treeview', rowheight=25, font=(None, 12))
tree_products_in_new_order.column("1", anchor=CENTER, width=350)
tree_products_in_new_order.heading("1", text="מוצר")
tree_products_in_new_order.column("2", anchor=CENTER, width=70)
tree_products_in_new_order.heading("2", text="מחיר")
tree_products_in_new_order.place(relx=.485, rely=.54, anchor=CENTER)
vsb = Scrollbar(frame_all_products_in_new_order, orient="vertical", command=tree_products_in_new_order.yview)
vsb.place(relx=.96, rely=.56, anchor=CENTER, height=679)
tree_products_in_new_order.configure(yscrollcommand=vsb.set)

lable_search = Label(frame_all_products_in_new_order, text="כל המוצרים", bg=color_menu_tracking_orders)
lable_search.place(relx=0.5, rely=0.01)


btn1 = Button(new_order_screen, text="כפתור", command=click)
btn1.place(relx=.55, rely=.5)




######### tracking orders screen: #########

menu_in_tracking_orders = Frame(tracking_order_screen, width=200, height=800, bg=color_menu_tracking_orders)
main_page_tracking_orders = Frame(tracking_order_screen, width=1100, height=800, bg=color_screen)
today_and_tomorow_screen = Frame(tracking_order_screen, width=1100, height=800, bg=color_screen)
future_orders_screen = Frame(tracking_order_screen, width=1100, height=800, bg=color_screen)
all_orders_screen = Frame(tracking_order_screen, width=1100, height=800, bg=color_screen)
not_pay_orders_screen = Frame(tracking_order_screen, width=1100, height=800, bg=color_screen)
search_orders_screen = Frame(tracking_order_screen, width=1100, height=800, bg=color_screen)

lable_search = Label(main_page_tracking_orders, text="נא לבחור מהרשימה", bg=color_screen)
lable_search.place(relx=0.5, rely=0.5)

def show_screen_in_traking_orders(screen):
    today_and_tomorow_screen.place_forget()
    future_orders_screen.place_forget()
    all_orders_screen.place_forget()
    not_pay_orders_screen.place_forget()
    search_orders_screen.place_forget()
    screen.place(x=0, y=0)


b1 = Button(menu_in_tracking_orders, text="הזמנות\nלהיום ומחר", width=12, command=lambda: show_screen_in_traking_orders(today_and_tomorow_screen), height=3, font=("Narkisim", 15, 'bold'), bg=color_btn_menu, fg='#ffffff')
b1.place(relx=.5, rely=.1,anchor= CENTER)
b2 = Button(menu_in_tracking_orders, text="הזמנות\nעתידיות", width=12, command=lambda: show_screen_in_traking_orders(future_orders_screen), height=3, font=("Narkisim", 15, 'bold'), bg=color_btn_menu, fg='#ffffff')
b2.place(relx=.5, rely=.25,anchor= CENTER)
b3 = Button(menu_in_tracking_orders, text="כל ההזמנות", width=12, command=lambda: show_screen_in_traking_orders(all_orders_screen), height=3, font=("Narkisim", 15, 'bold'), bg=color_btn_menu, fg='#ffffff')
b3.place(relx=.5, rely=.4,anchor= CENTER)
b4 = Button(menu_in_tracking_orders, text="הזמנות\nשלא שולמו", width=12, command=lambda: show_screen_in_traking_orders(not_pay_orders_screen), height=3, font=("Narkisim", 15, 'bold'), bg=color_btn_menu, fg='#ffffff')
b4.place(relx=.5, rely=.55,anchor= CENTER)
b5 = Button(menu_in_tracking_orders, text="חיפוש הזמנה", width=12, command=lambda: show_screen_in_traking_orders(search_orders_screen), height=3, font=("Narkisim", 15, 'bold'), bg=color_btn_menu, fg='#ffffff')
b5.place(relx=.5, rely=.7,anchor= CENTER)




##### all orders screen:


def select_order_to_list_ptoducts(event):
    for item in tree_products_in_order.get_children():
        tree_products_in_order.delete(item)
    selectedItem = tree_details_orders.selection()[0]
    for p in read_new_orders_from_json()[str(tree_details_orders.item(selectedItem)['values'][8])]["products"]:
        tree_products_in_order.insert("", END, values=[p["price"], p["name"]])


tree_details_orders = Treeview(all_orders_screen, columns=(9, 8, 7, 6, 5, 4, 3, 2, 1), show='headings', height=10)
style = Style()
style.theme_use("clam")
style.configure('Treeview.Heading', background=color_nenu_screen, font=(None, 14, 'bold'))
style.configure('Treeview', rowheight=25, font=(None, 12))
tree_details_orders.column("1", anchor=CENTER, width=60)
tree_details_orders.heading("1", text="ID")
tree_details_orders.column("2", anchor=CENTER, width=130)
tree_details_orders.heading("2", text="תאריך הזמנה")
tree_details_orders.column("3", anchor=CENTER, width=130)
tree_details_orders.heading("3", text="שם המזמין")
tree_details_orders.column("4", anchor=CENTER, width=130)
tree_details_orders.heading("4", text="טלפון")
tree_details_orders.column("5", anchor=CENTER, width=130)
tree_details_orders.heading("5", text="תאריך אספקה")
tree_details_orders.column("6", anchor=CENTER, width=160)
tree_details_orders.heading("6", text="הערות")
tree_details_orders.column("7", anchor=CENTER, width=100)
tree_details_orders.heading("7", text="מחיר כולל")
tree_details_orders.column("8", anchor=CENTER, width=100)
tree_details_orders.heading("8", text="?שולם")
tree_details_orders.column("9", anchor=CENTER, width=100)
tree_details_orders.heading("9", text="אמצעי")
tree_details_orders.place(relx=.5, rely=.3, anchor=CENTER)
vsb = Scrollbar(all_orders_screen, orient="vertical", command=tree_details_orders.yview)
vsb.place(relx=.983, rely=.32, anchor=CENTER, height=254)
tree_details_orders.configure(yscrollcommand=vsb.set)
tree_details_orders.bind("<<TreeviewSelect>>", select_order_to_list_ptoducts)



tree_products_in_order = Treeview(all_orders_screen, columns=(2, 1), show='headings', height=10)
style = Style()
style.theme_use("clam")
style.configure('Treeview.Heading', background=color_nenu_screen, font=(None, 14, 'bold'))
style.configure('Treeview', rowheight=25, font=(None, 12))
tree_products_in_order.column("1", anchor=CENTER, width=200)
tree_products_in_order.heading("1", text="מוצר")
tree_products_in_order.column("2", anchor=CENTER, width=100)
tree_products_in_order.heading("2", text="מחיר")
tree_products_in_order.place(relx=.5, rely=.8, anchor= CENTER)
vsb = Scrollbar(all_orders_screen, orient="vertical", command=tree_products_in_order.yview)
vsb.place(relx=.5, rely=.5, anchor=CENTER, height=255)
tree_products_in_order.configure(yscrollcommand=vsb.set)
# tree_products_in_order.bind("<<TreeviewSelect>>", print("need def"))



new_orders_f = read_new_orders_from_json()
for id in new_orders_f.keys():
    tree_details_orders.insert("", END, values=[new_orders_f[id]["method"], new_orders_f[id]["status"], new_orders_f[id]["price"], new_orders_f[id]["remarks"], new_orders_f[id]["date_delivery"], new_orders_f[id]["phone"], new_orders_f[id]["name"], new_orders_f[id]["date_order"], id])







##### products screen:

def add_products_to_tree_products_screen():
    for item in tree_all_products.get_children():
        tree_all_products.delete(item)
    for name in read_all_products_from_json().keys():
        tree_all_products.insert("", END, values=[read_all_products_from_json()[name]["price"], read_all_products_from_json()[name]["cost"], name])
    clear_entry_product()


def save_product():
    list_products = read_all_products_from_json()
    if len(entry_name_product.get()) == 0 or len(entry_cost_product.get()) == 0 or len(entry_price_product.get()) == 0 or not entry_cost_product.get().isnumeric() or not entry_price_product.get().isnumeric():
        return
    try:
        list_products[entry_name_product.get()]["cost"] = float(entry_cost_product.get())
        list_products[entry_name_product.get()]["price"] = float(entry_price_product.get())
    except:
        list_products[entry_name_product.get()] = {"cost": float(entry_cost_product.get()), "price": int(entry_price_product.get())}
    write_products_to_json(list_products)
    add_products_to_tree_products_screen()
    entry_name_product.delete(0, END)
    entry_cost_product.delete(0, END)
    entry_price_product.delete(0, END)
    tree_all_products.focus_set()


def clear_entry_product():
    entry_name_product.delete(0, END)
    entry_cost_product.delete(0, END)
    entry_price_product.delete(0, END)
    entry_search.delete(0, END)
    tree_all_products.focus_set()
    if len(tree_all_products.selection()) > 0:
        tree_all_products.selection_remove(tree_all_products.selection()[0])


def click_on_product(event):
    try:
        selectedItem = tree_all_products.selection()[0]
        entry_name_product.delete(0, END)
        entry_name_product.insert(0, tree_all_products.item(selectedItem)['values'][2])
        entry_cost_product.delete(0, END)
        entry_cost_product.insert(0, tree_all_products.item(selectedItem)['values'][1])
        entry_price_product.delete(0, END)
        entry_price_product.insert(0, tree_all_products.item(selectedItem)['values'][0])
    except:
        pass


def search_product_in_products_screen():
    for item in tree_all_products.get_children():
        tree_all_products.delete(item)
    for name in read_all_products_from_json().keys():
        if name.find(entry_search.get()) != -1:
            tree_all_products.insert("", END, values=[read_all_products_from_json()[name]["price"], read_all_products_from_json()[name]["cost"], name])


def delete_product_from_all_products():
    try:
        selectedItem = tree_all_products.selection()[0]
        list_products = read_all_products_from_json()
        if tree_all_products.item(selectedItem)['values'][2] in list_products:
            del list_products[tree_all_products.item(selectedItem)['values'][2]]
        write_products_to_json(list_products)
        add_products_to_tree_products_screen()
    except:
        pass

lable_search = Label(products_screen, text=":חיפוש", bg=color_screen)
lable_search.place(relx=0.8, rely=0.045)
entry_search = Entry(products_screen, width=35, justify='right')
entry_search.place(relx=0.62, rely=0.05)
b_search = Button(products_screen, text="חיפוש", command=search_product_in_products_screen, bg=color_btn_menu, fg='#ffffff')
b_search.place(relx=.55, rely=.045)
b_reset_search = Button(products_screen, text="איפוס", command=add_products_to_tree_products_screen, bg=color_btn_menu, fg='#ffffff')
b_reset_search.place(relx=.5, rely=.045)

tree_all_products = Treeview(products_screen, columns=(3,2,1), show='headings', height=25)
style = Style()
style.theme_use("clam")
style.configure('Treeview.Heading', background=color_nenu_screen, font=(None, 14, 'bold'))
style.configure('Treeview', rowheight=25, font=(None, 12))
tree_all_products.column("1", anchor=CENTER, width=500)
tree_all_products.heading("1", text="שם המוצר")
tree_all_products.column("2", anchor=CENTER, width=100)
tree_all_products.heading("2", text="עלות")
tree_all_products.column("3", anchor=CENTER, width=100)
tree_all_products.heading("3", text="מחיר")
tree_all_products.place(relx=.65, rely=.52, anchor= CENTER)
vsb = Scrollbar(products_screen, orient="vertical", command=tree_all_products.yview)
vsb.place(relx=.928, rely=.54, anchor= CENTER, height=625)
tree_all_products.configure(yscrollcommand=vsb.set)
tree_all_products.bind("<<TreeviewSelect>>", click_on_product)

lable_name_product = Label(products_screen, text=":שם המוצר", bg=color_screen, font=(None, 14, 'bold'))
lable_name_product.place(relx=0.28, rely=0.3)
entry_name_product = Entry(products_screen, width=40, justify="right", font=(None, 12))
entry_name_product.place(relx=0.07, rely=0.34)
lable_cost_product = Label(products_screen, text=":עלות", bg=color_screen, font=(None, 14, 'bold'))
lable_cost_product.place(relx=0.315, rely=0.45)
entry_cost_product = Entry(products_screen, width=17, justify='right', font=(None, 12))
entry_cost_product.place(relx=0.23, rely=0.49)
lable_price_product = Label(products_screen, text=":מחיר", bg=color_screen, font=(None, 14, 'bold'))
lable_price_product.place(relx=0.153, rely=0.45)
entry_price_product = Entry(products_screen, width=17, justify='right', font=(None, 12))
entry_price_product.place(relx=0.07, rely=0.49)

b_save = Button(products_screen, text="שמור", width=8, height=1, bg=color_btn_menu, fg='#ffffff', font=(None, 14, 'bold'), command=save_product)
b_save.place(relx=.27, rely=.6)
b_reset_add = Button(products_screen, text="ניקוי", width=8, height=1, bg=color_btn_menu, fg='#ffffff', font=(None, 14, 'bold'), command=clear_entry_product)
b_reset_add.place(relx=.17, rely=.6)
b_reset_add = Button(products_screen, text="מחק", width=8, height=1, bg=color_btn_menu, fg='#ffffff', font=(None, 14, 'bold'), command=delete_product_from_all_products)
b_reset_add.place(relx=.07, rely=.6)





window.mainloop()


