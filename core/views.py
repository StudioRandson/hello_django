from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request,nome,idade):
    return HttpResponse('<h2>Hello {}, idade: {}</h2>'.format(nome,idade))
