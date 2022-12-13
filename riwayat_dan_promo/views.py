from django.shortcuts import render, redirect
from riwayat_dan_promo.forms import *
from django.db import connection, transaction
from django.contrib import messages

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
    jenis = "MINIMUM TRANSAKSI"
    if request.method == 'POST':
            if promo_form.is_valid():
                promoname = request.POST.get('promoname')
                discount = request.POST.get('discount')
                minimumtransactionnum = request.POST.get('minimumtransactionnum')
                with transaction.atomic():
                    with connection.cursor() as cursor:
                            cursor.execute("""
                                        SELECT * FROM SIREST.PROMO 
                            """)
                            increment = cursor.rowcount
                            increment+=1
                            pid = "P" + str(increment)
                            try:
                                cursor.execute(f"""
                                        INSERT INTO SIREST.PROMO
                                        VALUES ('{pid}', '{promoname}', {discount})
                                """)
                                cursor.execute(f"""
                                        INSERT INTO SIREST.MIN_TRANSACTION_PROMO
                                        VALUES ('{pid}', {minimumtransactionnum})
                                """)
              
                                return redirect('riwayat_dan_promo:daftar_promosi')
                            except Exception as e:
                                messages.info(request, e)
            else:
                print(promo_form.errors)

    return render(request, 'buat_promo_form.html', 
            {'promo_form':promo_form, 'jenis': jenis})

def buat_promo_hari_spesial(request):
    promo_form = PromoHariSpesialForm(request.POST or None)
    jenis = 'HARI SPESIAL'
    if request.method == 'POST':
            if promo_form.is_valid():
                promoname = request.POST.get('promoname')
                discount = request.POST.get('discount')
                date = request.POST.get('date')
                with transaction.atomic():
                    with connection.cursor() as cursor:
                            cursor.execute("""
                                        SELECT * FROM SIREST.PROMO 
                            """)
                            increment = cursor.rowcount
                            increment+=1
                            pid = "P" + str(increment)
                            try:
                                cursor.execute(f"""
                                        INSERT INTO SIREST.PROMO
                                        VALUES ('{pid}', '{promoname}', {discount})
                                """)
                                cursor.execute(f"""
                                        INSERT INTO SIREST.SPECIAL_DAY_PROMO
                                        VALUES ('{pid}', '{date}')
                                """)
              
                                return redirect('riwayat_dan_promo:daftar_promosi')
                            except Exception as e:
                                messages.info(request, e) 
            else:
                  print(promo_form.errors)

    return render(request, 'buat_promo_form.html', 
            {'promo_form':promo_form, 'jenis': jenis})


def daftar_promosi(request):
    
    context = {}


    with connection.cursor() as cursor:
        cursor.execute(
                """
                    SELECT  DISTINCT ON (Id) *                    
                    FROM SIREST.PROMO 
                    LEFT JOIN SIREST.SPECIAL_DAY_PROMO USING (Id)
                    LEFT JOIN SIREST.MIN_TRANSACTION_PROMO USING (Id)
                    LEFT JOIN SIREST.RESTAURANT_PROMO ON Id = Pid
                    ORDER BY Id
                """
        ) 
        fields = [field_name[0] for field_name in cursor.description]
        rows = cursor.fetchall()
        promos = [dict(zip(fields, row)) for row in rows]
        context['promos'] = promos

    return render(request, 'daftar_promosi.html', context)

def detail_promo_min_transaksi(request, pid):
    context = {}

    with connection.cursor() as cursor:
        cursor.execute(
                f"""
                    SELECT *
                    FROM SIREST.PROMO 
                    NATURAL JOIN SIREST.MIN_TRANSACTION_PROMO
                    WHERE id = '{pid}'
                """
        ) 
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        promo = dict(zip(fields, row))
        context['promo'] = promo
    return render(request, 'detail_promosi.html', context)

def detail_promo_hari_spesial(request, pid):
    context = {}

    with connection.cursor() as cursor:
        cursor.execute(
                f"""
                    SELECT *
                    FROM SIREST.PROMO 
                    NATURAL JOIN SIREST.SPECIAL_DAY_PROMO
                    WHERE id = '{pid}'
                """
        ) 
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        promo = dict(zip(fields, row))
        context['promo'] = promo
    return render(request, 'detail_promosi.html', context)

