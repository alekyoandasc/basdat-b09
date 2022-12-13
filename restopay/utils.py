from django.db import connection
from collections import namedtuple

def dictfetchall(cursor):
    "Return all rows from a cursor as a list of dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listfecthall(cursor):
    return [x[0] for x in cursor.fetchall()]

# def listfetchone(cursor):
#       return [x[0] for x in cursor.fetchone()]
def dictfetchone(cursor):
    "Return all rows from a cursor as a list of dict"
    columns = [field_name[0] for field_name in cursor.description]
    row = cursor.fetchone()
    return dict(zip(columns, row))