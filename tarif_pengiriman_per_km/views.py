from django.db import connection, transaction
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.
def create(request):
    if request.COOKIES['user_type'] == 'admin':

        if request.method == "POST":
            with connection.cursor() as cursor:
                cursor.execute(
                        """
                            SELECT COUNT(*) FROM SIREST.DELIVERY_FEE_PER_KM
                        """
                ) 
                row = cursor.fetchone()

            id = f"DF{row[0]+1}"
            province = request.POST.get("provinsi")
            motorfee = request.POST.get("tarif_motor")
            carfee = request.POST.get("tarif_mobil")

            with transaction.atomic():
                with connection.cursor() as cursor:
                    try:
                        cursor.execute(f"""
                                INSERT INTO SIREST.DELIVERY_FEE_PER_KM
                                VALUES ('{id}', '{province}', '{motorfee}', '{carfee}')
                        """)

                        messages.success(request, "Tarif Pengiriman Berhasil Ditambah")
                
                        return redirect("tarif_pengiriman_per_km:read")
                    except Exception as e:
                        messages.info(request, e)   
            
        return render(request, 'tarif_pengiriman_per_km/create.html')

def read(request):
    context = {}

    with connection.cursor() as cursor:
        if request.COOKIES['user_type'] == 'admin':
            cursor.execute(
                f"""
                    SELECT * FROM SIREST.DELIVERY_FEE_PER_KM
                """
            )
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            transactions = [dict(zip(fields, row)) for row in rows]
            context['transactions'] = transactions

            return render(request, 'tarif_pengiriman_per_km/read.html', context=context)

def update(request, id):
    context = {}

    with connection.cursor() as cursor:
        if request.COOKIES['user_type'] == 'admin':
            cursor.execute(
                f"""
                    SELECT * FROM SIREST.DELIVERY_FEE_PER_KM
                    WHERE id = '{id}'
                """
            )
            fields = [field_name[0] for field_name in cursor.description]
            rows = cursor.fetchall()
            transactions = [dict(zip(fields, row)) for row in rows]
            context['transaction'] = transactions[0]

            if request.method == "POST":
                motorfee = request.POST.get('tarif_motor')
                carfee = request.POST.get('tarif_mobil')

                with transaction.atomic():
                    with connection.cursor() as cursor:
                        try:
                            cursor.execute(f"""
                                    UPDATE SIREST.DELIVERY_FEE_PER_KM
                                    SET motorfee = '{motorfee}', carfee = '{carfee}'
                                    WHERE id = '{id}'
                            """)
                    
                            messages.success(request, "Tarif Pengiriman Berhasil Diubah")
                            context['transaction']['motorfee'] = motorfee
                            context['transaction']['carfee'] = carfee

                            return redirect("tarif_pengiriman_per_km:read")

                        except Exception as e:
                            messages.info(request, e)

            return render(request, 'tarif_pengiriman_per_km/update.html', context=context)

def delete(request, id):
    if request.COOKIES['user_type'] == 'admin':
        with transaction.atomic():
            with connection.cursor() as cursor:
                try:
                    cursor.execute(f"""
                            DELETE FROM SIREST.DELIVERY_FEE_PER_KM
                            WHERE id = '{id}'
                    """)
            
                    messages.info(request, "Tarif pengiriman berhasil dihapus")

                except Exception as e:
                    messages.warning(request, "Tarif pengiriman tidak berhasil dihapus karena terdapat pelanggaran referential constraint")

        return redirect("tarif_pengiriman_per_km:read")