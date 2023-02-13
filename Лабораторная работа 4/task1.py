class Headphones:  # Базовый класс - наушники
    """
    Документация на базовый класс.
    Класс описывает модель наушников.
    """
    def __init__(self, brand: str, model_name: str, color: str):
        """Инициализация экземпляра класса."""
        self.brand = brand
        self.model_name = model_name
        self.color = color

    def __str__(self) -> str:
        """Метод возвращает строковое представление объекта."""
        return f"Бренд: {self.brand}. Модель: {self.model_name}. Цвет: {self.color}"

    def __repr__(self) -> str:
        """Метод возвращает представление объекта."""
        return f"{self.__class__.__name__}(brand={self.brand!r}, model_name={self.model_name!r}, color={self.color!r})"

    @staticmethod
    def change_the_volume(volume: int) -> int:  # Унаследован в дочерние классы
        """Статический метод увеличивает громкость."""
        return volume + 1

    @staticmethod
    def are_the_headphones_connected() -> str:
        """Статический метод показывает подключены ли наушники к устройству."""
        if not ...:
            return f"Наушники не подключены"
        else:
            return f"Наушники подключены"


class WirelessHeadphones(Headphones):  # Беспроводные наушники
    """
    Документация на дочерний класс.
    Класс описывает модель беспроводных наушников.
    """
    def __init__(self, brand: str, model_name: str, color: str, charging_type: str, battery_life: str):
        """
        Инициализация экземпляра класса.
        Часть параметров унаследованна из базового класса
        """
        super().__init__(brand, model_name, color)
        self.charging_type = charging_type
        self.battery_life = battery_life

    def __str__(self) -> str:
        """
        Метод возвращает строковое представление объекта.
        Метод унаследован из базового класса с изменениями
        """
        base_class = super().__str__()
        return f"{base_class}. Тип зарядки: {self.charging_type}. Время работы: {self.battery_life}"

    def __repr__(self) -> str:
        """Метод возвращает представление объекта."""
        return f"{self.__class__.__name__}(brand={self.brand!r}, model_name={self.model_name!r}, color={self.color!r}" \
               f", charging_type={self.charging_type!r}, battery_life={self.battery_life!r})"

    @staticmethod
    def are_the_headphones_connected() -> str:  # Перегрузили метод
        """
        Статический метод показывает подключены ли наушники к устройству.
        Метод перегрузили из базового класса
        """
        if not ...:
            return f"Проверьте, включен ли Bluetooth"
        else:
            return f"Наушники подключены"


class WiredHeadphones(Headphones):  # Проводные наушники
    """
    Документация на дочерний класс.
    Класс описывает модель проводных наушников.
    """
    def __init__(self, brand: str, model_name: str, color: str, wire_length: str):
        """
        Инициализация экземпляра класса.
        Часть параметров унаследованна из базового класса
        """
        super().__init__(brand, model_name, color)
        self.wire_length = wire_length

    def __str__(self) -> str:
        """
        Метод возвращает строковое представление объекта.
        Метод унаследован из базового класса с изменениями
        """
        base_class = super().__str__()
        return f"{base_class}. Длина зарядки: {self.wire_length}"

    def __repr__(self) -> str:
        """Метод возвращает представление объекта."""
        return f"{self.__class__.__name__}(brand={self.brand!r}, model_name={self.model_name!r}, color={self.color!r}" \
               f", wire_length={self.wire_length!r})"

    @staticmethod
    def headphones_are_connected() -> str:  # Перегрузили метод
        """
        Статический метод показывает подключены ли наушники к устройству.
        Метод перегрузили из базового класса
        """
        if not ...:
            return f"Подключите провод к устройству"
        else:
            return f"Наушники подключены"


if __name__ == "__main__":
    headphones_1 = Headphones('Apple', 'AirPodsMax', 'Black')
    headphones_2 = WirelessHeadphones('Apple', 'AirPods', 'White', 'USB Type-C', '24 ч')
    headphones_3 = WiredHeadphones('Apple', 'EarPods', 'Grey', '1,2 м')
    print(headphones_1)  # Бренд: Apple. Модель: AirPodsMax. Цвет: Black
    print(headphones_2)  # Бренд: Apple. Модель: AirPods. Цвет: White. Тип зарядки: USB Type-C. Время работы: 24 ч
    print(headphones_3)  # Бренд: Apple. Модель: EarPods. Цвет: Grey. Длина зарядки: 1,2 м
    pass
