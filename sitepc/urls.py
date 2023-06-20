from django.urls import path
from . import views

app_name = 'pericias'

urlpatterns = [
    path('', views.home, name='home'),  # home
    path('pericias/<int:id>/', views.pericias, name='pericia'),
]
