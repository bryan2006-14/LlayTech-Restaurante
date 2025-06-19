from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    image = models.ImageField(upload_to='products', verbose_name='Imagen')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Precio')
    active = models.BooleanField(default=False, verbose_name='Activo')
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Categoría')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['category', 'title']