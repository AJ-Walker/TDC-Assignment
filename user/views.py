from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def login(request):
    return render(request, 'user/login.html')