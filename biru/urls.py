from unicodedata import name
from django.urls import path, register_converter
from .converters import DateConverter
from . import views

register_converter(DateConverter, 'date')

urlpatterns = [
    path('create-kategori-restoran', views.create_kategori_restoran, name='create_kategori_resto'),
    path('read-kategori-restoran', views.read_kategori_restoran, name='read_kategori_restoran'),
    path('kategori-resto/delete/<int:id>', views.delete_kategori_restoran, name='delete_kategori_restoran'),
    path('create-bahan-makanan', views.create_bahan_makanan, name='create_bahan_makanan'),
    path('read-bahan-makanan', views.read_bahan_makanan, name='read_bahan_makanan'),
    path('bahan-makanan/delete/<str:id>', views.delete_bahan_makanan, name='delete_bahan_makanan'),
    path('read-transaksi-kurir', views.read_transaksi_kurir, name='read_transaksi_kurir'),
    path('read-detail-transaksi-kurir/<str:email>/<date:datetime>', views.read_detail_transaksi_kurir, name='read_detail_transaksi_kurir'),
    path('update-transaksi-kurir/<str:email>/<date:datetime>' , views.update_transaksi_kurir, name='update_transaksi_kurir')
]