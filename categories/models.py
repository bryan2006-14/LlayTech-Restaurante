from django.contrib import admin
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    image = models.ImageField(upload_to='categories', verbose_name='Imagen')
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['title',]
