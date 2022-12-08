from django.shortcuts import render, redirect
from riwayat_dan_promo.forms import *
from riwayat_dan_promo.models import *
from django.db import connection, transaction
# Create your views here.



    

def riwayat_transaksi(request):
    context = {}
    
    email = request.COOKIES['user_email']

    with connection.cursor() as cursor:
        if request.COOKIES['user_type'] == 'customer':
            cursor.execute(
                f"""
                    SELECT DISTINCT T.email, TF.Rname, TF.Rbranch, T.datetime, U.fname as CourierFname, U.lname as CourierLname, TS.id as statusid, TS.name as statusname, T.rating
                    FROM SIREST.TRANSACTION_HISTORY TH
                    NATURAL JOIN SIREST.TRANSACTION T
                    NATURAL JOIN SIREST.TRANSACTION_FOOD TF
                    JOIN SIREST.USER_ACC U ON U.email = T.CourierId
                    JOIN SIREST.TRANSACTION_STATUS TS ON TH.Tsid = TS.id
                    WHERE T.email = '{email}' AND (tsid = 'TS4' OR tsid = 'TS5')
                """
            )
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            transactions = [dict(zip(fields, row)) for row in rows]
            context['transactions'] = transactions
        elif request.COOKIES['user_type'] == 'resto':


            cursor.execute(
                f"""
                    SELECT T.email, TF.Rname, TF.Rbranch, T.datetime, U.fname as CourierFname, U.lname as CourierLname, TS.id as statusid, TS.name as statusname, T.rating, U2.fname as CustomerFname, U2.lname as CustomerLname
                    FROM SIREST.TRANSACTION_HISTORY TH
                    NATURAL JOIN SIREST.TRANSACTION T
                    NATURAL JOIN SIREST.TRANSACTION_FOOD TF
                    NATURAL JOIN SIREST.RESTAURANT R
                    JOIN SIREST.USER_ACC U ON U.email = T.CourierId
                    JOIN SIREST.USER_ACC U2 ON U2.email = T.email
                    JOIN SIREST.TRANSACTION_STATUS TS ON TH.Tsid = TS.id
                    WHERE R.email = '{email}' AND (tsid = 'TS4' OR tsid = 'TS5')
                """
            )
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            transactions = [dict(zip(fields, row)) for row in rows]
            context['transactions'] = transactions
        elif request.COOKIES['user_type'] == 'courier':
            cursor.execute(
                f"""
                    SELECT T.email, TF.Rname, TF.Rbranch, T.datetime, TS.id as statusid, TS.name as statusname, T.rating, U.fname as CustomerFname, U.lname as CustomerLname
                    FROM SIREST.TRANSACTION_HISTORY TH
                    NATURAL JOIN SIREST.TRANSACTION T
                    NATURAL JOIN SIREST.TRANSACTION_FOOD TF
                    JOIN SIREST.USER_ACC U ON U.email = T.email
                    JOIN SIREST.TRANSACTION_STATUS TS ON TH.Tsid = TS.id
                    WHERE T.CourierId = '{email}' AND (tsid = 'TS4' OR tsid = 'TS5')
                """
            )
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            transactions = [dict(zip(fields, row)) for row in rows]
            context['transactions'] = transactions
        
    return render(request, 'riwayat_transaksi.html', context)

def detail_transaksi(request, email, date, time):
    context = {}
    datetime = date + " " + time

    with connection.cursor() as cursor:
        cursor.execute(
                f"""
                    SELECT *, (T.totalprice - T.totaldiscount) as discountedprice
                    FROM SIREST.TRANSACTION T NATURAL JOIN SIREST.USER_ACC U
                    WHERE T.email = '{email}' AND T.datetime = '{datetime}'
                """
        )
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        transaction = dict(zip(fields, row))

        
        context['transaction'] = transaction
        cursor.execute(
                f"""
                    SELECT *
                    FROM SIREST.RESTAURANT R JOIN SIREST.TRANSACTION_FOOD TF USING (rname, rbranch)
                    WHERE TF.email = '{email}' AND TF.datetime = '{datetime}'
                """
        )
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        resto = dict(zip(fields, row))
        context['resto'] = resto

        cursor.execute(
                f"""
                    SELECT *
                    FROM SIREST.TRANSACTION_FOOD TF
                    WHERE TF.email = '{email}' AND TF.datetime = '{datetime}'
                """
        )
        fields = [field_name[0] for field_name in cursor.description]
        rows = cursor.fetchall()
        foods = [dict(zip(fields, row)) for row in rows]
        context['foods'] = foods

        pm_id = transaction['pmid']

        cursor.execute(
                f"""
                    SELECT *
                    FROM SIREST.PAYMENT_METHOD 
                    WHERE id = '{pm_id}'
                """
        )
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        pay_method = dict(zip(fields, row))
        context['pay_method'] = pay_method

        ps_id = transaction['psid']
        cursor.execute(
                f"""
                    SELECT *
                    FROM SIREST.PAYMENT_STATUS 
                    WHERE id = '{ps_id}'
                """
        )
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        pay_status = dict(zip(fields, row))
        context['pay_status'] = pay_status

        courier_id = transaction['courierid']
        cursor.execute(
                f"""
                    SELECT *
                    FROM SIREST.COURIER C NATURAL JOIN SIREST.USER_ACC U
                    WHERE email = '{courier_id}'
                """
        )
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        courier = dict(zip(fields, row))
        context['courier'] = courier
        
        cursor.execute(
                f"""
                    SELECT *
                    FROM SIREST.TRANSACTION_HISTORY TH JOIN SIREST.TRANSACTION_STATUS TS ON TH.TSid = TS.id
                    WHERE TH.email = '{email}' AND TH.datetime = '{datetime}'
                    ORDER BY TH.datetimestatus
                """
        )
        fields = [field_name[0] for field_name in cursor.description]
        rows = cursor.fetchall()
        transaction_status = [dict(zip(fields, row)) for row in rows]
        context['transaction_status'] = transaction_status

    return render(request, 'detail_transaksi.html', context) 

