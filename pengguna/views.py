from django.shortcuts import render, redirect
from django.contrib.auth.models import User as DjangoUser
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import AdminForm, PelangganForm, RestoranForm, KurirForm
from json import dumps

from django.db import connection, transaction

# Create your views here.

def homepage(request):
      context = {}
      with connection.cursor() as cursor:
            if request.COOKIES['user_type'] == 'admin':
            
                  cursor.execute(f"""
                        SELECT *
                        FROM SIREST.USER_ACC
                        WHERE email = '{request.COOKIES['user_email']}'
                  """)

                  fields = [field_name[0] for field_name in cursor.description]
                  row = cursor.fetchone()
                  admin = dict(zip(fields, row))
                  context['current_user'] = admin
                  cursor.execute("""
                        SELECT * FROM 
                        SIREST.USER_ACC
                        LEFT JOIN SIREST.TRANSACTION_ACTOR using (email) 
                        LEFT JOIN SIREST.COURIER using (email) 
                        LEFT JOIN SIREST.CUSTOMER USING (email)
                        LEFT JOIN SIREST.RESTAURANT USING (email)
                  """)

                  rows = cursor.fetchall()
                  fields = [field_name[0] for field_name in cursor.description]
                  users = [dict(zip(fields, row)) for row in rows]
                  context['users'] = users
            elif request.COOKIES['user_type'] == 'customer':
                  cursor.execute(f"""
                        SELECT *
                        FROM SIREST.USER_ACC NATURAL JOIN SIREST.TRANSACTION_ACTOR NATURAL JOIN SIREST.CUSTOMER
                        WHERE email = '{request.COOKIES['user_email']}'
                  """)
                  fields = [field_name[0] for field_name in cursor.description]
                  row = cursor.fetchone()
                  customer = dict(zip(fields, row))
                  context['current_user'] = customer

                  admin_email = customer['adminid']
                  if admin_email:
                        cursor.execute(f"""
                              SELECT fname, lname
                              FROM SIREST.USER_ACC
                              WHERE email = '{admin_email}'
                        """)
                        fields = [field_name[0] for field_name in cursor.description]
                        row = cursor.fetchone()
                        context['admin_name'] = row[0] + " " + row[1]

            elif request.COOKIES['user_type'] == 'resto':
                  cursor.execute(f"""
                        SELECT *
                        FROM SIREST.USER_ACC NATURAL JOIN SIREST.TRANSACTION_ACTOR NATURAL JOIN SIREST.RESTAURANT
                        WHERE email = '{request.COOKIES['user_email']}'
                  """)
                  fields = [field_name[0] for field_name in cursor.description]
                  row = cursor.fetchone()
                  resto = dict(zip(fields, row))
                  context['current_user'] = resto

                  rname = resto['rname']
                  rbranch = resto['rbranch']
                  cursor.execute(f"""
                        SELECT day, starthours, endhours
                        FROM SIREST.RESTAURANT_OPERATING_HOURS
                        WHERE (name, branch) = ('{rname}', '{rbranch}')
                  """)
                  fields = [field_name[0] for field_name in cursor.description]
                  rows = cursor.fetchall()
                  operating_hours = [dict(zip(fields, row)) for row in rows]
                  context['operating_hours'] = operating_hours

                  admin_email = resto['adminid']
                  if admin_email:
                        cursor.execute(f"""
                              SELECT fname, lname
                              FROM SIREST.USER_ACC
                              WHERE email = '{admin_email}'
                        """)
                        fields = [field_name[0] for field_name in cursor.description]
                        row = cursor.fetchone()
                        context['admin_name'] = row[0] + " " + row[1]


            elif request.COOKIES['user_type'] == 'courier':
                  cursor.execute(f"""
                        SELECT *
                        FROM SIREST.USER_ACC NATURAL JOIN SIREST.TRANSACTION_ACTOR NATURAL JOIN SIREST.COURIER
                        WHERE email = '{request.COOKIES['user_email']}'
                  """)
                  fields = [field_name[0] for field_name in cursor.description]
                  row = cursor.fetchone()
                  courier = dict(zip(fields, row))
                  context['current_user'] = courier

                  admin_email = courier['adminid']
                  if admin_email:
                        cursor.execute(f"""
                              SELECT fname, lname
                              FROM SIREST.USER_ACC
                              WHERE email = '{admin_email}'
                        """)
                        fields = [field_name[0] for field_name in cursor.description]
                        row = cursor.fetchone()
                        context['admin_name'] = row[0] + " " + row[1]

            
      return render(request, "home.html", context)

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
                              response.set_cookie('email', email)
                        return response
                  else:
                        messages.info(request, 'Email atau password tidak valid')
                        
      return render(request, 'login.html')

