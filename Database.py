import mysql.connector


class MyDatabase:
    def __init__(self):
        self.my_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Library"
        )
        self.my_cursor = self.my_connection.cursor()
        # print("working")
        # self.my_cursor.execute(qry)

    def iud(self, qry, values):
        try:
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            return True
        except Exception:
            return False

    def show_data(self, qry):
        try:
            self.my_cursor.execute(qry)
            data = self.my_cursor.fetchall()
            return data
        except Exception:
            return False

    def show_data_parameter(self, qry, values):
        try:
            self.my_cursor.execute(qry, values)
            data = self.my_cursor.fetchall()
            return data
        except Exception:
            return False

    def return_id(self, qry, values):
        try:
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            return self.my_cursor.lastrowid
        except Exception:
            return False
