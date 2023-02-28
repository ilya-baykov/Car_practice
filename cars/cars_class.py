def all_cars_info(cls):
    return cls.all_cars


class Auto:
    all_brands = {}
    info = {}

    def __init__(self, car_brand: str, modul_name: str, year_of_manufacture: int, power: int):
        self.__car_brand = car_brand
        self.__module_name = modul_name
        self.__year_of_manufacture = year_of_manufacture
        self.__power = power
        Auto.all_brands.setdefault(car_brand, []).append(modul_name)
        Auto.info.setdefault(car_brand, []).append(self)

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



bmw_m3_2017 = BMW("BMW", "M3", 2017, 460)
bmw_x5_2021 = BMW("BMW", "X5", 2021, 387)
bmw_x1_2022 = BMW("BMW", "X1", 2022, 204)
bmw_m5_2020 = BMW("BMW", "M5", 2020, 625)

toyota_corolla_2018 = Toyota("Toyota", "Corolla", 2018, 122)
toyota_rav4_2018 = Toyota("Toyota", "RAV4", 2018, 173)
toyota_chr_2019 = Toyota("Toyota", "C-HR", 2019, 116)
toyota_Land_Cruiser_Prado_2020 = Toyota("Toyota", "Land_Cruiser_Prado", 2020, 249)

mitsubishi_outlander_2021 = Mitsubishi("Mitsubishi", "Outlander", 2021, 184)
mitsubishi_eclipse_cross_2021 = Mitsubishi("Mitsubishi", "Eclipse Cross", 2021, 150)
mitsubishi_asx_2020 = Mitsubishi("Mitsubishi", "Asx", 2020, 140)
mitsubishi_pajero_sport_2021 = Mitsubishi("Mitsubishi", "Pajero_Sport", 2019, 181)
