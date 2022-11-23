from django.urls import path
from restoran.views import *

app_name="restoran"

urlpatterns = [
    path('', read_daftar_restoran, name="read_daftar_restoran"),
    path('<slug:rname>/<slug:rbranch>/detail/', read_detail_restoran, name="read_detail_restoran"),
    path('<slug:rname>/<slug:rbranch>/menu/', read_menu_restoran, name="read_menu_restoran"),
    path('<slug:rname>/<slug:rbranch>/tambah-makanan/', create_makanan, name="create_makanan"),
    path('<slug:rname>/<slug:rbranch>/<slug:fname>/update-makanan/', update_makanan, name="update_makanan"),
    path('<slug:rname>/<slug:rbranch>/<slug:fname>/delete-makanan/', delete_makanan, name="delete_makanan"),
]
