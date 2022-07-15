from django.shortcuts import render
from webconfig.Querys import SQL

# Create your views here.

def listar(request):
    odasql = SQL()
    listaPais = odasql.listarJSON("exec uspListarPais")

    return render(request, "pais/pais.html", {
        "listapais": listaPais,
        "nombre": ""
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

def buscarPais(request):
    nombre = request.POST.get("nombre").strip()
    print(nombre)
    odasql = SQL()

    if nombre=="" or nombre==None:
        listaPais = odasql.listarJSON("exec uspListarPais")
    else:
        listaPais = odasql.listarJSON("exec uspFiltrarPaisNombre @nombre={0}".format(nombre))

    return render(request, "pais/pais.html", {
        "listapais": listaPais,
        "nombre": nombre
    })