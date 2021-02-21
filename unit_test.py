import unittest
from System.Library import Book_Management
from System.Register import Register


class testing(unittest.TestCase):
    obj = Register()
    obj1 = Book_Management()

    def test_register(self):
        actual_result = self.obj.register(("Abhishek", "Bhattarai", "Sans", 525, "Ghar", 69420, "Staff", "yeiho"))
        answer = True
        self.assertEqual(actual_result, answer)

    def test_update(self):  # The last value i.e ID needs to be taken in care as it is auto_increment and primary
        actual_result = self.obj.update(("NotAbhi", "NotBhatt", "NotSans", 9, "NotG", 42069, "Students", 5))
        answer = True
        self.assertEqual(actual_result, answer)

    def test_addbooks(self):
        actual_result = self.obj1.add_books(
            ("Check", "Check", "Check", "Check", 1000, 20, "Check", "../Images/add_cover.jpg"))
        answer = True
        self.assertEqual(actual_result, answer)

    def test_updatebooks(self):
        actual_result = self.obj1.update_books(
            ("NotCheck", "NotCheck", "NotCheck", "NotCheck", 10, 5, "NotCheck", "../Images/add_cover.jpg", 3))
        answer = True
        self.assertEqual(actual_result, answer)
        
    def test_showpass(self):
        actual_result = self.obj.show_pass("NotAbhi", "Students")
        self.assertNotEqual(actual_result, False)
        # Not Equal because we expect True if there is data and False if no data.
