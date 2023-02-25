from django.urls import path, include
from cars import views as car_dispaly

urlpatterns = [
    path('bmw/<str:auto_model>', car_dispaly.bmw)
]
