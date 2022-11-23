from django.urls import path

from . import views
from .views import *

app_name = 'riwayat_dan_promo'

urlpatterns = [
      path('', riwayat_transaksi, name='riwayat_transaksi'),
      path('detail/<id>', detail_transaksi, name='detail_transaksi'),
      path('nilai/<id>', nilai_transaksi, name='nilai_transaksi'),
      path('buat_promo/', buat_promo, name='buat_promo'),
      path('buat_promo/promo_min_transaksi/', buat_promo_min_transaksi, name='buat_promo_min_transaksi'),
      path('buat_promo/promo_hari_spesial/', buat_promo_hari_spesial, name='buat_promo_hari_spesial'),
      path('daftar_promosi/', daftar_promosi, name='daftar_promosi'),
      path('promo_min_transaksi/<id>', detail_promo_min_transaksi, name='detail_promo_min_transaksi'),
      path('promo_hari_spesial/<id>', detail_promo_hari_spesial, name='detail_promo_hari_spesial'),
      path('ubah_promo_min_transaksi/<id>', ubah_promo_min_transaksi, name='ubah_promo_min_transaksi'),
      path('ubah_promo_hari_spesial/<id>', ubah_promo_hari_spesial, name='ubah_promo_hari_spesial'),
      path('daftar_promo_restoran/', daftar_promo_restoran, name='daftar_promo_restoran'),
      path('tambah_promo_restoran/', tambah_promo_restoran, name='tambah_promo_restoran'),
      path('promo_restoran/<id>', detail_promo_restoran, name='detail_promo_restoran'),
      path('ubah_promo_restoran/<id>', ubah_promo_restoran, name="ubah_promo_restoran")

      
]