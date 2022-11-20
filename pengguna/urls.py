from django.urls import path

from . import views
from .views import regis_admin, regis_pelanggan, regis_restoran, regis_kurir

urlpatterns = [
      path('regis_admin/', regis_admin, name='regis_admin'),
      path('regis_pelanggan/', regis_pelanggan, name='regis_pelanggan'),
      path('regis_restoran/', regis_restoran, name='regis_restoran'),
      path('regis_kurir/', regis_kurir, name='regis_kurir'),
]