class TransportVehicle:
    """Базовый класс транспортного средства."""
    def __init__(self, id: int, brand: str, model: str, year: int, color: str):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        pass

    def __repr__(self) -> str:
        """Возвращает строку для воссоздания объекта."""
        pass


class Car(TransportVehicle):
    """Дочерний класс - Автомобиль."""
    def __init__(self, id: int, brand: str, model: str, year: int, color: str, fuel_type: str, fuel_tank_capacity: float):
        super().__init__(id, brand, model, year, color)
        self.fuel_type = fuel_type
        self.fuel_tank_capacity = fuel_tank_capacity

    def drive(self, distance: float) -> str:
        """Метод для симуляции поездки на заданное расстояние."""
        pass
