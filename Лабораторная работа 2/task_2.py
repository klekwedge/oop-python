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


class Book:
    def __init__(self, id_, name, pages):
        """
        Инициализирует атрибуты объекта Book.

        Args:
            id_ (int): Идентификатор книги.
            name (str): Название книги.
            pages (int): Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает строку формата "Книга 'название_книги'".

        Returns:
            str: Строка с описанием книги.
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает строку, по которой можно инициализировать экземпляр класса.

        Returns:
            str: Строка инициализации объекта.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"



class Library:
    def __init__(self, books=None):
        """
        Инициализирует объект Library.

        Args:
            books (list, optional): Список книг. По умолчанию None.
        """
        self.books = books or []

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.

        Returns:
            int: Идентификатор для новой книги.
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке по идентификатору.

        Args:
            book_id (int): Идентификатор книги.

        Returns:
            int: Индекс книги в списке.

        Raises:
            ValueError: Если книги с запрашиваемым id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError(f"Книги с id={book_id} не существует")



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
