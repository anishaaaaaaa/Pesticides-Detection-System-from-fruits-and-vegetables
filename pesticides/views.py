from django.shortcuts import render
from django.conf.urls.static import static

# Create your views here.
def home(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def temphumi(request):
    return render(request, 'temp-humi.html')