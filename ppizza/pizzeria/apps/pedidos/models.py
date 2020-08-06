from django.db import models

# Create your models here.


class Pedido(models.Model):
    fecha = models.DateField()
    cliente = models.TextField()
    monto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'


class Pizza(models.Model):
    id_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='id_pedido')
    tamano = models.TextField()
    jamon = models.IntegerField(blank=True, null=True)
    champinon = models.IntegerField(blank=True, null=True)
    pimenton = models.IntegerField(blank=True, null=True)
    dob_queso = models.IntegerField(blank=True, null=True)
    aceitunas = models.IntegerField(blank=True, null=True)
    pepperoni = models.IntegerField(blank=True, null=True)
    salchichon = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pizza'
