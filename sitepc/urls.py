from django.urls import path
from sitepc import views

urlpatterns = [

    path('', views.home, name='home'),  # home
    path('sobre/', views.sobre, name='sobre',),
    path('palestras/<slug:id>/', views.palestras, name='palestras',),
    path('cursos/<id>/', views.cursos, name='cursos',),
    path('consultorias/<slug:id>/', views.consultorias, name='consultorias',),
    path('sistemas/<slug:id>/', views.sistemas, name='sistemas',),
    path('contato/', views.contato, name='contato',),
    path('faq/<slug:id>/', views.faq, name='FAQ',),
]