def ubah_promo_min_transaksi(request, pid):
    with connection.cursor() as cursor:
        cursor.execute(
                f"""
                    SELECT *
                    FROM SIREST.PROMO 
                    NATURAL JOIN SIREST.MIN_TRANSACTION_PROMO
                    WHERE id = '{pid}'
                """
        ) 
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        promo = dict(zip(fields, row))

    
    if request.method == 'POST':
        discount = request.POST.get('discount')
        minimumtransactionnum = request.POST.get('minimumtransactionnum')
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""
                        UPDATE SIREST.PROMO 
                        SET discount = {discount}
                        WHERE id = '{pid}'
                    """
                ) 
                cursor.execute(
                    f"""
                        UPDATE SIREST.MIN_TRANSACTION_PROMO 
                        SET minimumtransactionnum = {minimumtransactionnum}
                        WHERE id = '{pid}'
                    """
                ) 
        return redirect('riwayat_dan_promo:daftar_promosi')
    
    return render(request, 'ubah_promosi.html', 
            {'promo':promo})

def ubah_promo_hari_spesial(request, pid):
    with connection.cursor() as cursor:
        cursor.execute(
                f"""
                    SELECT *
                    FROM SIREST.PROMO 
                    NATURAL JOIN SIREST.SPECIAL_DAY_PROMO
                    WHERE id = '{pid}'
                """
        ) 
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        promo = dict(zip(fields, row))

    
    if request.method == 'POST':
        discount = request.POST.get('discount')
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""
                        UPDATE SIREST.PROMO 
                        SET discount = {discount}
                        WHERE id = '{pid}'
                    """
                ) 
        return redirect('riwayat_dan_promo:daftar_promosi')
    
    return render(request, 'ubah_promosi.html', 
            {'promo':promo})

def hapus_promo(request, pid):
    with transaction.atomic():
        with connection.cursor() as cursor:
            cursor.execute(
                f"""
                    DELETE FROM SIREST.SPECIAL_DAY_PROMO 
                    WHERE id = '{pid}'
                """
            ) 
            cursor.execute(
                f"""
                    DELETE FROM SIREST.MIN_TRANSACTION_PROMO 
                    WHERE id = '{pid}'
                """
            )
            cursor.execute(
                f"""
                    DELETE FROM SIREST.PROMO 
                    WHERE id = '{pid}'
                """
            )
    return redirect('riwayat_dan_promo:daftar_promosi')

def daftar_promo_restoran(request):
    context = {}


    with connection.cursor() as cursor:
        
        resto_email = request.COOKIES.get('user_email')
        cursor.execute(
                f"""
                    SELECT  *                    
                    FROM SIREST.PROMO 
                    LEFT JOIN SIREST.SPECIAL_DAY_PROMO USING (Id)
                    LEFT JOIN SIREST.MIN_TRANSACTION_PROMO USING (Id)
                    JOIN SIREST.RESTAURANT_PROMO ON Id = PId
                    NATURAL JOIN SIREST.RESTAURANT
                    WHERE email = '{resto_email}'
                    ORDER BY Id
                """
        ) 
        fields = [field_name[0] for field_name in cursor.description]
        rows = cursor.fetchall()
        resto_promos = [dict(zip(fields, row)) for row in rows]
        context['resto_promos'] = resto_promos

    return render(request, 'daftar_promo_restoran.html', context)

def detail_promo_restoran(request, pid):
    context = {}
    with connection.cursor() as cursor:
        
        resto_email = request.COOKIES.get('user_email')
        cursor.execute(
                f"""
                    SELECT  *                    
                    FROM SIREST.PROMO 
                    LEFT JOIN SIREST.SPECIAL_DAY_PROMO USING (Id)
                    LEFT JOIN SIREST.MIN_TRANSACTION_PROMO USING (Id)
                    JOIN SIREST.RESTAURANT_PROMO ON Id = PId
                    NATURAL JOIN SIREST.RESTAURANT
                    WHERE email = '{resto_email}' AND Id = '{pid}'
                """
        ) 
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        resto_promo = dict(zip(fields, row))
        context['resto_promo'] = resto_promo
    return render(request, 'detail_promo_restoran.html', context)

