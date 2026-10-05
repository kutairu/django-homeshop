"""Главный файл маршрутов проекта homeshop."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # все страницы магазина описаны в приложении shop
    path('', include('shop.urls')),
]
