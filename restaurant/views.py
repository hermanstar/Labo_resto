from django.shortcuts import render

from .models import Menu

def home(request):
    menus = Menu.objects.all()
    return render(request, 'home.html', {'menus': menus})


def menus_produit(request, slug):
    menu =  Menu.objects.get(slug=slug)
    menus = Menu.objects.all()

    return render(request, 'produits.html', {'menu': menu, 'menus': menus})


def resumer_commande():
    pass
