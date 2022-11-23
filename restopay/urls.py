from django.urls import path, include
from . import views
from django import views
from .views import add_saldo, tarik_saldo, lihat_saldo


urlpatterns = [
      path('lihat-saldo', lihat_saldo, name='lihat_saldo'),
      path('add-saldo', add_saldo, name='add_saldo'),
      path('tarik-saldo', tarik_saldo, name='tarik_saldo'),

]