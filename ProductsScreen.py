from tkinter import Frame, Label, Entry, Button, CENTER, Scrollbar, END, messagebox
from tkinter.ttk import Treeview, Style
import Function


class ProductsScreen:
    def __init__(self, window):
        self.products_screen = Frame(window, width=1300, height=800, bg=Function.colors("color_screen"))
        self.lable_search = Label(self.products_screen, text=":חיפוש", bg=Function.colors("color_screen"))
        self.lable_search.place(relx=0.62, rely=0.023)
        self.entry_search = Entry(self.products_screen, width=35, justify='right')
        self.entry_search.place(relx=0.45, rely=0.025)
        self.b_search = Button(self.products_screen, text="חיפוש", command=self.search_product_in_products_screen,
                               bg=Function.colors("color_btn_menu"), fg='#ffffff')
        self.b_search.place(relx=.4, rely=.02)
        self.b_reset_search = Button(self.products_screen, text="איפוס",
                                     command=self.add_products_to_tree_products_screen,
                                     bg=Function.colors("color_btn_menu"), fg='#ffffff')
        self.b_reset_search.place(relx=.35, rely=.02)

        self.style = Style()
        self.style.theme_use("clam")
        self.style.configure("Custom1.Treeview", rowheight=25, font=(None, 12))
        # self.style.map('Custom1.Treeview')
        self.style.configure('Custom1.Treeview.Heading', background=Function.colors("color_nenu_screen"), font=(None, 14, 'bold'))

        self.tree_all_products = Treeview(self.products_screen, columns=(3, 2, 1), show='headings', height=23, style="Custom1.Treeview")
        self.tree_all_products.column("1", anchor=CENTER, width=700)
        self.tree_all_products.heading("1", text="שם המוצר")
        self.tree_all_products.column("2", anchor=CENTER, width=100)
        self.tree_all_products.heading("2", text="עלות")
        self.tree_all_products.column("3", anchor=CENTER, width=100)
        self.tree_all_products.heading("3", text="מחיר")
        self.tree_all_products.place(relx=.5, rely=.45, anchor=CENTER)
        self.vsb = Scrollbar(self.products_screen, orient="vertical", command=self.tree_all_products.yview)
        self.vsb.place(relx=.855, rely=.47, anchor=CENTER, height=580)
        self.tree_all_products.configure(yscrollcommand=self.vsb.set)

        # אירוע בעת לחיצה כפולה
        self.tree_all_products.bind("<Double-1>", self.double_click_on_cell)

        # # אירוע בעת ריחוף
        # self.lbl=Label(self.products_screen ,bg="#EFDE74")
        # self.tree_all_products.bind("<Motion>", self.on_hover)

        self.lable_name_product = Label(self.products_screen, text=":שם המוצר", bg=Function.colors("color_screen"),
                                        font=(None, 14, 'bold'))
        self.lable_name_product.place(relx=0.78, rely=0.86)
        self.entry_name_product = Entry(self.products_screen, width=39, justify="right", font=(None, 12))
        self.entry_name_product.place(relx=0.5, rely=0.865)
        self.lable_cost_product = Label(self.products_screen, text=":עלות", bg=Function.colors("color_screen"), font=(None, 14, 'bold'))
        self.lable_cost_product.place(relx=0.455, rely=0.86)
        self.entry_cost_product = Entry(self.products_screen, width=17, justify='right', font=(None, 12))
        self.entry_cost_product.place(relx=0.33, rely=0.865)
        self.lable_price_product = Label(self.products_screen, text=":מחיר", bg=Function.colors("color_screen"), font=(None, 14, 'bold'))
        self.lable_price_product.place(relx=0.28, rely=0.86)
        self.entry_price_product = Entry(self.products_screen, width=17, justify='right', font=(None, 12))
        self.entry_price_product.place(relx=0.153, rely=0.865)

        self.b_save = Button(self.products_screen, text="שמור חדש", width=8, height=1, bg=Function.colors("color_btn_menu"),
                             fg='#ffffff', font=(None, 14, 'bold'), command=self.save_product)
        self.b_save.place(relx=.57, rely=.92)
        self.b_reset_add = Button(self.products_screen, text="ניקוי שדות", width=8, height=1,
                                  bg=Function.colors("color_btn_menu"), fg='#ffffff', font=(None, 14, 'bold'),
                                  command=self.clear_entry_product)
        self.b_reset_add.place(relx=.45, rely=.92)
        self.b_reset_del = Button(self.products_screen, text="מחק מוצר", width=8, height=1,
                                  bg=Function.colors("color_btn_menu"), fg='#ffffff', font=(None, 14, 'bold'),
                                  command=self.delete_product_from_all_products)
        self.b_reset_del.place(relx=.33, rely=.92)

        self.add_products_to_tree_products_screen()
        self.clear_entry_product()

    def start(self):
        self.products_screen.place(x=0, y=0)
        self.add_products_to_tree_products_screen()
        self.clear_entry_product()

    def close(self):
        self.products_screen.place_forget()

    def add_products_to_tree_products_screen(self):
        for item in self.tree_all_products.get_children():
            self.tree_all_products.delete(item)
        for name in Function.read_all_products_from_json().keys():
            self.tree_all_products.insert("", END, values=[Function.read_all_products_from_json()[name]["price"],
                                                           Function.read_all_products_from_json()[name]["cost"], name])
        self.clear_entry_product()

    def save_product(self):
        dict_products = Function.read_all_products_from_json()
        if len(self.entry_name_product.get()) == 0 or len(self.entry_cost_product.get()) == 0 or len(
                self.entry_price_product.get()) == 0 or not self.entry_cost_product.get().isnumeric() or not self.entry_price_product.get().isnumeric():
            return
        if self.entry_name_product.get() in dict_products:
            if not messagebox.askyesno("הערה", "קיים כבר מוצר בשם הזה.\nהאם להחליפו?"):
                return
        try:
            dict_products[self.entry_name_product.get()]["cost"] = int(self.entry_cost_product.get())
            dict_products[self.entry_name_product.get()]["price"] = int(self.entry_price_product.get())
        except:
            dict_products[self.entry_name_product.get()] = {"cost": int(self.entry_cost_product.get()),
                                                            "price": int(self.entry_price_product.get())}
        Function.write_products_to_json(dict_products)
        self.add_products_to_tree_products_screen()
        self.entry_name_product.delete(0, END)
        self.entry_cost_product.delete(0, END)
        self.entry_price_product.delete(0, END)
        self.tree_all_products.focus_set()

    def clear_entry_product(self):
        self.entry_name_product.delete(0, END)
        self.entry_cost_product.delete(0, END)
        self.entry_price_product.delete(0, END)
        self.entry_search.delete(0, END)
        self.tree_all_products.focus_set()
        if len(self.tree_all_products.selection()) > 0:
            self.tree_all_products.selection_remove(self.tree_all_products.selection()[0])

    def click_on_product(self, event):
        try:
            self.selectedItem = self.tree_all_products.selection()[0]
            self.entry_name_product.delete(0, END)
            self.entry_name_product.insert(0, self.tree_all_products.item(self.selectedItem)['values'][2])
            self.entry_cost_product.delete(0, END)
            self.entry_cost_product.insert(0, self.tree_all_products.item(self.selectedItem)['values'][1])
            self.entry_price_product.delete(0, END)
            self.entry_price_product.insert(0, self.tree_all_products.item(self.selectedItem)['values'][0])
        except:
            pass

    def search_product_in_products_screen(self):
        for item in self.tree_all_products.get_children():
            self.tree_all_products.delete(item)
        all_products = Function.read_all_products_from_json()
        for name in all_products.keys():
            if name.find(self.entry_search.get()) != -1:
                self.tree_all_products.insert("", END, values=[all_products[name]["price"], all_products[name]["cost"], name])

    def delete_product_from_all_products(self):
        try:
            selectedItem = self.tree_all_products.selection()[0]
            list_products = Function.read_all_products_from_json()
            if self.tree_all_products.item(selectedItem)['values'][2] in list_products:
                del list_products[self.tree_all_products.item(selectedItem)['values'][2]]
            Function.write_products_to_json(list_products)
            self.add_products_to_tree_products_screen()
        except:
            pass

    def double_click_on_cell(self, event):
        clicked = self.tree_all_products.identify_region(event.x, event.y)
        if clicked != "cell":
            return
        column = self.tree_all_products.identify_column(event.x)
        column_indx = int(column[1:]) - 1
        try:
            selectedItem = self.tree_all_products.selection()[0]
        except:
            return
        selected_all_value = self.tree_all_products.item(selectedItem)["values"]

        box_cell = self.tree_all_products.bbox(selectedItem, column)

        entry_edit = Entry(self.tree_all_products, width=box_cell[2], justify=CENTER)
        entry_edit.place(x=box_cell[0], y=box_cell[1], width=box_cell[2], height=box_cell[3])
        entry_edit.editing_column_index = column_indx
        entry_edit.editing_item_iid = selectedItem
        entry_edit.insert(0, selected_all_value[column_indx])
        entry_edit.select_range(0, END)
        entry_edit.focus()
        entry_edit.bind("<FocusOut>", self.focus_out_from_edit_entry)
        entry_edit.bind("<Return>", self.focus_out_from_edit_entry)

    def focus_out_from_edit_entry(self, event):
        selectedItem = event.widget.editing_item_iid

        list_products = Function.read_all_products_from_json()
        if event.widget.editing_column_index == 2:  # name
            list_products[event.widget.get()] = list_products.pop(self.tree_all_products.item(selectedItem)["values"][2])
        elif event.widget.editing_column_index == 1:  # cost
            if not event.widget.get().isnumeric():
                event.widget.destroy()
                return
            try:
                list_products[self.tree_all_products.item(selectedItem)["values"][2]]["cost"] = int(event.widget.get())
            except:
                return
        elif event.widget.editing_column_index == 0:  # price
            if not event.widget.get().isnumeric():
                event.widget.destroy()
                return
            try:
                list_products[self.tree_all_products.item(selectedItem)["values"][2]]["price"] = int(event.widget.get())
            except:
                return

        Function.write_products_to_json(list_products)
        self.add_products_to_tree_products_screen()

        event.widget.destroy()

    # def on_hover(self, event):
    #     tree = event.widget
    #     item = tree.identify_row(event.y)
    #     if item != '' and self.tree_all_products.identify_column(event.x) == "#3":
    #         self.lbl.config(text=tree.item(item)['values'][2])
    #         self.lbl.place(x=event.x, y=event.y)
    #     else:
    #         self.lbl.place_forget()