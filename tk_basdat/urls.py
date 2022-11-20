from django.urls import path
from django import views

from . import views
from .views import index, register

urlpatterns = [
      path('', index, name='index'),
      path('', index, name='tk_basdat'),
      path('register', register, name='register'),

]