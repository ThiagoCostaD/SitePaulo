from django.shortcuts import render


def home(request):
    return render(request, 'sitepc/pages/home.html')


def pericias(request, id):
    return render(request, 'sitepc/pages/pericias-view.html')
