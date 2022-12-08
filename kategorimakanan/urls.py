from django.urls import path

from . import views
from .views import *



urlpatterns = [
    path('', show_kategori_makanan, name='show_kategori_makanan'),
    path('create_kategori_makanan', show_create_kategori_makanan_page, name='show_create_kategori_makanan_page'),
    path('add_kategori_makanan', add_kategori_makanan, name='add_kategori_makanan'),
    path('delete_kategori_makanan/<id>', delete_kategori_makanan, name='delete_kategori_makanan'),
]