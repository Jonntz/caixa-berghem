from __future__ import unicode_literals
from djongo import models

#Create your models here.
class Operador(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    nome = models.CharField(max_length=20, null=False)
    idade = models.IntegerField(default=0, null=False)
    identificacao = models.CharField(max_length=5, null=False)
    senha = models.CharField(max_length=8, null=False)

    def __str__(self):
        return self.nome


class Produtos(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    nome = models.CharField(max_length=20, null=False)
    preco = models.FloatField(default=0, null=False)

    def __str__(self):
        return self.nome