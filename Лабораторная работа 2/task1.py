BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:  # класс Book
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:  # метод __str__
        return f'Книга "{self.name}"'

    def __repr__(self):  # метод __repr__
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'  # для строк важно указать !r


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # Книга "test_name_1"  # Книга "test_name_2"

    print(list_books)  # [Book(id_=1, name='test_name_1', pages=200), Book(id_=2, name='test_name_2', pages=400)]
