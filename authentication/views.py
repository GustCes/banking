from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("mundo, hola!. esta es mi primera vista!!!")

def countries(request):
    return HttpResponse("Countries view")

def departments(request):
    return HttpResponse("Departments view")

def cities(request):
    return HttpResponse("Cities view")