from django.contrib import admin
from .models import Categoria, Pericia


class CategoriaAdmin(admin.ModelAdmin):
    ...


@admin.register(Pericia)
class PericiaAdmin(admin.ModelAdmin):
    ...


admin.site.register(Categoria, CategoriaAdmin)
