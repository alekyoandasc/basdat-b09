from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('create-kategori-restoran', views.create_kategori_restoran, name='create_kategori_resto'),
    path('read-kategori-restoran', views.read_kategori_restoran, name='read_kategori_restoran'),
    path('kategori-resto/delete/<str:nama_kategori>', views.delete_kategori_restoran, name='delete_kategori_restoran'),
    path('create-bahan-makanan', views.create_bahan_makanan, name='reate_bahan_makanan'),
    path('read-bahan-makanan', views.read_bahan_makanan, name='read_kategori_restoran'),
    path('bahan-makanan/delete/<str:nama_bahan>', views.delete_bahan_makanan, name='delete_bahan_makanan'),
    path('read-transaksi-kurir', views.read_transaksi_kurir, name='read_transaksi_kurir'),
    path('read-detail-transaksi-kurir', views.read_detail_transaksi_kurir, name='read_detail_transaksi_kurir'),
]