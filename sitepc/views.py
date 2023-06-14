from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def manutencao(request):
    return render(request, 'manutencao.html')


def sobre(request):
    return HttpResponse('sobre')


def palestras(request):
    return HttpResponse('palestras')


def cursos(request):
    return HttpResponse('cursos')


def consultorias(request):
    return HttpResponse('consultorias')


def sistemas(request):
    return HttpResponse('sistemas')


def contato(request):
    return HttpResponse('contato')


def faq(request):
    return HttpResponse('faq')
