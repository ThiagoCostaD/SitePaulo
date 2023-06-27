from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    Nome = models.CharField(max_length=77)

    def __str__(self):
        return self.Nome


class Pericia(models.Model):
    titulo = models.CharField(max_length=77)
    descrição = models.TextField()
    publicado = models.BooleanField(default=False)
    img = models.ImageField(upload_to='sitepc/img/%Y/%m/%d/')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo
