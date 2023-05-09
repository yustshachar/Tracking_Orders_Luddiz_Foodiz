import configparser
import json
import os
from zipfile import ZipFile
from datetime import datetime
from tkinter import messagebox

version_number = "1.5"
ini_file_name = r"C:\ProgramData\Luddiz.Foodiz\Tracking Order\Config\Tracking_Order.ini"
all_products_file_name = r"C:\ProgramData\Luddiz.Foodiz\Tracking Order\Data\AllProducts.json"
all_order_file_name = r"C:\ProgramData\Luddiz.Foodiz\Tracking Order\Data\NewOrders.json"
logo_file = r"C:\ProgramData\Luddiz.Foodiz\Tracking Order\Config\logo.png"
backup_folder = r"C:\ProgramData\Luddiz.Foodiz\BackUp"

status_order_option = ["פתוח", "סגור - בוצע תשלום"]

inif = configparser.ConfigParser()
inif.read(ini_file_name)

if not (os.path.isfile(ini_file_name) and os.path.isfile(all_products_file_name) and os.path.isfile(all_order_file_name)):
    messagebox.showwarning("חוסר בקבצים", "יש חוסר באחד מקבצי התוכנה. יש לסדר ולנסות שנית.")
    exit()


def colors(name):
    return inif["colors"][name]


def last_id_order():
    return inif["last_ID"]["order"]


def update_id_order():
    new_id = str(int(last_id_order()) + 1)
    inif.set("last_ID", "order", new_id)
    inif["last_ID"]["order"] = new_id
    with open(ini_file_name, 'w') as w_if:
        inif.write(w_if)


def read_all_products_from_json():
    if not os.path.isfile(all_products_file_name):
        return {}
    # מחזיר מילון ממויין לפי השם של המוצר
    with open(all_products_file_name, encoding="utf8") as r_ap:
        dict_all = json.loads(r_ap.read())
        key_sort = sorted(dict_all)
        dict_sort = {}
        for key in key_sort:
            dict_sort[key] = dict_all[key]
        return dict_sort


def read_new_orders_from_json():
    if not os.path.isfile(all_order_file_name):
        return {}
    with open(all_order_file_name, encoding="utf8") as r_no:
        all_orders = json.loads(r_no.read())
        orders_sort = dict(sorted(all_orders.items(), key=lambda item: datetime.strptime(item[1]["date_delivery"], "%d-%m-%Y"), reverse=True))
        return orders_sort


def write_products_to_json(dict_products):
    with open(all_products_file_name, "wb") as w_p:
        w_p.write(json.dumps(dict_products, ensure_ascii=False).encode("utf-8"))


def write_order_to_json(dict_order):
    new = read_new_orders_from_json()
    new.update(dict_order)
    with open(all_order_file_name, "wb") as w_no:
        w_no.write(json.dumps(new, ensure_ascii=False).encode("utf-8"))

def delete_order_from_json_by_id(id):
    all_orders = read_new_orders_from_json()
    all_orders.pop(id)
    with open(all_order_file_name, "wb") as w_do:
        w_do.write(json.dumps(all_orders, ensure_ascii=False).encode("utf-8"))

def backup_all():
    if not messagebox.askyesno("BackUp Tracking Order", "האם לגבות את כל נתוני התוכנה?"):
        return
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    try:
        zipObj = ZipFile(f'{backup_folder}\TrackingOrdersV{version_number}-BackUp-{datetime.today().strftime("%d-%m-%Y-%H-%M-%S")}.zip', 'w')
        zipObj.write(ini_file_name, f"{os.path.basename(os.path.dirname(ini_file_name))}\\{os.path.basename(ini_file_name)}")
        zipObj.write(all_products_file_name, f"{os.path.basename(os.path.dirname(all_products_file_name))}\\{os.path.basename(all_products_file_name)}")
        zipObj.write(all_order_file_name, f"{os.path.basename(os.path.dirname(all_order_file_name))}\\{os.path.basename(all_order_file_name)}")
        zipObj.close()
        messagebox.showinfo("BackUp Tracking Order", "כל נתוני התוכנה גובו")
    except: messagebox.showinfo("BackUp Tracking Order", "שגיאה! לא בוצע גיבוי!")
