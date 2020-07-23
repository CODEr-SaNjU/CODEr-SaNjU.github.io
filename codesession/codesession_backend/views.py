from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'html_files/home.htm')