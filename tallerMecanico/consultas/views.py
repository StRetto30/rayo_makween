from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Atencion
from .forms import ConsultaForm
from django.contrib import messages

# Create your views here.

def formulariolist(request):
    atencion = Atencion.objects.all()
    return render(request, 'formulariolist.html', {'consultas': atencion})


def formulario(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            try:
                Atencion = form.save(commit=False)
                Atencion.save()

                
                messages.success(request, 'La consulta se ha enviado correctamente. Nos pondremos en contacto contigo.')

                return redirect('formulario.html')  
            except Exception as e:
                
                messages.error(request, f'Error al procesar la consulta: {str(e)}')
        else:
       
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = ConsultaForm()

    context = {'form': form}
    return render(request, 'formulario.html', context)






class PaginaPrincipal(View):
    def get(self, request):
        atenciones = Atencion.objects.filter(aprobado=True).order_by('-fecha')[:5]
        return render(request, 'index.html', {'atenciones': atenciones})



    