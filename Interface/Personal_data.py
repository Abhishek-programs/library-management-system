from tkinter import *
from tkinter import ttk, messagebox
from System.Library import Book_Management
from System.logs import Book
import Interface.Start as Start
from datetime import date
from PIL import ImageTk, Image


class Data:
    def __init__(self, id, first, last, user, id_no, status):
        self.id = id
        self.master = Tk()
        self.color1 = "#C4DFE6"
        self.color2 = "#90AFC5"
        self.master.title("Personal Data")
        self.master.geometry("760x600+350+100")
        self.master.config(background=self.color2)

        self.request_book = []

        self.book = Book_Management()
        self.book_operation = Book()

        # Menu
        my_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        book_menu = Menu(my_menu)
        my_menu.add_cascade(label="Books", menu=book_menu)
        book_menu.add_command(label="Request", command=lambda: (
            self.master.destroy(), Request_book(id, first, last, user, id_no, status)))
        book_menu.add_command(label="Return", command=lambda: (
            self.master.destroy(), Return_book(id, first, last, user, id_no, status)))

        Label(self.master, text=first + " " + last, font=("calibre", 12), bg=self.color1).grid(row=0, column=0,
                                                                                               columnspan=3,
                                                                                               sticky=EW)
        Label(self.master, text=user, font=("calibre", 12), bg=self.color1).grid(row=0, column=2, columnspan=4,
                                                                                 sticky=EW)
        Label(self.master, text=id_no, font=("calibre", 12), bg=self.color1).grid(row=1, column=0, columnspan=3,
                                                                                  sticky=EW)
        Label(self.master, text=status, font=("calibre", 12), bg=self.color1).grid(row=1, column=2, columnspan=4,
                                                                                   sticky=EW)

        self.your_book = LabelFrame(self.master, text="Your books", padx=10, pady=10, bg=self.color2)
        self.your_book.grid(row=2, column=0, columnspan=3, padx=5, pady=10)
        self.book_tree = ttk.Treeview(self.your_book, columns=("title", "genre", "issued_date"))
        self.book_tree.grid(row=0, column=0)
        self.book_tree['show'] = 'headings'
        self.book_tree.heading("title", text='Title')
        self.book_tree.heading("genre", text='Genre')
        self.book_tree.heading("issued_date", text='Issued Date')
        # self.book_tree.heading("return_date", text='Returned Date')
        self.book_tree.column("title", width=120)
        self.book_tree.column("genre", width=100)
        self.book_tree.column("issued_date", width=120)
        # self.book_tree.column("return_date", width=120)

        Button(self.master, text="Logout", bg=self.color1, command=self.logout, font=15).grid(row=4, column=0,
                                                                                              columnspan=6, pady=10)

    def logout(self):
        self.master.destroy()
        start = Start.Main()
        start.window()


