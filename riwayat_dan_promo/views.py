from django.shortcuts import render, redirect
from riwayat_dan_promo.forms import *
from riwayat_dan_promo.models import *
from django.db import connection, transaction
# Create your views here.



def fetch_transaksi():
    with connection.cursor() as cursor:
        cursor.execute(
            """
                SELECT * 
                FROM SIREST.transaction 
            """
        )
        rows = cursor.fetchall()

        return rows

def riwayat_transaksi(request):
    daftar_transaksi = fetch_transaksi()
    
    context = {
        'daftar_transaksi': daftar_transaksi
    }
    return render(request, 'riwayat_transaksi.html', context)

def detail_transaksi(request, id):
    return render(request, 'detail_transaksi.html') 

def nilai_transaksi(request, id):
    return render(request, 'nilai_transaksi.html') 

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