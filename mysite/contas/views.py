from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def login(request):
    return render(request, 'login.html')
    
def sair(request):
    return render(request, 'sair.html')

def cadastrar(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'cadastrar.html', {'form' : form})