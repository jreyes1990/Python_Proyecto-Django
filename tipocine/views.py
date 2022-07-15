from django.shortcuts import render
from webconfig.Querys import SQL

# Create your views here.

def listarTipoCine(request):
    odasql = SQL()
    listaTipoCine = odasql.listarJSON("exec uspListarTipoCine")

    return render(request, "tipocine/tipocine.html", {
        "listatipocine": listaTipoCine
    })

def buscarTipoCine(request):
    nombre = request.POST.get("nombreTipoCine")
    odasql = SQL()
    listaTipoCine = odasql.listarJSON("exec uspFiltrarTipoCine @nombre='{0}'".format(nombre))

    return render(request, "tipocine/tipocine.html", {
        "listatipocine": listaTipoCine,
        "nombreTipoCine": nombre
    })