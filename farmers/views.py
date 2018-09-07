from django.shortcuts import render


# Create your views here.
def index(req):
    return render(req, 'farmers/home.html')


def register(req):
    return render(req, 'farmers/register.html')


def products(req):
    return render(req, 'farmers/products.html')


def land(req):
    return render(req, 'farmers/land.html')


def invest(req):
    return render(req, 'farmers/invest.html')


def plant_register(req):
    return render(req, 'farmers/plant_register.html')


def profile(req):
    return render(req, 'farmers/profile.html')