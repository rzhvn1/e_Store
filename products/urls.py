from django.contrib import admin
from django.urls import path
from .views import products_page, order_page, register_page, all_users_page, about_us_page
#здесь пути для
urlpatterns = [
    path('', products_page, name = 'products'),
    path('order/', order_page),
    path('register/', register_page),
    path('all_users/', all_users_page),
    path('about_us/', about_us_page),
]
