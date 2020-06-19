"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


#from restaurant import views

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    # path('', views.home, name='home'),
    # path('menus/<int:pk>/', views.menus_produit, name='menus_produit'),
    #path('', views.home, name='home'),
    #path('menus/<int:pk>/', views.menus_produit, name='menus_produit'),
    # path('menus/<int:pk>/new/', views.new_produit, name='new_produit'),
    #path('', views.home, name='home'),
    #path('menus/<int:pk>/', views.menus_produit, name='menus_produit'),
    path('menus/' , include('restaurant.urls' , namespace='home')),
    path('admin/', admin.site.urls),
    
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)