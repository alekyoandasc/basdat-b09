from django.shortcuts import render, redirect
from biru.forms import CreateKategoriRestoForm, CreateBahanMakananForm
from django.http.response import HttpResponseRedirect

# Create your views here.
def create_kategori_restoran(request):
    form = CreateKategoriRestoForm(request.POST)
    return render(request, 'create_kategori_restoran.html',{'form':form})

def read_kategori_restoran(request):
    result = ()
    request.session['context_kategori'] = result
    if (len(request.session['context_kategori']) == 0):
        result = ("Indonesia", "India", "Jepang")
        request.session['context_kategori'] = result
    else:
        result = request.session['context_kategori']
    return render(request, 'read_kategori_restoran.html', {'result':result})

def delete_kategori_restoran(request, nama_kategori):
    if nama_kategori in request.session['context_kategori']:
        result = request.session['context_kategori']
        result.remove(nama_kategori)
        request.session['context_kategori'] = result
    return redirect('/read-kategori-restoran')


def create_bahan_makanan(request):
    form = CreateBahanMakananForm(request.POST)
    return render(request, 'create_bahan_makanan.html', {'form':form})

def read_bahan_makanan(request):
    result = ()
    request.session['context_bahan'] = result
    if (len(request.session['context_bahan']) == 0):
        result = ("Gula", "Garam")
        request.session['context_bahan'] = result
    else:
        result = request.session['context_bahan']
    return render(request, 'read_bahan_makanan.html', {'result':result})

def delete_bahan_makanan(request, nama_bahan):
    if nama_bahan in request.session['context_bahan']:
        result = request.session['context_bahan']
        result.remove(nama_bahan)
        print(result)
        request.session['context_bahan'] = result
    return redirect('/read-bahan-makanan')

def read_transaksi_kurir(request):
    result = {}
    return render(request, 'read_transaksi_kurir.html', result)

def read_detail_transaksi_kurir(request):
    result = {}
    return render(request, 'read_detail_transaksi_kurir.html', result)
