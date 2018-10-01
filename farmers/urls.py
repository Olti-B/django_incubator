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
    path('login', views.login, name='login'),
    path('reset', views.reset, name='reset'),
    path('make_post', views.make_post, name='make_post'),
    path('sold_products', views.sold_products, name='sold_products'),
]
