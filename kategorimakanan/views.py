from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
import psycopg2
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def show_kategori_makanan(request):
      if request.COOKIES['user_type'] == 'admin':
            with connection.cursor() as cur:
                  cur.execute('SET SEARCH_PATH to sirest')
                  cur.execute('SELECT * FROM FOOD_CATEGORY FC WHERE EXISTS (SELECT * FROM FOOD F WHERE FC.id = F.Fcategory)')

                  kategorimakanan_data_referenced = cur.fetchall()
                  print(kategorimakanan_data_referenced)
                  
                  cur.execute('SELECT * FROM FOOD_CATEGORY FC WHERE NOT EXISTS (SELECT * FROM FOOD F WHERE FC.id = F.Fcategory)')
                  kategorimakanan_data_not_referenced = cur.fetchall()

                  context = {
                        'kategorimakanan_data_referenced' : kategorimakanan_data_referenced,
                        'kategorimakanan_data_not_referenced' : kategorimakanan_data_not_referenced
                  }

            return render(request, 'kategori_makanan.html', context)

      return HttpResponse('Access denied')

def show_create_kategori_makanan_page(request):

    return render(request, 'create_kategori_makanan.html')

def add_kategori_makanan(request):
      if request.POST:
            with connection.cursor() as cur:
                  nama_kategori = request.POST.get('name')

                  # cur = conn.cursor()
                  cur.execute('SET SEARCH_PATH to sirest')

                  cur.execute('SELECT MAX(ID) FROM food_category')

                  max_id = cur.fetchone()
                  print(nama_kategori)
                  print(max_id[0])

                  new_id = int(max_id[0]) + 1

                  cur.execute(f"INSERT INTO food_category VALUES ({new_id}, '{nama_kategori}')")

                  connection.commit()
        
      return redirect('show_kategori_makanan')

def delete_kategori_makanan(request, id):
      if request.COOKIES['user_type'] == 'admin':
            if request.POST:
                  with connection.cursor() as cur:
                        cur.execute('SET SEARCH_PATH to sirest')
                  
                        print(f"DELETE FROM food_category WHERE id = {id}")
                        cur.execute(f"DELETE FROM food_category FC WHERE FC.id = '6'")

                        connection.commit()
            
            return redirect('show_kategori_makanan')

      return HttpResponse('Access denied')