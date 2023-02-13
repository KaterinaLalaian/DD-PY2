class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """" Бумажная книга """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError(f'Количество страниц должно быть типа int')
        if pages < 0:
            raise ValueError(f'Количество страниц не может быть отрицательным')
        self.pages = pages

    def __str__(self):
        str_paper = super().__str__()
        return f"{str_paper}. Страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """" Аудиокнига """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError(f'Продолжительность аудиокниги должна быть типа float')
        if duration <= 0:
            raise ValueError(f'Продолжительность аудиокниги не может быть отрицательной или равной нулю')
        self.duration = duration

    def __str__(self):
        str_audio = super().__str__()
        return f"{str_audio}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    book_1 = Book('Золотая рыбка', 'А. С. Пушкин')
    print(book_1)  # Книга Золотая рыбка. Автор А. С. Пушкин
    book_2 = PaperBook('Золотая рыбка', 'А. С. Пушкин', 30)
    print(book_2)  # Книга Золотая рыбка. Автор А. С. Пушкин. Страниц 30
    book_3 = AudioBook('Золотая рыбка', 'А. С. Пушкин', 14.42)
    print(book_3)  # Книга Золотая рыбка. Автор А. С. Пушкин. Продолжительность 14.42
