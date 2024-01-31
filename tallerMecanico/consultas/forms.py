from django import forms


class ConsultaForm(forms.Form):
    titulo = forms.CharField(max_length=255)
    diagnostico = forms.CharField(max_length=255)
    OPCIONES_CATEGORIA = [
        ('motor', 'Motor'),
        ('frenos', 'Sistema de frenos'),
        ('suspension', 'Suspensión'),
        ('transmision', 'Transmisión'),
        ('electrico', 'Sistema eléctrico')]
    categoria = forms.CharField(label='Categorías',widget=forms.Select(choices=OPCIONES_CATEGORIA))
    modelo = forms.CharField(label='Modelo', max_length=100)
    año = forms.IntegerField(label='Año')



    