from django.shortcuts import render


def home(request):
    return render(request, 'sitepc/manutencao.html')


def manutencao(request):
    return render(request, 'sitepc/manutencao.html')


def sobre(request):
    return render(request, 'sitepc/manutencao.html')


def palestras(request):
    return render(request, 'sitepc/manutencao.html')


def cursos(request):
    return render(request, 'sitepc/manutencao.html')


def consultorias(request):
    return render(request, 'sitepc/manutencao.html')


def sistemas(request):
    return render(request, 'sitepc/manutencao.html')


def contato(request):
    return render(request, 'sitepc/manutencao.html')


def faq(request):
    return render(request, 'sitepc/manutencao.html')
