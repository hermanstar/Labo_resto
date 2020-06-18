from django.db import models
from django.contrib.auth.models import User 


# Create your models here.


class Menu(models.Model):
    nom         = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom

class Categorie(models.Model):
    libelle = models.CharField(max_length=100, unique=True) # Exemple: Complement, entrée, sortie, Biere, Vin, Gazeuse, etc.
    type_cat    = models.CharField(max_length=30)  # Nourriture ou Boisson

    def __str__(self):
        return self.libelle

class Produit(models.Model):
    nom         = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100, null=True)
    prix        = models.DecimalField(max_digits=5, decimal_places=2)
    photo       = models.ImageField(upload_to="media/", null=True)
    pays        = models.CharField(max_length=100, null=True)
    categorie   = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    menu        = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='produits')

    def __str__(self):
        return self.nom

class Table(models.Model):
    nr_table = models.IntegerField(unique=True)
    nom      = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.nr_table

class Serveur(models.Model):
    nr_serveur  = models.IntegerField(unique=True)
    nom         = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.nom

class Commande(models.Model):
    nr_commande = models.TextField(max_length=10, unique=True)
    composition = models.TextField(max_length=1000) 
    total       = models.DecimalField(max_digits=5, decimal_places=2)
    date        = models.DateTimeField(auto_now_add=True)
    table    = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='commandes')
    serveur     = models.ForeignKey(Serveur, on_delete=models.CASCADE, related_name='commandes')


class Details(models.Model):
    table    = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='details')
    produit  = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='details')
    quantite = models.IntegerField()