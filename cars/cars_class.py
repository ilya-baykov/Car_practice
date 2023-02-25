class Auto:

    def __init__(self, car_brand: str, modul_name: str, year_of_manufacture: int, power: int):
        self.__car_brand = car_brand
        self.__module_name = modul_name
        self.__year_of_manufacture = year_of_manufacture
        self.__power = power

    @property
    def car_brand(self):
        return self.__car_brand

    @property
    def modul_name(self):
        return self.__module_name

    @property
    def year_of_manufacture(self):
        return self.__year_of_manufacture

    @property
    def power(self):
        return self.__power


class BMW(Auto):
    __all_cars = {}

    def __init__(self, car_brand: str, modul_name: str, year_of_manufacture: int, power: int):
        super().__init__(car_brand, modul_name, year_of_manufacture, power)
        BMW.__all_cars.setdefault(f"{car_brand}_{modul_name}", []).extend(
            [car_brand, modul_name, year_of_manufacture, power])

    def __str__(self):
        return f" Информация о машине {self.car_brand} {self.modul_name} - {self}"


if __name__ == '__main__':
    bmw_5 = BMW("BMW", "M5", 1999, 230)
    bmw_x5 = BMW("BMW", "X5", 2001, 320)
    bmw_x6 = BMW("BMW", "x6", 2005, 330)
