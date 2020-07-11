from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Menu , Produit, Commande, Table, Serveur, Choix

def home(request):
    menus = Menu.objects.all()
    return render(request, 'home.html', {'menus': menus})


def menus_produit(request, slug):
    menu =  Menu.objects.get(slug=slug)
    menus = Menu.objects.all()
    return render(request, 'produits.html', {'menu': menu, 'menus': menus})

  
    
def resumerCommande(request, pk):   
    commande_list  = Commande.objects.filter(pk=pk)
    commande       = commande_list[0]
    composition    = commande.composition.all()
    total_commande = commande.get_totals()
    produits       = Produit.objects.all()
    nombre_produits = len(commande.composition.all())

    context = {
        'commande'        : commande ,
        'produits'        : produits,
        'nombre_produits' : nombre_produits,       
        # 'tables'  : tables ,
        # 'serveurs' : serveurs ,
    }
    return render(request, 'commande.html', context)

def choisirProduit (request,nr_commande, slug):
    choix        = get_object_or_404(Produit, slug=slug)
    
    choix_cmd, creer = Choix.objects.get_or_create(
        choix = choix, 
    )
    commande_list  = Commande.objects.filter(nr_commande=nr_commande)
    
    if commande_list.exists(): 
        
        commande = commande_list[0] 
       # vérifier si le choix est déjà dans la commande
        if commande.composition.filter(choix__slug=choix.slug).exists():
            choix_cmd.quantite += 1
            choix_cmd.save()
          #  messages.info(request, f"{choix.nom} la quantite a été modifier.")
        else:
            commande.composition.add(choix_cmd)
         #   messages.info(request, f"{choix.nom} a été ajouter dans la commande.")
    else: 
        commande = Commande.objects.create(
            nr_commande  = 'joel'
        )
        commande.composition.add(choix_cmd)
        #messages.info(request, f"{choix.nom} a été ajouter à votre commande.")   
    return redirect('menus_produit',pk=choix.slug)    
    
def ajouterProduit (request,nr_commande, slug):
    choix        = get_object_or_404(Produit, slug=slug)
    
    choix_cmd, creer = Choix.objects.get_or_create(
        choix = choix, 
    )
    commande_list  = Commande.objects.filter(nr_commande=nr_commande)
    
    if commande_list.exists():       
        commande = commande_list[0] 
       # vérifier si le choix est déjà dans la commande
        if commande.composition.filter(choix__slug=choix.slug).exists():
            choix_cmd.quantite += 1
            choix_cmd.save()
          #  messages.info(request, f"{choix.nom} la quantite a été modifier.")
        else:
            commande.composition.add(choix_cmd)
         #   messages.info(request, f"{choix.nom} a été ajouter dans la commande.")  
    return redirect('resumerCommande',pk=1)
  


# Diminuer la quantité d'un produit 

def diminuerProduit (request,nr_commande, slug):
    choix          = get_object_or_404(Produit, slug=slug)
    commande_list  = Commande.objects.filter(nr_commande=nr_commande)
    
    if commande_list.exists():  
       commande = commande_list[0]  
       # vérifier si le choix est déjà dans la commande
       if commande.composition.filter(choix__slug=choix.slug).exists():
            choix_cmd = Choix.objects.filter(choix=choix)[0]
            if choix_cmd.quantite > 1 :
                choix_cmd.quantite -= 1
                choix_cmd.save()
            else: 
                commande.composition.remove(choix_cmd)
                choix_cmd.delete()
    return redirect('resumerCommande',pk=1)   

def retirerProduit(request,nr_commande, slug): 
    choix          = get_object_or_404(Produit, slug=slug)
    commande_list  = Commande.objects.filter(nr_commande=nr_commande)
    
    if commande_list.exists():  
        
       commande = commande_list[0]  
       # vérifier si le choix est déjà dans la commande
       if commande.composition.filter(choix__slug=choix.slug).exists():
            choix_cmd = Choix.objects.filter(choix=choix)[0]
            commande.composition.remove(choix_cmd)
            choix_cmd.delete()           
    return redirect('resumerCommande',pk=1)       