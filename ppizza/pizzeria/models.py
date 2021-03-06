# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
