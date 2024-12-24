from django.shortcuts import render
from django.http import HttpResponse

data = {
    'title': 'Главная страница',
    'values': ['some', 123, 'hello']
}

def index(request):
    return render(request,'main/index.html', {'data' : data})

def about(request):
    return render(request,'main/about.html')

def back(request):
    return render(request, 'main/down.html')

def pie(request):
    return render(request,'main/pie.html')


