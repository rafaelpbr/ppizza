from django.contrib import admin

from apps.pedidos.models import Pedido, Pizza

# Register your models here.
admin.site.register(Pedido)
admin.site.register(Pizza)