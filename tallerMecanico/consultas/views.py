from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Atencion
from .forms import ConsultaForm
from django.contrib import messages

# Create your views here.
def formulario(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            try:
                Atencion = form.save(commit=False)
                Atencion.save()

                
                messages.success(request, 'La consulta se ha enviado correctamente. Nos pondremos en contacto contigo.')

                return redirect('form-motor.html')  # Ajusta la redirección según tus necesidades
            except Exception as e:
                # Manejar cualquier error durante el procesamiento
                messages.error(request, f'Error al procesar la consulta: {str(e)}')
        else:
            # Mensaje de error en el formulario
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = ConsultaForm()

    context = {'form': form}
    return render(request, 'formulario.html', context)






class PaginaPrincipal(View):
    def get(self, request):
        atenciones = Atencion.objects.filter(aprobado=True).order_by('-fecha')[:5]
        return render(request, 'index.html', {'atenciones': atenciones})



    