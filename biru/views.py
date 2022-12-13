from django.shortcuts import render, redirect
from biru.forms import CreateKategoriRestoForm, CreateBahanMakananForm
from django.http.response import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.db import connection
from .utils import *

# Create your views here.

#[CREATE] Kategori Restoran
def create_kategori_restoran(request):
    if request.COOKIES['user_type'] == 'admin':
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM SIREST.RESTAURANT_CATEGORY ORDER BY id DESC LIMIT 1")
        result = dictfetchall(cursor)
        id = result[0].get('id')
        id = int(id) + 1
        cursor.close()
        form = CreateKategoriRestoForm(request.POST)
        if (form.is_valid() and request.POST):
            try:
                nama = form.cleaned_data['nama_kategori']
                cursor = connection.cursor()
                cursor.execute("SET SEARCH_PATH TO SIREST")
                cursor.execute("INSERT INTO RESTAURANT_CATEGORY(id, name) \
                                VALUES ('{}', '{}')".format(id, nama))
            except Exception as e:
                print(e)
            return redirect("/read-kategori-restoran")
    else:
        return HttpResponseForbidden("Forbidden") 
    return render(request, 'create_kategori_restoran.html', {'form':form})

#[READ] Kategori Restoran
def read_kategori_restoran(request):
    result = {}
    if request.COOKIES['user_type'] == 'admin':
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("SELECT id, name FROM RESTAURANT_CATEGORY")
        result['query1'] = namedtuplefetchall(cursor)
        cursor.execute("SELECT id FROM RESTAURANT_CATEGORY WHERE id NOT IN (SELECT RCategory FROM RESTAURANT)")
        result['query2'] = listfecthall(cursor)
    else:
        return HttpResponseForbidden("Forbidden")
    return render(request, 'read_kategori_restoran.html', result)

#[DELETE] Kategori Restoran
def delete_kategori_restoran(request, id):
    if request.COOKIES['user_type'] == 'admin':
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("DELETE FROM RESTAURANT_CATEGORY WHERE id = '{}'".format(id))
    else:
        return HttpResponseForbidden("Forbidden")
    return redirect('/read-kategori-restoran')

#[CREATE] Bahan Makanan
def create_bahan_makanan(request):
    if request.COOKIES['user_type'] == 'admin':
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM SIREST.INGREDIENT ORDER BY id DESC LIMIT 1")
        result = dictfetchall(cursor)
        id = result[0].get('id')
        id = "IN" + str(int(id[2:])+1)
        cursor.close()
        form = CreateBahanMakananForm(request.POST)
        if (form.is_valid() and request.POST):
            try:
                nama = form.cleaned_data['nama_bahan']
                cursor = connection.cursor()
                cursor.execute("SET SEARCH_PATH TO SIREST")
                cursor.execute("INSERT INTO INGREDIENT(id, name) \
                                VALUES ('{}', '{}')".format(id, nama))
            except Exception as e:
                print(e)
            return redirect("/read-bahan-makanan")
    else:
        return HttpResponseForbidden("Forbidden") 
    return render(request, 'create_bahan_makanan.html', {'form':form})

#[READ] Bahan Makanan
def read_bahan_makanan(request):
    result = {}
    if request.COOKIES['user_type'] == 'admin':
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("SELECT id, name FROM INGREDIENT")
        result['query1'] = namedtuplefetchall(cursor)
        cursor.execute("SELECT id FROM INGREDIENT \
                        WHERE id NOT IN (SELECT Ingredient FROM FOOD_INGREDIENT FI INNER JOIN FOOD F \
                        ON FI.FoodName = F.FoodName AND FI.RBranch = F.RBranch AND FI.RName = F.RName)")
        result['query2'] = listfecthall(cursor)
        print(result)
    else:
        return HttpResponseForbidden("Forbidden")
    return render(request, 'read_bahan_makanan.html', result)

#[DELETE] Bahan Makanan
def delete_bahan_makanan(request, id):
    if request.COOKIES['user_type'] == 'admin':
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("DELETE FROM INGREDIENT WHERE id = '{}'".format(id))
    else:
        return HttpResponseForbidden("Forbidden")
    return redirect('/read-bahan-makanan')

