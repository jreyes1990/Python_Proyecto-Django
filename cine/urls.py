from django.urls import path
from . import views

urlpatterns = [
    path("listar/",views.listarCine),
    path("listarcine/",views.listarCineAsincrono),
]