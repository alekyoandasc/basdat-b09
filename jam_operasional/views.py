from django.shortcuts import render
from django.db import connection
from restopay.utils import *

# Create your views here.
def create_jam_operasional(request):
      if request.session.get('role') == "":
            role = request.session.get('role')
            # with connection.cursor() as c:
            #       c.execute("")
            #       c.execute("")
            # response = {'hasil' : hasil}
            # return render(request, 'lihat_saldo.html', response)
      role = ""
      return render(request, 'create_jam_operasional.html', {'role':role})

def read_jam_operasional(request):
      result = {}
      if request.COOKIES.get('user_type') == 'resto':
            with connection.cursor() as cursor:
                  cursor.execute("SET SEARCH_PATH TO SIREST")
                  cursor.execute("""
                        SELECT DISTINCT day, starthours, endhours 
                        FROM RESTAURANT_OPERATING_HOURS; 
                  """)
                  result['query1'] = namedtuplefetchall(cursor)

      return render(request, 'read_jam_operasional.html', result)

def update_jam_operasional(request):
      result = {}
      if request.COOKIES.get('user_type') == 'resto':
            with connection.cursor() as cursor:
                  cursor.execute("SET SEARCH_PATH TO SIREST")
                  cursor.execute("""
                        SELECT DISTINCT day
                        FROM RESTAURANT_OPERATING_HOURS LIMIT 1;
                  """)
                  result['query'] = namedtuplefetchall(cursor)

      return render(request, 'update_jam_operasional.html', result)