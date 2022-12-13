from django.shortcuts import redirect, render
from django.db import connection, transaction

# Create your views here.
def read_daftar_restoran(request):
    # TODO: Filter semua restoran
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT RName FROM SIREST.RESTAURANT"""
        )
        fields = [field_name[0] for field_name in cursor.description]
        rows = cursor.fetchall()
        restaurants = [dict(zip(fields, row)) for row in rows]
        print(restaurants)
        context = {
            "restaurants": restaurants,
        }
    return render(request, "restoran/read_daftar_restoran.html", context)

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