
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('rayo', include('rayo.urls')),
    path('iniciar', include('iniciar.urls')),
    path('consultas', include('consultas.urls')),
    
]