class Request_book(Data):
    def __init__(self, id, first, last, user, id_no, status):
        super().__init__(id, first, last, user, id_no, status)
        self.master.resizable(False, False)
        self.show_book_view()

        self.avai_book = LabelFrame(self.master, text="Available Books", padx=10, pady=10, bg=self.color2)
        self.avai_book.grid(row=2, column=3, columnspan=2, padx=10, pady=10)
        self.order_tree = ttk.Treeview(self.avai_book, columns=("title", "genre", "ava"))
        self.order_tree.grid(row=0, column=1)
        self.order_tree['show'] = 'headings'
        self.order_tree.heading("title", text='Title')
        self.order_tree.heading("genre", text='Genre')
        self.order_tree.heading("ava", text='Availability')
        self.order_tree.column("title", width=120)
        self.order_tree.column("genre", width=120)
        self.order_tree.column("ava", width=100)
        self.show_order_in_tree()

        Button(self.master, text="Request", bg=self.color1, command=self.confirm).grid(row=3, column=0, columnspan=6)

    def show_order_in_tree(self):
        self.order_tree.delete(*self.order_tree.get_children())
        for i in self.book.show_books():
            available = "Yes"
            if i[-3] <= 0:
                available = "No"
            self.order_tree.insert("", "end", text=i[0], values=(i[1], i[4], available))
        self.order_tree.bind("<Double-1>", self.double_click)
        self.order_tree.bind("<ButtonRelease-1>", self.select)

    def select(self, ev):
        try:
            self.selected_id = self.order_tree.item(self.order_tree.selection(), 'text')
            self.selected_row = self.order_tree.item(self.order_tree.selection(), 'value')
            print(self.selected_id)
        except IndexError:
            pass

    def double_click(self, ev):
        win = Toplevel(self.master)
        data = self.book.show_books_data((self.selected_id,))[0]
        win.title(data[1])
        win.geometry("450x450")
        win.config(bg=self.color1)
        filename = data[-1]
        img = ImageTk.PhotoImage(Image.open(filename).resize((150, 175), Image.ANTIALIAS))
        image_label = Label(win, image=img, bg=self.color1)
        image_label.grid(row=0, column=0, rowspan=3, columnspan=2, padx=4)

        # Books details label
        Label(win, text="Title", font=("calibre", 11), bg=self.color1).grid(row=0, column=2, padx=4, pady=20)
        Label(win, text="Author", font=("calibre", 11), bg=self.color1).grid(row=1, column=2, padx=4,
                                                                             pady=20)
        Label(win, text="Publisher", font=("calibre", 11), bg=self.color1).grid(row=2, column=2, padx=4,
                                                                                pady=20)
        Label(win, text="Genre", font=("calibre", 11), bg=self.color1).grid(row=3, column=2, padx=4, pady=20)
        Label(win, text="Price", font=("calibre", 11), bg=self.color1).grid(row=4, column=0, padx=4, pady=20)
        Label(win, text="Quantity", font=("calibre", 11), bg=self.color1).grid(row=5, column=0, padx=4,
                                                                               pady=20)
        Label(win, text="Synopsis", font=("calibre", 11), bg=self.color1).grid(row=4, column=2, rowspan=3,
                                                                               padx=4, pady=20)

        # Entries for Books details
        title = Entry(win, width=25)
        title.grid(row=0, column=3)
        author = Entry(win, width=25)
        author.grid(row=1, column=3)
        publisher = Entry(win, width=25)
        publisher.grid(row=2, column=3)
        genre = Entry(win, width=25)
        genre.grid(row=3, column=3)
        price = Entry(win, width=15)
        price.grid(row=4, column=1)
        number = ttk.Spinbox(win, width=15, from_=0, to=100)
        number.grid(row=5, column=1)
        synopsis = Text(win, width=20, height=10)
        synopsis.grid(row=4, column=3, rowspan=3)

        title.insert(0, data[1])
        author.insert(0, data[2])
        publisher.insert(0, data[3])
        genre.insert(0, data[4])
        price.insert(0, data[5])
        number.set(data[6])
        synopsis.insert(END, data[7])

        title["state"] = DISABLED
        author["state"] = DISABLED
        publisher["state"] = DISABLED
        genre["state"] = DISABLED
        price["state"] = DISABLED
        number["state"] = DISABLED
        synopsis["state"] = DISABLED

        win.mainloop()

    def confirm(self):
        self.show_order_in_tree()
        # print(self.id, self.selected_id)
        quantity = self.book.select_quantity(self.selected_id)[0][0] - 1
        if quantity < 0:
            return messagebox.showinfo("No available", "Book is out of stock")
        self.book.lower_quantity(quantity, self.selected_id)
        self.book_operation.add_book_first((self.id, self.selected_id))
        self.show_book_view()
        self.show_order_in_tree()
        # self.request_book.append((self.selected_id,)+self.selected_row[:-1])

    def show_book_view(self):
        self.book_tree.delete(*self.book_tree.get_children())
        data = self.book_operation.show_book((self.id,))
        for i in data:
            self.book_tree.insert("", "end", text=i[0], values=i[1:])


class Return_book(Data):
    def __init__(self, id, first, last, user, id_no, status):
        super().__init__(id, first, last, user, id_no, status)
        self.master.geometry("860x600+350+100")
        self.master.resizable(False, False)

        self.show_book_view()

        self.issued = LabelFrame(self.master, text="Issued Books", padx=10, pady=10, bg=self.color2)
        self.issued.grid(row=2, column=3, columnspan=3, padx=10, pady=10)
        self.return_tree = ttk.Treeview(self.issued, columns=("title", "genre", "issued_date", "return_date"))
        self.return_tree.grid(row=0, column=0)
        self.return_tree['show'] = 'headings'
        self.return_tree.heading("title", text='Title')
        self.return_tree.heading("genre", text='Genre')
        self.return_tree.heading("issued_date", text='Issued Date')
        self.return_tree.heading("return_date", text='Returned Date')
        self.return_tree.column("title", width=100)
        self.return_tree.column("genre", width=100)
        self.return_tree.column("issued_date", width=120)
        self.return_tree.column("return_date", width=120)

        self.show_return_view()

    def show_book_view(self):
        self.book_tree.delete(*self.book_tree.get_children())
        data = self.book_operation.show_book_to_return((self.id,))
        for i in data:
            self.book_tree.insert("", "end", text=i[0], values=i[1:])
        self.book_tree.bind("<Double-1>", self.select)

    def select(self, ev):
        try:
            self.selected_id = self.book_tree.item(self.book_tree.selection(), 'text')
            self.selected_row = self.book_tree.item(self.book_tree.selection(), 'value')
            # print(self.selected_id, self.selected_row)
            if self.selected_row[-2] == "None":
                messagebox.showerror("Cannot Return", "The book has not been issued!!")
            else:
                self.book_operation.return_book(self.selected_id, date.today())
                quantity = self.book.select_quantity(self.selected_row[-1])[0][0] + 1
                self.book.lower_quantity(quantity, self.selected_row[-1])
                self.show_book_view()
                self.show_return_view()
        except IndexError:
            pass

    def show_return_view(self):
        self.return_tree.delete(*self.return_tree.get_children())
        data = self.book_operation.show_return_book((self.id,))
        for i in data:
            self.return_tree.insert("", "end", text=i[0], values=i[1:])
        # self.return_tree.bind("<Double-1>", self.select)


if __name__ == '__main__':
    a = Request_book(2, "Abhishek", "Hero", "Ho", "Hai", "!!")
    mainloop()
