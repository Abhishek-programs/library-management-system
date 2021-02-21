from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from datetime import date, datetime
from System.Library import Book_Management
import Interface.Start as Start
import Interface.Users as Users
from System.logs import Book as Book_operation
import System.search as search

from PIL import ImageTk, Image


class Main:
    def __init__(self):
        self.master = Tk()
        self.master.title("Library Management System")
        self.master.geometry("1110x560+250+50")
        self.master.resizable(False, False)
        self.color = "#90AFC5"
        self.master.config(background=self.color)
        self.book = Book_Management()
        self.book_operation = Book_operation()
        self.tree_item = []
        self.selected_text = []

        # Menu
        my_menu = Menu(self.master)
        self.master.config(menu=my_menu)
        book_menu = Menu(my_menu)
        my_menu.add_cascade(label="Books", menu=book_menu)
        book_menu.add_command(label="Operations", command=lambda: (self.master.destroy(), Operation()))
        book_menu.add_command(label="View", command=lambda: (self.master.destroy(), View()))

        members_menu = Menu(my_menu)
        my_menu.add_cascade(label="Members", menu=members_menu)
        members_menu.add_command(label="Operations", command=lambda: (self.master.destroy(), Users.My_Users()))

        options_menu = Menu(my_menu)
        my_menu.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Back", command=self.back)
        options_menu.add_separator()
        options_menu.add_command(label="Log Out", command=self.logout)

    def back(self):
        self.master.destroy()
        start = Start.Main()
        start.popup()

    def logout(self):
        self.master.destroy()
        start = Start.Main()
        start.window()


