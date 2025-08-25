from django.shortcuts import render, redirect
from django.db import models
from .models import Cliente



def home(request):
    return render(request, "app/home.html")

def cad_client(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        Cliente.objects.create(nome=nome)
        return redirect("/")  # redireciona após salvar"
    return render(request, "app/cadastro_cliente.html")


def admin_cliente(request):
    return render(request, "app/admin_cliente.html")