from cars.cars_class import *


def brand_presence(current_brand):
    """ Проверяет наличие конкретного бренда в автосалоне"""
    return current_brand.lower() in [brand.lower() for brand in Auto.all_brands]


def model_presence(current_brand, current_model):
    """ Проверяет наличие конкретной модели в конкретном бренде в автосалоне"""
    if current_brand.lower() in [brand.lower() for brand in Auto.all_brands]:
        all_models_current_brand = [model.lower() for model in Auto.all_brands.get(current_brand)]
        return current_model.lower() in all_models_current_brand
    return False
