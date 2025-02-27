from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Usuario
import re

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            messages.error(request, "Por favor, preencha todos os campos.")
            return render(request, "usuarios/login.html")

        try:
            user = Usuario.objects.get(email=email) 
        except Usuario.DoesNotExist:
            messages.error(request, "E-mail inexistente")
            return render(request, "usuarios/login.html")

        user = authenticate(username=user.username, password=password)

        if user is None:
            messages.error(request, "Senha inválida")
        else:
            login(request, user)
            return redirect("menu")

    return render(request, "usuarios/login.html")

def registrar_view(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if not nome.isalpha():
            messages.error(request, "O nome deve conter apenas letras.")
        elif not re.match(r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$", email):
            messages.error(request, "E-mail inválido.")
        elif len(senha) < 8 or not re.search(r"[A-Z]", senha) or not re.search(r"\d", senha) or not re.search(r"[!@#$%^&*]", senha):
            messages.error(request, "A senha deve ter pelo menos 8 caracteres, uma letra maiúscula, um número e um caractere especial.")
        elif senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
        else:
            user = Usuario.objects.create_user(username=email, email=email, password=senha, first_name=nome)
            user.save()
            messages.success(request, "Usuário registrado com sucesso!")
            return redirect("login")

    return render(request, "usuarios/registrar.html")

def menu_view(request):
    return render(request, "usuarios/menu.html")