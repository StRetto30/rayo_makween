from django.urls import path
from . import views

urlpatterns = [
    ###path('', views.Consultas_cli, name="consultas_cli"),
    path('', views.formulario, name="formulario"),
    
]