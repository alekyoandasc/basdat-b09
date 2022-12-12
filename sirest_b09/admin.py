from django.contrib import admin
from .models import *
from kategorimakanan.models import *

# Register your models here.

admin.site.register(Restoran)
admin.site.register(KategoriRestoran)
admin.site.register(KategoriMakanan)
admin.site.register(Makanan)