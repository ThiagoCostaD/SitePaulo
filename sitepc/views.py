import os
from venv import logger

# from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.utils.html import escape

from utils.pagination import make_pagination

from .models import Pericia

PER_PAGE = int(os.environ.get('PER_PAGE', 9))


def home(request):
    pericias = Pericia.objects.filter(
        publicado=True
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(
        request, pericias, PER_PAGE)

    return render(request, 'sitepc/pages/home.html', context={
        'pericias': page_obj,
        'pagination_range': pagination_range,
    })


def categoria(request, categoria_id):

    pericias = get_list_or_404(
        Pericia.objects.filter(
            categoria__id=categoria_id,
            publicado=True
        ).order_by('-id')
    )

    page_obj, pagination_range = make_pagination(
        request, pericias, PER_PAGE)

    return render(request, 'pericias/pages/categoria.html',
                  context={
                      'pericias': page_obj,
                      'pagination_range': pagination_range,
                      # type:ignore
                      'titulo': f'{pericias[0].categoria.nome} - Categoria |'
                  })


def pericias(request, id):

    try:
        pericia = get_object_or_404(Pericia, pk=id, publicado=True)
    except Http404:
        logger.error('pericia not found with id %s', id)
        raise

    return render(request, 'sitepc/pages/pericias-view.html',
                  context={
                      'pericia': pericia,
                      'pagina_detalhada': True,
                  })


def busca(request):
    termo_busca = escape(
        request.GET.get(
            'busca', ''
        ).strip()
    )

    if not termo_busca:
        raise Http404()

    pericias = Pericia.objects.filter(
        Q(
            Q(titulo__icontains=termo_busca) |
            Q(descricao__icontains=termo_busca),
        ),
        publicado=True,
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(
        request, pericias, PER_PAGE)

    return render(request, 'sitepc/pages/busca.html',
                  {
                      'titulo_pagina': f'Pesquisando por "{termo_busca}"  ',
                      'termo_busca': termo_busca,
                      'pericias': page_obj,
                      'pagination_range': pagination_range,
                      'additional_url_query': f'&busca={termo_busca}',
                  }
                  )
