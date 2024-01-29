from django.shortcuts import render

# Create your views here.
def index(request):
    user_is_cliente = request.user.groups.filter(name='Cliente').exists()
    context = {'user_is_cliente': user_is_cliente}
    return render(request, 'index.html', context)