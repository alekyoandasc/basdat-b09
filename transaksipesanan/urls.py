from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', show_pengisian_alamat, name='show_pengisian_alamat'),
    path('pemilihan_restoran/', show_pemilihan_restoran, name='show_pemilihan_restoran'),
    path('pemilihan_makanan/', show_pemilihan_makanan, name='show_pemilihan_makanan'),
]