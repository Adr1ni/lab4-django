from django.shortcuts import render
from .models import Entrada,Autor

def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})


def autoures_entradas(request,id):
    autor = Autor.objects.get(pk=id)
    entradas = Entrada.objects.filter(autor = autor)
    return render(request,'blog/entradas_autor.html',{
        'entradas':entradas,
        'autor':autor
    })
