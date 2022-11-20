from django.contrib import admin
from .models import Admin, Pelanggan, Restoran, Kurir

# Register your models here.
admin.site.register(Admin)
admin.site.register(Pelanggan)
admin.site.register(Restoran)
admin.site.register(Kurir)