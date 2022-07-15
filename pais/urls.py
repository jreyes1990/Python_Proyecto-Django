from django.urls import path
from . import views

urlpatterns = [
    path("listar/",views.listar),
    path("agregar/",views.agregarPais),
    path("buscarpais/",views.buscarPais),
]