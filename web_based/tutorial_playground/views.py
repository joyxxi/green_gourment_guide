from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Take a request -> return a respond


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Mosh'})