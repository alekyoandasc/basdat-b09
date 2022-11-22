from django.urls import path

from . import views
from .views import *

urlpatterns = [
      path('', homepage, name='homepage'),
      path('regis_admin/', regis_admin, name='regis_admin'),
      path('regis_pelanggan/', regis_pelanggan, name='regis_pelanggan'),
      path('regis_restoran/', regis_restoran, name='regis_restoran'),
      path('regis_kurir/', regis_kurir, name='regis_kurir'),
      path('login/', login_pengguna, name="login_pengguna"),
      path('logout/', logout_pengguna, name="logout_pengguna"),
      path('kategorimakanan/', show_kategori_makanan, name='show_kategori_makanan'),
      path('delete_kategori_makanan/<kategori_id>', delete_kategori_makanan, name='delete_kategori_makanan')
]