from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', show_pengisian_alamat, name='show_pengisian_alamat'),
    path('pemilihan_restoran/', show_pemilihan_restoran, name='show_pemilihan_restoran'),
    path('pemilihan_makanan/<rname>/<rbranch>', show_pemilihan_makanan, name='show_pemilihan_makanan'),
    path('daftar_pesanan/', show_daftar_pesanan, name='show_daftar_pesanan'),
    path('konfirmasi_pesanan/', show_konfirmasi_pesanan, name='show_konfirmasi_pesanan'),
    path('ringkasan_pesanan', show_ringkasan_pesanan, name='show_ringkasan_pesanan'),
    path('post_pengisian_alamat', post_pengisian_alamat, name='post_pengisian_alamat'),
    path('post_pemilihan_makanan', post_pemilihan_makanan, name='post_pemilihan_makanan'),
    path('cek_pemilihan_makanan/', show_cek_pesanan_berlangsung, name='show_cek_pesanan_berlangsung'),
    path('pesanan_berlangsung/<datetime>', show_pesanan, name='show_pesanan'),
]