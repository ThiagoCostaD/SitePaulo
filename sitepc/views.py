from django.shortcuts import render
from utils.pericias.fabrica import make_pericia


def home(request):
    return render(request, 'sitepc/pages/home.html', context={
        'pericias': [make_pericia() for _ in range(12)],
    })


def pericias(request, id):
    return render(request, 'sitepc/pages/pericias-view.html', context={
        'pericia': make_pericia(),
        'pagina_detalhada': True,
        'pagina_pericias': True,
    })
