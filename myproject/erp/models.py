from django.db import models

class Fabrica(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Fábrica'
        verbose_name_plural = 'Fábricas'


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'