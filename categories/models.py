from django.contrib import admin
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories')
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['title',]
