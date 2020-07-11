from django.db import models
from django.contrib.auth.models import User 
from django.utils.text import slugify

# Create your models here.


class Menu(models.Model):
    nom         = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    slug        = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug and self.nom : 
            self.slug = slugify(self.nom)
        super(Menu, self).save(*args, **kwargs)    
    
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
    photo       = models.ImageField(upload_to="produits/", null=True)
    pays        = models.CharField(max_length=100, null=True)
    categorie   = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    menu        = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='produits')
    slug        = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug and self.nom : 
            self.slug = slugify(self.nom)
        super(Produit, self).save(*args, **kwargs)       
    

    def __str__(self):
        return self.nom

class Table(models.Model):
    nr_table = models.IntegerField(unique=True)
    nom      = models.CharField(max_length=30, null=True)
    def __str__(self):
        return  str (self.nr_table)

class Serveur(models.Model):
    nr_serveur  = models.IntegerField(unique=True)
    nom         = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.nom
    
class Choix(models.Model):
    choix     = models.ForeignKey(Produit, on_delete=models.CASCADE)  
    quantite  = models.IntegerField(default=1)
    commander = models.BooleanField(default=False)
    creer     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantite} of {self.choix.nom}'

    def get_total(self):
        total      = self.choix.prix * self.quantite
        floattotal = float("{0:.2f}".format(total))
        return floattotal


class Commande(models.Model):
    composition = models.ManyToManyField(Choix) 
    nr_commande = models.CharField(max_length=10, unique=True)  
    commander   = models.BooleanField(default=False)  
    date        = models.DateTimeField(auto_now_add=True)
    table       = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='commandes')
    serveur     = models.ForeignKey(Serveur, on_delete=models.CASCADE, related_name='commandes')


    def get_totals(self):
        total = 0
        for cmd_choix in self.composition.all():
            total += cmd_choix.get_total()
        
        return total
    


