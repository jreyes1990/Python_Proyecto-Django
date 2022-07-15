from django.shortcuts import render
from webconfig.Querys import SQL

# Create your views here.

def listarTipoCine(request):
    odasql = SQL()
    listaTipoCine = odasql.listarJSON("exec uspListarTipoCine")

    return render(request, "tipocine/tipocine.html", {
        "listatipocine": listaTipoCine
    })