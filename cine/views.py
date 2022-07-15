from django.shortcuts import render
from webconfig.Querys import SQL
from django.http import HttpResponse
import json

# Create your views here.

def listarCine(request):
    return render(request, "cine/cine.html", {

    })

def listarCineAsincrono(request):
    odasql = SQL()
    listaCine = odasql.listarJSON("exec uspListarCine")
    return HttpResponse(json.dumps(listaCine))