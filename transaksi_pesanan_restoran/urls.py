from django.urls import path, include
from . import views
from django import views
from .views import read_tprestoran, detail_tprestoran


urlpatterns = [
      path('read', read_tprestoran, name='read'),
      path('detail', detail_tprestoran, name='detail'),

]