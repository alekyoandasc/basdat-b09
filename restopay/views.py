from django.shortcuts import render, redirect
# from django.shortcuts import connection
from django.db import connection, transaction
from collections import namedtuple
from django.contrib import messages
from .utils import *


# Create your views here.

def lihat_saldo(request):
      result = {}

      if request.COOKIES['user_type'] == 'admin' or request.COOKIES['user_type'] == 'resto' or request.COOKIES['user_type'] == 'customer' or request.COOKIES['user_type'] == 'courier':
            with connection.cursor() as cursor:
                  cursor.execute("SET SEARCH_PATH TO SIREST")
                  cursor.execute("""
                        SELECT restopay FROM TRANSACTION_ACTOR LIMIT 1;
                  """)
                  result['query1'] = namedtuplefetchall(cursor)

      return render(request, 'lihat_saldo.html', result)

def add_saldo(request):
      result = {}

      with connection.cursor() as cursor:
            cursor.execute("SET SEARCH_PATH TO SIREST")
            cursor.execute("SELECT restopay FROM TRANSACTION_ACTOR LIMIT 1")
            result['query1'] = namedtuplefetchall(cursor)
            cursor.execute("SELECT DISTINCT bankname, accountno FROM TRANSACTION_ACTOR")
            result['query2'] = namedtuplefetchall(cursor)

      return render(request, 'isi_saldo.html', result)

def tarik_saldo(request):
      result = {}

      with connection.cursor() as cursor:
            cursor.execute("SET SEARCH_PATH TO SIREST")
            cursor.execute("""
                        SELECT restopay
                        FROM TRANSACTION_ACTOR LIMIT 1;
            """)
            result['query1'] = namedtuplefetchall(cursor)
            cursor.execute("""
                  SELECT DISTINCT bankname, accountno FROM TRANSACTION_ACTOR;
            """)
            result['query2'] = namedtuplefetchall(cursor)

      return render(request, 'tarik_saldo.html', result)
