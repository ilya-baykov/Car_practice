def all_cars_info(cls):
    return cls.all_cars


class Auto:
    all_brands = {}

    def __init__(self, car_brand: str, modul_name: str, year_of_manufacture: int, power: int):
        self.__car_brand = car_brand
        self.__module_name = modul_name
        self.__year_of_manufacture = year_of_manufacture
        self.__power = power
        Auto.all_brands.setdefault(car_brand, []).append(modul_name)

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

    def __str__(self):
        return f"Информация о машине {self.car_brand} {self.modul_name.replace('_', ' ')} - {[self.car_brand, self.modul_name, f'{self.year_of_manufacture}г', f'{self.power} л.c']}"


class BMW(Auto):
    all_cars = {}

    def __init__(self, car_brand: str, modul_name: str, year_of_manufacture: int, power: int):
        super().__init__(car_brand, modul_name, year_of_manufacture, power)
        BMW.all_cars.setdefault(f"{car_brand}_{modul_name}", []).extend(
            [car_brand, modul_name, year_of_manufacture, power])


class Toyota(Auto):
    all_cars = {}

    def __init__(self, car_brand: str, modul_name: str, year_of_manufacture: int, power: int):
        super().__init__(car_brand, modul_name, year_of_manufacture, power)
        Toyota.all_cars.setdefault(f"{car_brand}_{modul_name}", []).extend(
            [car_brand, modul_name, year_of_manufacture, power])


class Mitsubishi(Auto):
    all_cars = {}

    def __init__(self, car_brand: str, modul_name: str, year_of_manufacture: int, power: int):
        super().__init__(car_brand, modul_name, year_of_manufacture, power)
        Mitsubishi.all_cars.setdefault(f"{car_brand}_{modul_name}", []).extend(
            [car_brand, modul_name, year_of_manufacture, power])
