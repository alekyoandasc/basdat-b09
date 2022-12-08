from django.shortcuts import render, redirect
from django.db import connection
import psycopg2


# Create your views here.
def show_pengisian_alamat(request):
    conn = psycopg2.connect(
    host="localhost",
    database="tk4",
    user="postgres",
    password="Zakirobinale123",
    )

    cur = conn.cursor()
    cur.execute('SET SEARCH_PATH to sirest')
    cur.execute('SELECT DISTINCT province FROM delivery_fee_per_km')

    province = cur.fetchall()
    print(f'ini province {province[0][0]}')

    context = {
        'province' : province
    }

    cur.close()
    conn.close()

    return render(request, 'pengisian_alamat.html', context)

def post_pengisian_alamat(request):
    print(request.POST)
    data_jalan = request.POST.get('Jalan')
    print(data_jalan)
    data_kecamatan = request.POST.get('Kecamatan')
    print(data_kecamatan)
    data_kota = request.POST.get('Kota')
    print(data_kota)
    data_provinsi = request.POST.get('Provinsi')
    print(data_provinsi)

    request.session['data_jalan'] = data_jalan
    request.session['data_kecamatan'] = data_kecamatan
    request.session['data_kota'] = data_kota
    request.session['data_provinsi'] = data_provinsi

    return redirect('show_pemilihan_restoran')

def show_pemilihan_restoran(request):
    conn = psycopg2.connect(
    host="localhost",
    database="tk4",
    user="postgres",
    password="Zakirobinale123",
    )

    print(request.session.get('data_provinsi'))
    data_provinsi = request.session.get('data_provinsi')


    cur = conn.cursor()
    cur.execute('SET SEARCH_PATH to sirest')
    cur.execute(f"SELECT * FROM RESTAURANT WHERE province LIKE '{data_provinsi}%'")

    restaurant_data = cur.fetchall()

    context = {
        'restaurant_data' : restaurant_data
    }

    cur.close()
    conn.close()

    return render(request, 'pemilihan_restoran.html', context)

def show_pemilihan_makanan(request, rname, rbranch):
    print(rname)
    print(rbranch)

    conn = psycopg2.connect(
    host="localhost",
    database="tk4",
    user="postgres",
    password="Zakirobinale123",
    )

    cur = conn.cursor()
    cur.execute('SET SEARCH_PATH to sirest')
    cur.execute(f"SELECT foodname, price FROM food WHERE rname='{rname}' AND rbranch='{rbranch}'")

    makanan_data = cur.fetchall()

    context = {
        'makanan_data' : makanan_data
    }

    cur.close()
    conn.close()

    return render(request, 'pemilihan_makanan.html', context)

def show_daftar_pesanan(request):
    return render(request, 'daftar_pesanan.html')

def show_konfirmasi_pesanan(request):
    return render(request, 'konfirmasi_pesanan.html')

def show_ringkasan_pesanan(request):
    return render(request, 'ringkasan_pesanan.html')