from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Django ORM - Object Relational Mapper
class Post(models.Model):           #representa uma tabela no bd
    title       = models.CharField(max_length=255, verbose_name='Título')
    content     = models.TextField(verbose_name='Corpo do artigo')
    user        = models.ForeignKey(User,on_delete=models.PROTECT, verbose_name='Autor')

    class Meta:
        verbose_name = 'Artigo'
        #verbose_name_plural = 'Artigos'

    def __str__(self):
       return self.title  
    
    
