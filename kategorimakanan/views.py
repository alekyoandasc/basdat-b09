from django.shortcuts import render, redirect
from kategorimakanan.models import *
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required(login_url='pengguna/login')
def show_kategori_makanan(request):
      kategori_makanan = KategoriMakanan.objects.all().values()
      context = {
            'kategori' : kategori_makanan,
      }
      return render(request, 'kategori_makanan.html', context)

def show_create_kategori_makanan_page(request):
    context = {
        'form' : KategoriMakananForm,
    }

    return render(request, 'create_kategori_makanan.html', context)

def add_kategori_makanan(request):
    if request.POST:
        kategori_makanan_form = KategoriMakananForm(request.POST)
        # print(f'{form.is_valid()}')
        if kategori_makanan_form.is_valid():
            kategori_makanan_form.save()
            return redirect('/')

def delete_kategori_makanan(request, kategori_id):
      kategori = KategoriMakanan.objects.get(id=kategori_id)
      kategori.delete()
      return redirect('show_kategori_makanan')