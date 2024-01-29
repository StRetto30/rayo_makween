from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicios, name="servicios"),
    path('', views.nosotros, name="nosotros"),
    path('', views.contacto, name="contacto"),
    path('', views.ayuda, name="ayuda"),
    
]
