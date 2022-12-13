from django.shortcuts import render, redirect
from django.db import connection
import datetime
import psycopg2


# Create your views here.
def show_pengisian_alamat(request):
    print(request.COOKIES)
    if request.COOKIES['user_type'] == 'customer':
        with connection.cursor() as cur:
            # cur.execute('SET SEARCH_PATH to sirest')
            cur.execute('SELECT DISTINCT province FROM sirest.delivery_fee_per_km')

            province = cur.fetchall()
            print(f'ini province {province[0][0]}')

            context = {
                'province' : province
            }

            cur.close()

        return render(request, 'pengisian_alamat.html', context)

    return redirect('/')

def post_pengisian_alamat(request):
    if request.COOKIES['user_type'] == 'customer':
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

    return redirect('/')

def show_pemilihan_restoran(request):
    if request.COOKIES['user_type'] == 'customer':
        with connection.cursor() as cur:
            # print(request.session.get('data_provinsi'))
            data_provinsi = request.session.get('data_provinsi')
            print(data_provinsi)
            
            print(f"select * from sirest.restaurant r left outer join (select * from sirest.restaurant_promo rp where current_date >= start and current_date <= endpromo) \
                as rp on r.rname = rp.rname and r.rbranch=rp.rbranch where r.province='{data_provinsi}'")
            # cur.execute('SET SEARCH_PATH to sirest')
            cur.execute(f"select * from sirest.restaurant r left outer join (select * from sirest.restaurant_promo rp where current_date >= start and current_date <= endpromo) \
                as rp on r.rname = rp.rname and r.rbranch=rp.rbranch where r.province='{data_provinsi}'")

            # cur.execute(f"SELECT * FROM restaurant_promo where rname='{rname}' and rbranch='{rbranch}' and current_date >= start and current_date <= endpromo")

            restaurant_data = cur.fetchall()
            print(restaurant_data)

            context = {
                'restaurant_data' : restaurant_data
            }


        return render(request, 'pemilihan_restoran.html', context)

    return redirect('/')

def show_pemilihan_makanan(request, rname, rbranch):
    print(rname)
    print(rbranch)
    if request.COOKIES['user_type'] == 'customer':

        with connection.cursor() as cur:
            request.session['rname'] = str(rname)
            request.session['rbranch'] = str(rbranch)
            # cur.execute('SET SEARCH_PATH to sirest')
            cur.execute(f"SELECT foodname, price FROM sirest.food WHERE rname='{rname}' AND rbranch='{rbranch}'")

            makanan_data = cur.fetchall()
            request.session['makanan_data'] = makanan_data
            print(makanan_data)
            


            cur.execute("SELECT * FROM sirest.payment_method")

            metode_pembayaran_data = cur.fetchall()

            context = {
                'makanan_data' : makanan_data,
                'metode_pembayaran_data' : metode_pembayaran_data,
            }


        return render(request, 'pemilihan_makanan.html', context)

    return redirect('')

def post_pemilihan_makanan(request):
    print(request.COOKIES['user_type'])
    
    if request.COOKIES['user_type'] == 'customer':

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

    return redirect('/')

def show_daftar_pesanan(request):
    if request.COOKIES['user_type'] == 'customer':
        rname = request.session.get('rname')
        rbranch = request.session.get('rbranch')
        data_provinsi = request.session.get('data_provinsi')
        with connection.cursor() as cur:
            # cur.execute("SET SEARCH_PATH TO SIREST")
            cur.execute(f"SELECT * FROM sirest.restaurant_promo, sirest.promo where restaurant_promo.pid = promo.id and rname='{rname}' and rbranch='{rbranch}' and current_date >= start and current_date <= endpromo")

            data_promo = cur.fetchone()
            request.session['data_promo'] = data_promo
            print(data_promo)

            cur.execute(f"SELECT * FROM sirest.DELIVERY_FEE_PER_KM where province='{data_provinsi}'")

            data_delivery = cur.fetchone()

            # print(data_delivery)
            # request.session['data_delivery'] = data_delivery


        daftar_pesanan = request.session.get('daftar_pesanan')
        total_harga_pesanan = request.session.get('total_harga_pesanan')
        metode_pengantaran = request.session.get('pengantaran')
        metode_pembayaran = request.session.get('pembayaran')

        print(daftar_pesanan)

        if metode_pengantaran == 'Motor':
            total_pengantaran = data_delivery[2]
        elif metode_pengantaran == 'Mobil':
            total_pengantaran = data_delivery[3]

        if data_promo:
            total_diskon = total_harga_pesanan * (data_promo[-1] / 100)
            total_biaya = total_harga_pesanan - total_diskon + total_pengantaran
        else:
            total_diskon = 0
            total_biaya = total_harga_pesanan + total_pengantaran


        request.session['total_pengantaran'] = total_pengantaran
        request.session['total_diskon'] = total_diskon
        request.session['total_biaya'] = total_biaya

        context = {
            'total_diskon' : total_diskon,
            'total_biaya' : total_biaya,
            'total_pengantaran' : total_pengantaran,
            'daftar_pesanan' : daftar_pesanan,
            'total_harga_pesanan' : total_harga_pesanan,
            'metode_pengantaran' : metode_pengantaran,
            'metode_pembayaran' : metode_pembayaran,
        }

        return render(request, 'daftar_pesanan.html', context)

    return redirect('/')

def show_konfirmasi_pesanan(request):
    if request.COOKIES['user_type'] == 'customer':

        current_time = datetime.datetime.now()
        current_time = current_time + datetime.timedelta(hours=7)
        request.session['time_pesanan'] = current_time

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
        total_diskon = request.session.get('total_diskon')
        total_biaya = request.session.get('total_biaya')
        user_name = request.COOKIES['user_name']

        with connection.cursor() as cur:
            # cur.execute('SET SEARCH_PATH to sirest')
            cur.execute(f"SELECT * FROM sirest.restaurant where rname = '{nama_restoran}' AND rbranch = '{nama_branch}'")

            data_restoran = cur.fetchall()
            jalan_restoran = data_restoran[0][4]
            kecamatan_restoran = data_restoran[0][5]
            kota_restoran = data_restoran[0][6]
            provinsi_restoran = data_restoran[0][7]

        context = {
            'user_name' : user_name,
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
            'total_diskon' : total_diskon,
            'total_biaya' : total_biaya,
        }

        return render(request, 'konfirmasi_pesanan.html', context)

    return redirect('/')

def show_ringkasan_pesanan(request):
    if request.COOKIES['user_type'] == 'customer':
        user_email = request.COOKIES['user_email']
        time_pesanan = request.session.get('time_pesanan')
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
        total_diskon = request.session.get('total_diskon')
        total_biaya = request.session.get('total_biaya')
        total_pengantaran = request.session.get('total_pengantaran')
        
        print('time pesanan : ')
        print(time_pesanan)
        with connection.cursor() as cur:
            # cur.execute('SET SEARCH_PATH to sirest')
            cur.execute(f"SELECT * FROM sirest.restaurant where rname = '{nama_restoran}' AND rbranch = '{nama_branch}'")

            data_restoran = cur.fetchall()
            jalan_restoran = data_restoran[0][4]
            kecamatan_restoran = data_restoran[0][5]
            kota_restoran = data_restoran[0][6]
            provinsi_restoran = data_restoran[0][7]
            
            # Insert into transaction
            cur.execute(f"INSERT into sirest.TRANSACTION values('{user_email}', TIMESTAMP '{time_pesanan}', '{data_jalan}', \
                '{data_kecamatan}', '{data_kota}', '{data_provinsi}', {total_harga_pesanan}, {total_diskon}, {total_pengantaran}, {total_biaya + total_pengantaran}, 4, 'PM2', 'PS2', 'DF02', 'jzinckep@yolasite.com');")

            # Insert into transaction_food
            for pesanan in daftar_pesanan:
                cur.execute(f"INSERT into sirest.TRANSACTION_FOOD values('{user_email}', TIMESTAMP '{time_pesanan}', '{nama_restoran}', '{nama_branch}', '{pesanan[0]}', '{pesanan[1]}', '{pesanan[-1]}')")

            cur.execute(f"INSERT into sirest.TRANSACTION_HISTORY values('{user_email}', TIMESTAMP '{time_pesanan}', 'TS1', TIMESTAMP '{time_pesanan}')")
            
        user_name = request.COOKIES['user_name']

        context = {
            'user_name' : user_name,
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
            'total_diskon' : total_diskon,
            'total_biaya' : total_biaya,
            'total_pengantaran' : total_pengantaran,
        }


        return render(request, 'ringkasan_pesanan.html', context)

    return redirect('/')

