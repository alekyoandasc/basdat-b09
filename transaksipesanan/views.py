from django.shortcuts import render

# Create your views here.
def show_pengisian_alamat(request):
    return render(request, 'pengisian_alamat.html')

def show_pemilihan_restoran(request):
    return render(request, 'pemilihan_restoran.html')

def show_pemilihan_makanan(request):
    return render(request, 'pemilihan_makanan.html')