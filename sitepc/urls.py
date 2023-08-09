from django.urls import path

from . import views

app_name = 'pericias'

urlpatterns = [
    path('', views.home, name='home'),
    path('sitepc/', views.busca, name='busca'),
    path('sitepc/categoria/<int:categoria_id>/',
         views.categoria, name='categoria'),
    path('sitepc/<int:id>/', views.pericias, name='pericia'),
]
