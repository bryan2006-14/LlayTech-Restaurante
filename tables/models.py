from django.db import models


class Table(models.Model):
    number = models.IntegerField(unique=True, verbose_name='Número')
    
    def __str__(self):
        return str(self.number)
    
    class Meta:
        verbose_name = 'mesa'
        verbose_name_plural = 'mesas'
