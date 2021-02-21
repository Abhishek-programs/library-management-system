from Database import MyDatabase

db = MyDatabase()


def binary_search(list_element, value, index):
    # set value to 'left' and 'right'
    left = 0
    right = len(list_element) - 1
    # start loop until left is greater than right
    while left <= right:
        # calculate midpoint
        mid = int((right + left) // 2)
        # check if item is equal to  value
        if list_element[mid][index] == value:
            # print(list_element[mid])
            return mid
        # if value is smaller than mid point, changing the right value to midpoint -1
        elif list_element[mid][index] > value:
            # print(list_element[mid])
            right = mid - 1
        # if value is greater than mid point, changing the left value to midpoint +1
        elif list_element[mid][index] < value:
            # print(list_element[mid])
            left = mid + 1
        # return false if nothing is satisfied
        else:
            return False
    # return false for not found
    return False


def search_by_title(value):
    qry = """select * from book order by title"""
    list_element = db.show_data(qry)
    index = 1
    a = binary_search(list_element, value, index)
    return list_element, a


def search_by_author(value):
    qry = """select * from book order by author"""
    list_element = db.show_data(qry)
    index = 2
    a = binary_search(list_element, value, index)
    return list_element, a


def search_by_username(value):
    qry = """select * from register order by username"""
    list_element = db.show_data(qry)
    index = 3
    a = binary_search(list_element, value, index)
    return list_element, a


def db_search(searchby, searchfor):
    # print(searchby)
    if searchby == "Title":
        searchby = "book.title"
    else:
        searchby = "register.username"
    qry = "SELECT requested_books.id, book.title, book.genre, register.username, requested_books.issued_date, \
                requested_books.returned_date \
                FROM requested_books \
                JOIN book ON requested_books.book_id = book.id \
                JOIN register ON requested_books.user_id = register.Id\
                WHERE {} LIKE '{}%'".format(searchby, searchfor)
    return db.show_data(qry)
