class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Автор книги."""
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        """Количество страниц в бумажной книге."""
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """Установка количества страниц с проверкой."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()} Количество страниц: {self._pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        """Продолжительность аудиокниги в часах."""
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """Установка продолжительности с проверкой."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()} Продолжительность: {self._duration} часов"
