from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    Nome = models.CharField(max_length=77)

    def __str__(self):
        return self.Nome


class Pericia(models.Model):
    Titulo = models.CharField(max_length=77)
    Descrição = models.TextField()
    Publicado = models.BooleanField(default=False)
    img = models.ImageField(upload_to='sitepc/img/%Y/%m/%d/')
    Categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)
    Autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Titulo
