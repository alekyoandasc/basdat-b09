from django.shortcuts import render, redirect
from django.db import connection
import datetime
import psycopg2


# Create your views here.
def show_pengisian_alamat(request):
    with connection.cursor() as cur:
        cur.execute('SET SEARCH_PATH to sirest')
        cur.execute('SELECT DISTINCT province FROM delivery_fee_per_km')

        province = cur.fetchall()
        print(f'ini province {province[0][0]}')

        context = {
            'province' : province
        }

        cur.close()

    return render(request, 'pengisian_alamat.html', context)

def post_pengisian_alamat(request):
    data_jalan = request.POST.get('Jalan')
    data_kecamatan = request.POST.get('Kecamatan')
    data_kota = request.POST.get('Kota')
    data_provinsi = request.POST.get('Provinsi')
    
    request.session['data_jalan'] = data_jalan
    request.session['data_kecamatan'] = data_kecamatan
    request.session['data_kota'] = data_kota
    request.session['data_provinsi'] = data_provinsi
    print(request.session.get('data_jalan'))

    return redirect('show_pemilihan_restoran')

def show_pemilihan_restoran(request):
    with connection.cursor() as cur:
        # print(request.session.get('data_provinsi'))
        data_provinsi = request.session.get('data_provinsi')
        print(data_provinsi)
        

        cur.execute('SET SEARCH_PATH to sirest')
        cur.execute(f"SELECT * FROM RESTAURANT WHERE province = '{data_provinsi}'")

        restaurant_data = cur.fetchall()

        context = {
            'restaurant_data' : restaurant_data
        }


    return render(request, 'pemilihan_restoran.html', context)

def show_pemilihan_makanan(request, rname, rbranch):
    print(rname)
    print(rbranch)

    with connection.cursor() as cur:
        request.session['rname'] = str(rname)
        request.session['rbranch'] = str(rbranch)
        cur.execute('SET SEARCH_PATH to sirest')
        cur.execute(f"SELECT foodname, price FROM food WHERE rname='{rname}' AND rbranch='{rbranch}'")

        makanan_data = cur.fetchall()
        request.session['makanan_data'] = makanan_data
        print(makanan_data)

        cur.execute("SELECT * FROM payment_method")

        metode_pembayaran_data = cur.fetchall()

        context = {
            'makanan_data' : makanan_data,
            'metode_pembayaran_data' : metode_pembayaran_data,
        }


    return render(request, 'pemilihan_makanan.html', context)

def post_pemilihan_makanan(request):
    print(request.POST)
    
    metode_pengantaran = request.POST.get('Pengantaran')
    metode_pembayaran = request.POST.get('Pembayaran')

    request.session['pengantaran'] = metode_pengantaran
    request.session['pembayaran'] = metode_pembayaran

    daftar_pesanan = []

    makanan_data = request.session.get('makanan_data')

    total_harga_pesanan = 0
    for key, data in request.POST.items():
        for makanan in makanan_data:
            if key == makanan[0] and int(data) != 0:
                nama_makanan = makanan[0]
                jumlah = int(data)
                harga_satuan = int(makanan[1])
                total_harga = jumlah * harga_satuan
                total_harga_pesanan += total_harga
                catatan = request.POST.get(nama_makanan + 'catataninput')
                daftar_pesanan.append((nama_makanan, jumlah, harga_satuan, total_harga, catatan))
                break
            
    # print(daftar_pesanan)
    request.session['daftar_pesanan'] = daftar_pesanan
    request.session['total_harga_pesanan'] = total_harga_pesanan

    return redirect('show_daftar_pesanan')

def show_daftar_pesanan(request):
    daftar_pesanan = request.session.get('daftar_pesanan')
    total_harga_pesanan = request.session.get('total_harga_pesanan')
    metode_pengantaran = request.session.get('pengantaran')
    metode_pembayaran = request.session.get('pembayaran')

    context = {
        'daftar_pesanan' : daftar_pesanan,
        'total_harga_pesanan' : total_harga_pesanan,
        'metode_pengantaran' : metode_pengantaran,
        'metode_pembayaran' : metode_pembayaran,
    }

    return render(request, 'daftar_pesanan.html', context)

