from django.urls import path, include
from . import views
from django import views
from .views import create_jam_operasional, read_jam_operasional, update_jam_operasional, delete_jam_operasional

app_name = "jam_operasional"

urlpatterns = [
      path('create', create_jam_operasional, name='create'),
      path('read', read_jam_operasional, name='read'),
      path('update', update_jam_operasional, name='update'),
      path('delete', delete_jam_operasional, name='delete'),
      # path('update/<str:rname>/<str:rbranch>/<str:day>', update_jam_operasional, name='update'),
      # path('/delete/<str:rname>/<str:rbranch>/<str:day>', delete_jam_operasional, name='delete'),

]