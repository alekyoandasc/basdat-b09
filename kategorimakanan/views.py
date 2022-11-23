from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def show_kategori_makanan(request):
      kategori_makanan = KategoriMakanan.objects.all().values()
      context = {
            'kategori' : kategori_makanan,
      }
      return render(request, 'kategori_makanan.html', context)

def show_create_kategori_makanan_page(request):
    return render(request, 'create_kategori_makanan.html')

# def add_kategori_makanan(request):
#     if request.POST:
#         kategori_makanan_form = KategoriMakananForm(request.POST)
#         # print(f'{form.is_valid()}')
#         if kategori_makanan_form.is_valid():
#             kategori_makanan_form.save()
#             return redirect('/')

# def delete_kategori_makanan(request, kategori_id):
#       kategori = KategoriMakananCustom.objects.get(id=kategori_id)
#       kategori.delete()
#       return redirect('show_kategori_makanan')