from django.shortcuts import render, get_object_or_404

from .models import Menu , Produit, Commande, Table, Serveur, Details

def home(request):
    menus = Menu.objects.all()
    return render(request, 'home.html', {'menus': menus})


def menus_produit(request, slug):
    menu =  Menu.objects.get(slug=slug)
    menus = Menu.objects.all()
    return render(request, 'produits.html', {'menu': menu, 'menus': menus})


def resumer_commande(request):
    produits = Produit.objects.all()
    commande = Commande.objects.all()
    details  = Details.objects.all()
    
    context = {
        'commande': commande ,
        'produits': produits ,
        
    }
    
    return render(request, 'commande.html', context)
