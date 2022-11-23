from django.shortcuts import redirect, render

# Create your views here.
def read_daftar_restoran(request):
    # TODO: Filter semua restoran
    return render(request, "restoran/read_daftar_restoran.html")

def read_detail_restoran(request, rname, rbranch):
    # TODO: Filter restoran
    return render(request, "restoran/read_detail_restoran.html")

def read_menu_restoran(request, rname, rbranch):
    # TODO: Filter restoran
    return render(request, "restoran/read_menu_restoran.html")

def create_makanan(request, rname, rbranch):
    if request.method == "POST":
        # TODO: Filter restoran, validasi data dan simpan makanan
        return redirect("restoran:read_menu_restoran", rname="kfc", rbranch="depok")
    return render(request, "restoran/create_makanan.html")

def update_makanan(request, rname, rbranch, fname):
    if request.method == "POST":
        # TODO: Filter makanan, validasi data dan simpan makanan
        return redirect("restoran:read_menu_restoran", rname="kfc", rbranch="depok")
    return render(request, "restoran/update_makanan.html")

def delete_makanan(request, rname, rbranch, fname):
    # TODO: Filter dan delete makanan
    if request.method == "POST":
        return redirect("restoran:read_menu_restoran", rname="kfc", rbranch="depok")