#[READ] Transaksi Pemesanan (POV Kurir)
def read_transaksi_kurir(request):
    result = {}
    email = request.COOKIES['email']
    if request.COOKIES['user_type'] == 'courier':
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("SELECT DISTINCT ON (TH.Email, TH.Datetime, TH.TSid) TF.Email, TF.Datetime, TF.RName, TF.RBranch, U.FName, U.Lname, TS.Name, TS.id\
                        FROM TRANSACTION_FOOD TF INNER JOIN TRANSACTION_HISTORY TH \
                        ON TF.Email = TH.Email AND TF.Datetime = TH.Datetime \
                        INNER JOIN USER_ACC U ON TH.Email = U.Email \
                        INNER JOIN TRANSACTION_STATUS TS ON TH.TSid = TS.id \
                        INNER JOIN TRANSACTION T ON TF.Email = T.Email AND TF.Datetime = T.Datetime \
                        WHERE T.CourierId = '{}'".format(email))
        result = namedtuplefetchall(cursor)
        print(result)
    else:
        return HttpResponseForbidden("Forbidden")
    return render(request, 'read_transaksi_kurir.html', {'result':result})

#[READ] Transaksi Pemesanan (POV Kurir)
def read_detail_transaksi_kurir(request, email, datetime):
    result = {}
    email_kurir = request.COOKIES['email']
    print(email, datetime, email_kurir)
    if request.COOKIES['user_type'] == 'courier':
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("SELECT * FROM TRANSACTION T INNER JOIN PAYMENT_METHOD PM \
                        ON T.PMid = PM.id WHERE CourierId = '{}' AND Email = '{}' AND Datetime = '{}' \
                        LIMIT 1".format(email_kurir, email, datetime))
        result['query1'] = namedtuplefetchall(cursor)

        cursor.execute("SELECT TF.RName, TF.Rbranch, Amount, Note, Street, District, City, Province FROM TRANSACTION_FOOD TF INNER JOIN RESTAURANT R \
                        ON TF.RName = R.Rname AND TF.RBranch = R.Rbranch WHERE TF.Email = '{}' AND TF.Datetime = '{}' \
                        LIMIT 1".format(email, datetime))
        result['query2'] = namedtuplefetchall(cursor)

        cursor.execute("SELECT * FROM TRANSACTION_FOOD TF WHERE TF.Email = '{}' AND TF.Datetime = '{}'".format(email, datetime))
        result['query3'] = namedtuplefetchall(cursor)

        cursor.execute("SELECT PS.Name FROM TRANSACTION T INNER JOIN PAYMENT_STATUS PS \
                        ON T.PSid = PS.id WHERE CourierId = '{}' AND Email = '{}' AND Datetime = '{}' \
                        LIMIT 1".format(email_kurir, email, datetime))
        result['query4'] = namedtuplefetchall(cursor)

        cursor.execute("SELECT * FROM COURIER WHERE Email = '{}'".format(email_kurir))
        result['query5'] = namedtuplefetchall(cursor)

        cursor.execute("SELECT RName, Rbranch, Amount, Note, Name, FoodName FROM TRANSACTION_FOOD TF INNER JOIN TRANSACTION_HISTORY TH \
                        ON TF.Email = TH.Email AND TF.Datetime = TH.Datetime \
                        INNER JOIN TRANSACTION_STATUS TS ON TH.TSid = TS.id \
                        WHERE TF.Email = '{}' AND TF.Datetime = '{}' LIMIT 1".format(email, datetime))
        result['query6'] = namedtuplefetchall(cursor)
    else:
        return HttpResponseForbidden("Forbidden")
    return render(request, 'read_detail_transaksi_kurir.html', result)

#[UPDATE] Transaksi Pemesanan (POV Kurir)
def update_transaksi_kurir(request, email, datetime):
    if request.COOKIES['user_type'] == 'courier':
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO SIREST") 
        cursor.execute("UPDATE TRANSACTION_HISTORY SET TSid = 'TS4' WHERE Email = '{}' AND Datetime = '{}'".format(email, datetime)) 
    else:
        return HttpResponseForbidden("Forbidden")
    return redirect("/read-transaksi-kurir")