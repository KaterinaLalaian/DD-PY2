import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Thermometer:
    def __init__(self, daytime_temperature: int, temperature_at_night: int):
        if not isinstance(daytime_temperature, int):
            raise TypeError("Температура утром должна быть типа int")
        self.daytime_temperature = daytime_temperature  # Температура днем
        if not isinstance(temperature_at_night, int):
            raise TypeError("Температура ночью должна быть типа int")
        self.temperature_at_night = temperature_at_night  # Температура ночью

    def measure_the_temperature(self) -> int:  # Измерить температуру
        ...

    def bring_down_the_temperature(self, delta_t: int) -> None:  # Сбить температуру
        if not isinstance(delta_t, int):
            raise TypeError("Изменение теипературы должно быть типа int")
        ...


class Table:
    def __init__(self, material: str, height: int):
        if not isinstance(material, str):
            raise TypeError("Материал стола должен быть типа str")
        self.material = material  # Материал стола
        if not isinstance(height, int):
            raise TypeError("Высота стола должна быть типа int")
        if height < 0:
            raise ValueError("Высота стола не может быть отрицательной")
        self.height = height  # Высота стола

    def put_the_object_on_the_table(self, item: str) -> None:  # Положить педмет на стол
        if not isinstance(item, str):
            raise TypeError("Предмет должен быть типа str")
        ...

    def what_is_on_the_table(self) -> dict:  # Что лежит на столе
        ...


class Flower:
    def __init__(self, name: str, bud_color: str):
        if not isinstance(name, str):
            raise TypeError("Название цветка должно быть типа str")
        self.name = name  # Название цветка
        if not isinstance(bud_color, str):
            raise TypeError("Цвет бутона должен быть типа str")
        self.bud_color = bud_color  # Цвет бутона

    def water_the_flower(self) -> None:  # Полить цветок
        ...

    def the_flower_is_alive(self) -> bool:  # Узнать жив ли цветок
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
