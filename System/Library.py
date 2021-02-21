from Database import MyDatabase


class Book_Management:
    def __init__(self):
        self.db = MyDatabase()

    def add_books(self, value):
        qry = """insert into book(title, author, publisher, genre, price, quantity, synopsis, image)
                    values(%s, %s, %s, %s, %s, %s, %s, %s)"""
        return self.db.iud(qry, value)

    def update_books(self, value):
        qry = """UPDATE book SET title=%s, author=%s, publisher=%s, genre=%s, price=%s, quantity=%s, synopsis=%s,
                    image=%s WHERE id=%s"""
        return self.db.iud(qry, value)

    def delete_books(self, value):
        qry = """delete from book where id=%s"""
        value = (value,)
        return self.db.iud(qry, value)

    def show_books(self):
        qry = """select * from book"""
        return self.db.show_data(qry)

    def select_quantity(self, value):
        qry = """select quantity from book where id=%s"""
        value = (value,)
        return self.db.show_data_parameter(qry, value)

    def lower_quantity(self, quantity, value):
        qry = """UPDATE book SET quantity =%s WHERE id=%s"""
        values = (quantity, value)
        return self.db.iud(qry, values)

    def raise_quantity(self, quantity, value):
        qry = """UPDATE book SET quantity =%s WHERE id=%s"""
        values = (quantity, value)
        return self.db.iud(qry, values)

    def show_books_data(self, value):
        qry = """select * from book where id =%s"""
        return self.db.show_data_parameter(qry, value)
