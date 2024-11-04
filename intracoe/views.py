from django.shortcuts import render

def index(request):
    # Aquí puedes pasar datos al contexto si es necesario
    context = {
        'mensaje': 'Bienvenido a la página principal'
    }
    return render(request, 'base.html', context)