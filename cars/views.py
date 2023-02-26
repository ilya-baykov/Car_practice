from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from cars.ALL_CARS import *


# Create your views here.

def catalog(requst):
    """Отображает на экране меню брендов"""
    total_result_display = "<ul>"
    for brand in Auto.all_brands:
        url_link = reverse("current_brand_URL", args=(brand,))
        total_result_display += f"<li><a href = '{url_link}'>{brand}</a></li>"
    total_result_display += "</ul>"
    return HttpResponse(total_result_display)


def current_brand_func(requst, current_brand: str):
    """Отображает на экране все модели конкретного бренда"""
    all_models_current_brand = Auto.get_all_models_current_brand(current_brand)
    total_result_display = "<ul>"
    for model in all_models_current_brand:
        url_link = reverse("current_model_brand_URL", args=(current_brand, model,))
        total_result_display += f"<li><a href = '{url_link}'>{model}</a></li>"
    total_result_display += "</ul>"
    return HttpResponse(F"{total_result_display}")


def current_model_func(requst, current_brand, current_model):
    info = Auto.get_info(current_brand, current_model)
    total_result_display = f"<p> Модель - {info.car_brand} {info.modul_name}<p>"
    total_result_display += f"<p> Год выпуска - {info.year_of_manufacture}<p>"
    total_result_display += f"<p> Мощность - {info.power} л.с<p>"
    return HttpResponse(f"{total_result_display}")
