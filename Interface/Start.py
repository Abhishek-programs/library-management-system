from tkinter import *
from tkinter import ttk, messagebox
import Interface.Book_operation as Book
import Interface.Users as Users
import Interface.Personal_data as Personal
from System.Register import Register as Reg

from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import bcrypt, bcrypt_check


def encrypt(password):
    password = password.encode('utf-8')
    b64pwd = b64encode(SHA256.new(password).digest())
    bcrypt_hash = bcrypt(b64pwd, 10)
    # decrypt(bcrypt_hash)
    return bcrypt_hash


def decrypt(bcrypt_hash, password_to_test):
    password_to_test = password_to_test.encode('utf-8')
    try:
        b64pwd_new = b64encode(SHA256.new(password_to_test).digest())
        bcrypt_check(b64pwd_new, bcrypt_hash)
        return True
    except ValueError:
        return False


class Main:
    def __init__(self):
        self.master = Tk()
        self.color1 = "#C4DFE6"
        self.color2 = "#90AFC5"
        self.master.title("Library Management System")
        self.master.geometry("700x500+450+150")
        self.master.resizable(False, False)
        self.master.config(background=self.color2)
        self.reg = Reg()

    def window(self):
        window = Frame(self.master, background=self.color2)
        window.pack(fill=X)
        Label(window, text="Library Management System", font=("calibre", 30), bg="#3E363F", fg=self.color1,
              pady=10).pack(side=TOP, fill=X)
        Button(window, text="Register", font=("calibre", 12), padx=15, bg=self.color1,
               activebackground=self.color1, relief=GROOVE, command=lambda: (self.master.destroy(), Register())).pack(
            pady=15)
        Canvas(window, width=300, height=2, bg="Black").pack(side=LEFT, anchor=N, pady=10)
        Canvas(window, width=300, height=2, bg="Black").pack(side=RIGHT, anchor=N, pady=10)
        Label(window, text="OR", font=("calibre", 15), bg=self.color2).pack(anchor=N)

        frame = Frame(self.master, background=self.color2)
        frame.pack()

        Label(frame, text="Username", font=("calibre", 17), bg=self.color2, padx=10, pady=10).grid(row=0, column=0)

        username = Entry(frame, width=20, font=("calibre", 12))
        username.grid(row=0, column=1)

        Label(frame, text="Password", font=("calibre", 17), bg=self.color2, padx=10, pady=10).grid(row=1, column=0)

        password = Entry(frame, width=20, font=("calibre", 12), show="*")
        password.grid(row=1, column=1)

        users = ttk.Combobox(frame, state="readonly", width=25, height=10, value=["Staff", "Student"])
        users.grid(row=2, column=0, columnspan=2, pady=10)

        Button(frame, text="Login", font=("calibre", 13), width=9, bg=self.color1,
               command=lambda: self.login(users.get(), username.get(), password.get())).grid(row=3, column=0,
                                                                                             columnspan=2)
        Button(frame, text="Exit", font=("calibre", 13), width=9, bg=self.color1, command=self.master.destroy).grid(
            row=4, column=0, columnspan=2, pady=20)

        mainloop()

    def login(self, status, username, password):  # checks for validity... WIP
        try:
            data = self.reg.show_pass(username, status)[0]
        except IndexError:
            messagebox.showerror("Error", "Couldn't Sign In")
        else:
            if decrypt(data[-1], password) or (data[-1] == password):
                if status == "Staff":
                    self.popup()
                else:
                    self.master.destroy()
                    Personal.Request_book(data[0], data[1], data[2], data[3], data[4], data[-2])
            else:
                messagebox.showerror("Error", "Wrong Credentials")

    def popup(self):
        self.master.destroy()
        win = Tk()
        win.title("Choice")
        win.geometry("250x120+680+330")
        win.resizable(False, False)
        win.config(background=self.color1)
        Button(win, text="Users Management", font=("calibre", 12), command=lambda: (win.destroy(), Users.My_Users()),
               relief=RIDGE).pack(pady=20)
        Button(win, text="Library Management", font=("calibre", 12), command=lambda: (win.destroy(), Book.Operation()),
               relief=RIDGE).pack()


