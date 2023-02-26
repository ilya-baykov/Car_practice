from cars.cars_class import *


class Handler(Auto):
    @classmethod
    def check_model_in_current_brand(cls, current_brand: str) -> str | bool:
        """ Проверяет наличие конкретного бренда
            Если такого бренда нет - возвращает False
            Иначе - возвращает строковое представление бренда
        """
        different_spelling = [current_brand.lower(), current_brand, current_brand.upper()]
        for spelling in different_spelling:
            if cls.all_brands.get(spelling):
                return spelling
        return False

    @classmethod
    def get_all_models_current_brand(cls, current_brand) -> list | bool:
        """Возвращает  список моделей конкретного бренды в виде списка
            Если такого бренда не существует - возвращает False
        """
        spelling_model = cls.check_model_in_current_brand(current_brand)
        if spelling_model:
            return [model for model in cls.all_brands.get(spelling_model)]
        return False

    @classmethod
    def info_about_current_model_in_current_brand(cls, current_brand, current_model) -> list | bool:
        """Возвращает экземпляр класса с конкретной модели конкретного бренда"""
        brand = Handler.check_model_in_current_brand(current_brand)
        if brand:
            return [car for car in Auto.info.get(brand) if car.modul_name == current_model]
        return False

    @classmethod
    def get_info(cls, current_brand, current_model):
        """ Возвращает  экземпляр класса конкретного автомобиля со всей информацией"""
        info = Handler.info_about_current_model_in_current_brand(current_brand, current_model)
        if info:
            car = info[0]
            return car
        return False
