from django.db import models


# Create your models here.

class OrdenTrabajo(models.Model):
    numero_orden = models.CharField('Número orden', primary_key=True, max_length=30)
    estado = models.IntegerField(default=1)

    class Meta:
        verbose_name = "OrdenDeTrabajo"
        verbose_name_plural = "OrdenDeTrabajos"

    def __str__(self):
        return '{}'.format(self.numero_orden)


class ImageOrdenTrabajo(models.Model):
    orden = models.ForeignKey(OrdenTrabajo, on_delete=models.PROTECT)
    fecha_public = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="image/%Y/%m/%d")

    class Meta:
        verbose_name = "ImagenOrdenDeTrabajo"
        verbose_name_plural = "ImagenOrdenDeTrabajos"