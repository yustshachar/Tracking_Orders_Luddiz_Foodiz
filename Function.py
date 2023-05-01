import configparser
import json
import os

ini_file_name = "Tracking_Order.ini"
all_products_file_name = "AllProducts.json"
all_order_file_name = "NewOrders.json"

status_order_option = ["פתוח", "סגור - בוצע תשלום"]

inif = configparser.ConfigParser()
inif.read(ini_file_name)


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
        return json.loads(r_no.read())


def write_products_to_json(dict_products):
    with open(all_products_file_name, "wb") as w_p:
        w_p.write(json.dumps(dict_products, ensure_ascii=False).encode("utf-8"))


def write_order_to_json(dict_order):
    new = read_new_orders_from_json()
    new.update(dict_order)
    with open(all_order_file_name, "wb") as w_no:
        w_no.write(json.dumps(new, ensure_ascii=False).encode("utf-8"))