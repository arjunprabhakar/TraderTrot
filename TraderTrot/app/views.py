from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request,'index.html')
def blog(request):
    return render (request,'blog.html')
def blogs(request):
    return render (request,'blog-details.html') 
def login(request):
    return render (request,'login.html')
def user_reg(request):
    return render (request,'user_reg.html')