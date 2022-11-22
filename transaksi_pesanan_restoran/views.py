from django.shortcuts import render

# Create your views here.
def read_tprestoran(request):
      if request.session.get('role') == "":
            role = request.session.get('role')
            # with connection.cursor() as c:
            #       c.execute("")
            #       c.execute("")
            # response = {'hasil' : hasil}
            # return render(request, 'lihat_saldo.html', response)
      role = ""
      return render(request, 'read_tp_restoran.html', {'role':role})

def detail_tprestoran(request):
      if request.session.get('role') == "":
            role = request.session.get('role')
            # with connection.cursor() as c:
            #       c.execute("")
            #       c.execute("")
            # response = {'hasil' : hasil}
            # return render(request, 'lihat_saldo.html', response)
      role = ""
      return render(request, 'detail_tprestoran.html', {'role':role})