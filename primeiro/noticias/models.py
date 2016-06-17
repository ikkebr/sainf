    from __future__ import unicode_literals

    from django.db import models

    # Create your models here.
    class Categoria(models.Model):
        nome = models.CharField(max_length=30)
        
        def __unicode__(self):
            return u"%s" % self.nome
            

    class Noticia(models.Model):
        titulo = models.CharField(max_length=200)
        data = models.DateTimeField()
        conteudo = models.TextField()
        
        categoria = models.ForeignKey(Categoria)
        
        def __unicode__(self):
            return u"%s" % self.conteudo
            
            
            
            