from Database import MyDatabase


class Book:
    def __init__(self):
        self.db = MyDatabase()

    def add_book_first(self, values):
        qry = """insert into requested_books(user_id, book_id) values(%s,%s)"""
        self.db.iud(qry, values)

    def show_book(self, value):
        qry = """select requested_books.id, book.title, book.genre, requested_books.issued_date from requested_books
        join book on requested_books.book_id = book.id
        join register on requested_books.user_id = register.Id where user_id=%s"""
        return self.db.show_data_parameter(qry, value)

    def issue_book(self, values):
        qry = """update requested_books set issued_date=%s where id=%s"""
        self.db.iud(qry, values)

    def dele(self, values):
        qry = """DELETE FROM requested_books WHERE id =%s"""
        self.db.iud(qry, values)

    def show_issue_book(self):
        qry = """select requested_books.id, book.id, book.title, book.genre, register.username, requested_books.issued_date
        from requested_books
        join book on requested_books.book_id = book.id
        join register on requested_books.user_id = register.Id
        where requested_books.issued_date is null"""
        return self.db.show_data(qry)

    def return_book(self, user_id, return_date):
        qry = """update requested_books set returned_date=%s where id =%s"""
        values = (return_date, user_id)
        self.db.iud(qry, values)
        return True

    def show_return_book(self, value):
        qry = """select requested_books.id, book.title, book.genre, requested_books.issued_date, requested_books.returned_date, requested_books.book_id
        from requested_books
        join book on requested_books.book_id = book.id
        join register on requested_books.user_id = register.Id
        where requested_books.returned_date is not null and requested_books.user_id=%s"""
        return self.db.show_data_parameter(qry, value)

    def show_book_to_return(self, value):
        qry = """select requested_books.id, book.title, book.genre, requested_books.issued_date, requested_books.book_id
        from requested_books
        join book on requested_books.book_id = book.id
        join register on requested_books.user_id = register.Id
        where requested_books.returned_date is null and requested_books.user_id=%s"""
        return self.db.show_data_parameter(qry, value)

    def show_returned_books(self):
        qry = """select requested_books.id, book.title, book.genre, register.username, requested_books.issued_date, requested_books.returned_date
        from requested_books
        join book on requested_books.book_id = book.id
        join register on requested_books.user_id = register.Id
        where requested_books.returned_date is not null"""
        return self.db.show_data(qry)

    def show_all_books(self):
        qry = """select requested_books.id, book.title, book.genre, register.username, requested_books.issued_date, requested_books.returned_date
        from requested_books
        join book on requested_books.book_id = book.id
        join register on requested_books.user_id = register.Id"""
        return self.db.show_data(qry)
