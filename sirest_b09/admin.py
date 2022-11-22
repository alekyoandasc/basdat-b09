from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Admin)
admin.site.register(Pelanggan)
admin.site.register(Restoran)
admin.site.register(Kurir)
admin.site.register(KategoriRestoran)
admin.site.register(KategoriMakanan)
admin.site.register(Makanan)