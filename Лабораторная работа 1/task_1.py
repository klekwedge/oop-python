from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Абстрактный класс, представляющий животное.

    Атрибуты:
        name (str): Имя животного.
        age (int): Возраст животного.
        species (str): Вид животного.

    Методы:
        make_sound() -> str:
            Воспроизвести звук, характерный для данного вида животного.

        move(distance: float) -> None:
            Переместить животное на заданное расстояние.

        feed(food_type: str, amount: float) -> bool:
            Покормить животное указанной едой в заданном количестве.
    """

    @abstractmethod
    def make_sound(self) -> str:
        pass

    @abstractmethod
    def move(self, distance: float) -> None:
        pass

    @abstractmethod
    def feed(self, food_type: str, amount: float) -> bool:
        pass


class Smartphone(ABC):
    """
    Абстрактный класс, представляющий смартфон.

    Атрибуты:
        brand (str): Бренд смартфона.
        model (str): Модель смартфона.
        storage_capacity (int): Объем встроенной памяти в гигабайтах.

    Методы:
        make_call(phone_number: str) -> None:
            Позвонить по указанному номеру телефона.

        send_message(recipient: str, message: str) -> None:
            Отправить сообщение указанному получателю.

        install_app(app_name: str) -> bool:
            Установить приложение на смартфон.
    """

    @abstractmethod
    def make_call(self, phone_number: str) -> None:
        pass

    @abstractmethod
    def send_message(self, recipient: str, message: str) -> None:
        pass

    @abstractmethod
    def install_app(self, app_name: str) -> bool:
        pass


class Vehicle(ABC):
    """
    Абстрактный класс, представляющий транспортное средство.

    Атрибуты:
        brand (str): Бренд транспортного средства.
        model (str): Модель транспортного средства.
        fuel_type (str): Тип используемого топлива.

    Методы:
        start_engine() -> None:
            Запустить двигатель.

        drive(speed: int) -> None:
            Начать движение с указанной скоростью.

        refuel(amount: float, fuel_type: str) -> None:
            Заправить транспортное средство указанным количеством топлива.
    """

    @abstractmethod
    def start_engine(self) -> None:
        pass

    @abstractmethod
    def drive(self, speed: int) -> None:
        pass

    @abstractmethod
    def refuel(self, amount: float, fuel_type: str) -> None:
        """
            Примеры:
            >>> car = Vehicle('Toyota', 'Camry', 'Benzin')
            >>> car.refuel(20, 'Benzin')
        """
        pass


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
