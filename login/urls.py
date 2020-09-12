from django.urls import path, include 
from .views import *

urlpatterns = [
    path('accounts/', include('registro.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    #CAIXA
    path('', listar_produtos_disponiveis, name='listar_produtos_disponiveis'),
    path('operadores', list_caixa, name='list_caixa'),
    path('cadastro/', create_caixa, name='create_caixa'),
    path('atualiza-caixa/<int:id>', update_caixa, name='update_caixa'),
    path('apaga-caixa/<int:id>', delete_caixa, name='delete_caixa'),
    path('preco/', soma_preco, name='soma_preco'),

    # PRODUTOS
    path('produtos/', list_products, name='list_products'),
    path('new/', create_products, name='create_products'),
    path('update/<int:id>/', update_products, name='update_products'),
    path('delete/<int:id>', delete_products, name='delete_products'),

]
