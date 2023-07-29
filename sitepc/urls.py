from django.urls import path

from . import views

app_name = 'pericias'

urlpatterns = [
    path('', views.home, name='home'),
    path('pericias/categoria/<int:categoria_id>/',
         views.categoria, name='categoria'),
    path('pericias/<int:id>/', views.pericias, name='pericia'),
]
