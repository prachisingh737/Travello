# calc/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def add(request):
    try:
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        result = int(num1) + int(num2)
    except (TypeError, ValueError):
        result = "Invalid input. Please provide valid integers."
    return render(request, 'result.html', {'result': result})

