from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .models import Operation
import re

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/calculator/')
    return render(request, 'login.html')

@login_required
def calculator(request):
    history = Operation.objects.filter(user=request.user).order_by('-timestamp')[:5]
    result = None
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
    try:
        result = eval(expression)
        operation = Operation(user=request.user, expression=expression, result=str(result))
        operation.save()
    except Exception:
        result = "Erro"
    return render(request, 'calculator.html', {'history': history, 'result': result})