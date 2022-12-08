from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', show_pengisian_alamat, name='show_pengisian_alamat'),
    path('pemilihan_restoran/', show_pemilihan_restoran, name='show_pemilihan_restoran'),
    path('pemilihan_makanan/', show_pemilihan_makanan, name='show_pemilihan_makanan'),
    path('daftar_pesanan/', show_daftar_pesanan, name='show_daftar_pesanan'),
    path('konfirmasi_pesanan/', show_konfirmasi_pesanan, name='show_konfirmasi_pesanan'),
    path('ringkasan_pesanan', show_ringkasan_pesanan, name='show_ringkasan_pesanan'),
]