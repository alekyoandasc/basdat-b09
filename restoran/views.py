from django.shortcuts import redirect, render
from django.db import connection, transaction

# Create your views here.
def read_daftar_restoran(request):
    # TODO: Filter semua restoran
    if request.COOKIES['user_type'] != 'restaurant':
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT RName, RBranch, Rating FROM SIREST.RESTAURANT"""
            )
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            restaurants = [dict(zip(fields, row)) for row in rows]
            context = {
                "restaurants": restaurants,
            }
        return render(request, "restoran/read_daftar_restoran.html", context)

def read_detail_restoran(request):
    # TODO: Filter restoran
    if request.COOKIES['user_type'] != 'restaurant':
        rname_get = request.GET.get("rname")
        rbranch_get = request.GET.get("rbranch")
        with connection.cursor() as cursor:
            cursor.execute(
                f"""
                SELECT DISTINCT * FROM SIREST.RESTAURANT R
                JOIN SIREST.RESTAURANT_CATEGORY RC
                ON R.RCategory = RC.Id
                WHERE R.RName='{rname_get}' AND R.RBranch='{rbranch_get}'
                """
            )
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            restaurant = [dict(zip(fields, row)) for row in rows][0]
            cursor.execute(
                f"""
                SELECT DISTINCT Day, StartHours, EndHours FROM SIREST.RESTAURANT_OPERATING_HOURS
                WHERE Name='{rname_get}' AND Branch='{rbranch_get}'
                """
            )
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            restaurant_oh = [dict(zip(fields, row)) for row in rows]

            restaurant["operating_hours"] = restaurant_oh

            cursor.execute(
                f"""
                SELECT DISTINCT PromoName FROM SIREST.RESTAURANT_PROMO
                JOIN SIREST.Promo ON PId=Id
                WHERE RName='{rname_get}' AND RBranch='{rbranch_get}'
                """
            )
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            promos = [dict(zip(fields, row)) for row in rows]

            restaurant["promos"] = promos
            context = {
                "restaurant": restaurant,
            }
        return render(request, "restoran/read_detail_restoran.html", context)

def read_menu_restoran(request):
    # TODO: Filter restoran
    context = {}
    if request.COOKIES['user_type'] != 'resto':
        rname_get = request.GET.get("rname")
        rbranch_get = request.GET.get("rbranch")
    else:
        email = request.COOKIES['user_email']
        with connection.cursor() as cursor:
            cursor.execute(
                f"""
                SELECT DISTINCT RName, RBranch FROM SIREST.RESTAURANT
                WHERE Email='{email}'
                """
            )
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            rdetail = [dict(zip(fields, row)) for row in rows][0]
            rname_get = rdetail["rname"]
            rbranch_get = rdetail["rbranch"]

    with connection.cursor() as cursor:
        cursor.execute(
            f"""
            SELECT * FROM SIREST.FOOD F
            JOIN SIREST.FOOD_CATEGORY FC
            ON F.FCategory = FC.Id
            WHERE F.RName='{rname_get}' AND F.RBranch='{rbranch_get}'
            """
        )
        fields = [field_name[0] for field_name in cursor.description]
        rows = cursor.fetchall()
        foods = [dict(zip(fields, row)) for row in rows]
        for i in range(len(foods)):
            cursor.execute(
                f"""
                SELECT Name FROM SIREST.FOOD_INGREDIENT
                JOIN SIREST.INGREDIENT ON Ingredient=Id
                WHERE RName='{rname_get}' AND RBranch='{rbranch_get}' AND FoodName='{foods[i]["foodname"]}'
                """
            )
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            ingredients = [dict(zip(fields, row)) for row in rows][0]["name"]

            foods[i]["ingredients"] = ingredients
        context = {
            "rname": rname_get,
            "rbranch": rbranch_get,
            "foods": foods,
            "role_user": request.COOKIES['user_type']
        }

    return render(request, "restoran/read_menu_restoran.html", context=context)

def create_makanan(request, rname, rbranch):
    if request.method == "POST":
        # TODO: Filter restoran, validasi data dan simpan makanan
        return redirect("restoran:read_menu_restoran")
    return render(request, "restoran/create_makanan.html")

def update_makanan(request):
    if request.method == "POST":
        # TODO: Filter makanan, validasi data dan simpan makanan
        return redirect("restoran:read_menu_restoran")
    return render(request, "restoran/update_makanan.html")

def delete_makanan(request):
    # TODO: Filter dan delete makanan
    if request.method == "POST":
        return redirect("restoran:read_menu_restoran")