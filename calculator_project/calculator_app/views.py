from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import re
from .models import Operation

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('calculator')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})
    return render(request, 'login.html')

@login_required
def calculator(request):
    history = Operation.objects.filter(user=request.user).order_by('-dt_inclusao')[:10]
    resultado = None
    if request.method == "POST":
        parametros = request.POST.get("expression", "")
        if re.match(r'^[0-9+\-*/. ]+$', parametros):
            try:
                resultado = eval(parametros)
                operation = Operation(user=request.user, parametros=parametros, resultado=str(resultado))
                operation.save()
            except Exception:
                resultado = "Erro"
        else:
            resultado = "Expressão inválida"
    return render(request, "calculator.html", {"resultado": resultado, "history": history})