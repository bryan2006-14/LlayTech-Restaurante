from django.db import models


PaymentTypeEnum = (
    ('CARD', 'card'),
    ('CASH', 'cash')
)

StatusPaymentEnum = (
    ('PENDING', 'pending'),
    ('PAID', 'paid')
)

class Payment(models.Model):
    table = models.ForeignKey(
        'tables.Table', on_delete=models.SET_NULL, null=True, verbose_name='Mesa')
    totalPayment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Importe total')   
    paymentType = models.CharField(max_length=255, choices=PaymentTypeEnum, verbose_name='Tipo de pago')
    statusPayment = models.CharField(max_length=255, choices=StatusPaymentEnum, verbose_name='Estado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    def __str__(self):
        return str(self.table)

    class Meta:
        verbose_name = 'pago'
        verbose_name_plural = 'pagos'
