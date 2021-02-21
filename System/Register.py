from Database import MyDatabase


class Register:
    def __init__(self):
        self.db = MyDatabase()

    def register(self, value):
        qry = """insert into register(firstname, lastname, username, id_no, address, contact, status, password)
                    values(%s, %s, %s, %s, %s, %s, %s, %s)"""
        return self.db.iud(qry, value)

    def update(self, value):
        qry = """update register set firstname=%s, lastname=%s, username=%s, id_no=%s, address=%s, contact=%s, status=%s
                    where id=%s"""
        return self.db.iud(qry, value)

    def show_pass(self, username, status):
        qry = """select * from register where username=%s and status=%s"""
        value = (username, status)
        return self.db.show_data_parameter(qry, value)

    def show(self):
        qry = """select * from register"""
        return self.db.show_data(qry)

    def dele(self, values):
        qry = """DELETE FROM requested_books WHERE user_id =%s"""
        self.db.iud(qry, values)
        qry = """DELETE FROM register WHERE id =%s"""
        return self.db.iud(qry, values)
