from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=77)


class Pericia(models.Model):
    titulo = models.CharField(max_length=77)
    descricao = models.TextField()
    publicado = models.BooleanField(default=False)
    img = models.ImageField(upload_to='sitepc/img/%Y/%m/%d/')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)
