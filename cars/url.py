from django.urls import path, include
from cars import views as car_dispaly

urlpatterns = [
    path('catalog', car_dispaly.catalog),
    path('catalog/<str:current_brand>', car_dispaly.current_brand_func, name="current_brand_URL"),
    path('catalog/<str:current_brand>/<str:current_model>', car_dispaly.current_model_func,
         name="current_model_brand_URL"),

]
