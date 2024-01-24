from django.forms import Form, CharField, EmailField, EmailInput, PasswordInput, CheckboxInput, BooleanField

class Formulario_Entrar(Form):
    correo_usuario = EmailField(
        required=True,
        widget=EmailInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    contrasenia_usuario = CharField(
        required = True,
        min_length = 4,
        max_length = 16,
        widget = PasswordInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )

    recordarme = BooleanField(
        required=False,
        widget=CheckboxInput()
    )