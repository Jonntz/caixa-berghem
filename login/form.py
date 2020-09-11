from django import forms
from .models import Produtos, Operador

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'preco']

class CaixaForm(forms.ModelForm):
    class Meta:
        model = Operador
        fields = ['nome', 'idade', 'identificacao', 'senha']