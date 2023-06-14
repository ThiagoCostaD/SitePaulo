from django.urls import path
from sitepc.views import home, sobre, palestras, cursos, consultorias, \
    sistemas, contato, faq

urlpatterns = [

    path('', home),  # home
    path('sobre/', sobre),
    path('palestras/', palestras),
    path('cursos/', cursos),
    path('consultorias/', consultorias),
    path('sistemas/', sistemas),
    path('contato/', contato),
    path('faq/', faq),
]
