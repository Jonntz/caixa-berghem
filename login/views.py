from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from .models import Operador as caixa, Produtos as prod
from .form import ProductForm, CaixaForm



#COMPRAS
@login_required
def listar_produtos_disponiveis(request):
    produtos = prod.objects.all()
    return render(request, 'compras.html', {'produtos': produtos})

def soma_preco(request):
    if(request.GET.get('add')):
        preco = prod.preco

        return preco
    
    return preco

#PRODUTOS
@login_required
def list_products(request):
    produtos = prod.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


@login_required
def create_products(request):
    form = ProductForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'produtos-form.html', {'form': form})

@login_required
def update_products(request, id):
    produto = prod.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=produto)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'produtos-form.html', {'form': form, 'produto': produto})

@login_required
def delete_products(request, id):
    produto = prod.objects.get(id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('list_products')

    return render(request, 'produtos-delete-confirm.html', {'produto': produto})


#CAIXA
@login_required
def list_caixa(request):
    operadores = caixa.objects.all()
    return render(request, 'caixa.html', {'operadores': operadores})

@login_required
def create_caixa(request):
    form = CaixaForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('list_caixa')

    return render(request, 'caixa-form.html', {'form': form})

@login_required
def update_caixa(request, id):
    operadores = caixa.objects.get(id=id)
    form = CaixaForm(request.POST or None, instance=operadores)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('list_caixa')

    return render(request, 'caixa-form.html', {'form': form, 'operadores': operadores})

@login_required
def delete_caixa(request, id):
    operadores = caixa.objects.get(id=id)

    if request.method == 'POST':
        operadores.delete()
        return redirect('list_caixa')
    
    return render(request, 'caixa-delete-confirm.html', {'operadores': operadores})