class Operation(Main):
    def __init__(self):
        super().__init__()
        # BookFrame
        # self.master.resizable(False, False)
        self.book_frame = LabelFrame(self.master, text="Book Details", bg=self.color, labelanchor='n', padx=20, pady=20)
        self.book_frame.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        # Design adding book Interface for books

        # Browse Images
        self.filename = "../Images/add_cover.jpg"
        self.img = ImageTk.PhotoImage(Image.open(self.filename).resize((150, 175), Image.ANTIALIAS))
        self.image_label = Label(self.book_frame, image=self.img, bg=self.color)
        self.image_label.grid(row=0, column=0, rowspan=3, columnspan=2, padx=4)
        Button(self.book_frame, text="Browse Cover Image", command=self.browse).grid(row=3, column=0, columnspan=2,
                                                                                     sticky=EW)

        # Books details label
        Label(self.book_frame, text="Title", font=("calibre", 11), bg=self.color).grid(row=0, column=2, padx=4, pady=20)
        Label(self.book_frame, text="Author", font=("calibre", 11), bg=self.color).grid(row=1, column=2, padx=4,
                                                                                        pady=20)
        Label(self.book_frame, text="Publisher", font=("calibre", 11), bg=self.color).grid(row=2, column=2, padx=4,
                                                                                           pady=20)
        Label(self.book_frame, text="Genre", font=("calibre", 11), bg=self.color).grid(row=3, column=2, padx=4, pady=20)
        Label(self.book_frame, text="Price", font=("calibre", 11), bg=self.color).grid(row=4, column=0, padx=4, pady=20)
        Label(self.book_frame, text="Quantity", font=("calibre", 11), bg=self.color).grid(row=5, column=0, padx=4,
                                                                                          pady=20)
        Label(self.book_frame, text="Synopsis", font=("calibre", 11), bg=self.color).grid(row=4, column=2, rowspan=3,
                                                                                          padx=4, pady=20)

        # Entries for Books details
        self.title = Entry(self.book_frame, width=25)
        self.title.grid(row=0, column=3)
        self.author = Entry(self.book_frame, width=25)
        self.author.grid(row=1, column=3)
        self.publisher = Entry(self.book_frame, width=25)
        self.publisher.grid(row=2, column=3)
        self.genre = Entry(self.book_frame, width=25)
        self.genre.grid(row=3, column=3)
        self.price = Entry(self.book_frame, width=15)
        self.price.grid(row=4, column=1)
        self.number = ttk.Spinbox(self.book_frame, state="readonly", width=15, from_=0, to=100)
        self.number.grid(row=5, column=1)
        self.synopsis = Text(self.book_frame, width=20, height=10)
        self.synopsis.grid(row=4, column=3, rowspan=3)

        Button(self.book_frame, text="Clear", bg=self.color, command=self.clear).grid(row=6, column=0, columnspan=3)

        Label(self.master, text="Search: ", font=("calibre", 12), bg=self.color).grid(row=0, column=1, pady=(10, 0))
        search_for = Entry(self.master, font=("calibre", 12))
        search_for.grid(row=0, column=2, pady=(10, 0))

        search_by = ttk.Combobox(self.master, state="readonly", width=20, values=["Title", "Author"])
        search_by.grid(row=0, column=3, padx=5, pady=(10, 0))

        s_btn = Button(self.master, text="Search", command=lambda: (self.search(search_by.get(), search_for.get())))
        s_btn.grid(row=0, column=4, pady=(10, 0), sticky=EW)
        Button(self.master, text="Show", command=self.show_in_tree).grid(row=0, column=5, pady=(10, 0))

        # Table View for Books CRUD
        self.book_tree = ttk.Treeview(self.master, columns=("title", "author", "publisher", "genre", "price", "qty"))
        self.book_tree.grid(row=1, column=1, columnspan=6, padx=15, pady=20)
        self.book_tree['show'] = 'headings'
        self.book_tree.heading("title", text='Title')
        self.book_tree.heading("author", text='Author')
        self.book_tree.heading("publisher", text='Publisher')
        self.book_tree.heading("genre", text='Genre')
        self.book_tree.heading("price", text='Price')
        self.book_tree.heading("qty", text='Quantity')
        self.book_tree.column("title", width=120)
        self.book_tree.column("author", width=100)
        self.book_tree.column("publisher", width=100)
        self.book_tree.column("genre", width=80)
        self.book_tree.column("price", width=100)
        self.book_tree.column("qty", width=100)
        self.show_in_tree()

        self.image1 = ImageTk.PhotoImage(Image.open("../Images/button_add.png").resize((150, 75), Image.ANTIALIAS))
        self.image2 = ImageTk.PhotoImage(Image.open("../Images/button_edit.png").resize((150, 75), Image.ANTIALIAS))
        self.image3 = ImageTk.PhotoImage(Image.open("../Images/button_remove.png").resize((150, 75), Image.ANTIALIAS))
        Button(self.master, borderwidth=0, image=self.image1, bg=self.color, command=self.add_books).grid(row=3,
                                                                                                          column=0)
        Button(self.master, borderwidth=0, image=self.image2, bg=self.color, command=self.edit_books).grid(row=3,
                                                                                                           column=1)
        Button(self.master, borderwidth=0, image=self.image3, bg=self.color, command=self.delete_books).grid(row=3,
                                                                                                             column=3)

    def browse(self):
        self.filename = filedialog.askopenfilename(initialdir="../Images/", title="Select Cover",
                                                   filetype=(("jpg files", "*.jpg"), ("all files", "*.*")))
        try:
            self.image_cover(self.filename)
        except AttributeError:
            a = messagebox.askyesno("Book Cover Image", "Does the book have cover image?")
            if a:
                self.browse()
            else:
                self.filename = "../Images/add_cover.jpg"

    def show_in_tree(self):
        self.book_tree.delete(*self.book_tree.get_children())
        self.tree_item = self.book.show_books()
        # print(self.tree_item)
        for i in self.tree_item:
            # print(i)
            self.book_tree.insert("", "end", text=str(i[0]) + "," + i[7] + "," + i[8], values=i[1:7])
        self.book_tree.bind("<ButtonRelease-1>", self.select)

    def select(self, ev):
        try:
            self.selected_text = self.book_tree.item(self.book_tree.selection(), 'text').split(",")
            selected_row = self.book_tree.item(self.book_tree.selection(), 'value')
            # print(self.user_tree.item(self.user_tree.selection(), 'text'))
            self.clear()
            self.title.insert(0, selected_row[0])
            self.author.insert(0, selected_row[1])
            self.publisher.insert(0, selected_row[2])
            self.genre.insert(0, selected_row[3])
            self.price.insert(0, selected_row[4])
            self.number.set(selected_row[5])
            self.synopsis.insert(END, self.selected_text[1])
            # print(self.selected_text)
            self.image_cover(self.selected_text[2])
        except IndexError:
            pass

    def image_cover(self, filename):
        self.filename = filename
        self.img = ImageTk.PhotoImage(Image.open(self.filename).resize((150, 175), Image.ANTIALIAS))
        self.image_label.grid_remove()
        self.image_label = Label(self.book_frame, image=self.img)
        self.image_label.grid(row=0, column=0, rowspan=3, columnspan=2, padx=4)

    def add_books(self):
        if (self.title.get() and self.author.get() and self.publisher.get() and self.genre.get() and
                self.price.get() and self.number.get() and self.synopsis.get(1.0, END) and self.filename):
            self.book.add_books((self.title.get(), self.author.get(), self.publisher.get(), self.genre.get(),
                                 self.price.get(), self.number.get(), self.synopsis.get(1.0, END), self.filename))
        else:
            messagebox.showerror("Empty Field", "Fill all the entry fields")
        self.show_in_tree()
        self.clear()

    def edit_books(self):
        self.book.update_books((self.title.get(), self.author.get(), self.publisher.get(), self.genre.get(),
                                self.price.get(), self.number.get(), self.synopsis.get(1.0, END), self.filename,
                                int(self.selected_text[0])))
        self.show_in_tree()
        self.clear()

    def delete_books(self):
        if self.book.delete_books((int(self.selected_text[0]))):
            messagebox.showinfo("Deleted", "Book is deleted")
        else:
            messagebox.showerror("Not Deleted", "Book has been issued or requested")
        self.show_in_tree()
        self.clear()

    def clear(self):
        self.title.delete(0, END)
        self.author.delete(0, END)
        self.publisher.delete(0, END)
        self.genre.delete(0, END)
        self.price.delete(0, END)
        self.number.delete(0, END)
        self.synopsis.delete(1.0, END)
        self.image_cover("../Images/add_cover.jpg")

    def search(self, searchby, searchfor):
        # data = self.exe.search()
        data = None
        a = None
        if searchby == "Title":
            data, a = search.search_by_title(searchfor)
        elif searchby == "Author":
            data, a = search.search_by_author(searchfor)
        else:
            messagebox.showerror('Error', 'wrong search')
        self.book_tree.delete(*self.book_tree.get_children())

        self.book_tree.insert('', END, values=data[a][1:])