class Register(Main):
    def __init__(self):
        super().__init__()
        self.var = StringVar()
        self.var.set('Student')

        Label(self.master, text="Registration", font=("calibre", 20), bg=self.color1, padx=20, pady=20).pack(fill=X)

        frame = LabelFrame(self.master, background=self.color1, padx=10, pady=10, relief=SUNKEN)
        frame.pack(padx=20, pady=20)

        Label(frame, text="First Name", bg=self.color1, padx=10, pady=5).grid(row=0, column=0)

        self.first_name = Entry(frame, width=20, font=("calibre", 10))
        self.first_name.grid(row=0, column=1)

        Label(frame, text="Last Name", bg=self.color1, padx=10, pady=5).grid(row=1, column=0)

        self.last_name = Entry(frame, width=20, font=("calibre", 10))
        self.last_name.grid(row=1, column=1)

        Label(frame, text="Username", bg=self.color1, padx=10, pady=5).grid(row=2, column=0)

        self.username = Entry(frame, width=20, font=("calibre", 10))
        self.username.grid(row=2, column=1)

        Label(frame, text="Password", bg=self.color1, padx=10, pady=5).grid(row=3, column=0)

        self.password = Entry(frame, width=20, font=("calibre", 10), show="*")
        self.password.grid(row=3, column=1)

        Label(frame, text="ID Card No.", bg=self.color1, padx=10, pady=5).grid(row=4, column=0)

        self.id_no = Entry(frame, width=20, font=("calibre", 10))
        self.id_no.grid(row=4, column=1)

        Label(frame, text="Address", bg=self.color1, padx=10, pady=5).grid(row=5, column=0)

        self.address = Entry(frame, width=20, font=("calibre", 10))
        self.address.grid(row=5, column=1)

        Label(frame, text="Contact", bg=self.color1, padx=10, pady=5).grid(row=6, column=0)

        self.contact = Entry(frame, width=20, font=("calibre", 10))
        self.contact.grid(row=6, column=1)

        Radiobutton(frame, text="Staff", variable=self.var, bg=self.color1, activebackground=self.color1,
                    value='Staff', command=self.radio).grid(row=7, column=0)
        Radiobutton(frame, text="Student", variable=self.var, bg=self.color1, activebackground=self.color1,
                    value='Student', command=self.radio).grid(row=7, column=1)

        Label(frame, text="Authority Code", bg=self.color1, padx=10, pady=5).grid(row=8, column=0)

        self.auth = Entry(frame, state=DISABLED)
        self.auth.grid(row=8, column=1)

        Button(frame, text="Register", width=10, bg=self.color1, command=self.register).grid(row=9, column=0,
                                                                                             columnspan=2, pady=10)

        Button(self.master, text="Back", bg=self.color1, command=self.back).pack()

    def radio(self):
        if self.var.get() == "Staff":
            self.auth['state'] = NORMAL
        else:
            self.auth['state'] = DISABLED

    def register(self):
        if (self.first_name.get() and self.last_name.get() and self.username.get() and self.id_no.get().isdigit() and
                self.address.get() and self.contact.get().isdigit() and self.var.get() and self.password.get()):
            passing = encrypt(self.password.get())
            if self.var.get() == "Staff" and self.auth.get() != "1010":
                messagebox.showerror("Wrong Admin Code", "The admin code for admin authority account is incorrect.")
            else:
                self.reg.register((self.first_name.get(), self.last_name.get(), self.username.get(), self.id_no.get(),
                                   self.address.get(), self.contact.get(), self.var.get(), passing))
                messagebox.showinfo("Registered", "Your account has been registered.")
                self.clear()
        else:
            # print(self.id_no.get().isdigit())
            if self.id_no.get().isdigit() and self.contact.get().isdigit():
                messagebox.showerror("Empty Field", "Fill all the entry fields")
            else:
                messagebox.showerror("Wrong Type", "Expected Integer in contact and ID no")

    def clear(self):
        self.first_name.delete(0, END)
        self.last_name.delete(0, END)
        self.username.delete(0, END)
        self.password.delete(0, END)
        self.id_no.delete(0, END)
        self.address.delete(0, END)
        self.contact.delete(0, END)
        self.auth.delete(0, END)
        self.var.set("Student")
        self.auth['state'] = DISABLED

    def back(self):
        self.master.destroy()
        b = Main()
        b.window()


if __name__ == '__main__':
    a = Main()
    a.window()
