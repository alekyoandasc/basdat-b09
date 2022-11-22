from django.shortcuts import render

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
      if request.session.get('role') == "":
            role = request.session.get('role')
            # with connection.cursor() as c:
            #       c.execute("")
            #       c.execute("")
            # response = {'hasil' : hasil}
            # return render(request, 'lihat_saldo.html', response)
      role = ""
      return render(request, 'read_jam_operasional.html', {'role':role})

def update_jam_operasional(request):
      if request.session.get('role') == "":
            role = request.session.get('role')
            # with connection.cursor() as c:
            #       c.execute("")
            #       c.execute("")
            # response = {'hasil' : hasil}
            # return render(request, 'lihat_saldo.html', response)
      role = ""
      return render(request, 'update_jam_operasional.html', {'role':role})