class View(Main):
    def __init__(self):
        super().__init__()
        self.master.geometry("600x455+250+50")
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack()

        self.all_book = Frame(self.notebook, width=570, height=500, bg=self.color)
        self.issue_book = Frame(self.notebook, width=570, height=500, bg=self.color)
        self.return_book = Frame(self.notebook, width=570, height=500, bg=self.color)

        self.all_book.pack()
        self.issue_book.pack()
        self.return_book.pack()

        self.notebook.add(self.all_book, text="Books")
        self.notebook.add(self.issue_book, text="Issue Books")
        self.notebook.add(self.return_book, text="Returned Books")

        self.all_view()
        self.issued_view()
        self.returned_view()

    def all_view(self):
        # Search for All
        Label(self.all_book, text="Search: ", font=("calibre", 12), bg=self.color).grid(row=0, column=0, pady=(10, 0))
        search_for = Entry(self.all_book, font=("calibre", 12))
        search_for.grid(row=0, column=1, pady=(10, 0))

        search_by = ttk.Combobox(self.all_book, state="readonly", width=20, values=["Requester", "Title"])
        search_by.grid(row=0, column=2, padx=5, pady=(10, 0))

        sbtn = Button(self.all_book, text="Search", command=lambda: (self.search(search_by.get(), search_for.get())))
        sbtn.grid(row=0, column=3, pady=(10, 0), sticky=EW)

        self.all_tree = ttk.Treeview(self.all_book, height=15,
                                     columns=("title", "genre", "user", "issued_date", "returned_date"))
        self.all_tree.grid(row=1, column=0, columnspan=5, pady=(20,), padx=19)
        self.all_tree['show'] = 'headings'
        self.all_tree.heading("title", text='Title')
        self.all_tree.heading("genre", text='Genre')
        self.all_tree.heading("user", text='Requester')
        self.all_tree.heading("issued_date", text='Issued Date')
        self.all_tree.heading("returned_date", text='Returned Date')
        self.all_tree.column("title", width=120)
        self.all_tree.column("genre", width=100)
        self.all_tree.column("user", width=100)
        self.all_tree.column("issued_date", width=120)
        self.all_tree.column("returned_date", width=120)
        self.all_book_view()

        Button(self.all_book, text="Show All", width=10, command=self.all_book_view).grid(row=2, column=0, columnspan=4)

    def issued_view(self):
        # View for the issued
        self.book_tree = ttk.Treeview(self.issue_book, height=15, columns=("title", "genre", "user"))
        self.book_tree.pack(fill=BOTH, padx=20, pady=20)
        self.book_tree['show'] = 'headings'
        self.book_tree.heading("title", text='Title')
        self.book_tree.heading("genre", text='Genre')
        self.book_tree.heading("user", text='Requester')
        self.book_tree.column("title", width=120)
        self.book_tree.column("genre", width=100)
        self.book_tree.column("user", width=100)
        self.show_book_view()

        Button(self.issue_book, text="Cancel Request", command=self.cancel).pack()

    def returned_view(self):
        # View for the returned
        self.return_tree = ttk.Treeview(self.return_book, height=15,
                                        columns=("title", "genre", "user", "issued_date", "returned_date"))
        self.return_tree.grid(row=1, column=1, columnspan=3, pady=20, padx=19)
        self.return_tree['show'] = 'headings'
        self.return_tree.heading("title", text='Title')
        self.return_tree.heading("genre", text='Genre')
        self.return_tree.heading("user", text='Requester')
        self.return_tree.heading("issued_date", text='Issued Date')
        self.return_tree.heading("returned_date", text='Returned Date')
        self.return_tree.column("title", width=120)
        self.return_tree.column("genre", width=100)
        self.return_tree.column("user", width=100)
        self.return_tree.column("issued_date", width=120)
        self.return_tree.column("returned_date", width=120)
        self.returned_book_view()

    def all_book_view(self):
        self.all_tree.delete(*self.all_tree.get_children())
        data = self.book_operation.show_all_books()
        for i in data:
            self.all_tree.insert("", "end", text=i[0], values=i[1:])
        # self.all_tree.bind("<Double-1>")

    def returned_book_view(self):
        self.return_tree.delete(*self.return_tree.get_children())
        data = self.book_operation.show_returned_books()
        for i in data:
            self.return_tree.insert("", "end", text=i[0], values=i[1:])
        self.return_tree.bind("<Double-1>", self.fine)

    def fine(self, ev):
        selected_row = self.return_tree.item(self.return_tree.selection(), 'value')
        # print(selected_row[-1], selected_row[-2])
        format_str = "%Y-%m-%d"
        datetime_obj = [datetime.strptime(selected_row[-1], format_str).date(),
                        datetime.strptime(selected_row[-2], format_str).date()]
        date_diff = (datetime_obj[0]-datetime_obj[1])
        if date_diff.days > 20:
            messagebox.showinfo("Fine", "You are fined Rs."+str(date_diff.days * 5))
        else:
            messagebox.showinfo("No fine", "You are not fined")

    def show_book_view(self):
        self.book_tree.delete(*self.book_tree.get_children())
        data = self.book_operation.show_issue_book()
        for i in data:
            self.book_tree.insert("", "end", text=(i[0], i[1]), values=i[2:])
        self.book_tree.bind("<ButtonRelease-1>", self.select)
        self.book_tree.bind("<Double-1>", self.select_double)

    def cancel(self):
        self.book_operation.dele((self.selected_id[0],))
        quantity = self.book.select_quantity(self.selected_id[1])[0][0] + 1
        self.book.lower_quantity(quantity, self.selected_id[1])
        self.all_book_view()
        self.show_book_view()

    def select(self, ev):
        try:
            self.selected_id = self.book_tree.item(self.book_tree.selection(), 'text').split()
            self.selected_row = self.book_tree.item(self.book_tree.selection(), 'value')
        except IndexError:
            pass

    def select_double(self, ev):
        try:
            a = messagebox.askyesno("Issue Book", "Do you want to issue the book?")
            if a:
                self.book_operation.issue_book((date.today(), self.selected_id[0]))
                self.show_book_view()
                self.all_book_view()
        except Exception:
            pass

    def search(self, searchby, searchfor):
        a = search.db_search(searchby, searchfor)
        print(a)
        self.all_tree.delete(*self.all_tree.get_children())
        for i in a:
            self.all_tree.insert("", "end", text=i[0], values=i[1:])


if __name__ == '__main__':
    Operation()
    mainloop()
