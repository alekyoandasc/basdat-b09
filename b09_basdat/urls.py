"""b09_basdat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tk_basdat.urls')),
    path('pengguna/', include('pengguna.urls')),
    path('kategorimakanan/', include('kategorimakanan.urls')),
    path('transaksipesanan/', include('transaksipesanan.urls')),
    path('restopay/', include('restopay.urls')),
    path('jam-operasional/', include('jam_operasional.urls')),
    path('transaksi-pesanan-restoran/', include('transaksi_pesanan_restoran.urls')),
    path('tarif-pengiriman-per-km/', include('tarif_pengiriman_per_km.urls')),
    path('restoran/', include("restoran.urls")),
]
