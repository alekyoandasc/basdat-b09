from django.shortcuts import render
from django.shortcuts import render
# from django.shortcuts import connection

# Create your views here.
def lihat_saldo(request):
      # index(request)
      # cursor = connection.cursor()
      if request.session.get('role') == "":
            role = request.session.get('role')
            # email = request.session.get('email')
            # response = {'email':email, 'role':role}
            # return render(request, 'index.html', response)
      role = ""
      return render(request, 'lihat_saldo.html', {'role':role})

def add_saldo(request):
      if request.session.get('role') == "":
            role = request.session.get('role')
            # with connection.cursor() as c:
            #       c.execute("")
            #       c.execute("")
            # response = {'hasil' : hasil}
            # return render(request, 'lihat_saldo.html', response)
      role = ""
      return render(request, 'isi_saldo.html', {'role':role})

def tarik_saldo(request):
      if request.session.get('role') == "":
            role = request.session.get('role')
            # with connection.cursor() as c:
            #       c.execute("")
            #       c.execute("")
            # response = {'hasil' : hasil}
            # return render(request, 'lihat_saldo.html', response)
      role = ""
      return render(request, 'tarik_saldo.html', {'role':role})

def validate_saldo(request):
      if request.session.get('role') == "":
            data_saldo = {
                  "saldonow" : request.POST.get("saldo"),
                  "nominalisi": request.POST.get("nominal"),
                  "bname": request.POST.get("bank_name"),
                  "norek": request.POST.get("no_rek")
            }