from django.db import models


StatusEnum = (
    ('PENDING', 'pending'),
    ('DELIVERED', 'delivered')
)

class Order(models.Model):
    table = models.ForeignKey('tables.Table', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Mesa')
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Producto')
    payment = models.ForeignKey('payments.Payment', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Pago')
    status = models.CharField(max_length=255, choices=StatusEnum, verbose_name='Estado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    close = models.BooleanField(default=False, verbose_name='Cerrado')
    
    def __str__(self):
        return str(self.table)
    
    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
    
