from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main.html')

def sale(request):
    return render(request, 'sale.html')