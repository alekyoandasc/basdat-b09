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
      path('detail_customer/<email>', detail_customer, name="detail_customer"),
      path('detail_resto/<email>', detail_resto, name="detail_resto"),
      path('detail_courier/<email>', detail_courier, name="detail_courier"),
      path('verifikasi/<email>', verifikasi, name="verifikasi")
]