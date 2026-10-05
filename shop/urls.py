from django.urls import path

from . import views

# app_name позволяет обращаться к маршрутам как shop:index, shop:catalog, shop:about
app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
]
