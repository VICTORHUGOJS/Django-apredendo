from django.db import models

# Create your models here.
#Django ORM - Object Relational Mapper
class Post(models.Model):           #representa uma tabela no bd
    title       = models.CharField(max_length=255)
    content     = models.TextField()
    
    
