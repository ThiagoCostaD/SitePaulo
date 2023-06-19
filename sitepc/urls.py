from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pericias-home'),  # home
    path('pericias/<int:id>/', views.pericias, name='pericias-pericia'),
]
