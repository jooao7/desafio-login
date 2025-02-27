from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Usuario
import re

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="E-mail")
    password = forms.CharField(widget=forms.PasswordInput(), label="Senha")

class RegistroForm(UserCreationForm):
    senha1 = forms.CharField(widget=forms.PasswordInput(), label="Senha")
    senha2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Senha")

    class Meta:
        model = Usuario
        fields = ["email"]

    def clean_senha1(self):
        senha = self.cleaned_data.get("senha1")
        if len(senha) < 8 or not re.search(r"\d", senha) or not re.search(r"[A-Z]", senha) or not re.search(r"[@$!%*?&]", senha):
            raise forms.ValidationError("A senha deve conter pelo menos 8 caracteres, 1 número, 1 letra maiúscula e 1 caractere especial.")
        return senha

    def clean(self):
        cleaned_data = super().clean()
        senha1 = cleaned_data.get("senha1")
        senha2 = cleaned_data.get("senha2")

        if senha1 and senha2 and senha1 != senha2:
            self.add_error("senha2", "As senhas não coincidem.")
