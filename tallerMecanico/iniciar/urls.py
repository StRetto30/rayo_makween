from django.urls import path
from .views import  VRegistro, cerrar_sesion, iniciosesion, recuperarcuenta

urlpatterns = [
    path('',VRegistro.as_view(), name="registro"),
    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
    path('iniciosesion',iniciosesion, name="iniciosesion"),
    path('recuperarcuenta', recuperarcuenta, name="recuperarcuenta"),

    
]
