from django.shortcuts import render
from .models import Noticia

def listar(request):
    lista_de_noticias = Noticia.objects.all()
    return render(request, 'noticias/listar.html', {'noticias': lista_de_noticias})