
from django.urls import path
from .views import login, sair, cadastrar

urlpatterns = [
    path('login/', login, name='login'),
    path('sair/', sair, name='sair'),
    path('cadastrar/', cadastrar, name='cadastrar')
]
