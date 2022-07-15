from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola mundo")

def curso(request):
    return HttpResponse("Bienvenido al curso de Django con Python")

def miPrimeraPagina(request):
    return render(request,"inicio.html",None)