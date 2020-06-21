from django.shortcuts import render, get_object_or_404

from .models import Menu

def home(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus ,
    }
    return render(request, 'home.html', context)


def menus_produit(request, slug):
    menu =  Menu.objects.get(slug=slug)
    menus = Menu.objects.all()
    
    context  = {
        'menus': menus ,
        'menu' : menu ,  
    }
    
    return render(request, 'produits.html', context) 



def resumer_commande():
    pass
