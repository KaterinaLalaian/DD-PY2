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


class Library:  # класс Library
    def __init__(self, books=None):  # books - необязательный аргумент со значением по умолчанию
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:  # Если книг в библиотеке нет, то возвращается 1
            return 1
        else:
            return self.books[-1].id_ + 1  # Если книги есть, то идентификатор последней книги увеличевается на 1

    def get_index_by_book_id(self, id_: int):
        for i, name in enumerate(self.books):
            if name.id_ == id_:  # Если книга существует, то возвращается индекс из списка
                return i
            else:
                raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки  #1

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки  #3

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1  #0
