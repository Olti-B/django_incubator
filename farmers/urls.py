from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('products', views.products, name='products'),
    path('land', views.land, name='land'),
    path('invest', views.invest, name='invest'),
    path('plant_register', views.plant_register, name='plant_register'),
    path('profile', views.profile, name='profile'),

]
