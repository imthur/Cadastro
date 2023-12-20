from django.shortcuts import render
from .models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    # Enviar e salvar os dados da tela no banco de dados.
    novoUsuario = Usuario()
    novoUsuario.nome = request.POST.get('nome')
    novoUsuario.idade = request.POST.get('idade')
    novoUsuario.save()
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)
