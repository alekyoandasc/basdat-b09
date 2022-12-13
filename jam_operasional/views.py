from django.shortcuts import render, redirect
from django.db import connection, transaction
from django.contrib import messages
from restopay.utils import *

# Create your views here.
def create_jam_operasional(request):
      if request.COOKIES['user_type'] == 'resto':
            if request.method == "POST":
                  with connection.cursor() as cursor:
                        cursor.execute("SET SEARCH_PATH TO SIREST")
                        cursor.execute("""
                              SELECT COUNT(*) FROM RESTAURANT_OPERATING_HOURS;
                        """)
                        row = cursor.fetchone()
                  
                  name = f"{row[0]+1}"
                  branch = f"{row[0]+1}"
                  day = request.POST.get("hari")
                  starthours = request.POST.get("jam_buka")
                  endhours = request.POST.get("jam_tutup")

                  with transaction.atomic():
                        with connection.cursor() as cursor:
                              try:
                                    cursor.execute("SET SEARCH_PATH TO SIREST")
                                    cursor.execute(f"""
                                          INSERT INTO SIREST.RESTAURANT_OPERATING_HOURS
                                          VALUES ('{name}', '{branch}', '{day}', '{starthours}', '{endhours}');
                                    """)
                                    messages.succes(request, "Jadwal Restoran Berhasil DIbuat")
                                    return redirect("jam_operasional:read")
                              except Exception as e:
                                    messages.info(request, e)
            return render(request, 'create_jam_operasional.html')


def read_jam_operasional(request):
      result = {}
      with connection.cursor() as cursor:

            if request.COOKIES.get('user_type') == 'resto':
            # with connection.cursor() as cursor:
                  cursor.execute("SET SEARCH_PATH TO SIREST")
                  cursor.execute("""
                        SELECT * 
                        FROM RESTAURANT_OPERATING_HOURS; 
                  """)
                  # result['query1'] = namedtuplefetchall(cursor)
                  fields = [field_name[0] for field_name in cursor.description]
                  rows = cursor.fetchall()
                  transactions = [dict(zip(fields, row)) for row in rows]
                  result['transactions'] = transactions


            return render(request, 'read_jam_operasional.html', result)

def update_jam_operasional(request):
      context = {}
      with connection.cursor() as cursor:
            if request.COOKIES.get('user_type') == 'resto':
            # with connection.cursor() as cursor:
                  cursor.execute("SET SEARCH_PATH TO SIREST")
                  cursor.execute(f"""
                        SELECT * 
                        FROM RESTAURANT_OPERATING_HOURS
                        ;
                  """)
                  fields = [field_name[0] for field_name in cursor.description]
                  rows = cursor.fetchall()
                  transactions = [dict(zip(fields, row)) for row in rows]
                  context['transaction'] = transactions[0]

                  if request.method == "POST":
                        starthours = request.POST.get('jam_buka')
                        endhours = request.POST.get('jam_tutup')

                        with transaction.atomic():
                              with connection.cursor() as cursor:
                                    try:
                                          cursor.execute("SET SEARCH_PATH TO SIREST")
                                          cursor.execute(f"""
                                                UPDATE RESTAURANT_OPERATING_HOURS
                                                SET starthours = '{starthours}', endhours = '{endhours}'
                                                ;
                                          """)
                                          messages.success(request, "Jam operasional berhasil diubah")
                                          context['transaction']['starthours'] = starthours
                                          context['transaction']['endhours'] = endhours

                                          return redirect("jam_operasional:read")
                                    except Exception as e:
                                          messages.info(request, e)
                  return render(request, 'update_jam_operasional.html', context=context)

def delete_jam_operasional(request):
      if request.COOKIES['user_type'] == 'resto':
            with transaction.atomic():
                  with connection.cursor() as cursor:
                        try:
                              cursor.execute("SET SEARCH_PATH TO SIREST")
                              cursor.execute(f"""
                                    DELETE FROM RESTAURANT_OPERATING_HOURS
                                    
                              """)
                              messages.info(request, "Jadwal Operasional berhasil dihapus")
                        except Exception as e:
                              messages.warning(request, "Jam operasiona tidak berhasil dihapus")
            return redirect("jam_operasional:read")
