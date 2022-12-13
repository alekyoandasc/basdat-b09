from django.urls import path
from restoran.views import *

app_name="restoran"

urlpatterns = [
    path('', read_daftar_restoran, name="read_daftar_restoran"),
    path('detail/', read_detail_restoran, name="read_detail_restoran"),
    path('menu/', read_menu_restoran, name="read_menu_restoran"),
    path('<slug:rname>/<slug:rbranch>/tambah-makanan/', create_makanan, name="create_makanan"),
    path('update-makanan/', update_makanan, name="update_makanan"),
    path('delete-makanan/', delete_makanan, name="delete_makanan"),
]
