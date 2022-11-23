from django.shortcuts import redirect, render

# Create your views here.
def create(request):
    if request.method == "POST":
        # TODO: Validasi data dan simpan
        return redirect("tarif_pengiriman_per_km:read")
    return render(request, 'tarif_pengiriman_per_km/create.html')

def read(request):
    return render(request, 'tarif_pengiriman_per_km/read.html')

def update(request, id):
    if request.method == "POST":
        # TODO: Validasi data dan simpan
        return redirect("tarif_pengiriman_per_km:read")
    return render(request, 'tarif_pengiriman_per_km/update.html')

def delete(request, id):
    if request.method == "POST":
        # TODO: Hapus data
        return redirect("tarif_pengiriman_per_km:read")