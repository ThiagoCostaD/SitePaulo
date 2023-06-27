from django.shortcuts import render
# from utils.pericias.fabrica import make_pericia
from .models import Pericia


def home(request):
    pericias = Pericia.objects.all().order_by('id')
    return render(request, 'sitepc/pages/home.html', context={
        'pericias': pericias,
    })


def pericias(request, id):
    pericias = Pericia.objects.filter()
    return render(request, 'sitepc/pages/home.html', context={
        'pericias': pericias,
        'is_datail_page': True
    })
