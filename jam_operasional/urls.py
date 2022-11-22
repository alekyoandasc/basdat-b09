from django.urls import path, include
from . import views
from django import views
from .views import create_jam_operasional, read_jam_operasional, update_jam_operasional


urlpatterns = [
      path('create', create_jam_operasional, name='create'),
      path('read', read_jam_operasional, name='read'),
      path('update', update_jam_operasional, name='update'),

]