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

    @classmethod
    def check_model_in_current_brand(cls, current_brand: str) -> str:
        """ Проверяет наличие конкретного бренда"""
        different_spelling = [current_brand.lower(), current_brand, current_brand.upper()]
        for spelling in different_spelling:
            if cls.all_brands.get(spelling):
                return spelling
        raise Exception(F"{current_brand} - Такой бренд не найден")

    @classmethod
    def get_all_models_current_brand(cls, current_brand):
        """Возвращает  список моделей конкретного бренды в виде списка """
        spelling_model = cls.check_model_in_current_brand(current_brand)
        if spelling_model:
            return [model for model in cls.all_brands.get(spelling_model)]
        else:
            raise Exception(f"Что то не так {current_brand} , {cls.all_brands}")

    @classmethod
    def info_about_current_model_in_current_brand(cls, current_brand, current_model) -> list:
        """Возвращает экземпляр класса с конкретной модели конкретного бренда"""
        brand = Auto.check_model_in_current_brand(current_brand)
        return [car for car in Auto.info.get(brand) if car.modul_name == current_model]

    @classmethod
    def get_info(cls, current_brand, current_model):
        """ Возвращает  экземпляр класса конкретного автомобиля со всей информацией"""
        info = Auto.info_about_current_model_in_current_brand(current_brand, current_model)
        if info:
            car = info[0]
            return car

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


if __name__ == '__main__':
    test_car_1 = BMW("BMW", "test_car_1", 2017, 460)
    test_car_2 = BMW("BMW", "test_car_2", 2017, 460)
    test_car_3 = BMW("BMW", "test_car_3", 2017, 460)
    print(Auto.get_all_models_current_brand("BMW"))
    print(Auto.info_about_current_model_in_current_brand("bmw", "test_car_1"))
    print(Auto.get_info("bmw", "test_car_1"))
