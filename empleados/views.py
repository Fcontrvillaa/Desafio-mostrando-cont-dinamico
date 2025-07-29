from django.shortcuts import render

# Create your views here.

def lista_empleados(request):
    empleados = [
        "Alice Smith",
        "Bob Johnson",
        "Charlie Brown",
        "Diana Prince",
        "Eve Adams",
        "Frank White"
    ]
    
    contexto = {"empleados":empleados}
    return render(request, "lista_empleados.html", contexto)