from django.contrib import admin
from .models import Categoria, Pericia


class CatgoriaAdmin(admin.ModelAdmin):
    ...


admin.site.register(Categoria, CatgoriaAdmin)


class PericiaAdmin(admin.ModelAdmin):
    ...


admin.site.register(Pericia, PericiaAdmin)