def show_cek_pesanan_berlangsung(request):
    if request.COOKIES['user_type'] == 'customer':
        user_email = request.COOKIES['user_email']

        with connection.cursor() as cur:
            cur.execute(f"SELECT * FROM sirest.transaction t, sirest.transaction_history th WHERE t.email = '{user_email}' \
                and t.datetime=th.datetime;")

            pesanan_data = cur.fetchall()

            print(pesanan_data)

            # time_pesanan = pesanan_data[0][1]

            # cur.execute(f"SELECT * FROM TRANSACTION_FOOD WHERE datetime=TIMESTAMP'{time_pesanan}'")

            # rdata = cur.fetchone()
            


        context = {
            'pesanan_data' : pesanan_data
        }
        return render(request, 'cek_pesanan_berlangsung.html', context)

    return redirect('/')

def show_pesanan(request, datetime):
    if request.COOKIES['user_type'] == 'customer':

        with connection.cursor() as cur:
            cur.execute(f"SELECT * FROM sirest.transaction t, sirest.transaction_history th WHERE t.email=th.email and t.datetime= TIMESTAMP'{datetime}'")

            data_pesanan_berlangsung = cur.fetchone()
            print(data_pesanan_berlangsung)

            cur.execute(f"SELECT * FROM sirest.transaction t, sirest.transaction_food tf WHERE t.email = tf.email and tf.datetime= TIMESTAMP'{datetime}'")

            data_makanan = cur.fetchall()
            rname = data_makanan[0][17]
            rbranch = data_makanan[0][18]
            print(data_makanan)

            cur.execute(f"SELECT street, district, city, province FROM sirest.restaurant WHERE rname='{rname}' and rbranch='{rbranch}'")
            data_restoran = cur.fetchone()
            jalan_restoran = data_restoran[0]
            kecamatan_restoran = data_restoran[1]
            kota_restoran = data_restoran[2]
            provinsi_restoran = data_restoran[3]

            cur.execute(f"SELECT foodname, note FROM sirest.TRANSACTION_FOOD WHERE datetime = TIMESTAMP '{datetime}'")

            daftar_pesanan = cur.fetchall()
            

        user_name = request.COOKIES['user_name']
        data_jalan = data_pesanan_berlangsung[2]
        data_kecamatan = data_pesanan_berlangsung[3]
        data_kota = data_pesanan_berlangsung[4]
        data_provinsi = data_pesanan_berlangsung[5]

        total_harga_pesanan = data_pesanan_berlangsung[5]
        total_diskon = data_pesanan_berlangsung[7]
        total_pengantaran = data_pesanan_berlangsung[6]
        total_biaya = data_pesanan_berlangsung[9]
        metode_pembayaran = data_pesanan_berlangsung[11]

        context = {
            'user_name': user_name,
            'data_jalan' : data_jalan,
            'data_kecamatan' : data_kecamatan,
            'data_kota' : data_kota,
            'data_provinsi' : data_provinsi,
            'rname' : rname,
            'rbranch' : rbranch,
            'total_harga_pesanan' : total_harga_pesanan,
            'total_diskon' : total_diskon,
            'total_pengantaran' : total_pengantaran,
            'total_biaya' : total_biaya,
            'metode_pembayaran' : metode_pembayaran,
            'data_pesanan_berlangsung' : data_pesanan_berlangsung,
            'jalan_restoran' : jalan_restoran,
            'kecamatan_restoran' : kecamatan_restoran,
            'kota_restoran' : kota_restoran,
            'provinsi_restoran' : provinsi_restoran,
            'daftar_pesanan' : daftar_pesanan,
        }

        return render(request, 'pesanan_berlangsung.html', context)

    return redirect('/')