def nilai_transaksi(request, email, date, time):
    
    datetime = date + " " + time
    context = {
        'email': email,
        'datetime': datetime
    }
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""
                        UPDATE SIREST.TRANSACTION
                        SET rating = {rating}
                        WHERE email = '{email}' AND datetime = '{datetime}'
                    """
            )
        return redirect('riwayat_dan_promo:riwayat_transaksi')
    return render(request, 'nilai_transaksi.html', context)

def buat_promo(request):
    return render(request, 'buat_promo.html')

def buat_promo_min_transaksi(request):
    promo_form = PromoMinTransaksiForm(request.POST or None)
    judul = "Form Promo Minimum Transaksi"
    if request.method == 'POST':
            if promo_form.is_valid():
                  promo = promo_form.save(commit=False)
                  promo.tipe_promo = 'm'
                  promo.save()
                  return redirect('riwayat_dan_promo:daftar_promosi')
            else:
                  print(promo_form.errors)

    return render(request, 'buat_promo_form.html', 
            {'promo_form':promo_form, 'judul': judul})

def buat_promo_hari_spesial(request):
    promo_form = PromoHariSpesialForm(request.POST or None)
    judul = 'Form Promo Hari Spesial'
    if request.method == 'POST':
            if promo_form.is_valid():
                  promo = promo_form.save(commit=False)
                  promo.tipe_promo = 'h'
                  promo.save()
                  return redirect('riwayat_dan_promo:daftar_promosi')
            else:
                  print(promo_form.errors)

    return render(request, 'buat_promo_form.html', 
            {'promo_form':promo_form, 'judul': judul})


def daftar_promosi(request):
    promosi = Promo.objects.all()
    context = {
        'daftar_promo': promosi,
    }
    return render(request, 'daftar_promosi.html', context)

def detail_promo_min_transaksi(request, id):
    promo = PromoMinTransaksi.objects.get(pk=id)
    context = {
        'promo': promo
    }
    return render(request, 'detail_promosi.html', context)

def detail_promo_hari_spesial(request, id):
    promo = PromoHariSpesial.objects.get(pk=id)
    context = {
        'promo': promo
    }
    return render(request, 'detail_promosi.html', context)

def ubah_promo_min_transaksi(request, id):
    promo = PromoMinTransaksi.objects.get(pk=id)
    judul = 'Ubah Promo Min Transaksi'
    initial_fields = {
        'nama_promo': promo.nama_promo,
        'diskon': promo.diskon,
        'min_transaksi': promo.min_transaksi
    }
    promo_form = PromoMinTransaksiForm(request.POST or None, initial=initial_fields)
    if request.method == 'POST':
        
        promo.diskon = request.POST.get('diskon')
        promo.min_transaksi = request.POST.get('min_transaksi')
        promo.save()
        return redirect('riwayat_dan_promo:daftar_promosi')
       

    promo_form.fields['nama_promo'].disabled = True
    promo_form.fields['nama_promo'].required = False

    return render(request, 'ubah_promosi.html', 
            {'promo_form':promo_form, 'judul': judul})

def ubah_promo_hari_spesial(request, id):
    promo = PromoHariSpesial.objects.get(pk=id)
    judul = 'Ubah Promo Hari Spesial'
    initial_fields = {
        'nama_promo': promo.nama_promo,
        'diskon': promo.diskon,
        'tanggal_spesial': promo.tanggal_spesial
    }
    promo_form = PromoHariSpesialForm(request.POST or None, initial=initial_fields)
    if request.method == 'POST':
            
        promo.diskon = request.POST.get('diskon')
        promo.save()
        return redirect('riwayat_dan_promo:daftar_promosi')
            

    promo_form.fields['nama_promo'].disabled = True   
    promo_form.fields['tanggal_spesial'].disabled = True

    promo_form.fields['nama_promo'].required = False   
    promo_form.fields['tanggal_spesial'].required = False

    return render(request, 'ubah_promosi.html', 
            {'promo_form':promo_form, 'judul': judul})


def daftar_promo_restoran(request):
    promosi = Promo.objects.all()
    context = {
        'daftar_promo': promosi,
    }
    return render(request, 'daftar_promo_restoran.html', context)

def detail_promo_restoran(request, id):
    promo = Promo.objects.get(pk=id)
    context = {
        'promo': promo
    }
    return render(request, 'detail_promo_restoran.html', context)

def tambah_promo_restoran(request):
    return render(request, 'tambah_promo_restoran.html')


def ubah_promo_restoran(request, id):
    return render(request, 'ubah_promo_restoran.html')