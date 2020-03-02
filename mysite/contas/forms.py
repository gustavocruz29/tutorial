from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroUsuarioForm(UserCreationForm):
    
    first_name = forms.CharField(label = 'Primeiro nome', max_length=50, required=True, help_text='Campo de nome obrigatório')
    last_name = forms.CharField(label = 'Ultimo nome', required=False, help_text='Campo de nome obrigatório')
    email = forms.EmailField(label = 'E-mail', max_length=250, help_text='Por favor informe um email válido!')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2']