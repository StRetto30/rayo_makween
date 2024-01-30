from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicios, name="servicios"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('contacto', views.contacto, name="contacto"),
    path('ayuda', views.ayuda, name="ayuda"),
    
]
