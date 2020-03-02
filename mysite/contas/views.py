from django.shortcuts import render, redirect
from .forms import CadastroUsuarioForm


def login(request):
    return render(request, 'login.html')
    
def sair(request):
    return render(request, 'sair.html')

def cadastrar(request):
    
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CadastroUsuarioForm()

    return render(request, 'cadastrar.html', {'form' : form})