def tambah_promo_restoran(request):
    context = {}

    with connection.cursor() as cursor:
        cursor.execute(
                """
                    SELECT  DISTINCT ON (Id) *                    
                    FROM SIREST.PROMO 
                    LEFT JOIN SIREST.SPECIAL_DAY_PROMO USING (Id)
                    LEFT JOIN SIREST.MIN_TRANSACTION_PROMO USING (Id)
                    LEFT JOIN SIREST.RESTAURANT_PROMO ON Id = Pid
                    ORDER BY Id
                """
        ) 
        fields = [field_name[0] for field_name in cursor.description]
        rows = cursor.fetchall()
        promos = [dict(zip(fields, row)) for row in rows]
        context['promos'] = promos


        email = request.COOKIES.get('user_email')
        cursor.execute(
                f"""
                    SELECT *                  
                    FROM SIREST.RESTAURANT
                    WHERE email = '{email}'
                """
        ) 
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        resto = dict(zip(fields, row))
        rname = resto['rname']
        rbranch = resto['rbranch']

    if request.method == "POST":
        promo = request.POST.get('promo')
        pid = promo.split("/")[0]
        start = request.POST.get('start')
        endpromo = request.POST.get('endpromo')

        with transaction.atomic():
            with connection.cursor() as cursor:
                try:
                    cursor.execute(f"""
                            INSERT INTO SIREST.RESTAURANT_PROMO
                            VALUES ('{rname}', '{rbranch}', '{pid}', '{start}', '{endpromo}')
                    """)
            
                    return redirect('riwayat_dan_promo:daftar_promo_restoran')
                except Exception as e:
                    messages.info(request, e) 


    return render(request, 'tambah_promo_restoran.html', context)


def ubah_promo_restoran(request, pid):

    context = {}
    with connection.cursor() as cursor:
        
        resto_email = request.COOKIES.get('user_email')
        
        cursor.execute(
                f"""
                    SELECT  *                    
                    FROM SIREST.PROMO 
                    LEFT JOIN SIREST.SPECIAL_DAY_PROMO USING (Id)
                    LEFT JOIN SIREST.MIN_TRANSACTION_PROMO USING (Id)
                    JOIN SIREST.RESTAURANT_PROMO ON Id = PId
                    NATURAL JOIN SIREST.RESTAURANT
                    WHERE email = '{resto_email}' AND Id = '{pid}'
                """
        ) 
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        resto_promo = dict(zip(fields, row))
        rname = resto_promo['rname']
        rbranch = resto_promo['rbranch']
        context['resto_promo'] = resto_promo
    if request.method == "POST":
        start = request.POST.get('start')
        endpromo = request.POST.get('endpromo')

        with transaction.atomic():
            with connection.cursor() as cursor:
                try:
                    cursor.execute(f"""
                            UPDATE SIREST.RESTAURANT_PROMO
                            SET start = '{start}', endpromo = '{endpromo}'
                            WHERE rname = '{rname}' AND rbranch = '{rbranch}' AND pid = '{pid}'
                    """)
            
                    return redirect('riwayat_dan_promo:daftar_promo_restoran')
                except Exception as e:
                    messages.info(request, e) 

    return render(request, 'ubah_promo_restoran.html', context)


def hapus_promo_restoran(request, pid):
    resto_email = request.COOKIES.get('user_email')
    with connection.cursor() as cursor:
        cursor.execute(
                f"""
                    SELECT *                  
                    FROM SIREST.RESTAURANT
                    WHERE email = '{resto_email}'
                """
        ) 
        fields = [field_name[0] for field_name in cursor.description]
        row = cursor.fetchone()
        resto = dict(zip(fields, row))
        rname = resto['rname']
        rbranch = resto['rbranch']
    with transaction.atomic():
        with connection.cursor() as cursor:
            cursor.execute(
                f"""
                    DELETE FROM SIREST.RESTAURANT_PROMO 
                    WHERE rname = '{rname}' AND rbranch = '{rbranch}' AND pid = '{pid}'
                """
            ) 

    return redirect('riwayat_dan_promo:daftar_promo_restoran')