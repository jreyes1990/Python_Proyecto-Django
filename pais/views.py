from django.shortcuts import render
from webconfig.Querys import SQL

# Create your views here.

def listar(request):
    odasql = SQL()
    listaPais = odasql.listarJSON("select * from pais")

    return render(request, "pais/pais.html", {
        "listapais": listaPais
    })

    '''
    return render(request,"pais/pais.html", {
        "saludo":"Hola mundo de programadores, estoy pasando un parametro",
        "dias":["lunes","martes","miercoles","jueves"],
        "cursos":[
            {"curso":"C#", "profesor":"Licito", "envivo":True},
            {"curso":"VB.Net", "profesor": "Hurol", "envivo":False}],
    }) 
    '''

def agregarPais(request):
    return render(request,"pais/agregarpais.html",None)