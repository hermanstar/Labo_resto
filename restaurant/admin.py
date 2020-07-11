from django.contrib import admin
from .models import Menu, Categorie, Produit, Table, Serveur, Commande, Choix

# Register your models here.

admin.site.register(Menu)
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Table)
admin.site.register(Serveur)
admin.site.register(Commande)
admin.site.register(Choix)