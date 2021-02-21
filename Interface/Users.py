from tkinter import *
from tkinter import ttk, messagebox
from System.Register import Register as Reg
import Interface.Start as Start
import Interface.Book_operation as Book
import System.search as search


class My_Users:
    def __init__(self):
        self.master = Tk()
        self.master.title("Users Management")
        self.master.geometry("1100x560+250+50")
        self.master.resizable(False, False)
        self.master.config(background="#C4DFE6")
        self.color = "#C4DFE6"
        self.reg = Reg()
        self.tree_item = []

        # Menu
        my_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        book_menu = Menu(my_menu)
        my_menu.add_cascade(label="Books", menu=book_menu)
        book_menu.add_command(label="Operations", command=lambda: (self.master.destroy(), Book.Operation()))
        book_menu.add_command(label="View", command=lambda: (self.master.destroy(), Book.View()))

        members_menu = Menu(my_menu)
        my_menu.add_cascade(label="Members", menu=members_menu)
        members_menu.add_command(label="Operations", command=lambda: (self.master.destroy(), My_Users()))

        options_menu = Menu(my_menu)
        my_menu.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Back", command=self.back)
        options_menu.add_separator()
        options_menu.add_command(label="Log Out", command=self.logout)

        Label(self.master, text="Users Management", font=("calibre", 30), bg="#3E363F", fg="#C4DFE6",
              pady=10).grid(row=0, column=0, columnspan=3, sticky=EW)

        # Frames
        self.view_frame = Frame(self.master, bg=self.color)
        self.view_frame.grid(row=1, column=0, columnspan=2)
        self.entry_frame = LabelFrame(self.master, text="Users Details", bg=self.color, padx=10, pady=10)
        self.entry_frame.grid(row=1, column=2, padx=10, pady=10)

        Button(self.master, text="Add", bg=self.color, font=20, relief=RIDGE, command=self.ad).grid(row=2, column=0)
        Button(self.master, text="Edit", bg=self.color, font=20, relief=RIDGE, command=self.ud).grid(row=2, column=1)
        Button(self.master, text="Delete", bg=self.color, font=20, relief=RIDGE, command=self.dl).grid(row=2, column=2)

        # View and Search for the users
        Label(self.view_frame, text="Search: ", font=("calibre", 12), bg=self.color).grid(row=0, column=0, pady=(10, 0))
        self.search_for = Entry(self.view_frame, font=("calibre", 12))
        self.search_for.grid(row=0, column=1, pady=(10, 0))

        Label(self.view_frame, text="By Username", font=12, bg=self.color).grid(row=0, column=2, padx=5, pady=(10, 0))

        Button(self.view_frame, text="Search", command=self.search).grid(row=0, column=3, pady=(10, 0), sticky=EW)
        Button(self.view_frame, text="Show All", command=self.show_in_tree).grid(row=0, column=4, pady=(10, 0))

        self.user_tree = ttk.Treeview(self.view_frame, columns=(
            "first_name", "last_name", "username", "id_no", "address", "contact", "status"))
        self.user_tree.grid(row=1, column=0, columnspan=8, padx=13, pady=10)
        self.user_tree['show'] = 'headings'
        self.user_tree.heading("first_name", text='First Name')
        self.user_tree.heading("last_name", text='Last Name')
        self.user_tree.heading("username", text='Username')
        self.user_tree.heading("id_no", text='ID Card No')
        self.user_tree.heading("address", text='Address')
        self.user_tree.heading("contact", text='Contact')
        self.user_tree.heading("status", text='Status')
        self.user_tree.column("username", width=110)
        self.user_tree.column("first_name", width=110)
        self.user_tree.column("last_name", width=100)
        self.user_tree.column("id_no", width=110)
        self.user_tree.column("address", width=130)
        self.user_tree.column("contact", width=110)
        self.user_tree.column("status", width=110)
        self.show_in_tree()

        # entry form for view select
        Label(self.entry_frame, text="First Name", font=("calibre", 13), bg=self.color, padx=10, pady=5).grid(row=0,
                                                                                                              column=0)

        self.first_name = Entry(self.entry_frame, width=20, font=("calibre", 10))
        self.first_name.grid(row=0, column=1)

        Label(self.entry_frame, text="Last Name", font=("calibre", 13), bg=self.color, padx=10, pady=5).grid(row=1,
                                                                                                             column=0)

        self.last_name = Entry(self.entry_frame, width=20, font=("calibre", 10))
        self.last_name.grid(row=1, column=1)

        Label(self.entry_frame, text="Username", font=("calibre", 13), bg=self.color, padx=10, pady=5).grid(row=2,
                                                                                                            column=0)

        self.username = Entry(self.entry_frame, width=20, font=("calibre", 10))
        self.username.grid(row=2, column=1)

        Label(self.entry_frame, text="ID Card No", font=("calibre", 13), bg=self.color, padx=10, pady=5).grid(row=3,
                                                                                                              column=0)

        self.id_no = Entry(self.entry_frame, width=20, font=("calibre", 10))
        self.id_no.grid(row=3, column=1)

        Label(self.entry_frame, text="Address", font=("calibre", 13), bg=self.color, padx=10, pady=5).grid(row=4,
                                                                                                           column=0)

        self.address = Entry(self.entry_frame, width=20, font=("calibre", 10))
        self.address.grid(row=4, column=1)

        Label(self.entry_frame, text="Contact", font=("calibre", 13), bg=self.color, padx=10, pady=5).grid(row=5,
                                                                                                           column=0)

        self.contact = Entry(self.entry_frame, width=20, font=("calibre", 10))
        self.contact.grid(row=5, column=1)

        Label(self.entry_frame, text="Status", font=("calibre", 13), bg=self.color, padx=10, pady=5).grid(row=6,
                                                                                                          column=0)

        self.user_combo = ttk.Combobox(self.entry_frame, state="readonly", width=20, values=["Staff", "Student"])
        self.user_combo.grid(row=6, column=1)

        Button(self.entry_frame, text="Clear", bg=self.color, command=self.clear).grid(row=7, column=0, columnspan=2)

        mainloop()

    def search(self):
        data, a = search.search_by_username(self.search_for.get())
        self.user_tree.delete(*self.user_tree.get_children())
        self.user_tree.insert('', END, values=data[a][1:])

    def back(self):
        self.master.destroy()
        start = Start.Main()
        start.popup()

    def logout(self):
        self.master.destroy()
        start = Start.Main()
        start.window()

    def show_in_tree(self):
        self.user_tree.delete(*self.user_tree.get_children())
        self.tree_item = self.reg.show()
        # print(self.tree_item)
        for i in self.tree_item:
            # print(i)
            self.user_tree.insert("", "end", text=i[0], values=i[1:8])
        self.user_tree.bind("<Double-1>", self.select)

    def select(self, ev):
        self.selected_id = self.user_tree.item(self.user_tree.selection(), 'text')
        self.selected_row = self.user_tree.item(self.user_tree.selection(), 'value')
        # print(self.user_tree.item(self.user_tree.selection(), 'text'))
        self.clear()
        try:
            self.first_name.insert(0, self.selected_row[0])
            self.last_name.insert(0, self.selected_row[1])
            self.username.insert(0, self.selected_row[2])
            self.id_no.insert(0, self.selected_row[3])
            self.address.insert(0, self.selected_row[4])
            self.contact.insert(0, self.selected_row[5])
            self.user_combo.set(self.selected_row[6])
        except Exception:
            pass

    def clear(self):
        self.first_name.delete(0, END)
        self.last_name.delete(0, END)
        self.username.delete(0, END)
        self.address.delete(0, END)
        self.contact.delete(0, END)
        self.id_no.delete(0, END)
        self.user_combo.set("")

    def ad(self):
        if (self.first_name.get() and self.last_name.get() and self.username.get() and self.id_no.get() and
                self.address.get() and self.contact.get() and self.user_combo.get()):
            win = Toplevel(self.master)
            win.geometry("200x100")
            Label(win, text="Add password", font=("calibre", 10)).pack(padx=5, pady=5)
            self.password = Entry(win, width=15, font=("calibre", 10), show="*")
            self.password.pack(padx=5, pady=5)
            Button(win, text="Confirm", command=self.confirm).pack(padx=5, pady=5)
        else:
            messagebox.showerror("Empty Field", "Don't leave any empty field")

    def confirm(self):
        password = Start.encrypt(self.password.get())
        # print(self.first_name.get(), self.last_name.get(), self.username.get(), self.id_no.get(),
        #       self.address.get(), self.contact.get(), self.user_combo.get(), self.password.get())
        self.reg.register((self.first_name.get(), self.last_name.get(), self.username.get(), self.id_no.get(),
                           self.address.get(), self.contact.get(), self.user_combo.get(), password))
        self.show_in_tree()
        self.clear()

    def ud(self):
        self.reg.update((self.first_name.get(), self.last_name.get(), self.username.get(), self.id_no.get(),
                         self.address.get(), self.contact.get(), self.user_combo.get(), self.selected_id))
        self.show_in_tree()
        self.clear()

    def dl(self):
        # print(self.selected_id)
        try:
            self.reg.dele((self.selected_id,))
            self.show_in_tree()
            self.clear()
        except Exception:
            messagebox.showerror("Selection Error", "Select a valid entry to delete")


if __name__ == '__main__':
    My_Users()
