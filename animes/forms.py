from django import forms
from .models import Usuarios
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm

class UsuarioRegistrarForms(forms.ModelForm):
    # Campos de senha e email com atributos personalizados
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Senha',
            'class': "form-control",
            'style': 'width: 300px; display: flex;'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'email@gmail.com',
            'class': "form-control",
            'style': 'width: 300px; display: flex;'
        })
    )
    
    class Meta:
        model = Usuarios
        fields = ["email", "password", "nomeUsuarios"]
        widgets = {
            'nomeUsuarios': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px;',
                'placeholder': 'Digite seu nome'
            }),
        }

    # Validação da senha para garantir que tenha pelo menos 8 caracteres
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        return password

    # Validação do campo email para garantir que o email não esteja em uso
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está registrado no nosso sistema!")
        return email

    # Validação do campo nome de usuário, garantindo que o nome não esteja em uso
    def clean_nomeUsuarios(self):
        nome = self.cleaned_data.get("nomeUsuarios")
        if Usuarios.objects.filter(nomeUsuarios=nome).exists():
            raise forms.ValidationError("Este nome já está em uso.")
        return nome

class UsuarioEntrarForm(forms.Form):
    email = forms.CharField(widget= forms.TextInput (attrs = {'placeholder': 'eamil', 'class': "form-control", 'style': 'Width: 300px; display: flex; '}))
    password = forms.CharField(widget= forms.PasswordInput (attrs = {'placeholder': 'senha', 'class': "form-control", 'style': 'Width: 300px; display: flex; '}) )
