from django.shortcuts import render
from django.contrib.auth.models import User as DjangoUser
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.template import RequestContext
from django.contrib.auth import authenticate

from django.urls import reverse
from sirest_b09.models import *
from .forms import AdminForm, PelangganForm, RestoranForm, KurirForm
from json import dumps

# Create your views here.

def homepage(request):
      return render(request, "home.html")

def login_pengguna(request):
      if request.method == "POST":
            # TODO: Validasi autentikasi
            return redirect('index')
      return render(request, 'login.html')

def logout_pengguna(request):
      # TODO: Logout pengguna
      return redirect('index')

def regis_admin(request):
      registered = False
      if request.method == 'POST':
            admin_form = AdminForm(data=request.POST)
            if admin_form.is_valid():
                  admin = admin_form.save()
                  # admin.set_password(admin.password)
                  admin.save()
                  registered = True
                  return redirect('home')
            else:
                  print(admin_form.errors)
      else:
            admin_form = AdminForm()
      return render(request, 'regis_admin.html', 
            {'admin_form':admin_form,
            'registered': registered})

def regis_pelanggan(request):
      registered = False
      if request.method == 'POST':
            pelanggan_form = PelangganForm(data=request.POST)
            if pelanggan_form.is_valid():
                  pelanggan = pelanggan_form.save()
                  pelanggan.save()
                  registered = True
                  return redirect('home')
            else:
                  print(pelanggan_form.errors)
      else:
            pelanggan_form = PelangganForm()
      return render(request, 'regis_pelanggan.html',
            {'pelanggan_form':pelanggan_form,
            'registered': registered})

def regis_restoran(request):
      registered = False
      if request.method == 'POST':
            restoran_form = RestoranForm(data=request.POST)
            if restoran_form.is_valid():
                  restoran = restoran_form.save()
                  restoran.save()
                  registered = True
                  return redirect('home')
            else:
                  print(restoran_form.errors)
      else:
            restoran_form = RestoranForm()
      return render(request, 'regis_restoran.html',
            {'restoran_form':restoran_form,
            'registered': registered})

def regis_kurir(request):
      registered = False
      if request.method == 'POST':
            kurir_form = KurirForm(data=request.POST)
            if kurir_form.is_valid():
                  kurir = kurir_form.save()
                  kurir.save()
                  registered = True
                  return redirect('home')
            else:
                  print(kurir_form.errors)
      else:
            kurir_form = KurirForm()
      return render(request, 'regis_kurir.html',
            {'kurir_form':kurir_form,
            'registered': registered})


def show_kategori_makanan(request):
      context = {
            'kategori' : KategoriMakanan.objects.all().values(),
      }
      return render(request, 'kategori_makanan.html', context)

def delete_kategori_makanan(request, kategori_id):
      kategori_makanan = KategoriMakanan.objects.get(id = kategori_id)
      kategori_makanan.delete()
      return redirect('show_kategori_makanan')
