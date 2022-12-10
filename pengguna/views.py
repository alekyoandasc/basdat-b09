from django.shortcuts import render
from django.contrib.auth.models import User as DjangoUser
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib import messages
from django.urls import reverse
from sirest_b09.models import *
from .forms import AdminForm, PelangganForm, RestoranForm, KurirForm
from json import dumps

from django.db import connection, transaction

# Create your views here.

def homepage(request):

      return render(request, "home.html")

def login_pengguna(request):
      if request.method == "POST":
            # TODO: Validasi autentikasi
            with connection.cursor() as cursor:
                  email = request.POST.get('email')
                  password = request.POST.get('password')
                  cursor.execute(f"""
                        SELECT * 
                        FROM SIREST.USER_ACC
                        WHERE email = '{email}'
                        AND password = '{password}'
                  """)
                  fields = [field_name[0] for field_name in cursor.description]
                  row = cursor.fetchone()
                  if row is not None:
                        user = dict(zip(fields, row))
                        response = HttpResponseRedirect(reverse("homepage"))
                        response.set_cookie('user_name', user['fname']+ " " + user['lname'])

                        cursor.execute(f"""
                              SELECT * 
                              FROM SIREST.ADMIN
                              WHERE email = '{email}'
                        """)
                        row = cursor.fetchone()
                        if row is not None:
                              response.set_cookie('user_type', 'admin')
                              return response

                        cursor.execute(f"""
                              SELECT * 
                              FROM SIREST.CUSTOMER
                              WHERE email = '{email}'
                        """)
                        row = cursor.fetchone()
                        if row is not None:
                              response.set_cookie('user_type', 'customer')
                              return response

                        cursor.execute(f"""
                              SELECT * 
                              FROM SIREST.RESTAURANT
                              WHERE email = '{email}'
                        """)
                        row = cursor.fetchone()
                        if row is not None:
                              response.set_cookie('user_type', 'restaurant')
                              return response
                        
                        cursor.execute(f"""
                              SELECT * 
                              FROM SIREST.COURIER
                              WHERE email = '{email}'
                        """)
                        row = cursor.fetchone()
                        if row is not None:
                              response.set_cookie('user_type', 'courier')
                        return response
                  else:
                        messages.info(request, 'Email atau password tidak valid')
                        
      return render(request, 'login.html')

def logout_pengguna(request):
      # TODO: Logout pengguna
      response = HttpResponseRedirect(reverse('login_pengguna'))
      response.delete_cookie('user_name')
      response.delete_cookie('user_type')
      return response

def regis_admin(request):
      registered = False
      if request.method == 'POST':
            admin_form = AdminForm(data=request.POST)
            if admin_form.is_valid():
                  admin = admin_form.save()
                  # admin.set_password(admin.password)
                  admin.save()
                  registered = True
                  return redirect('homepage')
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
                  return redirect('homepage')
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
                  return redirect('homepage')
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
                  return redirect('homepage')
            else:
                  print(kurir_form.errors)
      else:
            kurir_form = KurirForm()
      return render(request, 'regis_kurir.html',
            {'kurir_form':kurir_form,
            'registered': registered})