def logout_pengguna(request):
      # TODO: Logout pengguna
      response = HttpResponseRedirect(reverse('index'))
      response.delete_cookie('user_name')
      response.delete_cookie('user_email')
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


def detail_customer(request, email):
      context = {}
      with connection.cursor() as cursor:
            cursor.execute(f"""
                  SELECT *
                  FROM SIREST.USER_ACC NATURAL JOIN SIREST.TRANSACTION_ACTOR NATURAL JOIN SIREST.CUSTOMER
                  WHERE email = '{email}'
            """)
            fields = [field_name[0] for field_name in cursor.description]
            row = cursor.fetchone()
            customer = dict(zip(fields, row))
            context['current_user'] = customer

            admin_email = customer['adminid']
            if admin_email:
                  cursor.execute(f"""
                        SELECT fname, lname
                        FROM SIREST.USER_ACC
                        WHERE email = '{admin_email}'
                  """)
                  fields = [field_name[0] for field_name in cursor.description]
                  row = cursor.fetchone()
                  context['admin_name'] = row[0] + " " + row[1]

      return render(request, "detail_pengguna.html", context)


def detail_resto(request, email):
      context = {}
      with connection.cursor() as cursor:
            cursor.execute(f"""
                  SELECT *
                  FROM SIREST.USER_ACC NATURAL JOIN SIREST.TRANSACTION_ACTOR NATURAL JOIN SIREST.RESTAURANT
                  WHERE email = '{email}'
            """)
            fields = [field_name[0] for field_name in cursor.description]
            row = cursor.fetchone()
            resto = dict(zip(fields, row))
            context['current_user'] = resto

            rname = resto['rname']
            rbranch = resto['rbranch']
            cursor.execute(f"""
                  SELECT day, starthours, endhours
                  FROM SIREST.RESTAURANT_OPERATING_HOURS
                  WHERE (name, branch) = ('{rname}', '{rbranch}')
            """)
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            operating_hours = [dict(zip(fields, row)) for row in rows]
            context['operating_hours'] = operating_hours

            cursor.execute(f"""
                  SELECT promoname, start, endpromo
                  FROM SIREST.RESTAURANT_PROMO RP JOIN SIREST.PROMO P ON RP.Pid = P.id
                  WHERE (rname, rbranch) = ('{rname}', '{rbranch}')
            """)
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            promos = [dict(zip(fields, row)) for row in rows]
            context['promos'] = promos

            admin_email = resto['adminid']
            if admin_email:
                  cursor.execute(f"""
                        SELECT fname, lname
                        FROM SIREST.USER_ACC
                        WHERE email = '{admin_email}'
                  """)
                  fields = [field_name[0] for field_name in cursor.description]
                  row = cursor.fetchone()
                  context['admin_name'] = row[0] + " " + row[1]

      return render(request, "detail_pengguna.html", context)

def detail_courier(request, email):
      context = {}
      with connection.cursor() as cursor:
            cursor.execute(f"""
                  SELECT *
                  FROM SIREST.USER_ACC NATURAL JOIN SIREST.TRANSACTION_ACTOR NATURAL JOIN SIREST.COURIER
                  WHERE email = '{email}'
            """)
            fields = [field_name[0] for field_name in cursor.description]
            row = cursor.fetchone()
            courier = dict(zip(fields, row))
            context['current_user'] = courier

            admin_email = courier['adminid']
            if admin_email:
                  cursor.execute(f"""
                        SELECT fname, lname
                        FROM SIREST.USER_ACC
                        WHERE email = '{admin_email}'
                  """)
                  fields = [field_name[0] for field_name in cursor.description]
                  row = cursor.fetchone()
                  context['admin_name'] = row[0] + " " + row[1]

      return render(request, "detail_pengguna.html", context)


def verifikasi(request, email):
      with transaction.atomic():
            with connection.cursor() as cursor:
                  adminid = request.COOKIES['user_email']
                  cursor.execute(f"""
                        UPDATE SIREST.TRANSACTION_ACTOR
                        SET adminid = '{adminid}'
                        WHERE email = '{email}'
                  """)
      
      return redirect('homepage')