def show_konfirmasi_pesanan(request):
    current_time = datetime.datetime.now()
    current_time = current_time + datetime.timedelta(hours=7)

    data_jalan = request.session.get('data_jalan')
    data_kecamatan = request.session.get('data_kecamatan')
    data_kota = request.session.get('data_kota')
    data_provinsi = request.session.get('data_provinsi')
    nama_restoran = request.session.get('rname')
    nama_branch = request.session.get('rbranch')
    daftar_pesanan = request.session.get('daftar_pesanan')
    total_harga_pesanan = request.session.get('total_harga_pesanan')
    metode_pengantaran = request.session.get('pengantaran')
    metode_pembayaran = request.session.get('pembayaran')

    with connection.cursor() as cur:
        cur.execute('SET SEARCH_PATH to sirest')
        cur.execute(f"SELECT * FROM restaurant where rname = '{nama_restoran}' AND rbranch = '{nama_branch}'")

        data_restoran = cur.fetchall()
        jalan_restoran = data_restoran[0][4]
        kecamatan_restoran = data_restoran[0][5]
        kota_restoran = data_restoran[0][6]
        provinsi_restoran = data_restoran[0][7]

    context = {
        'data_jalan' : data_jalan,
        'data_kecamatan' : data_kecamatan,
        'data_kota' : data_kota,
        'data_provinsi' : data_provinsi,
        'nama_restoran' : nama_restoran,
        'nama_branch' : nama_branch,
        'daftar_pesanan' : daftar_pesanan,
        'total_harga_pesanan' : total_harga_pesanan,
        'metode_pengantaran' : metode_pengantaran,
        'metode_pembayaran' : metode_pembayaran,
        'current_time' : current_time,
        'jalan_restoran' : jalan_restoran,
        'kecamatan_restoran' : kecamatan_restoran,
        'kota_restoran' : kota_restoran,
        'provinsi_restoran' : provinsi_restoran,
    }

    return render(request, 'konfirmasi_pesanan.html', context)

def show_ringkasan_pesanan(request):
    data_jalan = request.session.get('data_jalan')
    data_kecamatan = request.session.get('data_kecamatan')
    data_kota = request.session.get('data_kota')
    data_provinsi = request.session.get('data_provinsi')
    nama_restoran = request.session.get('rname')
    nama_branch = request.session.get('rbranch')
    daftar_pesanan = request.session.get('daftar_pesanan')
    total_harga_pesanan = request.session.get('total_harga_pesanan')
    metode_pengantaran = request.session.get('pengantaran')
    metode_pembayaran = request.session.get('pembayaran')

    with connection.cursor() as cur:
        cur.execute('SET SEARCH_PATH to sirest')
        cur.execute(f"SELECT * FROM restaurant where rname = '{nama_restoran}' AND rbranch = '{nama_branch}'")

        data_restoran = cur.fetchall()
        jalan_restoran = data_restoran[0][4]
        kecamatan_restoran = data_restoran[0][5]
        kota_restoran = data_restoran[0][6]
        provinsi_restoran = data_restoran[0][7]

    context = {
        'data_jalan' : data_jalan,
        'data_kecamatan' : data_kecamatan,
        'data_kota' : data_kota,
        'data_provinsi' : data_provinsi,
        'nama_restoran' : nama_restoran,
        'nama_branch' : nama_branch,
        'daftar_pesanan' : daftar_pesanan,
        'total_harga_pesanan' : total_harga_pesanan,
        'metode_pengantaran' : metode_pengantaran,
        'metode_pembayaran' : metode_pembayaran,
        'jalan_restoran' : jalan_restoran,
        'kecamatan_restoran' : kecamatan_restoran,
        'kota_restoran' : kota_restoran,
        'provinsi_restoran' : provinsi_restoran,
    }


    return render(request, 'ringkasan_pesanan.html', context)