from django.contrib import admin
from .models import Noticia, Categoria

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data']
    list_filter = ['categoria', 'data']
    search_fields = ['titulo', 'conteudo']

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Categoria)