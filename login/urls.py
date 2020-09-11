from django.urls import path, include 
from .views import list_products, create_products, update_products, delete_products,list_caixa, create_caixa, update_caixa, delete_caixa

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    
    #CAIXA
    path('', list_caixa, name='list_caixa'),
    path('cadastro/', create_caixa, name='create_caixa'),
    path('atualiza-caixa/<int:id>', update_caixa, name='update_caixa'),
    path('apaga-caixa/<int:id>', delete_caixa, name='delete_caixa'),

    # PRODUTOS
    path('produtos/', list_products, name='list_products'),
    path('new/', create_products, name='create_products'),
    path('update/<int:id>/', update_products, name='update_products'),
    path('delete/<int:id>', delete_products, name='delete_products'),

]
