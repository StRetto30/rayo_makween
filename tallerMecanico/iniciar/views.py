from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

class VRegistro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request,"registro.html",{"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)

        if form.is_valid():

            email=form.save()

            login(request, email)

            return redirect('index')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request,'registro.html',{"form":form})

def cerrar_sesion(request):
    logout(request)

    return redirect('index')





def iniciosesion(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('index')
            else:
                messages.error(request, "usuario no válido")
        else:
            messages.error(request, "información incorrecta")

    form=AuthenticationForm()
    return render(request,"iniciosesion.html",{"form":form})


def recuperarcuenta(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            usuario=authenticate(username=nombre_usuario)
            if usuario is not None:
                login(request, usuario)
                return redirect('index')
            else:
                messages.error(request, "usuario no válido")
        else:
            messages.error(request, "información incorrecta")

    form=AuthenticationForm()
    return render(request,"recuperarcuenta.html",{"form":form})