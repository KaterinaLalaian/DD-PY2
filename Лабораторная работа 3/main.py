class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError(f'Название должно быть типа str')
        self._name = new_name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        if not isinstance(new_author, str):
            raise TypeError(f'Автор должен быть типа str')
        self._author = new_author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """" Бумажная книга """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError(f'Количество страниц должно быть типа int')
        if new_pages < 0:
            raise ValueError(f'Количество страниц не может быть отрицательным')
        self._pages = new_pages

    def __str__(self):
        str_paper = super().__str__()
        return f"{str_paper}. Страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"


class AudioBook(Book):
    """" Аудиокнига """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError(f'Продолжительность аудиокниги должна быть типа float')
        if new_duration <= 0:
            raise ValueError(f'Продолжительность аудиокниги не может быть отрицательной или равной нулю')
        self._duration = new_duration

    def __str__(self):
        str_audio = super().__str__()
        return f"{str_audio}. Продолжительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"


if __name__ == "__main__":
    book_1 = Book('Золотая рыбка', 'А. С. Пушкин')
    print(book_1)  # Книга Золотая рыбка. Автор А. С. Пушкин
    book_2 = PaperBook('Золотая рыбка', 'А. С. Пушкин', 30)
    print(book_2)  # Книга Золотая рыбка. Автор А. С. Пушкин. Страниц 30
    book_3 = AudioBook('Золотая рыбка', 'А. С. Пушкин', 14.42)
    print(book_3)  # Книга Золотая рыбка. Автор А. С. Пушкин. Продолжительность 14.42
