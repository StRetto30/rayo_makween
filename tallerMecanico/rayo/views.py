from django.shortcuts import render

# Create your views here.
def servicios(request):
    context={}
    return render(request, 'servicios.html', context)


def nosotros(request):
    context={}
    return render(request, 'nosotros.html', context)

def contacto(request):
    context={}
    return render(request, 'Contacto.html', context)

def ayuda(request):
    context={}
    return render(request, 'ayuda.html', context)