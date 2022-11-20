from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#       return HttpResponse("Hello World!")

def index(request):
      # index(request)
      # cursor = connection.cursor()
      if request.session.get('role') == "":
            role = request.session.get('role')
            # email = request.session.get('email')
            # response = {'email':email, 'role':role}
            # return render(request, 'index.html', response)
      role = ""
      return render(request, 'index.html', {'role':role})

def register(request):
      return render(request, 'register.html')