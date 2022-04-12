import json
from csv import reader


class LibraryUser:
    def __init__(self, name, gender, address, age):
        self.name = name
        self.gender = gender
        self.address = address
        self.age = age
        self.books = []

    def add_book(self, book_item):
        self.books.append(book_item)


def read_users_from_json(file_name):
    with open(file_name, "r") as users_file:
        return json.load(users_file)


def read_books_from_csv(file_name, number_of_columns=0):
    with open(file_name, "r") as books_file:
        books_file = reader(books_file)
        header = [column_name.lower() for column_name in next(books_file)]
        books_list = []
        for row in books_file:
            if number_of_columns != 0:
                books_list.append(dict(zip(header, row[:number_of_columns])))
            else:
                books_list.append(dict(zip(header, row)))
        return books_list


def write_result_in_json(file_name, values):
    with open(file_name, "w") as result_file:
        result_file.write(json.dumps(values, indent=4))


def distribution_of_books_by_users(users, books, file_name="result.json", model_generator="List comprehension"):
    users_len = len(users)
    users_list = []
    if model_generator == "List comprehension":
        users_list = [LibraryUser(user["name"], user["gender"], user["address"], user["age"]) for user in users]
    elif model_generator == "Loop":
        for user in users:
            users_list.append(LibraryUser(user["name"], user["gender"], user["address"], user["age"]))
    else:
        print(
            f'Invalid value model_generator = {model_generator}, please select one of the options:\
List comprehension or Loop')
        return
    for i, book in enumerate(books):
        users_list[i % users_len].add_book(book)
    write_result_in_json(f"{file_name}", [user.__dict__ for user in users_list])


distribution_of_books_by_users(users=read_users_from_json("users.json"), books=read_books_from_csv("books.csv"),
                               model_generator="Loop")
