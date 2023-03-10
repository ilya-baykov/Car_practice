from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from cars.handler_cls import *
from django.template.loader import render_to_string


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
    all_models_current_brand = Handler.get_all_models_current_brand(current_brand)
    if all_models_current_brand:
        total_result_display = "<ul>"
        for model in all_models_current_brand:
            url_link = reverse("current_model_brand_URL", args=(current_brand, model,))
            total_result_display += f"<li><a href = '{url_link}'>{model}</a></li>"
        total_result_display += "</ul>"
        return HttpResponse(F"{total_result_display}")
    else:
        return HttpResponseNotFound(f"Извините , но мы не нашли такой бренд - {current_brand}")



def current_model_func(requst, current_brand, current_model):
    info = Handler.get_info(current_brand, current_model)
    data = {
        "brand": info.car_brand,
        "model": info.modul_name,
        "year_of_manufacture": info.year_of_manufacture,
        "power": info.power
    }
    return render(requst, 'cars/current_model_info.html', context=data)


