from django.urls import path
from tarif_pengiriman_per_km.views import *

app_name="tarif_pengiriman_per_km"

urlpatterns = [
    path('create/', create, name="create"),
    path('read/', read, name="read"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]
