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
                        response.set_cookie('user_email', user['email'])

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
                              response.set_cookie('user_type', 'resto')
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
      if request.method == 'POST':
            admin_form = AdminForm(data=request.POST)
            if admin_form.is_valid():
                  email = request.POST.get('email')
                  password = request.POST.get('password')
                  fname = request.POST.get('fname')
                  lname = request.POST.get('lname')
                  no_hp = request.POST.get('no_hp')
                  with transaction.atomic():
                        with connection.cursor() as cursor:
                              try:
                                    cursor.execute(f"""
                                          INSERT INTO SIREST.USER_ACC
                                          VALUES ('{email}', '{password}', '{no_hp}', '{fname}', '{lname}')
                                    """)
                                    cursor.execute(f"""
                                          INSERT INTO SIREST.ADMIN
                                          VALUES ('{email}')
                                    """)
                                    response = HttpResponseRedirect(reverse("homepage"))
                                    response.set_cookie('user_name', fname + " " + lname)
                                    response.set_cookie('user_email', email)
                                    response.set_cookie('user_type', 'admin')
                                    return response
                              except Exception as e:
                                    messages.info(request, e)
                  
            else:
                  print(admin_form.errors)
      else:
            admin_form = AdminForm()
      return render(request, 'regis_admin.html', 
            {'admin_form':admin_form})

def regis_pelanggan(request):

      if request.method == 'POST':
            pelanggan_form = PelangganForm(data=request.POST)
            if pelanggan_form.is_valid():
                  email = request.POST.get('email')
                  password = request.POST.get('password')
                  fname = request.POST.get('fname')
                  lname = request.POST.get('lname')
                  no_hp = request.POST.get('no_hp')
                  nik = request.POST.get('nik')
                  bank_name = request.POST.get('bank_name')
                  no_rek = request.POST.get('no_rek')
                  bdate = request.POST.get('bdate')
                  gender = request.POST.get('gender')

                  with transaction.atomic():
                        with connection.cursor() as cursor:
                              try:
                                    cursor.execute(f"""
                                          INSERT INTO SIREST.USER_ACC
                                          VALUES ('{email}', '{password}', '{no_hp}', '{fname}', '{lname}')
                                    """)
                                    cursor.execute(f"""
                                          INSERT INTO SIREST.TRANSACTION_ACTOR
                                          VALUES ('{email}', '{nik}', '{bank_name}', '{no_rek}', 0, NULL)
                                    """)
                                    cursor.execute(f"""
                                          INSERT INTO SIREST.CUSTOMER
                                          VALUES ('{email}', '{bdate}', '{gender}')
                                    """)
                                    response = HttpResponseRedirect(reverse("homepage"))
                                    response.set_cookie('user_name', fname + " " + lname)
                                    response.set_cookie('user_email', email)
                                    response.set_cookie('user_type', 'customer')
                                    return response
                              except Exception as e:
                                    messages.info(request, e)
                  
            else:
                  print(pelanggan_form.errors)
      else:
            pelanggan_form = PelangganForm()
      return render(request, 'regis_pelanggan.html',
            {'pelanggan_form':pelanggan_form})

def regis_restoran(request):
      with connection.cursor() as cursor:
            cursor.execute("""
                  SELECT DISTINCT province
                  FROM SIREST.DELIVERY_FEE_PER_KM
            """)
            rows = cursor.fetchall()
            PROVINCES = [row[0] for row in rows]
            

            cursor.execute("""
                  SELECT *
                  FROM SIREST.RESTAURANT_CATEGORY
            """)
            rows = cursor.fetchall()

            CATEGORIES = [{'id':row[0], 'name':row[1]} for row in rows]
      if request.method == 'POST':
            restoran_form = RestoranForm(data=request.POST)
            if restoran_form.is_valid():
                  email = request.POST.get('email')
                  password = request.POST.get('password')
                  fname = request.POST.get('fname')
                  lname = request.POST.get('lname')
                  no_hp = request.POST.get('no_hp')
                  nik = request.POST.get('nik')
                  bank_name = request.POST.get('bank_name')
                  no_rek = request.POST.get('no_rek')
                  rest_name = request.POST.get('rest_name')
                  branch = request.POST.get('branch')
                  no_telp = request.POST.get('no_telp')
                  street = request.POST.get('street')
                  district = request.POST.get('district')
                  city = request.POST.get('city')
                  province = request.POST.get('province')
                  category = request.POST.get('category')
                  with transaction.atomic():
                        with connection.cursor() as cursor:
                              try:
                                    cursor.execute(f"""
                                          INSERT INTO SIREST.USER_ACC
                                          VALUES ('{email}', '{password}', '{no_hp}', '{fname}', '{lname}')
                                    """)
                                    cursor.execute(f"""
                                          INSERT INTO SIREST.TRANSACTION_ACTOR
                                          VALUES ('{email}', '{nik}', '{bank_name}', '{no_rek}', 0, NULL)
                                    """)
                                    cursor.execute(f"""
                                          INSERT INTO SIREST.RESTAURANT
                                          VALUES ('{rest_name}', '{branch}', '{email}', '{no_telp}', '{street}', '{district}', '{city}', '{province}', 0, '{category}')
                                    """)
                                    response = HttpResponseRedirect(reverse("homepage"))
                                    response.set_cookie('user_name', fname + " " + lname)
                                    response.set_cookie('user_email', email)
                                    response.set_cookie('user_type', 'resto')
                                    return response
                              except Exception as e:
                                    messages.info(request, e)
            else:
                  print(restoran_form.errors)
      else:
            restoran_form = RestoranForm()
      return render(request, 'regis_restoran.html',
            {'restoran_form':restoran_form, 'province': PROVINCES, 'category': CATEGORIES})

def regis_kurir(request):

      
      if request.method == 'POST':
            kurir_form = KurirForm(data=request.POST)
            if kurir_form.is_valid():
                  email = request.POST.get('email')
                  password = request.POST.get('password')
                  fname = request.POST.get('fname')
                  lname = request.POST.get('lname')
                  no_hp = request.POST.get('no_hp')
                  nik = request.POST.get('nik')
                  bank_name = request.POST.get('bank_name')
                  no_rek = request.POST.get('no_rek')
                  plate_num = request.POST.get('plate_num')
                  sim_num = request.POST.get('sim_num')
                  vehicle_brand = request.POST.get('vehicle_brand')
                  trans_type = request.POST.get('trans_type')

                  with transaction.atomic():
                        with connection.cursor() as cursor:
                              try:
                                    cursor.execute(f"""
                                          INSERT INTO SIREST.USER_ACC
                                          VALUES ('{email}', '{password}', '{no_hp}', '{fname}', '{lname}')
                                    """)
                                    cursor.execute(f"""
                                          INSERT INTO SIREST.TRANSACTION_ACTOR
                                          VALUES ('{email}', '{nik}', '{bank_name}', '{no_rek}', 0, NULL)
                                    """)
                                    cursor.execute(f"""
                                          INSERT INTO SIREST.COURIER
                                          VALUES ('{email}', '{plate_num}', '{sim_num}', '{trans_type}', '{vehicle_brand}')
                                    """)
                                    response = HttpResponseRedirect(reverse("homepage"))
                                    response.set_cookie('user_name', fname + " " + lname)
                                    response.set_cookie('user_email', email)
                                    response.set_cookie('user_type', 'courier')
                                    return response
                              except Exception as e:
                                    messages.info(request, e)
                  
            else:
                  print(kurir_form.errors)
      else:
            kurir_form = KurirForm()
      return render(request, 'regis_kurir.html',
            {'kurir_form':kurir_form})

