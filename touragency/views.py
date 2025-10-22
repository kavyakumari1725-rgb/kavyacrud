from django.shortcuts import render
from . models import Tour

# Create your views here.
def index(response):
    return render(response,'index.html')
def packages(response):
    return render(response,'packages.html')
def destination(response):
    tours=Tour.objects.all()
    context={'tours':tours}
    return render(response,'destination.html',context)
def about_us(response):
    return render(response,'about_us.html')