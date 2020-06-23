from django.urls import path

from restaurant import views


app_name = 'restaurant'

urlpatterns = [
    path('',views.home , name='home' ),
    path('<slug:slug>/', views.menus_produit, name='menus_produit'),
    # path('commandes/', views.resumer_commande, name='resumer_commande'),
]
