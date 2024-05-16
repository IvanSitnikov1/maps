from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def one(request):
    return render(request, 'main/1.html')

def two(request):
    return render(request, 'main/2.html')

def three(request):
    return render(request, 'main/3.html')